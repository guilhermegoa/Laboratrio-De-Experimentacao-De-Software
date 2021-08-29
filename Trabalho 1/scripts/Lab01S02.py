# Arthur Rocha Amaral
# Guilherme Oliveira Antônio
#
# Lab01S02: Paginação (consulta 1000 repositórios) + dados em arquivo .csv
#
# Rodar comando para inciar ambiente virtual e acessa-lo.
#    python3 - venv .venv
#    source .venv/bin/activate
#
# Instalar biblioteca usada.
#    python -m pip install --pre gql[all]
#
# Colocar um novo token gerado pelo github
# https://docs.github.com/pt/github/authenticating-to-github/keeping-your-account-and-data-secure/creating-a-personal-access-token
#
# Rodar
#    pytthon scripts/Lab01S02.py -token TOKEN

from gql import gql, Client
from gql.transport.aiohttp import AIOHTTPTransport
from datetime import datetime
import os
import argparse
import json

parser = argparse.ArgumentParser()
parser.add_argument('-token', help='token help', required=True)
args = parser.parse_args()


def Lab01S02():
    url = 'https://api.github.com/graphql'
    token = args.token

    headers = {'Authorization': f'bearer {token}'}

    transport = AIOHTTPTransport(url, headers)

    session = Client(transport=transport, fetch_schema_from_transport=True)

    query = gql(
        """
        query ($after: String, $pageSize: Int) {
            search(type: REPOSITORY, first: $pageSize, query: "stars:>0", after: $after) {
                nodes {
                    ... on Repository {
                            nameWithOwner
                            stargazerCount
                            createdAt
                            updatedAt
                            url
                        releases {
                            totalCount
                        }
                        open: issues (states: OPEN) {
                            totalCount
                        }
                        closed: issues (states: CLOSED){
                            totalCount
                        }
                        pullRequests(states: MERGED) {
                            totalCount
                        }
                        primaryLanguage {
                            name
                        }
                    }
                }
                pageInfo {
                    endCursor
                    hasNextPage
                }
            }
        }
        """
    )

    count = 0
    afterKey = None
    repos = []
    pageSize = 100
    pageQuantity = 10

    while count < pageQuantity:
        print(f'Requesting page {count + 1}/{pageQuantity}')

        params = json.dumps({"after": afterKey, "pageSize": pageSize})
        result = session.execute(query, variable_values=params)

        count += 1
        afterKey = result['search']['pageInfo']['endCursor']
        repos += result['search']['nodes']

        if afterKey == None:
            break

    saveOnFile(repos)


def saveOnFile(repos):
    if not os.path.exists('files'):
        os.mkdir('files')
    elif os.path.exists('files/Lab01S02.csv'):
        os.remove('files/Lab01S02.csv')

    file = open('files/Lab01S02.csv', 'a')

    file.write(
        'nameWithOwner;url;star;age;lastUpdate;releases;issuesOpen;issuesClosed;issuesProportion;pullRequests;primaryLanguage\n')

    # errorCount = 0

    for repo in repos:
        # try:
        nameWithOwner = repo['nameWithOwner']
        url = repo['url']
        star = repo['stargazerCount']

        today = datetime.now()

        createdAt = datetime.strptime(
            repo['createdAt'], "%Y-%m-%dT%H:%M:%SZ")

        updatedAt = datetime.strptime(
            repo['updatedAt'], "%Y-%m-%dT%H:%M:%SZ")

        releases = repo['releases']['totalCount']

        issuesOpen: int = repo['open']['totalCount']
        issuesClosed: int = repo['closed']['totalCount']
        issuesProportion = (
            issuesOpen/issuesClosed) if issuesClosed > 0 else None

        pullRequests = repo['pullRequests']['totalCount']
        primaryLanguage = repo['primaryLanguage'] != None and repo['primaryLanguage']['name'] or None

        file.write(
            f'{nameWithOwner};{url};{star};{(today-createdAt).days};{(today-updatedAt).days};{releases};{issuesOpen};{issuesClosed};{issuesProportion};{pullRequests};{primaryLanguage}\n')
        # except:
        #     errorCount += 1
        #     print(
        #         f'Error when try tho register the repository {nameWithOwner} of {errorCount} errors')
    file.close()


Lab01S02()
