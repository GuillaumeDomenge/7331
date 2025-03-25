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


void copyArray(const std::string arr1[], std::string arr2[], int numberOfLines) {
  for (int i = 0; i < numberOfLines; i++) {
    arr2[i] = arr1[i];
  }
}

std::vector<std::pair<int, int>> getBlockLocations(const std:: string arr[], const int &numberOfLines, const int &lengthOfLines) {
  std::vector<std::pair<int, int>> tempVec;
  for (int i = 0; i < numberOfLines; i++) {
    for (int j = 0; j < lengthOfLines; j++) {
      if (arr[i][j] == '#') {
        tempVec.push_back({i,j});
      }
    }
  }
  return tempVec;
}

void getNextPositionDirection(const std::vector<std::pair<int, int>> &obtacles, std::pair<int, int> &position, char &direction, const int &numberOfLines, const int &lengthOfLines) {
  std::pair<int, int> tempPos = {numberOfLines, lengthOfLines};
  switch (direction) {
    case 'E': //<-------------------------------------------------------------Case East
      for (const auto& block : obtacles) {
        if (block.first == position.first && block.second > position.second && block.second < tempPos.second) {
          tempPos.first = block.first;
          tempPos.second = block.second;
        }
      }
      if (tempPos.second == numberOfLines) {
        position.second = numberOfLines;
      }else{
        position.second = tempPos.second-1;
      }
      direction = 'S';
      break;
    case 'S': //<--------------------------------------------------------------Case South
      for (const auto& block : obtacles) {
        if (block.first > position.first && block.second == position.second && block.first < tempPos.first) {
          tempPos.first = block.first;
          tempPos.second = block.second;
        }
      }
      if (tempPos.second == numberOfLines) {
        position.first = lengthOfLines;
      }else{
        position.first = tempPos.first-1;
      }
      direction = 'W'; 
      break;
    case 'W': // <---------------------------------------------------------------Case West
      for (const auto& block : obtacles) {
        if (block.first == position.first && block.second < position.second && block.second > tempPos.second) {
          tempPos.first = block.first;
          tempPos.second = block.second;
        }
      }
      if (tempPos.second == numberOfLines) {
        position.second = numberOfLines;
      }else{
        position.second = tempPos.second-1;
      }
      direction = 'N';
      break;
    default://<-------------------------------------------------------------------Case North
      for (const auto& block : obtacles) {
        if (block.first < position.first && block.second == position.second && block.first > tempPos.first) {
          tempPos.first = block.first;
          tempPos.second = block.second;
        }
      }
      if (tempPos.second == numberOfLines) {
        position.first = lengthOfLines;
      }else{
        position.first = tempPos.first+1;
      }
      direction = 'E';
  }
}

bool isInObstacles(const std::vector<std::pair<int, int>> &vec, const std::pair<int, int> &instance) {
  for (const auto& element : vec) {
    if (element == instance) return true;
  }
  return false;
}

bool isInPaths(const std::vector<std::pair<std::pair<int,int>, char>> &vec, const std::pair<std::pair<int, int>, char> &instance) {
  for (const auto& element : vec) {
    if (element == instance) return true;
  }
  return false;
}

int simulatePaths(const std::vector<std::pair<int, int>> &obtacles, std::pair<int, int> &position, const std::pair<int, int> &dimensions) {
  int isOutside = 0;
  char direction = 'N';
  std::vector<std::pair<std::pair<int, int>, char>> paths;
  paths.push_back({position, direction});
  while (isOutside == 0) {
    getNextPositionDirection(obtacles, position, direction, dimensions.first, dimensions.second);
    if (isInPaths(paths, {position, direction})) {
      isOutside = 2;
      break;
    }
    paths.push_back({position, direction});
    if (position.first == dimensions.first || position.second == dimensions.second) {
      isOutside = 1;
      break;
    }
  }
  return isOutside;
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

  const std::pair<int, int> dimensions = {lineCount, lineLength};

  std::string arr[lineCount];
  std::string paths[lineCount];
  std::string arrNoX[lineCount];
  for (int i = 0; i < lineCount; i++) {
    arr[i] = lines[i];
  }  
  copyArray(arr, arrNoX, lineCount);
  std::pair<int,int> position = getPosition(arr,lineCount,lineLength);
  int countLoops = 0;


  std::cout << "Does it run?" << std::endl;
  for (int i = 0; i < lineCount; i++) {
    for (int j = 0; j < lineLength; j++) {
      if ((i != position.first || j != position.second) && arr[i][j] != '#') {
        arrNoX[i][j] = '#';
        std::vector<std::pair<int, int>> tempVec = getBlockLocations(arrNoX, dimensions.first, dimensions.second);
        int tempInt = simulatePaths(tempVec, position, dimensions);
        if ( tempInt == 2) {
          countLoops++;
        }
      } 
    }
  }

  std::cout << "Number of loops found : " << countLoops << std::endl;
  std::cout << "Number of Xs in original problem :" << countX(arr,lineCount,lineLength) << std::endl;
  return 0;
}




