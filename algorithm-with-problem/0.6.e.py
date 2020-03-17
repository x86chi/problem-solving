class Stack:
	def __init__(self):
		self.elements = []
	 
	def push(self, value):
		self.elements.append(value)
	
	def pop(self):
		if self.size() > 0:
			return self.elements.pop()
		else:
			return None
	
	def size(self):
		return len(self.elements)

# Implement a queue with two stacks
class Queue:
	def __init__(self):
		self.inbox = Stack()
		self.outbox = Stack()

	def enqueue(self, value):
		self.inbox.push(value)
	
	def dequeue(self):
		if self.outbox.size() is 0:
			while not self.inbox.size() is 0:
				pop = self.inbox.pop()
				self.outbox.push(pop)
		return self.outbox.pop()

if __name__ == '__main__':
	q = Queue()
	q.enqueue(1)
	q.enqueue(2)
	q.enqueue(3)
	print(q.dequeue())
	print(q.dequeue())
	print(q.dequeue())

