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
import os
import argparse
import json

parser = argparse.ArgumentParser()
parser.add_argument('-token', help='token help', required=True)
args = parser.parse_args()

if not os.path.exists('files'): 
    os.mkdir('files')
elif os.path.exists('files/Lab01S02.csv') :
    os.remove('files/Lab01S02.csv')

def Lab01S02():
    url = 'https://api.github.com/graphql'
    token = args.token

    headers = {'Authorization': f'bearer {token}'}

    transport = AIOHTTPTransport(url, headers)

    session = Client(transport=transport, fetch_schema_from_transport=True)

    query = gql(
        """
        query ($after: String) {
            search(type: REPOSITORY, first: 100, query: "stars:>0", after: $after) {
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

    params = json.dumps({"after":None})

    result = session.execute(query, variable_values=params)

    count = 0

    while result['search']['pageInfo']['hasNextPage'] and count < 10:
        print(f'{count} - Requesting...')
        
        count+=1

        saveOnFile(result['search']['nodes'])

        params = json.dumps({"after":result['search']['pageInfo']['endCursor']})

        result = session.execute(query, variable_values=params)

def saveOnFile(repos):
    
    file = open('files/Lab01S02.csv', 'a')

    for repo in repos:
        nameWithOwner = repo['nameWithOwner']
        url = repo['url']
        star = repo['stargazerCount']
        createdAt = repo['createdAt']
        updatedAt = repo['updatedAt']
        releases = repo['releases']['totalCount']
        issuesOpen = repo['open']['totalCount']
        issuesClosed = repo['closed']['totalCount']
        pullRequests = repo['pullRequests']['totalCount']
        primaryLanguage = repo['primaryLanguage'] != None and repo['primaryLanguage']['name'] or None

        file.write(f'{nameWithOwner};{url};{star};{createdAt};{updatedAt};{releases};{issuesOpen};{issuesClosed};{pullRequests};{primaryLanguage}\n')
    
    file.close()

Lab01S02()