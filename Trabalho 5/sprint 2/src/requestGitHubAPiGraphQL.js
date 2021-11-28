const fs = require('fs');
const gitHubGraphQlApi = require('./client/githubApiClient');

const repositoryStargazersQuery = `query ($cursor: String, $itemsPerPage: Int) {
      repository(owner: "elixir-lang", name: "elixir") {
        stargazers(first: $itemsPerPage, after: $cursor) {
          pageInfo {
            endCursor
            hasNextPage
      }
      nodes {
            login
            id
            databaseId
            avatarUrl
            url
            isSiteAdmin
      }
    }
  }
}`

const requestGitHubAPiGraphQL = async () => {
    const PER_PAGE = 100;
    let requestTime = []; // time on milliseconds
    let contentLength = []; // size on bytes

    console.log('Start requests')

    let endCursorState = null;
    let hasNextPageState = false;
    let page = 0;
    do {
        console.log(`Current page: ${++page}`);
        const requestBody = {
            query: repositoryStargazersQuery,
            variables: {
                cursor: endCursorState,
                itemsPerPage: PER_PAGE
            }
        }

        try {
            const resStargazers = await gitHubGraphQlApi.post('/graphql', requestBody);

            const { endCursor, hasNextPage } = resStargazers.data.data.repository.stargazers.pageInfo;

            endCursorState = endCursor;
            hasNextPageState = hasNextPage;

            requestTime.push(resStargazers.headers['request-duration']);
            contentLength.push(resStargazers.headers['content-length']);
        }
        catch (e) {
            console.log(e);
            return;
        }
    } while (hasNextPageState);

    console.log('End requests')


    const fileName = 'graphQLData'
    const headerFile = 'currentPage,requestTime,contentLength,type\n'

    const stream = fs.createWriteStream(`files/${fileName}.csv`)

    stream.write(headerFile)

    for (let i = 0; i < page; i++) {
        let currentPage = i + 1
        stream.write(`${currentPage},${requestTime[i]},${contentLength[i]},graphql
        `)
    }
}

module.exports = requestGitHubAPiGraphQL