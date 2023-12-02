#include <string>       // std::string
#include <iostream>     // std::cout
#include <sstream>      // std::stringstream
#include <algorithm>

class Solution {
private :

public :

	int solution(const std::string &input) {
		std::string line;
		std::stringstream stream(input);
		int sum = 0;

		while (std::getline(stream, line)) {
			std::string number;
			std::for_each(line.cbegin(), line.cend(), [&](char c) {
				if (std::isdigit(c)) {
					if (number.size() == 0 || number.size() == 1)
						number.push_back(c);
					else if (number.size() == 2)
						number[1] = c;
				} }
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
