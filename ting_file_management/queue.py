from ting_file_management.abstract_queue import AbstractQueue
from collections import deque


class Queue(AbstractQueue):
    def __init__(self):
        self.queue = deque()

    def __len__(self):
        return len(self.queue)

    def enqueue(self, value):
        return self.queue.append(value)

    def dequeue(self):
        return self.queue.popleft()

    def search(self, index):
        try:
            if index < 0:
                raise IndexError()
            self.queue[index]
        except IndexError:
            raise IndexError("Índice Inválido ou Inexistente")
        return self.queue[index]
