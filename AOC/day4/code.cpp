#include <iostream>
#include <fstream>
#include <vector>
#include <string>

int main() {
    std::ifstream file("input.txt"); // Open the file
    if (!file) {
        std::cerr << "Error opening file!" << std::endl;
        return 1;
    }

    std::vector<std::vector<char>> lines; // Vector to store lines as vector of characters
    std::string line;

    while (std::getline(file, line)) { // Read each line
        std::vector<char> charVec(line.begin(), line.end()); // Convert line to vector<char>
        lines.push_back(charVec); // Store in main vector
    }

    file.close(); // Close the file

    const int NLINES = lines.size();
    const int NCHAR  = lines[0].size();

    int count = 0;

    for(int i = 1; i < NLINES-1 ; i++){
        for(int j = 1; j < NCHAR-1 ; j++){
            if (lines[i][j] == 'A') { 
                std::cout << "Here at A\n";
                if (lines[i-1][j-1] == 'M' && lines[i+1][j+1] == 'S'){
                    std::cout << "Here at B\n";
                    if (lines[i+1][j-1] == 'M' && lines[i-1][j+1] == 'S') {
                        count++;
                    }
                    else if(lines[i+1][j-1] == 'S' && lines[i-1][j+1] == 'M') {
                        count++;
                    }
                }
                else if(lines[i-1][j-1] =='S' && lines[i+1][j+1] == 'M'){
                    std::cout << "Here at B\n";
                    if (lines[i+1][j-1] == 'M' && lines[i-1][j+1] == 'S') {
                        count++;
                    }
                    else if(lines[i+1][j-1] == 'S' && lines[i-1][j+1] == 'M') {
                        count++;
                    }
                }
            }
        }
    }
    std::cout << count;
    return 0;
}
