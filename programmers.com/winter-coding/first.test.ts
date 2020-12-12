import solution from './first'

test('first case', () => {
  expect(
    solution(6, [
      [1, 3, 1],
      [3, 5, 0],
      [5, 4, 0],
      [2, 5, 0]
    ])
  ).toBe('O?O?X?')
})

test('second case', () => {
  expect(
    solution(7, [
      [5, 6, 0],
      [1, 3, 1],
      [1, 5, 0],
      [7, 6, 0],
      [3, 7, 1],
      [2, 5, 0]
    ])
  ).toBe('O?O?XXO')
})
