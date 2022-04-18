# http2 背景知识

https://zhuanlan.zhihu.com/p/26559480
https://imququ.com/post/http2-resource.html

# curl 支持 http2

为了让 curl 支持 HTTP2 我们需要安装 nghttp2（http2 的 C 语言库）：

## 安装编译工具等

sudo apt-get install git g++ make binutils autoconf automake autotools-dev libtool pkg-config \
zlib1g-dev libcunit1-dev libssl-dev libxml2-dev libev-dev libevent-dev libjansson-dev \
libjemalloc-dev cython python3-dev python-setuptools

## 编译安装 nghttp2

git clone https://github.com/tatsuhiro-t/nghttp2.git
cd nghttp2
autoreconf -i
automake 本页面由 v\_姚宇辰于 2022/04/15 迁移自 wiki 姚璐颖空间
依赖包的安装
yum install zlib-devel.x86_64
yum install expat-devel.x86_64
依赖一般在 config 和 make 的时候报错会提示，如，装 python 的时候缺 expat,因为 make 的时候报错了：
expat 报错
/home/blb/tools/songjian/Python-2.7.16/Modules/\_elementtree.c:2056:19: error: expat.h: No such file or directory
一般先 yum search expat,然后找到 devel 的包，如果没有,就去网上搜一个。
openssl 的编译安装
compile openssl
./config shared zlib --prefix=/home/blb/openssl
make -j 10
make install
指定 openssl 编译 python
添加环境变量，写到.bash_profile 里面：
.bash_profile
export LD_LIBRARY_PATH=/home/blb/python27/lib:/home/blb/openssl/lib/:$LD_LIBRARY_PATH
export PATH=/home/blb/python27/bin:/home/blb/openssl/bin:$PATH
export SSL=/home/blb/openssl
source /home/blb/.bash_profile
编译 python 前需要修改 setup.py,Modules/Setup,Modules/Setup.dist3 个文件。
setup.py 一定要改，主要是为了改 ssl 位置，否则会用系统默认的 ssl。
Setup.dist 文件,参考
https://stackoverflow.com/questions/32856389/how-to-import-ssl-in-python-2-7-6

执行 python 编译
compile python
./configure --prefix=/home/blb/python27/ --enable-shared --with-threads --enable-unicode=ucs4 --with-system-expat --with-system-ffi
make -j10
make install
这样做只能在 blb 和 root 下能用.要让所有用户能用的话,在 root 下编译,指定 prefix 的路径为/usr/local/openssl,然后各用户把 export 路径改到这个路径

测试
切换账户
直接 sudo su blb 切换，会发现编译好的 python 并没有生效：

su - blb，否则不会加载.bash_profile 文件
相关产物
https://ylybucket.su.bcebos.com/tools%2Fsongjian.tar.gz
直接 wget，按照上述步骤编译安装，可快速得到一个这样的 Python 2.7.16 +OpenSSL 1.1.1c 环境。

autoconf
./configure
make
sudo make install
echo '/usr/local/lib' > /etc/ld.so.conf.d/local.conf
ldconfig

## 升级 curl 版本

cd ~
sudo apt-get build-dep curl
wget http://curl.haxx.se/download/curl-7.46.0.tar.bz2
tar -xvjf curl-7.46.0.tar.bz2
cd curl-7.46.0
./configure --with-nghttp2=/usr/local --with-ssl
sudo make && make install
echo '/usr/local/lib' > /etc/ld.so.conf.d/local.conf
ldconfig
升级完版本之后，我们再查看 curl 版本时会发布特性中会增加 HTTP2 功能支持。此时 –http2 参数就可以正常使用了：
如果运行 curl --version 出现 SSL_COMP_free_compression_methods 找不到符号，需要修改下 lib/vtls/openssl.c 里面的宏，关掉压缩

# 测试

curl --http2 -I https://nghttp2.org
测试 curl with http2
我们再使用如下命令测试 sysgeek 主页看看：
curl --http2 -I https://www.sysgeek.cn
