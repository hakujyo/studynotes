# 依赖包的安装

```bash
yum install zlib-devel.x86_64
yum install expat-devel.x86_64
```

依赖一般在 config 和 make 的时候报错会提示，如，装 python 的时候缺 expat,因为 make 的时候报错了：

## expat 报错

```bash
/home>/blb/tools/songjian/Python-2.7.16/Modules/\_elementtree.c:2056:19: error: expat.h: No such file or directory
```

一般先 yum search expat,然后找到 devel 的包，如果没有,就去网上搜一个。

# openssl 的编译安装

## compile openssl

```bash
./config shared zlib --prefix=/home/blb/openssl
make -j 10
make install
```

# 指定 openssl 编译 python

添加环境变量，写到.bash_profile 里面：

## .bash_profile

```bash
export LD_LIBRARY_PATH=/home/blb/python27/lib:/home/blb/openssl/lib/:$LD_LIBRARY_PATH

export PATH=/home/blb/python27/bin:/home/blb/openssl/bin:$PATH

export SSL=/home/blb/openssl
```

> source /home/blb/.bash_profile

编译 python 前需要修改 setup.py,Modules/Setup,Modules/Setup.dist3 个文件。
setup.py 一定要改，主要是为了改 ssl 位置，否则会用系统默认的 ssl。
Setup.dist 文件,参考
https://stackoverflow.com/questions/32856389/how-to-import-ssl-in-python-2-7-6
![image](https://github.com/hakujyo/studynotes/blob/master/pictures/Setup.dist.JPG)

## 执行 python 编译

```bash
./configure --prefix=/home/blb/python27/ --enable-shared --with-threads --enable-unicode=ucs4 --with-system-expat --with-system-ffi
make -j10
make install
```

这样做只能在 blb 和 root 下能用.要让所有用户能用的话,在 root 下编译,指定 prefix 的路径为/usr/local/openssl,然后各用户把 export 路径改到这个路径

# 测试

切换账户
直接 sudo su blb 切换，会发现编译好的 python 并没有生效：
![image](https://github.com/hakujyo/studynotes/blob/master/pictures/python_error.JPG)
su - blb，否则不会加载.bash_profile 文件 #相关产物
https://ylybucket.su.bcebos.com/tools%2Fsongjian.tar.gz
直接 wget，按照上述步骤编译安装，可快速得到一个这样的 Python 2.7.16 +OpenSSL 1.1.1c 环境。
