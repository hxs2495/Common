import ctypes

so = ctypes.cdll.LoadLibrary
lib = so("/home/hxs/CLionProjects/QtStudy/lib/request_function/get_post_request.so")
lib.get_request(url="http://127.0.0.1:8000/test/get/data/")
