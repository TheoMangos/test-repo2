
cmake_minimum_required(VERSION 3.8)
project(asccas)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
    add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# find dependencies
find_package(ament_cmake REQUIRED)
find_package(ament_cmake_python REQUIRED)
find_package(std_msgs REQUIRED)
find_package(rclpy REQUIRED)

find_package(rosidl_default_generators REQUIRED)
rosidl_generate_interfaces(${PROJECT_NAME}
    "srv/Service1.srv"
    "srv/GoalService.srv"
    "srv/ResultService.srv"

)

if(BUILD_TESTING)
    find_package(ament_lint_auto REQUIRED)
    # the following line skips the linter which checks for copyrights
    # comment the line when a copyright and license is added to all source files
    set(ament_cmake_copyright_FOUND TRUE)
    # the following line skips cpplint (only works in a git repo)
    # comment the line when this package is in a git repo and when
    # a copyright and license is added to all source files
    set(ament_cmake_cpplint_FOUND TRUE)
    ament_lint_auto_find_test_dependencies()
endif()

if(BUILD_TESTING)
find_package(ament_cmake_pytest REQUIRED)
set(_pytest_tests
  # Add test files here
)
foreach(_test_path ${_pytest_tests})
  get_filename_component(_test_name ${_test_path} NAME_WE)
  ament_add_pytest_test(${_test_name} ${_test_path}
    APPEND_ENV PYTHONPATH=${CMAKE_CURRENT_BINARY_DIR}
    TIMEOUT 60
    WORKING_DIRECTORY ${CMAKE_SOURCE_DIR}
  )
endforeach()
endif()


include_directories(
  include
  ${catkin_INCLUDE_DIRS}
)



# Install launch files
install(
  DIRECTORY launch
  DESTINATION share/${PROJECT_NAME}
)

# Install cpp nodes
install(
  TARGETS 
  DESTINATION lib/${PROJECT_NAME}
)

# Install Python executables
install(PROGRAMS
  asccas/Node1.py 
asccas/Node2.py 

  DESTINATION lib/${PROJECT_NAME}
)


# customize CMakeLists.txt below
# asdsd
# end CMakeLists.txt customization

ament_package()
