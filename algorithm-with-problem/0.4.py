class CircularQueue:

	def __init__(self):
		self.QUEUE_CAPACITY = 8

		self.queue = [None] * self.QUEUE_CAPACITY
		self.head = 0
		self.tail = -1
		self.queue_size = 0

	def enqueue(self, n :int):
		if self.queue_size == self.QUEUE_CAPACITY:
			print("queue full!")
			return
		self.tail = (self.tail + 1) % self.QUEUE_CAPACITY
		self.queue_size = self.queue_size + 1
		self.queue[self.tail] = n

	def dequeue(self):
		if self.queue_size == 0:
			print("queue empty!")
			return
		self.head = (self.head + 1) % self.QUEUE_CAPACITY
		self.queue_size = self.queue_size - 1
		return self.queue[self.head - 1]


class NativeQueue:
	def __init__(self):
		self.queue = []
	
	def enqueue(self, val):
		self.queue.insert(0, val)
	
	def dequeue(self):
		if self.is_empty():
			return None
		else:
			return self.queue.pop()
	
	def size(self):
		return len(self.queue)
	def is_empty(self):
		return self.size() == 0

def main(func):
		while True:
			number = int(input("input number: "))
			if number > 0:
				func.enqueue(number)
			elif number == 0:
				print(func.dequeue())
			if number < 0:
				return print(func.queue)

if __name__ == '__main__':
	main(CircularQueue())
	# main(NativeQueue())
