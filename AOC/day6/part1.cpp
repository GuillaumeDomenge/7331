#include <iostream>
#include <string>
#include <fstream>
#include <vector>
#include <utility>
// #include <iterator>
// Function definition space
//
//
//

std::pair<int, int> getPosition(std::string arr[], const int &numberOfLines, const int &lengthOfLines) {
  int positionY = 0;
  int positionX = 0;
  std::pair<int, int> tempPair = {0,0};
  for (int i = 0; i < numberOfLines; i++) {
    positionX = 0;
    for (int j = 0; j < lengthOfLines; j++) {
      if (arr[i][j] == '^') {
        tempPair = {positionY,positionX};
        return tempPair;
      }
      positionX++;
    }
    positionY++;
  }
  return tempPair; 
}

int countX(std::string arr[], const int &numberOfLines, const int &lengthOfLines) {
  int numberofX = 0;
  for (int i = 0; i < numberOfLines; i++) {
    for (int j = 0; j < lengthOfLines; j++) {
      if (arr[i][j] == 'X') {
        numberofX++;
      }
    }
  }
  return numberofX;
}





// Main code
//
int main() {
  std::ifstream file("/home/guillaume/Documents/7331/AOC/day6/input.txt");
  if (!file) {
    std::cerr << "Error opening file!" << std::endl;
    return 1;
  }

  int lineCount = 0;
  int lineLength = 0;
  std::string line;


  std::vector<std::string> lines;
  while (std::getline(file, line)) {
    lineCount++;
    // std::cout << lineCount << std::endl;
    lines.push_back(line);
    lineLength = line.length();
  }


  std::string arr[lineCount];
  for (int i = 0; i < lineCount; i++) {
    arr[i] = lines[i];
  }  


  std::cout << "Does it run?" << std::endl;
  // for (int i = 0; i < lineCount; i++) {
  //   arr[i].replace(5,1,"@");
  //   std::cout << arr[i] << std::endl;
  // }
  std::pair<int,int> position = getPosition(arr,lineCount,lineLength);
  // std::cout << position.first << "|" << position.second << std::endl;
  // std::cout << arr[52][72];
  int isOutside = 0;
  int direction = 0;
  while (isOutside == 0) {
    switch (direction) {
      case 1:
        if (position.second+1 == lineLength){
          arr[position.first].replace(position.second,1,"X");
          isOutside = 1;
          break;
        }
        if (arr[position.first][position.second+1] == '#') {
          direction = (direction+1) % 4;
          break;
        }
        arr[position.first].replace(position.second+1,1,"^");
        arr[position.first].replace(position.second,1,"X");
        position.second++;
        break;
      case 2:
        if (position.first+1 == lineCount){
          arr[position.first].replace(position.second,1,"X");
          isOutside = 1;
          break;
        }
        if (arr[position.first+1][position.second] == '#') {
          direction = (direction+1) % 4;
          break;
        }
        arr[position.first+1].replace(position.second,1,"^");
        arr[position.first].replace(position.second,1,"X");
        position.first++;
        break;
      case 3:
        if (position.second == 0){
          arr[position.first].replace(position.second,1,"X");
          isOutside = 1;
          break;
        }
        if (arr[position.first][position.second-1] == '#') {
          direction = (direction+1) % 4;
          break;
        }
        arr[position.first].replace(position.second-1,1,"^");
        arr[position.first].replace(position.second,1,"X");
        position.second--;
        break;
      default:
        if (position.first == 0){
          arr[position.first].replace(position.second,1,"X");
          isOutside = 1;
          break;
        }
        if (arr[position.first-1][position.second] == '#') {
          direction = (direction+1) % 4;
          break;
        }
        arr[position.first-1].replace(position.second,1,"^");
        arr[position.first].replace(position.second,1,"X");
        position.first--;
    }
  }
  for (int i = 0; i < lineCount; i++) {
    // arr[i].replace(5,1,"@");
    std::cout << arr[i] << std::endl;
  }
  std::cout << countX(arr,lineCount,lineLength);
  return 0;
}




