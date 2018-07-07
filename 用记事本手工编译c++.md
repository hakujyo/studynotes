用记事本手工编译c++！
0x01下载MinGW的安装文件http://sourceforge.net/projects/mingw/files/latest/download?source=files

安装需要科学上网注意，c++的话组件选gcc。


0x02配置环境变量

path 添加 C:\MinGW\bin;C:\MinGW\libexec\gcc\mingw32\4.5.2;C:\MinGW\mingw32\bin
include 添加 C:\MinGW\include;C:\MinGW\lib\gcc\mingw32\4.5.2\include
lib 添加 C:\MinGW\lib;

0x03用g++编译

写一个小程序，比如helloworld：

写一个helloworld
写一个helloworld
学一些gcc的基本用法：
命令格式：gcc [选项] [文件名]
编译的四个阶段：
-E：仅执行编译预处理；
-c：仅执行编译操作，不进行连接操作；
-S：将C代码转换为汇编代码；
-o：指定生成的输出文件。
预处理
1.预处理，生成预编译文件
> ```shell
>gcc -E test.cpp -o test.i
>
2.编译，生成汇编代码（.s文件）
> ```shell
>g++ -S test.i -o test.s
>
3.汇编，生成目标文件
> ```shell
>g++ -c test.s -o test.o
>
4.链接，生成可执行文件
> ```shell
>g++ test.o -o test
>

5.看看效果，test.exe文件生成了！
 

当然你也可以直接用f5运行：

G++编译命令：

cmd /k g++.exe -g -W -Wall -o $(CURRENT_DIRECTORY)

/$(NAME_PART).exe “$(FULL_CURRENT_PATH)” & PAUSE & EXIT、

这样就生成了一个exe文件，也就是二进制的目标文件。

G++的运行命令cmd /k $(CURRENT_DIRECTORY)/$(NAME_PART).exe & PAUSE & EXIT
