#include <stdio.h>
#include <stdint.h>
// Define constants for test status
#define TestPass 0
#define TestFail 1
// Function to test AND with register values
int AND_reg(int regA, int regB, uint32_t expected_res) {
    int testStatus = TestPass;
    uint32_t result;
    asm volatile (
        "mov r3, %[regA]\n"
        "mov r5, %[regB]\n"
        "and %[res], r3, r5\n"
        : [res] "=r" (result)
        : [regA] "r" (regA), [regB] "r" (regB)
        : "r3", "r5"
    );
    if (result != expected_res)
        testStatus = TestFail;

    return testStatus;
}
// Main function to run the tests
int main() {
    int testStatus;
    printf("Running ARM AND instruction tests...\n");

    // AND tests
    testStatus = AND_reg(0xF0F0F0F0, 0x0F0F0F0F, 0x00000000);
    printf("AND_reg test 1: %s\n", testStatus == TestPass ? "PASS" : "FAIL");

    testStatus = AND_reg(0xFFFFFFFF, 0x12345678, 0x12345678);
    printf("AND_reg test 2: %s\n", testStatus == TestPass ? "PASS" : "FAIL");
    testStatus = AND_reg(0xFFFFFFFF, 0x12345678, 0x00000000);  

    printf("AND_reg test 3: %s\n", testStatus == TestPass ? "PASS" : "FAIL");
    testStatus = AND_reg(0xAAAAAAAA, 0x55555555, 0x00000000);
    printf("AND_reg test 4: %s\n", testStatus == TestPass ? "PASS" : "FAIL");

    testStatus = AND_reg(0x12345678, 0x87654321, 0x02244220);
    printf("AND_reg test 5: %s\n", testStatus == TestPass ? "PASS" : "FAIL");
    
    testStatus = AND_reg(0x12345678, 0x87654321, 0xFFFFFFFF);  
    printf("AND_reg test 6: %s\n", testStatus == TestPass ? "PASS" : "FAIL");

    testStatus = AND_reg(0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF);
    printf("AND_reg test 7: %s\n", testStatus == TestPass ? "PASS" : "FAIL");

    testStatus = AND_reg(0x00000000, 0xFFFFFFFF, 0x00000000);
    printf("AND_reg test 8: %s\n", testStatus == TestPass ? "PASS" : "FAIL");

    testStatus = AND_reg(0x12345678, 0x00000000, 0x00000000);
    printf("AND_reg test 9: %s\n", testStatus == TestPass ? "PASS" : "FAIL");

    testStatus = AND_reg(0x80000000, 0x00000001, 0x00000000);
    printf("AND_reg test 10: %s\n", testStatus == TestPass ? "PASS" : "FAIL");
    
    testStatus = AND_reg(0xAAAAAAAA, 0x55555555, 0xFFFFFFFF);  
    printf("AND_reg test 11: %s\n", testStatus == TestPass ? "PASS" : "FAIL");

    testStatus = AND_reg(0x7FFFFFFF, 0x7FFFFFFF, 0x7FFFFFFF);
    printf("AND_reg test 12: %s\n", testStatus == TestPass ? "PASS" : "FAIL");

    testStatus = AND_reg(0xAAAAAAAA, 0xFFFFFFFF, 0xAAAAAAAA);
    printf("AND_reg test 13: %s\n", testStatus == TestPass ? "PASS" : "FAIL");

    testStatus = AND_reg(0xF0F0F0F0, 0x0F0F0F0F, 0xFFFFFFFF);  
    printf("AND_reg test 14: %s\n", testStatus == TestPass ? "PASS" : "FAIL");

    printf("Finished running ARM AND instruction tests.\n");

    return 0;
}
