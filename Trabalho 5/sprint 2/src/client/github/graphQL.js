const axios = require('axios');
const registerClientInterceptors = require('../../utils/axios-client-timer');

const instance = axios.create({
  baseURL: "https://api.github.com",
});

registerClientInterceptors(instance)

const TOKEN = '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';

instance.defaults.headers.authorization = `Bearer ${TOKEN}`;

module.exports = instance;