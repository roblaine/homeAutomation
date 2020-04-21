const sum = require('../src/utils/sum');

describe('Sum function should add 2 values', () => {
  test('adds 1 + 2 to equal 3', () => {
    expect(sum(1, 2)).toBe(3);
  });
});
