[toc]

# 打包压缩

具体参考《鸟哥的 Linux 私房菜》：http://cn.linux.vbird.org/linux_basic/0240tarcompress.php

## 常见压缩格式：

| 扩展名     | 含义                                          |
| ---------- | --------------------------------------------- |
| \_.Z       | compress 程序压缩的文件                       |
| \_.gz      | gzip 程序压缩的文件                           |
| \_.bz2     | bzip2 程序压缩的文件                          |
| \_.tar     | tar 程序打包的数据，并没有压缩过              |
| \_.tar.gz  | tar 程序打包的文件，其中并且经过 gzip 的压缩  |
| \_.tar.bz2 | tar 程序打包的文件，其中并且经过 bzip2 的压缩 |

一般现在常用的压缩技术是 gzip 和 bzip2。一般不单独使用压缩工具对单个文件压缩，而是通过打包工具 tar 对整个文件夹进行打包并压缩。

## .tar 常见参数：

| 参数        | 含义                                                        | 备注                                              |
| ----------- | ----------------------------------------------------------- | ------------------------------------------------- |
| -c          | 创建打包文件，可搭配 -v 来察看过程中被打包的档名(filename)  | 打包参数，-c, -t, -x 不可同时出现在一串命令列中。 |
| -t          | 察看打包文件的内容含有哪些档名，重点在察看『档名』          |
| -x          | 解打包或解压缩的功能，可以搭配 -C (大写) 在特定目录解开     |
| -j          | 透过 bzip2 的支持进行压缩/解压缩：此时档名最好为 \_.tar.bz2 | 压缩参数                                          |
| -z          | 透过 gzip 的支持进行压缩/解压缩：此时档名最好为 \_.tar.gz   |
| -v          | 在压缩/解压缩的过程中，将正在处理的档名显示出来             |
| -f filename | -f 后面要立刻接要被处理的档名，建议 -f 单独写一个选项       |
| -C          | 这个选项用在解压缩，若要在特定目录解压缩，可以使用这个选项  |

### 最常见的 tar 命令

**通过 bzip2 压缩技术：**

压　缩：tar -jcv -f filename.tar.bz2 要被压缩的文件或目录名称

查　询：tar -jtv -f filename.tar.bz2

解压缩：tar -jxv -f filename.tar.bz2 -C 欲解压缩的目录

**通过 gzip 压缩技术：**

压　缩：tar -zcv -f filename.tar.gz 要被压缩的文件或目录名称

查　询：tar -ztv -f filename.tar.gz

解压缩：tar -zxv -f filename.tar.gz -C 欲解压缩的目录

推荐使用 bzip2 技术，可以得到更好的压缩比。

# 磁盘

## 磁盘管理

https://www.runoob.com/linux/linux-filesystem.html

## inode

inode 知识点学习可以参考这篇文章：https://www.cnblogs.com/jiangxiaoxian/p/9610903.html

笔记：
![image](https://github.com/hakujyo/studynotes/blob/master/pictures/inode.png)

这就是为什么你买 256GB 的硬盘，实际可用只有 200+GB。

![image](https://github.com/hakujyo/studynotes/blob/master/pictures/inode2.png)

这就是为什么：

1.你删掉的文件还能继续跑。。。。

2.你以为文件删了。。。磁盘还是满的

## 进程管理

| 作用         | 命令                   | 常见应用                                 |
| ------------ | ---------------------- | ---------------------------------------- |
|              | ps -ef                 |                                          |
| 查看进程状态 | cat /proc/[pid]/status | 寻找某个子进程的父进程（ppid）以结束程序 |

# cpu

概念参考：CPU：chip、core 和 processor 的关系

# 定时任务

| 任务            | 命令                               | 备注                                        |
| --------------- | ---------------------------------- | ------------------------------------------- |
| 查看定时任务    | crontab -l                         |                                             |
| 编辑定时任务    | crontab -e                         | 【分】【时】【日】【月】【星期】【command】 |
| 重启 crond      | sudo su root;service crond restart |                                             |
| 查看 crond 状态 | service crond status               |                                             |

## 常用系统命令

| 功能               | 命令                                                     |
| ------------------ | -------------------------------------------------------- |
| 添加用户组用户名   | groupadd blb && useradd blb -g blb                       |
| 查看系统内核       | cat /proc/version                                        |
| 查看操作系统版本   | cat /etc/os-release                                      |
|                    | cat /etc/redhat-release（红帽）                          |
| 查看磁盘           | du -sh \*\|grep G                                        |
|                    | df -h                                                    |
| 查看 cpu 信息      | cat /proc/cpuinfo \| grep name \| cut -f2 -d: \| uniq -c |
| 查看内存信息       | cat /proc/meminfo                                        |
| 添加环境变量       | echo "export PATH=$PATH:/usr/local/git/bin" >> ~/.bashrc |
| 查看机器 ip 信息   | ifconfig/ip a                                            |
| 虚机上加 ip 地址   | ip addr add 2400:da00:e003:c02::19 dev eth0              |
|                    | ip -6 route show                                         |
| 上传下载文件       | lrzsz                                                    |
|                    | rz 上传                                                  |
|                    | sz 下载                                                  |
|                    | rz -e 上传大文件                                         |
|                    | sz -e 下载大文件                                         |
| 杀掉进程           | killall [program name]                                   |
| 通过端口号查询进程 | netstat -nlp \| grep port                                |
|                    | ll /proc/[pid]/cwd                                       |

**遇到的坑：**

1. 有时候，文件删除后，磁盘仍然是满的，需要 lsof |grep deleted 看一下是否有文件删掉了但是还被占用着，这种情况需要将打开该文件的进程关闭或者重启，磁盘占用才能被顺利释放。

2. 之前用 top 查看内存占用，结果并没有找到占用最多内存的程序，很奇怪，以下脚本出自宋老板：

    > for proc in `ls /proc/ |grep "^[0-9]"`;do if [ -f /proc/$proc/statm ];then rss=0;tep=`cat /proc/$proc/statm | awk '{print $2}'`;cwd=`readlink /proc/$proc/cwd`;exe=`readlink /proc/$proc/exe`;rss=`echo "scale=4;$tep * 4 / 1024" | bc`;echo "$proc ${rss}MB $cwd $exe";fi;done | sort -nrk2 |less

3. 内存过大解决办法：

    top

    shift+M 按内存占用倒序排序

    如果占用都不大，可能是 cached 占用了，解决方法：https://blog.csdn.net/hellojoy/article/details/80760010

4. 解决机器登录慢

    systemctl restart systemd-logind
    closewait:https://my.oschina.net/gehui/blog/494898
