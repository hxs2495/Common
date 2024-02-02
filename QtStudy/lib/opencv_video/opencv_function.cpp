//
// Created by hxs on 2023/12/26.
//
#include <opencv2/opencv.hpp>
#include <iostream>

void open_video() {
    cv::VideoCapture cap(0);
    if (!cap.isOpened()) {
        std::cerr << "Error: 无法打开摄像头" << std::endl;
        return;
    }

    cv::namedWindow("Camera", cv::WINDOW_AUTOSIZE);

    while (true) {
        cv::Mat frame;
        cap >> frame;
        if (frame.empty()) {
            std::cerr << "Error: 无法从摄像头读取图像" << std::endl;
            break;
        }
        cv::imshow("Camera", frame);

        // 检测是否按下了键盘上的 'q' 键，如果是则退出循环
        if (cv::waitKey(1) == 'q') {
            break;
        }
    }

    // 不再需要手动释放资源，使用 RAII 自动管理资源

}
