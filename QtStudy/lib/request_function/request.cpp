//
// Created by hxs on 2023/12/26.
//
#include <iostream>
#include <string>
#include <boost/asio.hpp>

// http请求的回调函数类型
using HttpCallback = std::function<void(std::string const &)>;

void http_request(std::string const &url, HttpCallback callback) {
    // 创建asio io_service对象
    boost::asio::io_service io_service;

    // 创建TCP resolver对象，并解析出目标主机名和端口号
    boost::asio::ip::tcp::resolver resolver(io_service);
    auto const resolver_results = resolver.resolve(url, "80");

    // 创建TCP socket对象，并连接到目标主机
    boost::asio::ip::tcp::socket socket(io_service);
    boost::asio::connect(socket, resolver_results.begin(), resolver_results.end());

    // 构造HTTP GET请求报文
    std::string request = "GET / HTTP/1.1\r\n";
    request += "Host: " + url + "\r\n";
    request += "Connection: close\r\n";
    request += "\r\n";

    // 向服务器发送HTTP GET请求报文
    boost::asio::write(socket, boost::asio::buffer(request));

    // 读取服务器响应报文
    boost::asio::streambuf response;
    boost::asio::read_until(socket, response, "\r\n");

    // 提取HTTP响应状态码
    std::istream response_stream(&response);
    std::string http_version;
    unsigned int status_code;
    std::string status_message;
    response_stream >> http_version >> status_code;
    std::getline(response_stream, status_message);

    if (!response_stream || http_version.substr(0, 5) != "HTTP/") {
        std::cerr << "无效的 HTTP 响应\n";
        return;
    }

    if (status_code != 200) {
        std::cerr << "返回带有状态代码的响应 " << status_code << "\n";
        return;
    }

    // 读取服务器响应内容并调用回调函数
    std::string response_body((std::istreambuf_iterator<char>(&response)), std::istreambuf_iterator<char>());
    callback(response_body);
}

