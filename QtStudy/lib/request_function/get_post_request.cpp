//
// Created by hxs on 2023/12/26.
//
#include <curl/curl.h>
#include <iostream>
#include <cstring>
#include <vector>
#include <jsoncpp/json/json.h>

// 定义一个结构体，用于存储接收到的数据
struct MemoryStruct {
    char *memory;
    size_t size;
};

// 用于接收数据的回调函数
size_t write_memory_callback(char *ptr, size_t size, size_t nmemb, void *data) {
    size_t realsize = size * nmemb;
    MemoryStruct *mem = (MemoryStruct *) data;

    char *tmp = (char *) realloc(mem->memory, mem->size + realsize + 1);
    if (tmp == NULL) {
        std::cerr << "内存不足，无法分配缓冲区" << std::endl;
        return 0;
    }

    mem->memory = tmp;
    memcpy(&(mem->memory[mem->size]), ptr, realsize);
    mem->size += realsize;
    mem->memory[mem->size] = 0;

    return realsize;
}

// 发送 GET 请求并返回 JSON 数据
Json::Value send_get_request(const std::string &url) {
    CURL *curl_handle;
    CURLcode res;
    MemoryStruct chunk = {NULL, 0};
    Json::Value json_data;

    curl_global_init(CURL_GLOBAL_ALL);
    curl_handle = curl_easy_init();
    if (curl_handle) {
        curl_easy_setopt(curl_handle, CURLOPT_URL, url.c_str());
        curl_easy_setopt(curl_handle, CURLOPT_FOLLOWLOCATION, 1L);
        curl_easy_setopt(curl_handle, CURLOPT_WRITEFUNCTION, write_memory_callback);
        curl_easy_setopt(curl_handle, CURLOPT_WRITEDATA, (void *) &chunk);

        res = curl_easy_perform(curl_handle);
        if (res != CURLE_OK) {
            std::cerr << "curl_easy_perform() failed: " << curl_easy_strerror(res) << std::endl;
        } else {
            // 解析 JSON 数据
            Json::CharReaderBuilder builder;
            Json::CharReader *reader = builder.newCharReader();
            std::string err;
            if (reader->parse(chunk.memory, chunk.memory + chunk.size, &json_data, &err)) {
                std::cout << "接收的 JSON 数据:\n" << json_data << std::endl;
            } else {
                std::cerr << "无法解析 JSON 数据: " << err << std::endl;
            }
            delete reader;
        }

        curl_easy_cleanup(curl_handle);
    }
    curl_global_cleanup();

    return json_data;
}

// 发送 POST 请求并返回 JSON 数据
Json::Value send_post_request(const std::string &url, const std::string &post_data) {
    CURL *curl_handle;
    CURLcode res;
    MemoryStruct chunk = {NULL, 0};
    Json::Value json_data;

    curl_global_init(CURL_GLOBAL_ALL);
    curl_handle = curl_easy_init();
    if (curl_handle) {
        curl_easy_setopt(curl_handle, CURLOPT_URL, url.c_str());
        curl_easy_setopt(curl_handle, CURLOPT_POST, 1L);
        curl_easy_setopt(curl_handle, CURLOPT_POSTFIELDS, post_data.c_str());
        curl_easy_setopt(curl_handle, CURLOPT_FOLLOWLOCATION, 1L);
        curl_easy_setopt(curl_handle, CURLOPT_WRITEFUNCTION, write_memory_callback);
        curl_easy_setopt(curl_handle, CURLOPT_WRITEDATA, (void *) &chunk);

        res = curl_easy_perform(curl_handle);
        if (res != CURLE_OK) {
            std::cerr << "curl_easy_perform() failed: " << curl_easy_strerror(res) << std::endl;
        } else {
            // 解析 JSON 数据
            Json::CharReaderBuilder builder;
            Json::CharReader *reader = builder.newCharReader();
            std::string err;
            if (reader->parse(chunk.memory, chunk.memory + chunk.size, &json_data, &err)) {
                std::cout << "接收的 JSON 数据:\n" << json_data << std::endl;
            } else {
                std::cerr << "无法解析 JSON 数据: " << err << std::endl;
            }
            delete reader;
        }

        curl_easy_cleanup(curl_handle);
    }
    curl_global_cleanup();

    return json_data;
}

extern "C" {
void get_request(const std::string &url) {
    send_get_request(url);
}
}

//    // 发送 GET 请求并解析 JSON 数据
//    std::string get_url = "http://192.168.1.27:5004/data/";
//    Json::Value get_data = send_get_request(get_url);

//    // 发送 POST 请求并解析 JSON 数据
//    std::string post_url = "http://192.168.1.27:5004/data/";
//    std::string post_data = "key1=value1&key2=value2";
//    Json::Value post_result = send_post_request(post_url, post_data);
