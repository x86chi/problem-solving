import solution from './substring'

test('banana', () => {
  expect(solution(['ba', 'na', 'n', 'a'], 'banana')).toBe(3)
})

test('apple', () => {
  expect(solution(['app', 'ap', 'p', 'l', 'e', 'ple', 'pp'], 'apple')).toBe(2)
})

test('another banana', () => {
  expect(solution(['ba', 'an', 'nan', 'ban', 'n'], 'banana')).toBe(-1)
})
