#include <string>       // std::string
#include <iostream>     // std::cout
#include <sstream>      // std::stringstream
#include <vector>
#include <map>
#include <algorithm>

class Solution {
private :

public :
	int solution(const std::string &input) {
		std::string line;
		std::stringstream stream(input);
		std::vector<std::string> map;

		std::map<std::pair<int, int>, std::pair<int, int>> weird_map;
		auto find_gear = [&](int row, int col, int size, int number) {
			int d1[3] = {-1, 0, 1};
			col--;
			for (size_t ind = 0; ind < size; ind++) {
				col += 1;
				for (size_t i = 0; i < 3; i++)
				{
					for (size_t j = 0; j < 3; j++)
					{
						if (row + d1[j] < 0 || row + d1[j] >= map.size()
							|| col + d1[i] < 0 || col + d1[i] >= map[0].size())
							continue;
						if (map[row + d1[j]][col + d1[i]] == '*') {
							std::pair<int, int> coordinates = {row + d1[j], col + d1[i]};
							weird_map[coordinates] = weird_map.count(coordinates)
								? std::make_pair(weird_map[coordinates].first * number, weird_map[coordinates].second + 1)
								: std::make_pair(number, 1);
							return;
						}
					}
				}
			}
		};
		while (std::getline(stream, line)) map.push_back(line);
		int sum = 0;
		for (size_t j = 0; j < map.size(); j++) {
			std::string line = map[j];
			for (size_t i = 0; i < line.size(); i++){
				if (isdigit(line[i])) {
					std::string number;
					while (isdigit(line[i])) number.push_back(line[i++]);
					find_gear(j, i - number.size(), number.size(), stoi(number));
				}
			}
		}
		for (auto &[key, value] : weird_map) if (value.second == 2) sum += value.first;
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
