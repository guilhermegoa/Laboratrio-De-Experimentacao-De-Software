const replaceAll = (text, pattern, replacer) => {
  if (text.includes(pattern)) {
    const newText = text.replace(pattern, replacer);
    return replaceAll(newText, pattern, replacer)
  }
  return text;
}

module.exports = replaceAll