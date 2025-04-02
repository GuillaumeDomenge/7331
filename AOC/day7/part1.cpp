#include <iostream>
#include <string>
#include <vector>
#include <fstream>
#include <algorithm>







int solveEq(int Y, std::vector<long> &list, int index){
  if (index == 0 && Y == list[0]) {
    return 1;
  }
  if (Y < 0) {
    return 0;
  }
  if (list[index] !=0 && Y % list[index] == 0) {
    return std::max(solveEq(Y/list[index], list, index - 1),solveEq(Y-list[index], list, index - 1));
  }
  return solveEq(Y-list[index], list, index - 1);
}

void getVectors(std::vector<std::string> &lines, std::vector<long> &Ys, std::vector<std::vector<long>> &nums) {
  for (const auto &row : lines) {
    // std::cout << "Trying row"<< std::endl;
    std::vector<long> temp_numvec;
    std::string temp_string;
    for (const auto &element : row) {
      // std::cout << element;
      if (element == ':') {
        Ys.push_back(std::stol(temp_string));
        temp_string = "";
        continue;
      }
      if (element == ' ') {
        // std::cout << "Trying" << std::endl;
        try {
          temp_numvec.push_back(std::stol(temp_string));
          temp_string = "";
          continue;
        } catch (...) {}
      }
      temp_string.push_back(element);
    }
    temp_numvec.push_back(std::stol(temp_string));
    nums.push_back(temp_numvec);
    // std::cout << std::endl;
  }
}

long calAnswer(const std::vector<long> &Ys, std::vector<std::vector<long>> &Nums, const int line_count) {
  int counter = 0;
  for (int i = 0; i < line_count ; i++) {
    if (solveEq(Ys[i], Nums[i], Nums[i].size()-1) == 1) {
      counter++;
    }
  }
  return counter;
}

int main() {
  std::ifstream file("/home/guillaume/Documents/7331/AOC/day7/input.txt");
  if (!file) {
    std::cerr << "Error opening file!" << std::endl;
    return 1;
  }

  int line_count = 0;
  std::string line;

  std::vector<std::string> lines;
  while (std::getline(file, line)) {
    line_count ++;
    lines.push_back(line);
  }
  std::vector<long> vec_Ys;
  std::vector<std::vector<long>> vec_numbers;
  std::cout <<"before get getVectors"<<std::endl;
  getVectors(lines, vec_Ys, vec_numbers);
  std::cout<<vec_numbers[847].size()<<std::endl;
  for (int j = 0; j < vec_numbers[847].size();j++) {
    std::cout << vec_numbers[847][j]<< " ";
  }
  // for (int i=0; i<vec_Ys.size();i++) {
  //   std::cout<<vec_Ys[i]<<": ";
  //   for (int j = 0; j < vec_numbers[i].size();j++) {
  //     std::cout<<" "<<vec_numbers[i][j];
  //   }
  //   std::cout<<std::endl;
  //   
  // }
  std::cout<<"before calAnswer"<< std::endl;
  int answer = calAnswer(vec_Ys, vec_numbers, line_count);
  std::cout << answer<<std::endl;


  return 0;
}
