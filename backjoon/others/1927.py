import sys


class MinHeap:
    def __init__(self):
        self.data = []

    def push(self, value):
        """힙에 값을 추가"""
        self.data.append(value)
        self._sift_up(len(self.data) - 1)

    def pop(self):
        """최솟값을 제거하고 반환"""
        if not self.data:
            return 0
        
        if len(self.data) == 1:
            return self.data.pop()
        
        # 루트와 마지막 원소를 교환
        self._swap(0, len(self.data) - 1)
        min_value = self.data.pop()
        self._sift_down(0)
        return min_value

    def _sift_up(self, idx):
        """자식 노드를 위로 올림 (부모보다 작으면)"""
        while idx > 0:
            parent = (idx - 1) // 2
            if self.data[parent] <= self.data[idx]:
                break
            self._swap(parent, idx)
            idx = parent

    def _sift_down(self, idx):
        """부모 노드를 아래로 내림 (자식보다 크면)"""
        size = len(self.data)
        while True:
            left = 2 * idx + 1
            right = 2 * idx + 2
            smallest = idx

            if left < size and self.data[left] < self.data[smallest]:
                smallest = left
            if right < size and self.data[right] < self.data[smallest]:
                smallest = right
            
            if smallest == idx:
                break
            
            self._swap(idx, smallest)
            idx = smallest

    def _swap(self, a, b):
        """두 인덱스의 값을 교환"""
        self.data[a], self.data[b] = self.data[b], self.data[a]


def main():
    n = int(sys.stdin.readline())
    heap = MinHeap()
    
    for _ in range(n):
        x = int(sys.stdin.readline())
        
        if x == 0:
            print(heap.pop())
        else:
            heap.push(x)


main()
