#include <iostream>
#include <string>

void challenge()
{
  std::string input;
  std::getline(std::cin, input);

  std::cout << input << std::endl;
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

