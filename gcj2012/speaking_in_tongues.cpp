#include <iostream>
#include <string>

char transtable[] = "yhesocvxduiglbkrztnwjpfmaq";
void challenge()
{
  std::string input, output;
  std::getline(std::cin, input);

  for (std::string::const_iterator c = input.begin(); c != input.end(); ++c)
  {
    if (*c < 'a' || *c > 'z')
      output += *c;
    else
      output += transtable[*c - 'a'];
  }

  std::cout << output << std::endl;
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

