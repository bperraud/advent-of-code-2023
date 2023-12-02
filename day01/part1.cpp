#include <string>       // std::string
#include <iostream>     // std::cout
#include <sstream>      // std::stringstream

class Solution {
private :

public :

	int solution(const std::string &input) {

		std::string line;
		std::stringstream stream(input);

		while (std::getline(stream, line)) {

			std::cout << line << std::endl;
		}
		return 0;
	}
};

int main(int argc, char **argv) {

	Solution s;

	if (argc != 2)
		return 1;

	std::cout << s.solution(argv[1]) << std::endl;

	return 0;
}
