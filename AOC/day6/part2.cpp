#include <iostream>
#include <string>
#include <fstream>
#include <vector>
#include <utility>
// #include <algorithm>

// #include <array> /
// #include <iterator>
// Function definition space
//
//
//
#define RESET   "\033[0m"       // Reset color
#define RED     "\033[31m"      // Red
#define GREEN   "\033[32m"      // Green
#define YELLOW  "\033[33m"      // Yellow
#define BLUE    "\033[34m"      // Blue

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

void printTableau(std::string arr[], const int &numberOfLines, const int &lengthOfLines) {
  char tempChar;
  for (int i = 0; i < numberOfLines; i++) {
    for (int j = 0; j < lengthOfLines; j++) {
      tempChar = arr[i][j];
      switch (tempChar)
      {
      case '.' :
        std::cout << RESET << '.';
        break;
      case '#' :
        std::cout << BLUE << '#' << RESET;
        break;
      case '@' :
        std::cout << YELLOW << '@' << RESET;
        break;
      default:
        std::cout << RED << tempChar << RESET;
        break;
      }
    }
    std::cout << std::endl; 
  }
}

void replaceX(std::string arr[], const int &numberOfLines, const int &lengthOfLines) {
  for (int i = 0; i < numberOfLines; i++) {
    for (int j = 0; j < lengthOfLines; j++) {
      if (arr[i][j] == 'X') {
        arr[i][j] = '.';
      }
    } 
  }
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

void simulateRunX(std::string arr[], const int &numberOfLines, const int &lengthOfLines, const std::pair<int, int> &pos) {
    // std::cout << position.first << "|" << position.second << std::endl;
  std::pair<int, int> position = {pos.first,pos.second};
  int isOutside = 0;
  int direction = 0;
  while (isOutside == 0) {
    switch (direction) {
      case 1:
        if (position.second+1 == lengthOfLines){
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
        if (position.first+1 == numberOfLines){
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
}

int simulateRunPath(std::string arr[], int isOutside, const int &numberOfLines, const int &lengthOfLines, const std::pair<int, int> &pos) {
  // std::cout << position.first << "|" << position.second << std::endl;
  std::pair<int, int> position = {pos.first, pos.second};
  int passes[numberOfLines][lengthOfLines] = {};

  int countIteration = 0;
  int direction = 0;
  while (isOutside == 0) {
    
    // for (int i = 0; i < numberOfLines; i++) {
    // // arr[i].replace(5,1,"@");
    // std::cout << arr[i] << std::endl;
    // }
    if (countIteration > 10000) {
      printTableau(arr,numberOfLines, lengthOfLines);
      std::cout << "Loop in iteration : " << countIteration<< std::endl;
      std::cout << "--------------------------------------------------------------------------------------------------" << std::endl;
      std::cout << "--------------------------------------------------------------------------------------------------" << std::endl;
      std::cout << "--------------------------------------------------------------------------------------------------" << std::endl;
      std::cout << "--------------------------------------------------------------------------------------------------" << std::endl;
    }
    
    countIteration++;
    if (passes[position.first][position.second] > 4) {
      std::cout << "somehow" << std::endl;
      isOutside = 2;
      return isOutside;
      break;
    }
    switch (direction) {
      case 1: // <--------------------------------------------------------------Case Right
        if (position.second+1 == lengthOfLines){
          arr[position.first].replace(position.second,1,">");
          isOutside = 1;
          return isOutside;
        }
        if (arr[position.first][position.second+1] == '#') {
          direction = (direction+1) % 4;
          break;
        }
        if (arr[position.first][position.second+1] == '>') {
          isOutside = 2;
          break;
        }
        arr[position.first].replace(position.second+1,1,"@");
        arr[position.first].replace(position.second,1,">");
        passes[position.first][position.second]++;
        position.second++;
        break;
      case 2: // <----------------------------------------------------------------Case Down
        if (position.first+1 == numberOfLines){
          arr[position.first].replace(position.second,1,"v");
          isOutside = 1;
          return isOutside;
        }
        if (arr[position.first+1][position.second] == '#') {
          direction = (direction+1) % 4;
          break;
        }
        if (arr[position.first+1][position.second] == 'v') {
          isOutside = 2;
          return isOutside;
        }
        arr[position.first+1].replace(position.second,1,"@");
        arr[position.first].replace(position.second,1,"v");
        passes[position.first][position.second]++;
        position.first++;
        break;
      case 3: //<------------------------------------------------------------------Case Left
        if (position.second == 0){
          arr[position.first].replace(position.second,1,"<");
          isOutside = 1;
          return isOutside;
        }
        if (arr[position.first][position.second-1] == '#') {
          direction = (direction+1) % 4;
          break;
        }
        if (arr[position.first][position.second-1] == '<') {
          isOutside = 2;
          return isOutside;
        }
        arr[position.first].replace(position.second-1,1,"@");
        arr[position.first].replace(position.second,1,"<");
        passes[position.first][position.second]++;
        position.second--;
        break;
      default: //<-------------------------------------------------------------Case Up
        if (position.first == 0){
          arr[position.first].replace(position.second,1,"^");
          isOutside = 1;
          return isOutside;
        }
        if (arr[position.first-1][position.second] == '#') {
          direction = (direction+1) % 4;
          break;
        }
        if (arr[position.first-1][position.second] == '^') {
          isOutside = 2;
          return isOutside;
        }
        arr[position.first-1].replace(position.second,1,"@");
        arr[position.first].replace(position.second,1,"^");
        passes[position.first][position.second]++;
        position.first--;
    }
  }
  return 0;
}

void copyArray(const std::string arr1[], std::string arr2[], int numberOfLines) {
  for (int i = 0; i < numberOfLines; i++) {
    arr2[i] = arr1[i];
  }
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
  std::string paths[lineCount];
  std::string arrNoX[lineCount];
  for (int i = 0; i < lineCount; i++) {
    arr[i] = lines[i];
  }  
  copyArray(arr, arrNoX, lineCount);
  const std::pair<int,int> position = getPosition(arr,lineCount,lineLength);

  std::cout << "Does it run?" << std::endl;
  // for (int i = 0; i < lineCount; i++) {
  //   arr[i].replace(5,1,"@");
  //   std::cout << arr[i] << std::endl;
  simulateRunX(arr,lineCount,lineLength, position);
  copyArray(arr,paths,lineCount);
  int countCheckedPaths = 0;
  int isOutside = 0;
  int countPaths = 0;
  for (int i = 0; i < lineCount; i++) {
    for (int j = 0; j < lineLength; j++) {
      if (i == position.first && j == position.second) {
        break;
      } 
      if (arr[i][j]=='X') {
        copyArray(arrNoX, paths, lineCount);
        isOutside = 0;
        paths[i].replace(j,1,"#");
        isOutside = simulateRunPath(paths, isOutside, lineCount, lineLength, position);
        std::cout << "This many checked paths : " << countCheckedPaths << std::endl;
        countCheckedPaths++;
        if (isOutside == 2) {
          std::cout << "what is happening"<< std::endl;
          countPaths++;
        }
      }
    }
  }
  // simulateRunPath(paths,isOutside,lineCount,lineLength, position);
  // }
  // for (int i = 0; i < lineCount; i++) {
  //   // arr[i].replace(5,1,"@");
  //   std::cout << arr[i] << std::endl;
  // }
  std::cout << "Number of Xs in original problem :" << countX(arr,lineCount,lineLength) << std::endl;
  std::cout << "Number of loops found :" << countPaths << std::endl;
  return 0;
}




