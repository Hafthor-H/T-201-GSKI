from dalist import DAList

def check(actual, expected, msg):
    if actual != expected:
        raise ValueError(f"{msg}\nExpected: {expected}\nActual:   {actual}")
    print("PASS:", msg)

def expect_raises(exc, fn, msg):
    try:
        fn()
    except exc:
        print("PASS:", msg)
        return
    except Exception as e:
        raise ValueError(f"{msg}\nExpected {exc.__name__}, got {type(e).__name__}: {e}")
    raise ValueError(f"{msg}\nExpected {exc.__name__}, but nothing was raised")

# -------------------------
# Part 2: append + resize
# -------------------------
D = DAList(4)
for x in [1, 2, 5]:
    D.append(x)
check(str(D), "[1, 2, 5]", "append builds list")
check(len(D), 3, "len after append")

# fill capacity and trigger resize
D.append(9)              # now full at capacity=4
check(str(D), "[1, 2, 5, 9]", "append to fill capacity")
D.append(10)             # should resize and still work
check(str(D), "[1, 2, 5, 9, 10]", "append triggers resize")

# -------------------------
# Part 1: insert (middle/start/end + bounds)
# -------------------------
E = DAList(4)
for x in [1, 2, 4]:
    E.append(x)

E.insert(2, 3)
check(str(E), "[1, 2, 3, 4]", "insert in middle")

E.insert(0, 0)
check(str(E), "[0, 1, 2, 3, 4]", "insert at start (may resize)")

E.insert(len(E), 5)
check(str(E), "[0, 1, 2, 3, 4, 5]", "insert at end (index == len)")

expect_raises(IndexError, lambda: E.insert(len(E)+1, 999), "insert past end raises")

# -------------------------
# Part 1: reverse
# -------------------------
E.reverse()
check(str(E), "[5, 4, 3, 2, 1, 0]", "reverse works")

# -------------------------
# Part 2: remove (first occurrence) + ValueError
# -------------------------
R = DAList(4)
for x in [1, 2, 2, 3]:
    R.append(x)

R.remove(2)
check(str(R), "[1, 2, 3]", "remove first occurrence only")
expect_raises(ValueError, lambda: R.remove(999), "remove missing raises ValueError")

# -------------------------
# Part 2: pop (returns correct value)
# -------------------------
P = DAList(4)
for x in [10, 20, 30]:
    P.append(x)

v = P.pop(1)
check(v, 20, "pop returns removed value")
check(str(P), "[10, 30]", "pop removes at index")

# -------------------------
# Part 2: extend
# -------------------------
X = DAList(4)
for x in [5, 4, 1]:
    X.append(x)
X.extend(["a", "b", "c"])
check(str(X), "[5, 4, 1, a, b, c]", "extend appends iterable items")

# -------------------------
# Part 2: copy (independent container)
# -------------------------
C = X.copy()
check(str(C), str(X), "copy matches contents")
X[0] = 999
check(str(X), "[999, 4, 1, a, b, c]", "mutating original works")
check(str(C), "[5, 4, 1, a, b, c]", "copy is independent container")

# -------------------------
# Part 1: index + count
# -------------------------
check(C.index("a"), 3, "index finds first occurrence")
check(C.count("b"), 1, "count works")
expect_raises(ValueError, lambda: C.index("zzz"), "index missing raises ValueError")

# -------------------------
# Part 1: __getitem__ + bounds
# -------------------------
check(C[1], 4, "__getitem__ returns correct element")
expect_raises(IndexError, lambda: C[999], "__getitem__ out of range raises")

# -------------------------
# Part 1: del + shift
# -------------------------
D2 = DAList(4)
for x in [5, 4, "a", "b", "c"]:
    D2.append(x)

del D2[2]
check(str(D2), "[5, 4, b, c]", "del shifts left")

# -------------------------
# Part 1: clear
# -------------------------
D2.clear()
check(str(D2), "[]", "clear empties list")
check(len(D2), 0, "len after clear")

# -------------------------
# Part 1: iteration order (basic)
# -------------------------
It = DAList(4)
for x in [1, 2, 3]:
    It.append(x)
check([x for x in It], [1, 2, 3], "iteration yields in order")

print("\nMINIMAL rubric tests PASSED ✅")
