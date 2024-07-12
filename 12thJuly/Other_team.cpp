#include <iostream>
#include <vector>
#include <stdexcept>
#include <cmath>
#include <tuple>
#include <algorithm>

using namespace std;

vector<float> vsub_arm_32(const vector<float>& vecA, const vector<float>& vecB, const string& size= "F32") {
    if (vecA.size() != vecB.size()){
        throw invalid_argument("vectors must be of the same length for ARM32 VSUB operation");
    }

    vector<float> result(vecA.size());
    for (size_t i =0; i < vecA.size(); ++i){
        if (size == "F32" || size == "F16" || size == "F64"){
            result[i] = vecA[i] - vecB[i];
        }
        else{
            throw invalid_argument("Unsupported data type size");
        }
    }
    return result;
}
vector<float> vsub_thumb_fp(const vector<float>& vecA, const vector<float>& vecB, const string& size= "F32") {
    if (vecA.size() != vecB.size()){
        throw invalid_argument("vectors must be of the same length for thumb VSUB operation");
    }

    vector<float> result(vecA.size());
    for (size_t i =0; i < vecA.size(); ++i){
        if (size == "F32" || size == "F16" || size == "F64"){
            result[i] = vecA[i] - vecB[i];
        }
        else{
            throw invalid_argument("Unsupported data type size");
        }
    }
    return result;
}

tuple<int, int, int, int> nczv_arm32_fp(const vector<float>& vec) {
    int N= any_of(vec.begin(), vec.end(), [](float x) {return x < 0;}) ? 1 : 0;
    int Z= all_of(vec.begin(), vec.end(), [](float x) {return x < 0;}) ? 1 : 0;
    int C=0;
    int V=0;
    return make_tuple(N, Z, C, V);
}

tuple<int, int, int, int> nczv_thumb_fp(const vector<float>& vec) {
    int N= any_of(vec.begin(), vec.end(), [](float x) {return x < 0;}) ? 1 : 0;
    int Z= all_of(vec.begin(), vec.end(), [](float x) {return x < 0;}) ? 1 : 0;
    int C=0;
    int V=0;
    return make_tuple(N, Z, C, V);
}
class testCase {
public:
    vector<float> vecA;
    vector<float> vecB;
    vector<float> expected_res;

    testCase(const vector<float>& a, const vector<float>& b, const vector<float>& res)
        : vecA(a), vecB(b), expected_res(res) {}

};
int main(){
    vector<testCase> vsub_fp_test_cases = {
        testCase({10.50, 20.75, 30.35, 40.80}, {1.25, 2.50, 3.75, 4.00}, {9.25, 18.25, 26.50, 36.80}),
        testCase({0.00, 0.00, 0.00, 0.00}, {1.10, 2.20, 3.30, 4.40}, {-1.10, -2.20, -3.30, -4.40}),
        testCase({100.99, 200.99, 300.99, 400.99}, {100.99, 200.99, 300.99, 400.99}, {0.00, 0.00, 0.00, 0.00}),
        testCase({-10.50, -20.75, -30.25, -40.80}, {-1.25, -2.50, -3.75, -4.00}, {-9.25, -18.25, -26.50, -36.80}),
        testCase({-2147483648.00, -2147483548.00}, {-1.00, -1.00}, {-2147483647.00, -2147483647.00}),
        testCase({2147483648.00, 2147483548.00}, {1.00, 1.00}, {2147483647.00, 2147483647.00}),
        testCase({}, {}, {}),
        testCase({0.00}, {0.00}, {0.00}),

    }
}
    cout << "ARM32 VSUB FP Test Cases:" << endl;
    for (const string& size: {"F32", "F16", "F64"}){
        cout << "Testing operand size: "<< size << endl;
        for (size_t i=0; i < vsub_fp_test_cases.size(); i++){
            const testCase& test = vsub_fp_test_cases[i];
            vector<float> result = vsub_arm32_fp(test.vecA, test.vecB, size);
            bool status = result == test.expected_res;
            auto nczv = nczv_arm_32_fp(result);
            cout << "Test Case" << i + 1 <<";" << (status ? "Pass" : "Fail") << endl;
            cout << "vecA: ";
            for (float val : test.vecA) cout << val << "";
            cout << endl;
            cout << "vecB: ";
            for (float val : test.vecB) cout << val << "";
            cout << endl;
            cout << "Expected REsult";
            for (float val : test.expected_res) cout << val << "";
            cout << endl;
            cout <<"calculated result;v" ;
            for (float val : result) cout << val << "";
            cout << endl;
            cout <<"NCZV; " << get<0>(nczv) << "," <<get<1>(nczv) <<", " <<get<2>(nczv)<<","<< get<3>(nczv) << endl;
            cout << endl;
            }
        }

    cout << "Thumbs VSUB FP Test Cases:" << endl;
    for (const string& size: {"F32", "F16", "F64"}){
        cout << "Testing operand size: "<< size << endl;
        for (size_t i=0; i < vsub_fp_test_cases.size(); i++){
            const testCase& test = vsub_fp_test_cases[i];
            vector<float> result = vsub_arm32_fp(test.vecA, test.vecB, size);
            bool status = result == test.expected_res;
            auto nczv = nczv_arm_32_fp(result);
            cout << "Test Case" << i + 1 <<";" << (status ? "Pass" : "Fail") << endl;
            cout << "vecA: ";
            for (float val : test.vecA) cout << val << "";
            cout << endl;
            cout << "vecB: ";
            for (float val : test.vecB) cout << val << "";
            cout << endl;
            cout << "Expected REsult";
            for (float val : test.expected_res) cout << val << "";
            cout << endl;
            cout <<"calculated result;v" ;
            for (float val : result) cout << val << "";
            cout << endl;
            cout <<"NCZV; " << get<0>(nczv) << "," <<get<1>(nczv) <<", " <<get<2>(nczv)<<","<< get<3>(nczv) << endl;
            cout << endl;
            }
        }
        return 0;

    }
