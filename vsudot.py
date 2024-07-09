import numpy as np

def vsudot_python(vec_a, vec_b, index):
    """
    Simulate VSUDOT (by element) operation in Python
    vec_a: list of four 32-bit elements, each containing four signed 8-bit integers
    vec_b: list of four 32-bit elements, each containing four unsigned 8-bit integers
    index: index of the element in vec_b to use (0-3)
    """
    assert len(vec_a) == 4 and len(vec_b) == 4
    result = [0] * 4
   
    # Extract the indexed element from vec_b
    b_element = vec_b[index]
   
    for i in range(4):
        # Extract four signed 8-bit integers from vec_a[i]
        a_signed = [(vec_a[i] >> (8 * j)) & 0xFF for j in range(4)]
        a_signed = [x - 256 if x > 127 else x for x in a_signed]  # Convert to signed
       
        # Extract four unsigned 8-bit integers from the indexed element of vec_b
        b_unsigned = [(b_element >> (8 * j)) & 0xFF for j in range(4)]
       
        # Perform dot product
        dot_product = sum(a * b for a, b in zip(a_signed, b_unsigned))
       
        result[i] += dot_product  # Accumulate the result
   
    return result

class TestCaseVSUDOT:
    def __init__(self, vec_a, vec_b, index, expected_res, initial_res):
        self.vec_a = vec_a
        self.vec_b = vec_b
        self.index = index
        self.expected_res = expected_res
        self.initial_res = initial_res

def create_vsudot_test_cases():
    return [
        TestCaseVSUDOT(
            [0x01020304, 0x05060708, 0x090A0B0C, 0x0D0E0F10],  # vec_a
            [0x01020304, 0x05060708, 0x090A0B0C, 0x0D0E0F10],  # vec_b
            1,  # index
            [0x50, 0xD4, 0x158, 0x1DC],  # expected_res
            [0, 0, 0, 0]  # initial_res
        ),
        TestCaseVSUDOT(
            [0xFFFEFDFC, 0xFBFAF9F8, 0xF7F6F5F4, 0xF3F2F1F0],  # vec_a (negative values)
            [0x01020304, 0x05060708, 0x090A0B0C, 0x0D0E0F10],  # vec_b
            2,  # index
            [-0x8A, -0x1AE, -0x2D2, -0x3F6],  # expected_res
            [0, 0, 0, 0]  # initial_res
        ),
        TestCaseVSUDOT(
            [0x01010101, 0x02020202, 0x03030303, 0x04040404],  # vec_a
            [0x01010101, 0x02020202, 0x03030303, 0x04040404],  # vec_b
            0,  # index
            [0x10, 0x20, 0x30, 0x40],  # expected_res (accumulated)
            [0x0C, 0x18, 0x24, 0x30]  # initial_res (for accumulation)
        ),
        TestCaseVSUDOT(
            [0xFF010203, 0xFD050607, 0xFB090A0B, 0xF90D0E0F],  # vec_a (mixed signs)
            [0x01010101, 0x02020202, 0x03030303, 0x04040404],  # vec_b
            3,  # index
            [0x0C, 0x24, 0x3C, 0x54],  # expected_res
            [0, 0, 0, 0]  # initial_res
        ),
    ]

def main():
    vsudot_test_cases = create_vsudot_test_cases()
    print("Python VSUDOT Test Cases:")
    for i, test in enumerate(vsudot_test_cases):
        result = vsudot_python(test.vec_a, test.vec_b, test.index)
        
        # Apply initial result (accumulation)
        result = [r + ir for r, ir in zip(result, test.initial_res)]
        
        status = "PASS" if result == test.expected_res else "FAIL"
       
        print(f"Test case {i + 1}: {status}")
        print(f"VecA: {[hex(x) for x in test.vec_a]}")
        print(f"VecB: {[hex(x) for x in test.vec_b]}")
        print(f"Index: {test.index}")
        print(f"Initial Result: {[hex(x) for x in test.initial_res]}")
        print(f"Expected Result: {[hex(x) if isinstance(x, int) else x for x in test.expected_res]}")
        print(f"Calculated Result: {[hex(x) if isinstance(x, int) else x for x in result]}")
        print()

if __name__ == "__main__":
    main()