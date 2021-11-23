const axios = require('axios');

const instance = axios.create({
    baseURL: "https://api.github.com",
});

instance.interceptors.request.use((config) => {
    config.headers['request-startTime'] = new Date().getTime();
    return config;
})

instance.interceptors.response.use((response) => {
    const currentTime = new Date().getTime();
    const startTime = response.config.headers['request-startTime'];
    response.headers['request-duration'] = currentTime - startTime;
    return response;
})

const TOKEN = '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';

instance.defaults.headers.authorization = `Bearer ${TOKEN}`;

module.exports = instance;