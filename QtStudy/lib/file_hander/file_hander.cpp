//
// Created by hxs on 2023/12/28.
//
#include <iostream>
#include <fstream>
#include <string>

// 读取文件内容
std::string readFile(const std::string &filename) {
    std::ifstream file(filename);
    std::string content;
    std::string line;
    if (file.is_open()) {
        while (std::getline(file, line)) {
            content += line + "\n";
        }
        file.close();
    } else {
        std::cout << "无法打开文件：" << filename << std::endl;
    }
    return content;
}

// 写入内容到文件
void writeFile(const std::string &filename, const std::string &content) {
    std::ofstream file(filename);
    if (file.is_open()) {
        file << content;
        file.close();
        std::cout << "文件写入成功：" << filename << std::endl;
    } else {
        std::cout << "无法打开文件：" << filename << std::endl;
    }
}

//int main() {
//    // 测试读取文件
//    std::string filename = "example.txt";
//    std::string content = readFile(filename);
//    std::cout << "文件内容：" << std::endl;
//    std::cout << content << std::endl;
//
//    // 测试写入文件
//    std::string newContent = "这是新的文件内容";
//    writeFile("new_example.txt", newContent);
//
//    return 0;
//}
