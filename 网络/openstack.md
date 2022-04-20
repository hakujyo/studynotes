# NEUTRON

## neutron cli

| 作用                          | 命令                                                                              |
| ----------------------------- | --------------------------------------------------------------------------------- |
| 查看 vpc                      | neutron vpc-list --tenant-id ${tenant_id}98654                                    |
| 查看一个 vpc 下的 subnet 信息 | neutron subnet-list --network-id ${vpc_id}                                        |
| 查看 subnet 信息              | neutron subnet-show ${subnet_id}                                                  |
| 查看 device 对应的 port 信息  | neutron port-list --device-id  ${vm_id}                                           |
| 根据 port id 查看 port 信息   | neutron port-show ${port_id}                                                      |
| 更新 port                     | neutron port-update ${port-id} --fixed_ips type=dict list=true ip_address='${ip}' |
| 更新 port(模拟虚机迁移)       | neutron port-update ${port_id} --binding:host_id ${CN hostname}                   |

看路由信息
环境
nmg02-bce-test92.nmg02.baidu.com
设置环境变量-超级管理员账户

source /home/bcc/etc/openstack-admin.rc
先拿到路由表

neutron route-table-list --vpc-id xxx
看路由规则

neutron route-rule-list --route-table-id xxx
看流表
登陆 vm 所对应的物理机（CN），先通过执行 ovs-vsctl show 根据 port 找到 tag，也就是 vlan_id，然后查看 17 号流表。ovs-ofctl dump-flows br-tun,table=17,dl_vlan=xxx，看优先级是 1 的流表是不是 src 和 dst 都是 0
