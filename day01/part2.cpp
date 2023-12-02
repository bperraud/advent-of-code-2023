#include <string>       // std::string
#include <iostream>     // std::cout
#include <sstream>      // std::stringstream
#include <algorithm>
#include <map>
#include <cstring>

class Solution {
private :

public :

	int solution(const std::string &input) {
		std::string line;
		std::stringstream stream(input);
		int sum = 0;

		const std::map<std::string, char> digit_map = {
			{ "one", '1'},
			{ "two", '2'},
			{ "three", '3'},
			{ "four", '4'},
			{ "five", '5'},
			{ "six", '6'},
			{ "seven", '7'},
			{ "eight", '8'},
			{ "nine", '9'}
		};

		auto valid_digit = [&](std::string s) {
			int ret = 1;
			for (auto [key, value] : digit_map) {
				if (strcmp(std::string(key.data(), s.size()).c_str(), s.c_str()) != 0)
					continue;
				if (key.size() == s.size())
					return (int) value;
				return 0;
			}
			return -1;
		};

		while (std::getline(stream, line)) {
			std::string number;
			std::string digit_str = "";
			std::for_each(line.cbegin(), line.cend(), [&](char c) {
				int res = valid_digit(digit_str + c);
				if (res == 0)
					digit_str.push_back(c);
				else if (res > 0) {
					digit_str = c;
					c = res;
				}
				else {
					if (!digit_str.empty())
						digit_str = std::string(1, digit_str.back()) + std::string(1, c);
					else
						digit_str = c;
				}
				if (std::isdigit(c)) {
					if (number.size() == 0 || number.size() == 1)
						number.push_back(c);
					else if (number.size() == 2)
						number[1] = c;
				}}
			);
			if (number.size() == 1)
				number.push_back(number[0]);
			sum += std::stoi(number);
		}
		return sum;
	}
};

int main(int argc, char **argv) {

	Solution s;

	if (argc != 2)
		return 1;

	std::cout << s.solution(argv[1]) << std::endl;

	return 0;
}
