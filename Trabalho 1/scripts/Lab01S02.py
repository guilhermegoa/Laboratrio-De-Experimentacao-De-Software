# Lab01S02: Paginação (consulta 1000 repositórios) + dados em arquivo .csv

from gql import gql, Client
from gql.transport.aiohttp import AIOHTTPTransport
import os
import argparse

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
        query {
        search(type: REPOSITORY, first: 100, query: "stars:>0") {
                nodes {
                ... on Repository {
                        name
                        url
                        stargazerCount
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

    if not os.path.exists('files'): 
        os.mkdir('files')
    elif os.path.exists('files/Lab01S02.csv') :
        os.remove('files/Lab01S02.csv')

    result = session.execute(query)

    count = 0

    while result['search']['pageInfo']['hasNextPage'] and count < 12:
        print(f'{count} - Requesting...')
        
        count+=1

        saveOnFile(result['search']['nodes'])

        query = gql(
            """
            query ($after: String!) {
                search(type: REPOSITORY, first: 100, query: "stars:>0", after: $after) {
                        nodes {
                        ... on Repository {
                                name
                                url
                                stargazerCount
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

        params = { "after": result['search']['pageInfo']['endCursor'] }

        result = session.execute(query, variable_values=params)


def saveOnFile(repos):
    
    file = open('files/Lab01S02.csv', 'a')

    for repo in repos:
        name = repo['name']
        url = repo['url']
        star = repo['stargazerCount']

        file.write(f'{name};{url};{star}\n')
    
    file.close()

Lab01S02()