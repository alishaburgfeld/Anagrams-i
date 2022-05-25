// Can you translate this driver code to unit tests?

var ana = require("./characterMatch");

test("should match anagrams", () => {
  expect(ana.isCharacterMatch("abc", "cba")).toBe(true);
  expect(ana.isCharacterMatch("charm", "march")).toBe(true);
  expect(ana.isCharacterMatch("zach", "attack")).toBe(false);
  expect(ana.isCharacterMatch("CharM", "mARcH")).toBe(true);
  expect(ana.isCharacterMatch("abcde2", "c2abed")).toBe(true);
});

test("should match challenge anagram", () => {
    expect(ana.isCharacterMatch("Anna Madrigal", "A man and a girl")).toBe(true);
});
