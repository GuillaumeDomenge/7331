#include <algorithm>
#include <fstream>
#include <iostream>
#include <string>
#include <vector>
#include <cmath>

template <typename T>

void printJaggedVector(const std::vector<std::vector<char>> &jagged) {
  for (const auto &row : jagged) {
    for (const auto &element : row) {
      std::cout << element << " ";
    }
    std::cout << '\n'; // Newline after each row
  }
}

void printVector(const std::vector<int>& vec) {
    std::cout << "[ ";
    for (const auto& elem : vec) {
        std::cout << elem << " ";
    }
    std::cout << "]";
}

void printVectorOfVectorsOfInts(const std::vector<std::vector<int>> &vec) {
  for (const auto &row : vec) {
    for (const auto& element : row) {
      std::cout << element << "~";
    }
    std::cout << std::endl;
  }
}
void printVectorOfVectorsOfStrings(const std::vector<std::string> &vec) {
  for (const auto &row : vec) {
    std::cout << row << std::endl;
  }
}


bool isBreakingRule(const std::vector<std::string> &rules , const int &inti, const int &intj) {
  std::string tempString = std::to_string(intj) + "|" + std::to_string(inti);
  if (std::find(rules.begin(),rules.end(), tempString) != rules.end()) {
    std::cout << "Breaking rule : " << tempString;
    return true;
  }else {
    return false;
  }
}

std::vector<std::string> joinRules(const std::vector<int> &rl, const std::vector<int> &rr) {
  std::vector<std::string>  answRules;
  for (int i = 0; i < rl.size(); i++ ) {
    std::string tempString = std::to_string(rl[i]) + "|" + std::to_string(rr[i]);
    answRules.push_back(tempString);
  }
  return answRules;
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
        if (element == ',') { //<------------Defining character break to
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

  std::vector<std::string> rulesString = joinRules(rulesL,rulesR);

  int sum_correct = 0;
  int count_incorrect = 0;
  for (const auto &instruction : instructions){ 
    int is_correct = 1;
    for (int i = 0; i < instruction.size()-1; i++){
      for (int j = i+1; j < instruction.size(); j++){
        if (isBreakingRule(rulesString, instruction[i], instruction[j])){
          is_correct = 0;
          std::cout << "    Instruction : ";
          printVector(instruction);
          std::cout << " broke a rule at : " << std::endl;
          std::cout << "i = " << instruction[i]<< ", j = " << instruction[j] << std::endl;
          break;
        }
        if (is_correct == 0) break;
      } 
    }
    if (is_correct == 1) {
      sum_correct += instruction[ (int)std::floor( (double)instruction.size()/2)];
    }else{
      count_incorrect++;
    }
  }
  std::cout << "Count_incorrect " << count_incorrect << std::endl; 
  std::cout << "The sum is: "<<sum_correct<<std::endl;
  std::cout << rulesL.size() << std::endl;
  std::cout << rulesR.size() << std::endl;

  // printVectorOfVectorsOfStrings(rulesString);
  std::cout << instructions.size() <<std::endl;
  return 0;
}
