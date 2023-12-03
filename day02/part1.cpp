#include <string>       // std::string
#include <iostream>     // std::cout
#include <sstream>      // std::stringstream
#include <map>

class Solution {
private :

public :

	int solution(const std::string &input) {

		std::map<char, int> color_cubes = {
			{ 'r', 12},
			{ 'g', 13},
			{ 'b', 14}
		};

		std::string line;
		std::stringstream stream(input);
		int game = 1;
		int sum_invalid_game = 0;
		while (std::getline(stream, line)) {
			for (size_t i = std::string("Game :").size() + std::to_string(i).size(); i < line.size(); i++)
			{
				if (std::isdigit(line[i])) {
					std::string number_str;
					while (std::isdigit(line[i]))
						number_str.push_back(line[i++]);
					i++;
					if (stoi(number_str) > color_cubes[line[i]]) {
						sum_invalid_game += game;
						break;
					}
				}
			}
			game++;
		}
		return ((game-1)*(game)) / 2 - sum_invalid_game;
	}
};

int main(int argc, char **argv) {

	Solution s;

	if (argc != 2)
		return 1;

	std::cout << s.solution(argv[1]) << std::endl;

	return 0;
}
