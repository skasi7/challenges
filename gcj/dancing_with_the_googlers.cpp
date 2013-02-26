#include <algorithm>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>

void challenge()
{
  std::string input;
  std::getline(std::cin, input);

  int googlers, surprises, target;
  std::vector<int> scores;
  {
    std::istringstream istr(input);
    istr >> googlers >> surprises >> target;
    scores.reserve(googlers);

    int score;
    for (int i = 0; i < googlers; ++i)
    {
      istr >> score;
      scores.push_back(score);
    }
  }

  int min_score = std::max(3 * target - 2, target),
      min_surprise_score = std::max(3 * target - 4, target);

  int result = 0;
  for (std::vector<int>::const_iterator it = scores.begin(); it != scores.end(); ++it)
  {
    if (*it >= min_score)
    {
      result += 1;
    }
    else if (*it >= min_surprise_score && surprises > 0)
    {
      result += 1;
      surprises -= 1;
    }
  }

  std::cout << result << std::endl;
}

int main(int argc, char** argv)
{
  unsigned int testcases;
  std::cin >> testcases;

  {
    // Discard first line
    std::string firstline;
    std::getline(std::cin, firstline);
  }

  for (unsigned int testcase = 1; testcase <= testcases; ++testcase)
  {
    std::cout << "Case #" << testcase << ": ";
    challenge();
  }

  return 0;
}

