"""
test_dalist_part1_part2.py

Comprehensive tests for DAList Parts 1 and 2 (NO Part 3 negative-index tests).

Run:
    python test_dalist_part1_part2.py

Assumptions:
- Your implementation lives in dalist.py and exposes class DAList.
- __str__ prints string elements without quotes (e.g., [a, b]) based on your __str__.
"""

from dalist import DAList


def check(actual, expected, msg=""):
    if actual != expected:
        raise AssertionError(f"{msg}\nExpected: {expected}\nActual:   {actual}")
    print("PASS:", msg)


def expect_raises(exc_type, fn, msg=""):
    try:
        fn()
    except exc_type:
        print("PASS:", msg)
        return
    except Exception as e:
        raise AssertionError(
            f"{msg}\nExpected {exc_type.__name__}, but got {type(e).__name__}: {e}"
        )
    raise AssertionError(f"{msg}\nExpected {exc_type.__name__}, but no exception was raised.")


def build_with(values, capacity=4):
    d = DAList(capacity)
    for v in values:
        d.append(v)
    return d


def main():
    # ---------------------------------------------------------------------
    # Part 1: construction, len, get/set, str, del, iter/next
    # ---------------------------------------------------------------------
    D = DAList(4)
    check(len(D), 0, "len(empty)")

    # append a few (append is Part 2, but needed for setup)
    D.append(1)
    D.append(2)
    D.append(5)
    check(str(D), "[1, 2, 5]", "__str__ after appends")
    check(len(D), 3, "len(after appends)")

    # __getitem__
    check(D[0], 1, "__getitem__ index 0")
    check(D[1], 2, "__getitem__ index 1")
    check(D[2], 5, "__getitem__ index 2")
    expect_raises(IndexError, lambda: D[3], "__getitem__ out of range raises")

    # __setitem__
    D[1] = 99
    check(str(D), "[1, 99, 5]", "__setitem__ updates element")
    expect_raises(IndexError, lambda: D.__setitem__(10, 0), "__setitem__ too large index raises")

    # __iter__ / __next__
    collected = [x for x in D]
    check(collected, [1, 99, 5], "__iter__/__next__ iteration order")

    # __delitem__
    del D[1]
    check(str(D), "[1, 5]", "__delitem__ removes and shifts")
    check(len(D), 2, "len(after del)")

    # clear (Part 1)
    D.clear()
    check(str(D), "[]", "clear empties")
    check(len(D), 0, "len(after clear)")

    # count / index (Part 1)
    E = build_with([7, 7, 8, 7], capacity=4)
    check(E.count(7), 3, "count counts occurrences")
    check(E.index(8), 2, "index finds first occurrence")
    expect_raises(ValueError, lambda: E.index(999), "index missing raises ValueError")

    # insert (Part 1): insert at start/middle/end and resizing
    F = build_with([1, 2, 4], capacity=4)
    F.insert(2, 3)
    check(str(F), "[1, 2, 3, 4]", "insert middle")

    F.insert(0, 0)
    check(str(F), "[0, 1, 2, 3, 4]", "insert at start (should resize when full)")

    # insert at end (index == len allowed in your code because range(len, index, -1) won't run)
    F.insert(len(F), 5)
    check(str(F), "[0, 1, 2, 3, 4, 5]", "insert at end (index == len)")

    expect_raises(IndexError, lambda: F.insert(len(F) + 1, 999), "insert past end raises IndexError")

    # reverse (Part 1)
    F.reverse()
    check(str(F), "[5, 4, 3, 2, 1, 0]", "reverse order")

    # ---------------------------------------------------------------------
    # Part 2: append, copy, extend, pop, remove
    # ---------------------------------------------------------------------
    G = DAList(4)
    for v in [1, 2, 3, 4]:
        G.append(v)
    check(str(G), "[1, 2, 3, 4]", "append fills capacity")

    # append triggers resize
    G.append(5)
    check(str(G), "[1, 2, 3, 4, 5]", "append triggers resize when full")

    # copy
    H = G.copy()
    check(str(H), str(G), "copy same contents")
    G[0] = 999
    check(str(G), "[999, 2, 3, 4, 5]", "mutate original after copy")
    check(str(H), "[1, 2, 3, 4, 5]", "copy independent container")

    # extend
    G.extend(["a", "b", "c"])
    check(str(G), "[999, 2, 3, 4, 5, a, b, c]", "extend appends iterable elements")

    # remove (first occurrence only)
    I = build_with([1, 2, 2, 3], capacity=4)
    I.remove(2)
    check(str(I), "[1, 2, 3]", "remove removes first occurrence and shifts")
    expect_raises(ValueError, lambda: I.remove(999), "remove missing raises ValueError")

    # pop (by index)
    J = build_with([10, 20, 30, 40], capacity=4)
    val = J.pop(1)
    check(val, 20, "pop returns removed value")
    check(str(J), "[10, 30, 40]", "pop removes correct index")
    # out of range (depends on underlying array bounds; should raise IndexError)
    expect_raises(IndexError, lambda: J.pop(999), "pop out of range raises IndexError")

    print("\nAll Part 1 & 2 tests PASSED ✅")


if __name__ == "__main__":
    main()
