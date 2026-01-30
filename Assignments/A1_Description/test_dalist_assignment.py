"""
test_dalist_assignment.py

Tests aligned to A1_Description.pdf requirements:
- Part 1: implement Part 1 methods, non-negative indices
- Part 2: implement Part 2 methods, reuse existing methods when possible
- Part 3: add negative index support "same as Python list"
- "Test your code thoroughly!"

Run:
    python test_dalist_assignment.py
"""

from dalist import DAList


def check(actual, expected, msg):
    if actual != expected:
        raise AssertionError(f"FAIL: {msg}\nExpected: {expected}\nActual:   {actual}")
    print("PASS:", msg)


def expect_raises(exc_type, fn, msg):
    try:
        fn()
    except exc_type:
        print("PASS:", msg)
        return
    except Exception as e:
        raise AssertionError(f"FAIL: {msg}\nExpected {exc_type.__name__}, got {type(e).__name__}: {e}")
    raise AssertionError(f"FAIL: {msg}\nExpected {exc_type.__name__}, but nothing was raised.")


def build(values, capacity=4):
    d = DAList(capacity)
    for v in values:
        d.append(v)
    return d


def test_part1():
    print("\n=== Part 1 ===")

    A = DAList(4)
    check(len(A), 0, "__len__ empty == 0")
    check(str(A), "[]", "__str__ empty == []")
    expect_raises(IndexError, lambda: A[0], "__getitem__ on empty raises IndexError")

    for x in [1, 2, 3]:
        A.append(x)

    check(len(A), 3, "__len__ after appends")
    check(A[0], 1, "__getitem__ index 0")
    check(A[2], 3, "__getitem__ last valid index")
    expect_raises(IndexError, lambda: A[3], "__getitem__ index == len raises IndexError")
    expect_raises(IndexError, lambda: A[999], "__getitem__ huge index raises IndexError")

    A[1] = 99
    check(str(A), "[1, 99, 3]", "__setitem__ updates element")
    expect_raises(IndexError, lambda: A.__setitem__(len(A) + 1, 7), "__setitem__ index > len raises IndexError")

    # Python-like: setting at index==len should raise
    expect_raises(IndexError, lambda: A.__setitem__(len(A), 7), "__setitem__ index == len should raise (Python-like)")

    B = build([1, 2, 4], capacity=4)
    B.insert(2, 3)
    check(str(B), "[1, 2, 3, 4]", "insert in middle")

    B.insert(0, 0)
    check(str(B), "[0, 1, 2, 3, 4]", "insert at start")

    B.insert(len(B), 5)
    check(str(B), "[0, 1, 2, 3, 4, 5]", "insert at end (index == len)")

    expect_raises(IndexError, lambda: B.insert(len(B) + 1, 999), "insert past end raises IndexError")

    C = build([10, 20, 30, 40], capacity=4)
    del C[1]
    check(str(C), "[10, 30, 40]", "__delitem__ removes middle and shifts")

    del C[0]
    check(str(C), "[30, 40]", "__delitem__ removes start and shifts")

    del C[len(C) - 1]
    check(str(C), "[30]", "__delitem__ removes last element")

    expect_raises(IndexError, lambda: C.__delitem__(len(C)), "__delitem__ index == len raises IndexError")
    expect_raises(IndexError, lambda: C.__delitem__(999), "__delitem__ huge index raises IndexError")

    D = build([7, 7, 8, 7], capacity=4)
    check(D.count(7), 3, "count counts occurrences")
    check(D.index(8), 2, "index finds first occurrence")
    expect_raises(ValueError, lambda: D.index(999), "index missing raises ValueError")

    D.clear()
    check(str(D), "[]", "clear empties list")
    check(len(D), 0, "len after clear")

    E = build([1, 2, 3], capacity=4)
    check([x for x in E], [1, 2, 3], "iteration yields elements in order")

    F = build([1, 2, 3, 4, 5], capacity=4)
    F.reverse()
    check(str(F), "[5, 4, 3, 2, 1]", "reverse reverses all elements")


def test_part2():
    print("\n=== Part 2 ===")

    A = DAList(4)
    for x in [1, 2, 3, 4]:
        A.append(x)
    check(str(A), "[1, 2, 3, 4]", "append fills to capacity")

    A.append(5)
    check(str(A), "[1, 2, 3, 4, 5]", "append triggers resize when full")

    A.extend(["a", "b", "c"])
    check(str(A), "[1, 2, 3, 4, 5, a, b, c]", "extend appends iterable items")

    B = A.copy()
    check(str(B), str(A), "copy same contents")
    A[0] = 999
    check(str(A), "[999, 2, 3, 4, 5, a, b, c]", "mutating original after copy")
    check(str(B), "[1, 2, 3, 4, 5, a, b, c]", "copy independent container")

    C = build([1, 2, 2, 3], capacity=4)
    C.remove(2)
    check(str(C), "[1, 2, 3]", "remove removes first occurrence")
    expect_raises(ValueError, lambda: C.remove(999), "remove missing raises ValueError")

    D = build([10, 20, 30, 40], capacity=4)
    v = D.pop(1)
    check(v, 20, "pop returns element at index")
    check(str(D), "[10, 30, 40]", "pop removes correct index and shifts")

    # duplicate correctness: pop by index, not by value
    E = build([5, 7, 5, 9], capacity=4)
    v2 = E.pop(2)
    check(v2, 5, "pop returns element at index (duplicate case)")
    check(str(E), "[5, 7, 9]", "pop removes by index, not first matching value (duplicate case)")

    expect_raises(IndexError, lambda: D.pop(len(D)), "pop index == len raises IndexError")
    expect_raises(IndexError, lambda: D.pop(999), "pop huge index raises IndexError")


def test_part3():
    print("\n=== Part 3 (negative indices) ===")

    A = build([1, 2, 3, 4], capacity=4)
    check(A[-1], 4, "__getitem__ -1 is last element")
    check(A[-4], 1, "__getitem__ -len is first element")
    expect_raises(IndexError, lambda: A[-5], "__getitem__ too negative raises IndexError")

    A[-1] = 99
    check(str(A), "[1, 2, 3, 99]", "__setitem__ -1 updates last element")
    expect_raises(IndexError, lambda: A.__setitem__(-999, 0), "__setitem__ too negative raises IndexError")

    del A[-1]
    check(str(A), "[1, 2, 3]", "__delitem__ -1 deletes last element")
    expect_raises(IndexError, lambda: A.__delitem__(-999), "__delitem__ too negative raises IndexError")

    B = build([1, 2, 3, 4], capacity=4)
    B.insert(-1, 99)
    check(str(B), "[1, 2, 3, 99, 4]", "insert(-1, x) inserts before last (Python-like)")

    C = build([10, 20, 30, 40], capacity=4)
    pv = C.pop(-1)
    check(pv, 40, "pop(-1) returns last")
    check(str(C), "[10, 20, 30]", "pop(-1) removes last")


def main():
    test_part1()
    test_part2()
    test_part3()
    print("\nALL ASSIGNMENT TESTS PASSED ✅")


if __name__ == "__main__":
    main()
