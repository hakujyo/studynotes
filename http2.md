# http2 背景知识

https://zhuanlan.zhihu.com/p/26559480
https://imququ.com/post/http2-resource.html

# curl 支持 http2

为了让 curl 支持 HTTP2 我们需要安装 nghttp2（http2 的 C 语言库）：

## 安装编译工具等

```bash
sudo apt-get install git g++ make binutils autoconf automake autotools-dev libtool pkg-config \
zlib1g-dev libcunit1-dev libssl-dev libxml2-dev libev-dev libevent-dev libjansson-dev \
libjemalloc-dev cython python3-dev python-setuptools
```

## 编译安装 nghttp2

```bash
git clone https://github.com/tatsuhiro-t/nghttp2.git
cd nghttp2
autoreconf -i
automake
autoconf
./configure
make
sudo make install
echo '/usr/local/lib' > /etc/ld.so.conf.d/local.conf
ldconfig
```

## 升级 curl 版本

```bash
cd ~
sudo apt-get build-dep curl
wget http://curl.haxx.se/download/curl-7.46.0.tar.bz2
tar -xvjf curl-7.46.0.tar.bz2
cd curl-7.46.0
./configure --with-nghttp2=/usr/local --with-ssl
sudo make && make install
echo '/usr/local/lib' > /etc/ld.so.conf.d/local.conf
ldconfig
```

升级完版本之后，我们再查看 curl 版本时会发布特性中会增加 HTTP2 功能支持。此时 –http2 参数就可以正常使用了：
如果运行 curl --version 出现 SSL_COMP_free_compression_methods 找不到符号，需要修改下 lib/vtls/openssl.c 里面的宏，关掉压缩

```bash
curl --http2 -I https://nghttp2.org
```

测试 curl with http2

我们再使用如下命令测试 sysgeek 主页看看：

```bash
curl --http2 -I https://www.sysgeek.cn
```
