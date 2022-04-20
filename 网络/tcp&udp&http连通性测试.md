# tcp&udp&http 服务部署助手

```bash
wget http://ylybucket.su.bcebos.com/TestHelper%2Fhttp_tcp_udp_deploy.sh
```

# 下载资源（tcp_server,tcp_client,udp_server,udp_client）

```bash
wget https://ylybucket.su.bcebos.com/TestHelper%2Fsocket_pool.py
```

# 后台启动

## udp server

```bash
nohup python ./socket_pool.py --port=8003  --proto=udp --server &
```

## udp client

```bash
python socket_pool.py --client  --srv_ip=100.65.1.44 --port=8003 --proto=udp
```

> (以下两种服务展示文件目录，暴露.ssh 文件，会被认为有安全漏洞，不建议使用)

## ipv4 http&tcp

```bash
nohup python -m SimpleHTTPServer 80 &
```

## 双栈 http&tcp（支持 ipv4&ipv6）

```bash
nohup python -c "import socket,SocketServer,CGIHTTPServer;SocketServer.TCPServer.address_family=socket.AF_INET6;CGIHTTPServer.test()" 80 &
```

# 查看端口占用情况

```bash
netstat -apn
```

# 查看已有端口号（如查看所有 80 端口使用情况）

```bash
netstat -ntulp |grep 80
```

> -t : 指明显示 TCP 端口

> -u : 指明显示 UDP 端口

> -l : 仅显示监听套接字

> -p : 显示进程标识符和程序名称

> -n : 不进行 DNS 轮询，显示 IP(可以加速操作)

# 测试四层连通性：

## tcp

```bash
nc -z -v [ip] [port]
```

## udp

> nc 指令测 udp 状态不太准：udp 没有连接状态，发出去就不管了，不像 tcp 需要对端回个确认包，所以发出去之后是不知道对面有没有收到的

```bash
nc -z -v -u [ip] [port]
```

## 测试七层连通性：

```bash
curl http://xxx:port/
```

## 四层打流量

http://man.linuxde.net/iperf

```bash
iperf3 -s -p [port]
iperf3 -c [ip] -t [time] -p [port]
```

### ipv6 udp server

```bash
iperf -s -u -V -p 8003
```

### ipv6 client

```bash
iperf -c 2400:da00:e003:c02::4f -p 8899 -b 8 -t 300 -V
```

### 七层打流量

```bash
ab -n 12000 -c 300 http://xxx:port/
```

### query param 测分流

```bash
wget https://ylybucket.su.bcebos.com/TestHelper%2Ftest_tool.tar.bz2
wget https://ylybucket.su.bcebos.com/TestHelper%2Fpython2.7.17.tar.bz2
```

解压后，修改 code.py 里希望显示的内容(test01/test02 等等)

```bash
source venv/bin/activate
nohup python code.py 1234 &
```
