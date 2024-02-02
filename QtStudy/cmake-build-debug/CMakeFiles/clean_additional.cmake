# Additional clean files
cmake_minimum_required(VERSION 3.16)

if("${CONFIG}" STREQUAL "" OR "${CONFIG}" STREQUAL "Debug")
  file(REMOVE_RECURSE
  "CMakeFiles/QtStudy_autogen.dir/AutogenUsed.txt"
  "CMakeFiles/QtStudy_autogen.dir/ParseCache.txt"
  "QtStudy_autogen"
  )
endif()
