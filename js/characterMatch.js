/**
 * Returns whether the strings are case-insensitive anagrams of each other.
 *
 * @param {String} string1 The first string to compare
 * @param {String} string2 The second string to compare
 * @returns
 */
const isCharacterMatch = (string1, string2) => {
  const obj1 = {};
  for (const char of string1.toLowerCase()) {
    if (char !== " ") obj1[char] = (obj1[char] || 0) + 1;
  }

  const obj2 = {};
  for (const char of string2.toLowerCase()) {
    if (char !== " ") obj2[char] = (obj2[char] || 0) + 1;
  }

  const allKeys = new Set([...Object.keys(obj1), ...Object.keys(obj2)])

  for (const key of allKeys) {
    if (obj1[key] !== obj2[key]) {
      return false;
    }
  }

  return true;

  // const entries1 = Object.entries(obj1);
  // const entries2 = Object.entries(obj2);

  // const filter1 = entries1.filter((el) => entries2.includes(el));
  // const filter2 = entries2.filter((el) => entries1.includes(el));

  // return !(filter1.length > 0 || filter2.length > 0);
};

module.exports = { isCharacterMatch };
