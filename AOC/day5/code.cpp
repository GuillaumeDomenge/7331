
#include <fstream>
#include <iostream>
#include <string>
#include <vector>

void printJaggedVector(const std::vector<std::vector<char>> &jagged) {
  for (const auto &row : jagged) {
    for (const auto &element : row) {
      std::cout << element << " ";
    }
    std::cout << '\n'; // Newline after each row
  }
}

void printVectorOfVectorsOfInts(const std::vector<std::vector<int>> &vec) {
  for (const auto &row : vec) {
    for (const auto& element : row) {
      std::cout << element << "~";
    }
    std::cout << std::endl;
  }
}


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

  std::vector<int> rulesL;
  std::vector<int> rulesR;
  std::vector<std::vector<int>> instructions;

  int isrules = 1;
  int isleft;
  for (const auto &row : lines) { //<------------------------Iterating through
                                  // the lines of lines var
    isleft = 1;
    std::string leftnum = "";
    std::string rightnum = "";
    if (row.size() < 2) { //<----------------------------------Switching from
                          // writing rules to instructions
      isrules = 0;
    } else if (isrules == 0) { //<-----------------------------Case when writing
                               // instrucctions
      std::vector<int> tInstruc;
      std::string tempString;
      for (const auto &element :
           row) { //<------------Iterating over row elements for instructions
        if (element == ',') { //<------------Defining character breake to
                              // diferentiate numbers
          try {
            tInstruc.push_back(std::stoi(tempString));
          } catch (const std::exception &e) {
            std::cout << "stoi error --- " << tempString << std::endl;
          }
          tempString = "";
        } else {
          tempString.push_back(element);
        }
      }
      instructions.push_back(tInstruc);
    } else { //<----------------------------------------Case when writing rules
      for (const auto &element :
           row) { //<----------Iterating over row elements for rules
        if (isleft == 0) {
          rightnum.push_back(element);
        } else if (element == '|') { //<-------------Switching from writing
                                     // lefthand rule to righthand
          isleft = 0;
        } else {
          leftnum.push_back(element);
        }
      }
      try {
        rulesL.push_back(std::stoi(leftnum));
        rulesR.push_back(std::stoi(rightnum));
      } catch (std::exception &e) {
        std::cout << "stoi error ---" << leftnum << "--- & ---" << rightnum
                  << "---" << std::endl;
      }
    }
  }

  // for (const auto &element : rulesR) {
  //   std::cout << element << std::endl;
  // }
  // for (int i = 0; rulesL.size()-1; i++) {
  //   std::cout << rulesL[i] << " | " << rulesR[i] << std::endl;
  // }
  // std::cout << str;
  // printJaggedVector(lines);
  printVectorOfVectorsOfInts(instructions);
  std::cout << instructions.size() <<std::endl;
  return 0;
}
