import numpy as np

def vsudot_python(vec_a, vec_b):
    """Simulate VSUDOT operation in Python"""
    assert len(vec_a) == len(vec_b)
    size = len(vec_a)
    result = []
    for i in range(0, size, 8):
        chunk_a = vec_a[i:i+8]
        chunk_b = vec_b[i:i+8]
        dot_product = sum(a * b for a, b in zip(chunk_a, chunk_b))
        result.append(dot_product)
    return result

class TestCaseInt8Sudot:
    def __init__(self, vec_a, vec_b, expected_res):
        self.vec_a = vec_a
        self.vec_b = vec_b
        self.expected_res = expected_res

def create_vsudot_int_test_cases():
    return [
        TestCaseInt8Sudot([1, 2, 3, 4, 5, 6, 7, 8], [1, 2, 3, 4, 5, 6, 7, 8], [204]),
        TestCaseInt8Sudot([-1, -2, -3, -4, -5, -6, -7, -8], [1, 2, 3, 4, 5, 6, 7, 8], [-204]),
        TestCaseInt8Sudot([1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1], [8]),
        TestCaseInt8Sudot([127, 127, 127, 127, 127, 127, 127, 127], [1, 1, 1, 1, 1, 1, 1, 1], [1016]),
        TestCaseInt8Sudot([0, 0, 0, 0, 0, 0, 0, 0], [1, 2, 3, 4, 5, 6, 7, 8], [0]),
        # New test cases
        TestCaseInt8Sudot([1, -1, 1, -1, 1, -1, 1, -1], [1, 1, 1, 1, 1, 1, 1, 1], [0]),
        TestCaseInt8Sudot([127, -128, 127, -128, 127, -128, 127, -128], [1, 1, 1, 1, 1, 1, 1, 1], [-4]),
        TestCaseInt8Sudot([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16], 
                          [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [36, 100]),
        TestCaseInt8Sudot([-128, -128, -128, -128, -128, -128, -128, -128], 
                          [1, 1, 1, 1, 1, 1, 1, 1], [-1024]),
        TestCaseInt8Sudot([127, 127, 127, 127, 127, 127, 127, 127], 
                          [-1, -1, -1, -1, -1, -1, -1, -1], [-1016]),
        TestCaseInt8Sudot([1, 10, 100, -100, -10, -1, 0, 50], 
                          [1, 1, 1, 1, 1, 1, 1, 1], [50]),
        TestCaseInt8Sudot([1, 2, 3, 4, 5, 6, 7, 8], 
                          [8, 7, 6, 5, 4, 3, 2, 1], [120]),
        TestCaseInt8Sudot([127, 126, 125, 124, 123, 122, 121, 120], 
                          [1, 2, 3, 4, 5, 6, 7, 8], [3080]),
        TestCaseInt8Sudot([-128, -127, -126, -125, -124, -123, -122, -121], 
                          [8, 7, 6, 5, 4, 3, 2, 1], [-3164]),
        TestCaseInt8Sudot([0, 0, 0, 0, 127, 127, 127, 127], 
                          [1, 1, 1, 1, 1, 1, 1, 1], [508]),
    ]

def main():
    vsudot_int_test_cases = create_vsudot_int_test_cases()
    print("Python VSUDOT INT Test Cases:")
    for i, test in enumerate(vsudot_int_test_cases):
        result = vsudot_python(test.vec_a, test.vec_b)
        
        status = "PASS" if result == test.expected_res else "FAIL"
        
        print(f"Test case {i + 1}: {status}")
        print(f"VecA: {test.vec_a}")
        print(f"VecB: {test.vec_b}")
        print(f"Expected Result: {test.expected_res}")
        print(f"Calculated Result: {result}")
        print()

if __name__ == "__main__":
    main()