# Arthur Rocha Amaral
# Guilherme Oliveira Antônio
# 
# Lab01S01: Consulta graphql para 100 repositórios + requisição automática
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
#    pytthon scripts/Lab01S01.py -token TOKEN

from gql import gql, Client
from gql.transport.aiohttp import AIOHTTPTransport
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-token', help='token help', required=True)
args = parser.parse_args()

def Lab01S01():

    url = 'https://api.github.com/graphql'
    token = args.token

    headers = {'Authorization': f'bearer {token}'}

    transport = AIOHTTPTransport(url, headers)

    session = Client(transport=transport, fetch_schema_from_transport=True)

    #Consulta graphql para 100 repositórios
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
            }
        }
        """
    )

    result = session.execute(query)

    for repo in result['search']['nodes']:
        print(repo)

Lab01S01()