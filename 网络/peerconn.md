# peerconn 是什么

一种连接不同 vpc 的互连服务。具体来说，可以实现 vpcA 下的 bcc 与 vpcB 下的 bcc 流量互通。vpcA 与 vpcB 可以是同一账号下的，也可以是不同账号下的。

一个 peerconn，需要有两个 vpc，每个 vpc 要有一个 port，在这两个 port 之间会创建一个 vxlan 实现不同 vpc 的流量互通。一个 peerconn 只有一个 vni。

# 打流量

工具：netperf
下载地址：https://github.com/HewlettPackard/netperf/releases
最新版的编译安装可能有问题，2.4.5 可用。
