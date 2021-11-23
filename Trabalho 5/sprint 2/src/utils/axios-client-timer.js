const registerClientInterceptors = (axiosInstance) => {
  axiosInstance.interceptors.request.use((config) => {
    config.headers['request-start-time'] = new Date().getTime();
    return config;
  })

  axiosInstance.interceptors.response.use((response) => {
    const currentTime = new Date().getTime();
    config.headers['request-end-time'] = currentTime;
    const startTime = response.config.headers['request-startTime'];
    response.headers['request-duration'] = currentTime - startTime;
    return response;
  })
}

module.exports = registerClientInterceptors