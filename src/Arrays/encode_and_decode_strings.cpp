#include <iostream>
#include <vector>
#include <string>

using namespace std;

string encode(vector<string>& strs)
{
    // build a string where each str in strs begins with a delimiter + its length
    // you have the delimiter as a flag and 
    // the length to know how many characters after to 'collect' when decoding
    // this works b/c you're controlling the when + how of string slicing when decoding
    string builder = "";
    for (string str : strs)
    {
        int len = str.length();
        builder += ('|' + to_string(len) + '|' + str);
    }

    return builder;
}

vector<string> decode(string s)
{
    vector<string> strs = {};

    size_t i = 0;
    while (i < s.size())
    {
        if (s[i] == '|') // find delimiter
        {
            // find start/end of the embedded len value,
            // then denote the start of the word given 'end'
            int lengthStart = i + 1;
            int lengthEnd = s.find('|', lengthStart);
            int wordStart = lengthEnd + 1;

            // convert len to int
            int len = stoi(s.substr(lengthStart, lengthEnd - lengthStart));

            // adding the word to 'strs'
            string word = s.substr(wordStart, len);
            strs.push_back(word);
            i = wordStart + len; // equal to: startIndex + len
        }
    }

    return strs;
}

int main()
{
    vector<string> input = {"we","say",":","yes","!@#$%^&*()"};

    string encodeOutput = encode(input);
    cout << "encode: " << encodeOutput << endl;

    input = decode(encodeOutput); // reusing input
    cout << "decode: ";
    for (string s : input)
    {
        cout << s << " ";
    }
}
