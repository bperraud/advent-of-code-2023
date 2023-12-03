#include <string>       // std::string
#include <iostream>     // std::cout
#include <sstream>      // std::stringstream
#include <map>

class Solution {
private :

public :

	int solution(const std::string &input) {
		std::string line;
		std::stringstream stream(input);
		int game = 1;
		int sum_invalid_game = 0;
		int res = 0;
		while (std::getline(stream, line)) {
			std::map<char, int> color_cubes = {
				{ 'r', 1},
				{ 'g', 1},
				{ 'b', 1}
			};
			for (size_t i = std::string("Game :").size() + std::to_string(game).size(); i < line.size(); i++)
			{
				if (std::isdigit(line[i])) {
					std::string number_str;
					while (std::isdigit(line[i]))
						number_str.push_back(line[i++]);
					i++;
					color_cubes[line[i]] = std::max(color_cubes[line[i]], stoi(number_str));
				}
			}
			int power = 1;
			for (auto &[key, value] :  color_cubes)
				power*= value;
			res += power;
			game++;
		}
		return res;
	}
};

int main(int argc, char **argv) {

	Solution s;

	if (argc != 2)
		return 1;

	std::cout << s.solution(argv[1]) << std::endl;

	return 0;
}
