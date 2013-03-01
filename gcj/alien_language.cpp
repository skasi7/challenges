#include <algorithm>
#include <iostream>
#include <string>
#include <vector>
#include <regex.h>

typedef std::vector<std::string> StringVector;

/*
#include <regex>

void challenge(const StringVector & words)
{
  std::string input;
  std::getline(std::cin, input);

  std::replace(input.begin(), input.end(), '(', '[');
  std::replace(input.begin(), input.end(), ')', ']');

  std::regex txtRegex("[a-z]+\\.txt");
  std::cout << std::regex_match("foo.txt", txtRegex) << std::endl;
  std::cout << std::regex_match("foo.dat", txtRegex) << std::endl;
  std::cout << std::regex_match("zoiberg", txtRegex) << std::endl;

  return;

  std::regex pat(input, std::regex::basic);
  unsigned int result = 0;
  for (const auto & word : words) {
    // std::cout << std::regex_match(word, pat) << std::endl;
    if (std::regex_match(word, pat)) {
      ++result;
    }
  }

  std::cout << result << std::endl;
}
 */

void challenge(const StringVector & words)
{
  std::string input;
  std::getline(std::cin, input);

  std::replace(input.begin(), input.end(), '(', '[');
  std::replace(input.begin(), input.end(), ')', ']');

  regex_t pat;
  regcomp(&pat, input.c_str(), REG_NOSUB);

  unsigned int result = 0;
  for (StringVector::const_iterator word = words.begin();
      word != words.end(); ++word) {
    if (!regexec(&pat, word->c_str(), 0, NULL, 0)) {
      ++result;
    }
  }

  std::cout << result << std::endl;
}
 
  

int main(int argc, char** argv)
{
  unsigned int L, D, testcases;
  std::cin >> L;
  std::cin >> D;
  std::cin >> testcases;

  {
    // Discard first line
    std::string firstline;
    std::getline(std::cin, firstline);
  }

  StringVector words;
  for (unsigned int i = 0; i < D; ++i) {
    std::string word;
    std::getline(std::cin, word);
    words.push_back(word);
  }
  
  for (unsigned int testcase = 1; testcase <= testcases; ++testcase)
  {
    std::cout << "Case #" << testcase << ": ";
    challenge(words);
  }

  return 0;
}

