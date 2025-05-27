#include <iostream>
#include <vector>
#include <string>
#include <sstream>

using namespace std;

vector<long long> stringToVect(const string &text) {
    vector<long long> vec;
    istringstream iss(text);
    long long num;
    while (iss >> num) {
        vec.push_back(num);
    }
    return vec;
}

vector<long long> blink(const vector<long long> &vec) {
    vector<long long> temp_vec;
    for (long long num : vec) {
        if (num == 0) {
            temp_vec.push_back(1);
        } else {
            string num_str = to_string(num);
            if (num_str.length() % 2 == 0) {
                int half_len = num_str.length() / 2;
                string first_part = num_str.substr(0, half_len);
                string second_part = num_str.substr(half_len);
                temp_vec.push_back(stoll(first_part));
                temp_vec.push_back(stoll(second_part));
            } else {
                temp_vec.push_back(num * 2024LL);  // Using LL suffix for long long literal
            }
        }
    }
    return temp_vec;
}

// void printVector(const vector<long long> &vec) {
//     cout << "[";
//     for (size_t i = 0; i < vec.size(); ++i) {
//         cout << vec[i];
//         if (i != vec.size() - 1) {
//             cout << ", ";
//         }
//     }
//     cout << "]" << endl;
// }

int main() {
    string input = "5178527 8525 22 376299 3 69312 0 275";
    string example = "125 17";
    int n = 75;

    vector<long long> vec = stringToVect(input);
    // cout << "Initial vector: ";
    // printVector(vec);

    for (int i = 0; i < n; i++) {
        vec = blink(vec);
        cout << "iter " << i << endl;
        // printV ector(vec);
        
        // Early exit if vector gets too large
        // if (vec.size() > 1000) {
        //     cout << "Vector too large, stopping early..." << endl;
        //     break;
        // }
    }

    cout << "Final vector size: " << vec.size() << endl;
    return 0;
}
