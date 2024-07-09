#include <iostream>
#include <vector>
#include <stdexcept>
#include <tuple>
#include <algorithm>
#include "arm_neon.h"

using namespace std;

// Widening subtraction function using ARM NEON intrinsics for ARM32 with inline assembly
static void vsubw_arm_neon(int16_t* vecA, int16_t* vecB, int32_t* result, size_t size) {
    for (size_t i = 0; i < size; i += 4) {
        int16x4_t a = vld1_s16(&vecA[i]);
        int16x4_t b = vld1_s16(&vecB[i]);
        int32x4_t res;

        asm volatile(
            "vsubw.s16 %q0, %q1, %q2"
            : "=w"(res)
            : "w"(a), "w"(b)
        );

        vst1q_s32(&result[i], res);
    }
}

// Widening subtraction function using ARM NEON intrinsics for Thumb with inline assembly
static void vsubw_thumb_neon(int16_t* vecA, int16_t* vecB, int32_t* result, size_t size) {
    for (size_t i = 0; i < size; i += 4) {
        int16x4_t a = vld1_s16(&vecA[i]);
        int16x4_t b = vld1_s16(&vecB[i]);
        int32x4_t res;

        asm volatile(
            "vsubw.s16 %q0, %q1, %q2"
            : "=w"(res)
            : "w"(a), "w"(b)
        );

        vst1q_s32(&result[i], res);
    }
}

class TestCaseInt16 {
public:
    vector<int16_t> vecA;
    vector<int16_t> vecB;
    vector<int32_t> expected_res;

    TestCaseInt16(const vector<int16_t>& a, const vector<int16_t>& b, const vector<int32_t>& res)
        : vecA(a), vecB(b), expected_res(res) {}
};

static vector<TestCaseInt16> create_vsubw_int_test_cases() {
    return {
        TestCaseInt16({10, 20, 30, 40}, {1, 2, 3, 4}, {9, 18, 27, 36}),
        TestCaseInt16({0, 0, 0, 0}, {1, 2, 3, 4}, {-1, -2, -3, -4}),
        TestCaseInt16({100, 200, 300, 400}, {100, 200, 300, 400}, {0, 0, 0, 0}),
        TestCaseInt16({-10, -20, -30, -40}, {-1, -2, -3, -4}, {-9, -18, -27, -36}),
        TestCaseInt16({32767, 32767, 32767, 32767}, {-1, -1, -1, -1}, {32768, 32768, 32768, 32768}),
        TestCaseInt16({-32768, -32768, -32768, -32768}, {1, 1, 1, 1}, {-32769, -32769, -32769, -32769}),
    };
}

int main() {
    vector<TestCaseInt16> vsubw_int_test_cases = create_vsubw_int_test_cases();

    cout << "ARM32 VSUBW INT Test Cases:" << endl;
    for (size_t i = 0; i < vsubw_int_test_cases.size(); ++i) {
        const TestCaseInt16& test = vsubw_int_test_cases[i];

        // Convert vectors to arrays for direct manipulation
        size_t size = test.vecA.size();
        int16_t vecA[size];
        int16_t vecB[size];
        int32_t result[size];

        copy(test.vecA.begin(), test.vecA.end(), vecA);
        copy(test.vecB.begin(), test.vecB.end(), vecB);

        vsubw_arm_neon(vecA, vecB, result, size);

        vector<int32_t> result_vec(result, result + size);

        bool statusA = (result_vec == test.expected_res);

        cout << "Test case " << i + 1 << " (ARM32): " << (statusA ? "PASS" : "FAIL") << endl;
        cout << "VecA: ";
        for (int val : test.vecA) cout << val << " ";
        cout << endl;
        cout << "VecB: ";
        for (int val : test.vecB) cout << val << " ";
        cout << endl;
        cout << "Expected Result: ";
        for (int val : test.expected_res) cout << val << " ";
        cout << endl;
        cout << "Calculated Result: ";
        for (int val : result_vec) cout << val << " ";
        cout << endl;
        cout << endl;
    }

    cout << "Thumb VSUBW INT Test Cases:" << endl;
    for (size_t i = 0; i < vsubw_int_test_cases.size(); ++i) {
        const TestCaseInt16& test = vsubw_int_test_cases[i];

        // Convert vectors to arrays for direct manipulation
        size_t size = test.vecA.size();
        int16_t vecA[size];
        int16_t vecB[size];
        int32_t result[size];

        copy(test.vecA.begin(), test.vecA.end(), vecA);
        copy(test.vecB.begin(), test.vecB.end(), vecB);

        vsubw_thumb_neon(vecA, vecB, result, size);

        vector<int32_t> result_vec(result, result + size);

        bool statusB = (result_vec == test.expected_res);

        cout << "Test case " << i + 1 << " (Thumb): " << (statusB ? "PASS" : "FAIL") << endl;
        cout << "VecA: ";
        for (int val : test.vecA) cout << val << " ";
        cout << endl;
        cout << "VecB: ";
        for (int val : test.vecB) cout << val << " ";
        cout << endl;
        cout << "Expected Result: ";
        for (int val : test.expected_res) cout << val << " ";
        cout << endl;
        cout << "Calculated Result: ";
        for (int val : result_vec) cout << val << " ";
        cout << endl;
        cout << endl;
    }

    return 0;
}
