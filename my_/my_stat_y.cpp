#include <iostream>
#include <sys/stat.h>
#include <pwd.h>
#include <unistd.h>

using namespace std;

int main(int argc, char *argv[])
{
    // 1. 检查参数
    if (argc != 2) {
        cerr << "Usage: ./my-stat <file>" << endl;
        return 1;
    }

    // 2. 获取文件属性
    struct stat st;

    if (stat(argv[1], &st) != 0) {
        cerr << "Error: file does not exist" << endl;
        return 1;
    }

    // 3. 文件类型
    cout << "File: " << argv[1] << endl;

    if (S_ISREG(st.st_mode))
        cout << "Type: regular file" << endl;
    else if (S_ISDIR(st.st_mode))
        cout << "Type: directory" << endl;
    else
        cout << "Type: other" << endl;

    // 4. 文件大小
    double size = st.st_size;

    if (size < 1024)
        cout << "Size: " << size << " B" << endl;
    else if (size < 1024 * 1024)
        cout << "Size: " << size / 1024 << " KB" << endl;
    else if (size < 1024 * 1024 * 1024)
        cout << "Size: " << size / (1024 * 1024) << " MB" << endl;
    else
        cout << "Size: " << size / (1024 * 1024 * 1024) << " GB" << endl;

    // 5. 文件所有者
    struct passwd *owner = getpwuid(st.st_uid);

    if (owner != nullptr)
        cout << "Owner: " << owner->pw_name << endl;

    // 6. 本用户是否有读权限
    cout << "Readable: "
         << (access(argv[1], R_OK) == 0 ? "yes" : "no") << endl;

    // 7. 本用户是否有写权限
    cout << "Writable: "
         << (access(argv[1], W_OK) == 0 ? "yes" : "no") << endl;
    
    cout << "Executable: "
     << (access(argv[1], X_OK) == 0 ? "yes" : "no") << endl;
    return 0;
}