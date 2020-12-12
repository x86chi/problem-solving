export default function solution(letters: string[], target: string) {
  const store = Array<number>(target.length).fill(0)

  for (let index = 1; index < target.length + 1; index++) {
    for (const letter of letters) {
      const { length } = letter
      if (index - length < 0) continue

      if (letter === target.substring(index - length, index)) {
        if (index - length === 0) {
          store[index - 1] += 1
          continue
        }
        if (store[index - length - 1] > 0) {
          store[index - 1] =
            store[index - 1] === 0
              ? store[index - length - 1] + 1
              : Math.min(store[index - 1], store[index - length - 1] + 1)
        }
      }
    }
  }
  const answer = store[store.length - 1]
  return answer === 0 ? -1 : answer
}
