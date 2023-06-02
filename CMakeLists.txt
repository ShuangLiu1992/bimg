cmake_minimum_required(VERSION 3.15)

project(bimg)

file(GLOB_RECURSE BIMG_SRC
        ./src/image.cpp
        ./src/image_cubemap_filter.cpp
        ./src/image_decode.cpp
        ./src/image_gnf.cpp
        ./3rdparty/tinyexr/deps/miniz/miniz.c
        )

add_library(${PROJECT_NAME})
target_sources(${PROJECT_NAME} PRIVATE ${BIMG_SRC})
target_include_directories(${PROJECT_NAME} PRIVATE ./include/)
find_package(astc_encoder REQUIRED)
target_link_libraries(${PROJECT_NAME} PUBLIC astc_encoder::astc_encoder)
find_package(bx REQUIRED)
target_link_libraries(${PROJECT_NAME} PUBLIC bx::bx)
target_include_directories(${PROJECT_NAME} PUBLIC ./include)
target_include_directories(${PROJECT_NAME} PUBLIC ./3rdparty)
target_include_directories(${PROJECT_NAME} PUBLIC ./3rdparty/nvtt)
target_include_directories(${PROJECT_NAME} PUBLIC ./3rdparty/iqa/include/)
target_include_directories(${PROJECT_NAME} PUBLIC ./3rdparty/tinyexr/deps/miniz)

install(TARGETS ${PROJECT_NAME}
    RUNTIME DESTINATION ${CMAKE_INSTALL_BINDIR}
    LIBRARY DESTINATION ${CMAKE_INSTALL_LIBDIR}
    ARCHIVE DESTINATION ${CMAKE_INSTALL_LIBDIR}
    INCLUDES DESTINATION ${CMAKE_INSTALL_INCLUDEDIR}
    PUBLIC_HEADER DESTINATION ${CMAKE_INSTALL_INCLUDEDIR}
)