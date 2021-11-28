const axios = require('axios');
require('dotenv').config();

const instance = axios.create({
    baseURL: "https://api.github.com",
});

instance.interceptors.request.use((config) => {
    config.headers['request-start-time'] = new Date().getTime();
    return config;
})

instance.interceptors.response.use((response) => {
    const currentTime = new Date().getTime();
    const startTime = response.config.headers['request-startTime'];

    response.headers['request-startTime'] = startTime;
    response.headers['request-end-time'] = currentTime;

    response.headers['request-duration'] = currentTime - startTime;
    return response;
})


const TOKEN = process.env.TOKEN;

instance.defaults.headers.authorization = `Bearer ${TOKEN}`;

module.exports = instance;

