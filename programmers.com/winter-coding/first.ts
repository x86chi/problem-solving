type Delivery = [number, number, 0 | 1]

const order = {
  first: 0,
  second: 1,
  isDelivered: 2
} as const

enum ItemStatus {
  STOCK = 'O',
  SOLD_OUT = 'X',
  UNKNOWN = '?'
}

export default function solution(n: number, deliveries: Delivery[]) {
  const logs = Array<ItemStatus>(n + 1).fill(ItemStatus.UNKNOWN)

  deliveries.sort((a, b) => {
    const isDelivered = {
      a: a[order.isDelivered],
      b: b[order.isDelivered]
    }
    return isDelivered.b - isDelivered.a
  })

  for (const delivery of deliveries) {
    const [first, second, isDelivered] = delivery

    if (isDelivered) {
      logs[first] = ItemStatus.STOCK
      logs[second] = ItemStatus.STOCK
      continue
    }

    if (logs[first] === ItemStatus.STOCK) {
      logs[second] = ItemStatus.SOLD_OUT
      continue
    }

    if (logs[second] === ItemStatus.STOCK) {
      logs[first] = ItemStatus.SOLD_OUT
      continue
    }
  }

  return logs.slice(1).join('')
}
