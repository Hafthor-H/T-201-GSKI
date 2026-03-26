class PQMinList:

    def __init__(self):
        self._data = []

    def push(self, element: int) -> None:
        self._data.append(element)

    def pop(self) -> int:
        if not self._data:
            raise IndexError("pop from empty PQ")
        e = min(self._data)
        self._data.remove(e)
        return e

    def peek(self) -> int:
        if not self._data:
            raise IndexError("peek from empty PQ")
        return min(self._data)

    def size(self) -> int:
        return len(self._data)

    def copy(self) -> "PQMinList":
        mh = PQMinList()
        mh._data = self._data[:]  # shallow copy is sufficient as we are only working with 
        return mh                 # non-mutable data (int).