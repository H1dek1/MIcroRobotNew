cmake_minimum_required(VERSION 2.8)
project(MicroRobot CXX)

add_library(microrobot
  STATIC
    environment.cpp
    external_magnetic_field.cpp
    paramagnetic_particle.cpp
    permanent_magnetic_particle.cpp
    swimmer.cpp
  )

target_include_directories(microrobot
  PUBLIC ../include
  )
add_executable(run main.cpp)
target_link_libraries(run microrobot)
