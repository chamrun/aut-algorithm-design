class MaxHeap:
    def __init__(self, numbers):
        self.heap = []
        for i in range(len(numbers)):
            self.insert(numbers[i])

    def insert(self, data):
        self.heap.append(data)
        self.heapify_up(len(self.heap) - 1)

    def heapify_up(self, index):
        if index == 0:
            return
        parent = (index - 1) // 2
        if self.heap[parent] < self.heap[index]:
            self.swap(parent, index)
            self.heapify_up(parent)

    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def kth_largest(self, k):
        for i in range(k - 1):
            self.extract_max()
        return self.extract_max()

    def extract_max(self):
        if len(self.heap) == 0:
            return None
        self.swap(0, len(self.heap) - 1)
        max_value = self.heap.pop()
        self.heapify_down(0)
        return max_value

    def heapify_down(self, index):
        left = 2 * index + 1
        right = 2 * index + 2
        largest = index
        if left < len(self.heap) and self.heap[left] > self.heap[largest]:
            largest = left
        if right < len(self.heap) and self.heap[right] > self.heap[largest]:
            largest = right
        if largest != index:
            self.swap(index, largest)
            self.heapify_down(largest)


def main():
    numbers = [10, 30, 20, 0, 40, 100, 80, 90, 70, 50, 60]

    k = 7
    max_heap = MaxHeap(numbers)
    print(max_heap.kth_largest(k))
    # print(max_heap.kth_smallest(k))


if __name__ == '__main__':
    main()
