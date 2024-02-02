cmake_minimum_required(VERSION 3.24)
project(QtStudy)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_AUTOMOC ON)
set(CMAKE_AUTORCC ON)
set(CMAKE_AUTOUIC ON)

# 查找并加载 Qt5 库
find_package(Qt5 COMPONENTS Core Gui Widgets REQUIRED)
find_package(SQLite3 REQUIRED)
find_package(jsoncpp REQUIRED)
find_package(CURL REQUIRED)
find_package(OpenCV REQUIRED)

# 添加可执行文件
add_executable(QtStudy
        main.cpp
        ui/ui_windowtest.h
        sources/main_window.cpp
        headers/main_window.h
        )

# 链接 Qt5 库
target_link_libraries(QtStudy
        Qt5::Core
        Qt5::Gui
        Qt5::Widgets
        SQLite::SQLite3
        pthread
        jsoncpp_lib
        CURL::libcurl
        )

# 如果找到了 OpenCV 库，将其链接到你的项目中
if (OpenCV_FOUND)
    target_link_libraries(QtStudy ${OpenCV_LIBS})
endif ()