class TaskQueue:
    def __init__(self):
        self.queue = []

    def add_task(self, task):
        if len(self.queue) > 20:
            raise Exception("Queue is full")
        self.queue.append(task)

    def extract_task(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        return self.queue.pop(0)

    def is_empty(self):
        return len(self.queue) == 0

    def clear(self):
        self.queue = []

    def size(self):
        return len(self.queue)


if __name__ == "__main__":

    def test(qty:int) -> str:
        queue = TaskQueue()
        for i in range(qty):
            queue.add_task(f"Task {i+1}")
        try:
            queue.add_task("Extra task")
        except Exception as error_msg:
            print("Exception:", error_msg)

        while not queue.is_empty():
            print("Extracted task:", queue.extract_task())
        try:
            print(queue.extract_task())

        except Exception as error_msg:
            print("Exception:", error_msg)

# queue > 20
test(21)

# queue = 0
test(0)