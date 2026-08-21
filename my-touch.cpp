// my-touch.cpp
#include <cstdio>
#include <cstring>
#include <cerrno>

int main(int argc, char *argv[])
{
    // argc < 2 表示没有提供要创建的文件
    if (argc < 2) {
        std::fprintf(stderr, "Usage: %s FILE...\n", argv[0]);
        return 1;
    }

    // argv[1] ~ argv[argc-1] 都是用户传入的文件名
    for (int i = 1; i < argc; ++i) {
        // fopen() 以写入模式打开文件，不存在则创建
        FILE *fp = std::fopen(argv[i], "w");

        if (fp == nullptr) {
            // errno 保存失败原因
            std::fprintf(
                stderr,
                "my-touch: cannot touch '%s': %s\n",
                argv[i],
                std::strerror(errno)
            );
        } else {
            std::fclose(fp);
        }
    }

    return 0;
}