from Heap import Heap


def run_tests():
    print("Running tests...")

    # Test 1: basic push + peek
    h = Heap()
    h.push(10)
    h.push(3)
    h.push(8)
    h.push(1)
    print("Test 1:", "PASS" if h.peek() == 1 else "FAIL")

    # Test 2: pop works
    h.pop()
    print("Test 2:", "PASS" if h.peek() == 3 else "FAIL")

    # Test 3: size updates
    print("Test 3:", "PASS" if h.size() == 3 else "FAIL")

    # Test 4: negative numbers
    h2 = Heap()
    h2.push(-9)
    h2.push(6)
    h2.push(42)
    h2.push(-5)
    print("Test 4:", "PASS" if h2.peek() == -9 else "FAIL")

    # Test 5: copy independence (CRITICAL)
    h3 = Heap()
    h3.push(4)
    h3.push(2)
    h3.push(7)

    h4 = h3.copy()
    h3.pop()

    cond = (h3.peek() == 4 and h4.peek() == 2)
    print("Test 5 (copy):", "PASS" if cond else "FAIL")

    # Test 6: copy memory separation
    h5 = Heap()
    h5.push(5)
    h5.push(1)

    h6 = h5.copy()
    h6.push(0)

    cond = (h5.peek() == 1 and h6.peek() == 0)
    print("Test 6 (copy memory):", "PASS" if cond else "FAIL")

    print("Done.")


run_tests()