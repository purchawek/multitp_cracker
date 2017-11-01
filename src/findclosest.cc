#include <iostream>
#include <vector>
#include <fstream>
#include <limits>

// compilation g++ -c -fPIC findclosest.cc -o findclosest.o && g++ -shared -Wl,-soname,libfindclosest.so -o libfindclosest.so findclosest.o

std::vector<std::string> DICTIONARY;

void load_dictionary(std::string fname) {
    std::ifstream reader;
    reader.open(fname);
    std::string word;

    while(reader >> word) {
        DICTIONARY.push_back(word);
    }
}

int edit_distance(std::string a, std::string b) {

    auto min = [](std::initializer_list<int> nums) -> int {
        int min = *nums.begin();
        for (auto i : nums) if (i < min) min = i;
        return min;
    };

    int c[a.length()+1][b.length()+1];

    for (size_t i = 0; i <= a.length(); i++)
        c[i][0]  = i;

    for (size_t j = 0; j <= b.length(); j++)
        c[0][j] = j;

    for (size_t i = 1; i <= a.length(); i++)
        for (size_t j = 1; j <= b.length(); j++)
            c[i][j] = min({c[i-1][j]+1, c[i][j-1]+1,
                          c[i-1][j-1] + static_cast<int>(a[i-1] != b[j-1])});

    return c[a.length()][b.length()];
}

typedef std::pair<std::string, int> BestPair;
typedef std::vector<BestPair> BestVector;

BestVector find_similar(std::string word){ 
    static size_t size = 1;
    BestVector best(size);
    for (size_t i = 0; i < size; i++) {
        best[i] = BestPair("", std::numeric_limits<int>().max());
    }

    auto add_best = [&best](std::string word, int diff) {
        if (diff < 0) std::cout << word << std::endl;
        for(size_t i = 0; i < size; i++) {
            if (best[i].second >= diff) {
                best.insert(i + best.begin(), BestPair(word, diff));
                best.resize(size);
                break;
            }
        }
    };

    for(auto &w : DICTIONARY) {
        if (w.size() == word.size()) {
            add_best(w, edit_distance(word, w));
            if(best[0].second == 0) return best;
        }
    }
    return best;
}

extern "C" {
    void load(const char * fname) {
        load_dictionary(std::string(fname));
    }
    char * find_closest(char *word, char *string) {
        auto result = find_similar(std::string(word));
        snprintf(string, result[0].first.size()+1, "%s", result[0].first.c_str());
        return string;
    }
}

int main(int argc, char **argv) {

    if (argc < 2) {
        std::cerr << "Usage: " << argv[0] << " dict_file" << std::endl;
    }
    std::string a = "", b = "";

    load_dictionary(std::string(argv[1]));
    std::cout << "Ready!" << std::endl;

    std::cin >> a;
    for (auto a : find_similar(a))
        std::cout << a.first << ", " << a.second << std::endl;
}
