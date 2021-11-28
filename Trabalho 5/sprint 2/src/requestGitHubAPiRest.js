const fs = require('fs');
const api = require('./client/githubApiClient');

const requestGitHubAPiRest = async () => {
    const PERPAGE = 100;
    let lastPage = 0;
    let requestTime = []; // time on milliseconds
    let contentLength = []; // size on bytes

    const resRepo = await api.get(`repos/elixir-lang/elixir`);

    lastPage = Math.round(resRepo.data.stargazers_count / PERPAGE);

    console.log('Start requests')
    for (let page = 0; page < lastPage; page++) {
        console.log(`Current page: ${page}`);

        const resStargazers = await api.get(`repos/elixir-lang/elixir/stargazers\?per_page\=${PERPAGE}&page\=${page}`);

        requestTime.push(resStargazers.headers['request-duration']);
        contentLength.push(resStargazers.headers['content-length']);
    }
    console.log('End requests')

    const fileName = 'restData'
    const headerFile = 'currentPage,requestTime,contentLength,type\n'

    const stream = fs.createWriteStream(`files/${fileName}.csv`)

    stream.write(headerFile)

    for (let page = 0; page < lastPage; page++) {
        let currentPage = page + 1
        stream.write(`${currentPage},${requestTime[page]},${contentLength[page]},rest\n`)
    }
}

module.exports = requestGitHubAPiRest