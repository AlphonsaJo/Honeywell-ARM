# Define VSUBW function for ARM32
def vsubw_arm32(vecA, vecB):
    if len(vecA) != len(vecB):
        raise ValueError("Vectors must be of the same length for ARM32 VSUBW operation")

    result = []
    for i in range(len(vecA)):
        result.append(int(vecA[i]) - int(vecB[i]))

    return result

# Define VSUBW function for Thumb
def vsubw_thumb(vecA, vecB):
    if len(vecA) != len(vecB):
        raise ValueError("Vectors must be of the same length for Thumb VSUBW operation")

    result = []
    for i in range(len(vecA)):
        result.append(int(vecA[i]) - int(vecB[i]))

    return result


# Define the TestCase class
class TestCase:
    def __init__(self, vecA, vecB, expected_res):
        self.vecA = vecA
        self.vecB = vecB
        self.expected_res = expected_res

# Define test cases
vsubw_test_cases = [
    # Basic cases
    TestCase([10, 20, 30, 40], [1, 2, 3, 4], [9, 18, 27, 36]),
    TestCase([0, 0, 0, 0], [1, 2, 3, 4], [-1, -2, -3, -4]),
    TestCase([100, 200, 300, 400], [100, 200, 300, 400], [0, 0, 0, 0]),
    # Negative numbers and overflow cases
    TestCase([-10, -20, -30, -40], [-1, -2, -3, -4], [-9, -18, -27, -36]),
    TestCase([-2147483648, -2147483648], [-1, -1], [-2147483647, -2147483647]),
    # Large numbers
    TestCase([2147483647, 2147483647], [1, 1], [2147483646, 2147483646]),
    # Edge cases
    TestCase([], [], []),
    TestCase([0], [0], [0]),
    # Additional edge cases
    TestCase([0, -1, -2147483648, 2147483647], [0, -1, 2147483647, -2147483648], [0, 0, -4294967295, 4294967295]),
    TestCase([-1, -1, -1, -1], [-1, -1, -1, -1], [0, 0, 0, 0]),
    TestCase([2147483647, 2147483647, 2147483647, 2147483647], [2147483647, 2147483647, 2147483647, 2147483647], [0, 0, 0, 0]),
]

# Execute test cases for ARM32 VSUBW
print("ARM32 VSUBW Test Cases:")
for i, test in enumerate(vsubw_test_cases):
    result = vsubw_arm32(test.vecA, test.vecB)
    status = result == test.expected_res
    print(f"Test case {i + 1}: {'PASS' if status else 'FAIL'}")
    print(f"VecA: {test.vecA}")
    print(f"VecB: {test.vecB}")
    print(f"Expected Result: {test.expected_res}")
    print(f"Calculated Result: {result}\n")

# Execute test cases for Thumb VSUBW
print("Thumb VSUBW Test Cases:")
for i, test in enumerate(vsubw_test_cases):
    result = vsubw_thumb(test.vecA, test.vecB)
    status = result == test.expected_res
    print(f"Test case {i + 1}: {'PASS' if status else 'FAIL'}")
    print(f"VecA: {test.vecA}")
    print(f"VecB: {test.vecB}")
    print(f"Expected Result: {test.expected_res}")
    print(f"Calculated Result: {result}\n")
