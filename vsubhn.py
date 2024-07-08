# Define VSUBHN function for ARM32
def vsubhn_arm32(vecA, vecB):
    if len(vecA) != len(vecB):
        raise ValueError("Vectors must be of the same length for ARM32 VSUBHN operation")

    result = []
    for i in range(len(vecA)):
        # Subtract and then narrow the result to 16 bits
        diff = vecA[i] - vecB[i]
        narrowed_diff = diff & 0xFFFF  # Keep only the lower 16 bits
        result.append(narrowed_diff)

    return result

# Define VSUBHN function for Thumb
def vsubhn_thumb(vecA, vecB):
    if len(vecA) != len(vecB):
        raise ValueError("Vectors must be of the same length for Thumb VSUBHN operation")

    result = []
    for i in range(len(vecA)):
        # Subtract and then narrow the result to 16 bits
        diff = vecA[i] - vecB[i]
        narrowed_diff = diff & 0xFFFF  # Keep only the lower 16 bits
        result.append(narrowed_diff)

    return result


# Define the TestCase class
class TestCase:
    def __init__(self, vecA, vecB, expected_res):
        self.vecA = vecA
        self.vecB = vecB
        self.expected_res = expected_res

# Define test cases
vsubhn_test_cases = [
    # Basic cases
    TestCase([10, 20, 30, 40], [1, 2, 3, 4], [9, 18, 27, 36]),
    TestCase([0, 0, 0, 0], [1, 2, 3, 4], [0xFFFF, 0xFFFE, 0xFFFD, 0xFFFC]),
    TestCase([100, 200, 300, 400], [100, 200, 300, 400], [0, 0, 0, 0]),
    # Negative numbers and overflow cases
    TestCase([-10, -20, -30, -40], [-1, -2, -3, -4], [0xFFF7, 0xFFEC, 0xFFE1, 0xFFD6]),
    TestCase([-2147483648, -2147483648], [-1, -1], [1, 1]),
    # Large numbers
    TestCase([2147483647, 2147483647], [1, 1], [0xFFFE, 0xFFFE]),
    # Edge cases
    TestCase([], [], []),
    TestCase([0], [0], [0]),
    # Additional edge cases
    TestCase([0, -1, -2147483648, 2147483647], [0, -1, 2147483647, -2147483648], [0, 0, 0x8001, 0x7FFF]),
    TestCase([-1, -1, -1, -1], [-1, -1, -1, -1], [0, 0, 0, 0]),
    TestCase([2147483647, 2147483647, 2147483647, 2147483647], [2147483647, 2147483647, 2147483647, 2147483647], [0, 0, 0, 0]),
]

# Execute test cases for ARM32 VSUBHN
print("ARM32 VSUBHN Test Cases:")
for i, test in enumerate(vsubhn_test_cases):
    result = vsubhn_arm32(test.vecA, test.vecB)
    status = result == test.expected_res
    print(f"Test case {i + 1}: {'PASS' if status else 'FAIL'}")
    print(f"VecA: {test.vecA}")
    print(f"VecB: {test.vecB}")
    print(f"Expected Result: {test.expected_res}")
    print(f"Calculated Result: {result}\n")

# Execute test cases for Thumb VSUBHN
print("Thumb VSUBHN Test Cases:")
for i, test in enumerate(vsubhn_test_cases):
    result = vsubhn_thumb(test.vecA, test.vecB)
    status = result == test.expected_res
    print(f"Test case {i + 1}: {'PASS' if status else 'FAIL'}")
    print(f"VecA: {test.vecA}")
    print(f"VecB: {test.vecB}")
    print(f"Expected Result: {test.expected_res}")
    print(f"Calculated Result: {result}\n")
