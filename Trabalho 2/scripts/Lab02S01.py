# Arthur Rocha Amaral
# Guilherme Oliveira Antônio
#
# Lab02S01: Consulta graphql para 100 repositórios + requisição automática
#
# Rodar comando para inciar ambiente virtual e acessa-lo.
#    python3 -m venv .venv
#    source .venv/bin/activate
#
# Instalar biblioteca usada.
#    python -m pip install --pre gql[all]
#
# Colocar um novo token gerado pelo github
# https://docs.github.com/pt/github/authenticating-to-github/keeping-your-account-and-data-secure/creating-a-personal-access-token
#
# Rodar
#    python scripts/Lab02S01.py --token TOKEN --should-fetch true --should-analyse true

from gql import gql, Client
from gql.transport.aiohttp import AIOHTTPTransport
from datetime import datetime
import os
import argparse
import json
import subprocess

parser = argparse.ArgumentParser()
parser.add_argument('--token', help='token help', required=True)
parser.add_argument(
    '--should-fetch', help='should get the popular reposities analyses ypu can set false to block this step', required=False, default="true", choices={"true", "false"})
parser.add_argument('--should-analyse',
                    help='should run reposities analyses ypu can set false to block this step', required=False, default="true", choices={"true", "false"})
args = parser.parse_args()

analyseDataFilePath = 'files/analyse-data.txt'
repositoryFilePath = 'files/popular-java-repos.csv'


def FetchJavaRepos(token):
    url = 'https://api.github.com/graphql'
    headers = {'Authorization': f'bearer {token}'}

    transport = AIOHTTPTransport(url, headers)
    session = Client(transport=transport, fetch_schema_from_transport=True)

    query = gql(
        """
        query($after: String, $pageSize: Int) {
            search(
                type: REPOSITORY
                first: $pageSize
                query: "language:java"
                after: $after
            ) {
                pageInfo {
                    endCursor
                    hasNextPage
                }
                nodes {
                    ... on Repository {
                        nameWithOwner
                        url
                        stargazerCount
                        createdAt
                        releases {
                            totalCount
                        }
                        pullRequests {
                            totalCount
                        }
                        primaryLanguage {
                            name
                        }
                    }
                }
            }
        }
        """
    )

    count = 0
    after_key = None
    repos = []
    page_size = 100
    page_quantity = 10
    has_next_page = True

    while count < page_quantity and has_next_page:
        print(f'Requesting page {count + 1}/{page_quantity}')

        params = json.dumps({"after": after_key, "pageSize": page_size})
        result = session.execute(query, variable_values=params)

        count += 1
        after_key = result['search']['pageInfo']['endCursor']
        has_next_page = result['search']['pageInfo']['hasNextPage']
        repos += result['search']['nodes']

    SaveOnFile(repos)


def SaveOnFile(repos: list):
    if not os.path.exists('files'):
        os.mkdir('files')
    elif os.path.exists(repositoryFilePath):
        os.remove(repositoryFilePath)

    file = open(repositoryFilePath, 'a')

    file.write(
        'nameWithOwner;url;stars;age;releases;pullRequests;primaryLanguage\n')

    today = datetime.now()
    yearFormat = "{0:.1f}"

    for repo in repos:
        if repos.count(repo) > 1:
            repos.remove(repo)
        else:
            name_with_owner = repo["nameWithOwner"]
            url = repo["url"]
            stargazer_count = repo["stargazerCount"]
            age = yearFormat.format((today - datetime.strptime(
                repo['createdAt'], "%Y-%m-%dT%H:%M:%SZ")).days / 365.25)
            releases = repo["releases"]["totalCount"]
            pull_requests = repo["pullRequests"]["totalCount"]
            primary_language = repo["primaryLanguage"]["name"]

            file.write(
                f'{name_with_owner};{url};{stargazer_count};{age};{releases};{pull_requests};{primary_language}\n')
    print(f"Total items saved in csv: {repos.__len__()} items")
    file.close()


def AnalyseCode():
    if not os.path.exists(repositoryFilePath):
        print('Repository path not exist')
        return

    lastRepoReadLineNumber = 0
    lastRepoReadLineNumberKey = 'lastRepoReadLineNumberKey'

    analyseDataFile = open(analyseDataFilePath, 'w')
    repositoriesFile = open(repositoryFilePath, 'r')

    lines = analyseDataFile.readlines() if analyseDataFile.readable() else []

    for line in lines:
        lineData = line.split("=")

        if(lineData[0] == lastRepoReadLineNumberKey):
            lastRepoReadLineNumber = int(lineData[1])

    repositories = repositoriesFile.readlines(
        0) if repositoriesFile.readable() else []

    del repositories[0]

    actualLine = lastRepoReadLineNumber if lastRepoReadLineNumber < (
        repositories.__len__() - 1) else 0

    while actualLine < repositories.__len__():
        repoData = repositories[actualLine].split(';')
        repositoryName = repoData[0].split('/')[1]
        repositoryUrl = repoData[1]

        # Download repository
        subprocess.call(
            [
                'sh',
                'scripts/get-repository-metrics.sh',
                repositoryName,
                repositoryUrl
            ]
        )
        
        # Analyse repository
        subprocess.call(
            [
                'sh',
                'scripts/analyse-repository.sh',
                repositoryName
            ]
        )

        try:
            analyseDataFile = open(analyseDataFilePath, 'w')
            analyseDataFile.write(
                f'{lastRepoReadLineNumberKey}={actualLine}\n')
        finally:
            analyseDataFile.flush()
            analyseDataFile.close()
            actualLine += 1

    os.remove(analyseDataFilePath)
    print("All repositories analysed")


if args.should_fetch == 'true':
    FetchJavaRepos(args.token)

if args.should_analyse == 'true':
    AnalyseCode()
