# pip 下载镜像慢问题：

就近选择国内镜像：

```bash
pip install django -i https://pypi.tuna.tsinghua.edu.cn/simple
```

# 有关 python2 和 3 冲突的问题

可以给 python2 和 3 的 exe 文件改名，比如改成 python2.exe 和 python3.exe。

使用 pip 时，用 python[ver] -m [...] 区分 python2 和 3，例如：

```bash
python3 -m pip install django -i https://pypi.tuna.tsinghua.edu.cn/simple
```

# python 支持 openssl 指定版本

-   编译安装 openssl：https://github.com/openssl/openssl/blob/master/INSTALL

```bash
./config --prefix=/opt/openssl --openssldir=/usr/local/ssl
```

-   源码编译安装 python

```bash
./configure --prefix=/usr/local/python CPPFLAGS="-I/opt/openssl/include" LDFLAGS="-L/opt/openssl/lib"
make
install
```

# python 指定版本安装 pip

```bash
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python get-pip.py pip==19.3.1
```

> 可直接降级 pip，注意 pip==20.0.1 版本有 bug，需降级

# python virtualenv 做环境隔离

## 安装

```bash
python2 -m pip install virtualenv
python2 -m virtualenv --no-site-packages venv
```

## 启动 venv 环境

### linux

```bash
source venv/bin/activate
```

OR

```bash
source venv/Scripts/activate
```

### windows

```bash
venv/Sciptes/activate.bat
```

### pycharm

setting 里把 intepreter 设置为 venv 中的 python，然后重启 pycharm

## 退出 venv 环境

```bash
deactivate
```

## virtualenv 的一些坑

之前在用 virtualenv 移植 python 运行环境的时候遇到过\_ssl.so 找不到的问题，和 virtualenv 本身不会复制系统库文件\_ssl.so 有关，如果用 virtualenv 需要自己替换\_ssl.so 文件参考：

https://blog.csdn.net/u012291393/article/details/78452221

```bash
find / -iname _ssl.so
```

# 依赖包管理

推荐使用 requirements.txt 管理

## 生成 requirements.txt

```bash
pip freeze > requirements.txt
```

### 查看依赖包

```bash
pip list
```

### 使用 requirements.txt：

```bash
pip install -r requirements.txt
```

# python 离线打包依赖

-   先用上面的方法生成一个 requirements.txt
-   在有网的情况下，执行下面命令，将依赖的文件包下载到 packages 目录中
    pip download -d packages/ -r requirements.txt
-   最后将 package 目录和 requirement.txt 文件拷贝到需要安装的没有网络的机器上

```bash
pip install --no-index --find-links=packages/ -r requirements.txt
```
