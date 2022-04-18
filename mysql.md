| 作用                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | 操作                          |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------- |
| 展示表结构                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | show create table table_name; |
| 查询表索引                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | show index from table_name;   |
| 创建普通 user                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | use mysql;                    |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| INSERT  INTO `user`(`Host`,`User`,`Password`,`Select_priv`,`Insert_priv`,`Update_priv`,`Delete_priv`,`Create_priv`,`Drop_priv`,`File_priv`,`References_priv`,`Index_priv`,`Alter_priv`,`Show_db_priv`,`Create_tmp_table_priv`,`Lock_tables_priv`,`Execute_priv`,`Create_view_priv`,`Show_view_priv`,`Create_routine_priv`,`Alter_routine_priv`,`Event_priv`,`Trigger_priv`) VALUES ('%','blb','blb','Y','Y','Y','Y','Y','Y','Y','Y','Y','Y','Y','Y','Y','Y','Y','Y','Y','Y','Y','Y'); |
| 数据库导入导出表结构                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |

导出：
mysqldump -h10.107.42.56 -P3306 -ubcc -pbcc -d meta_server >meta_server.sql;
导入：
mysql -h10.136.32.34 meta_server -P7010 -ubce-sandbox -p2BGgkVZzEeimX2BGgkVZzEeiSXxBcgQV < meta_server.sql |
| 对比表结构差异 |
安装：
wget https://ylybucket.su.bcebos.com/tools%2Fmysql-utilities-1.6.5.tar.gz
tar -zxvf mysql-utilities-1.6.5.tar.gz
cd mysql-utilities-1.6.5
python setup.py build
python setup.py install
mysqldiff --version

mysql-connector-python 安装
下载地址：https://dev.mysql.com/downloads/connector/python/
mysql-utilities 安装
下载地址：http://downloads.mysql.com/archives/utilities/
mysqldiff --server1=root:password@127.0.0.1:3306 --server2=root:password@127.0.0.1:3306 --force --difftype=sql db1:db2
安装以后执行查看版本命令，如果能显示版本表示安装成功
mysqldiff --version
MySQL Utilities mysqldiff version 1.6.5
License type: GPLv2
mysqldiff 使用方法
命令：
mysqldiff --server1=root:password@host1:port --server2=root:password@host2:port --force --difftype=sql db1(.table1):db2(.table3)
参考：https://blog.csdn.net/fdipzone/article/details/78884518
|
|查看建表语句 |
SHOW CREATE TABLE tbl_name |
|改变表约束 |
ALTER TABLE table_name ADD UNIQUE (name) |
| 改变表增加主键 |
alter table elb_instance add primary key(id); |
| | alter table elb_cert change column id id int(11) not null default null auto_increment; |
