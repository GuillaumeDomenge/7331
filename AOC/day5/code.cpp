#include <iostream>
#include <fstream>
#include <vector>
#include <string>

int main() {
    std::ifstream file("/home/guillaume/Documents/7331/AOC/day5/input.txt");
    if (!file) {
        std::cerr << "Error opening file!" << std::endl;
        return 1;
    }


    std::vector<std::vector<char>> lines;
    std::string line;

    while (std::getline(file, line)) {
        std::vector<char> charVec(line.begin(), line.end());
        lines.push_back(charVec);
    }

    file.close();
    const int NLINES = lines.size();

    for(int i = 1; i < NLINES-1 ; i++){
        int nchar = lines[i].size(); 
        for(int j = 1; i < nchar ; i++){
            std::cout << lines[i][j];
        }
        std::cout << std::endl;
    }
}
