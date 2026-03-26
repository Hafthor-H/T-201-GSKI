"""Page 377 Data structors & algorithms"""

class Heap:
    def __init__(self) -> None:
        self._data = []
        self.len = 0

    ####___Private Methods___###
    def _is_empty(self):
        return len(self._data) == 0

    def _parent(self, j):
        return (j - 1) // 2

    def _left(self, j):
        return 2*j + 1

    def _right(self, j):
        return 2*j + 2
    
    def _has_left(self, j):
        return self._left(j) < len(self._data) #Index beyond end of list?
    
    def _has_right(self, j):
        return self._right(j) < len(self._data) #Index beyond end of list?

    def _swap(self, i, j):
        """Swap the elements at the indces i and j of array"""
        self._data[i], self._data[j] = self._data[j], self._data[i]

    def _upheap(self,j ):
        parent = self._parent(j)
        if j > 0 and self._data[j] < self._data[parent]:
            self._swap(j, parent)
            self._upheap(parent) #recursion at the position of the parent, runs until it finds the correct index

    def _downheap(self, j):
        if self._has_left(j):
            left = self._left(j)
            small_child = left #Right might be smaller
            
            if self._has_right(j):
                right = self._right(j)
                if self._data[right] < self._data[left]:
                    small_child = right
            
            if self._data[small_child] < self._data[j]:
                self._swap(j, small_child)
                self._downheap(small_child) #recursion at the position of the small_child, runs until it finds the correct index


    ####___Public Methods___###

    def __str__(self) -> str:
        return str(self._data)

    def push(self, item):
        self._data.append(item)
        self._upheap(len(self._data)-1)

    def pop(self):
        if self._is_empty():
            raise Exception("Heap is empty")
        self._swap(0,len(self._data)-1)
        item = self._data.pop()
        self._downheap(0)
        # return (item)

    def peek(self):
        """Returns the index and value of the smallest value in the Heap"""
        if self._is_empty():
            raise Exception("Heap is empty")
        item = self._data[0]
        return item

    def size(self):
        return len(self._data)
    
    def copy(self):
        copy_heap = Heap()
        copy_heap._data = self._data[:]
        return copy_heap

def main():
    n = int(input())
    heaps = {}

    for _ in range(n):
        line = input().split()
        op = line[1]
        id = line[0]

        if id not in heaps:
            heaps[id] = Heap()

        heap = heaps[id]

        if op == "+":
            heap.push(int(line[2]))
        elif op == "a":
            other_id = line[2]
            if other_id not in heaps:
                heaps[other_id] = Heap()
            heaps[id] = heaps[other_id].copy()
        elif op == "-":
            heap.pop()
        elif op == "p":
            print(heap.peek())
        elif op == "s":
            print(heap.size())

if __name__ == "__main__":
    main()