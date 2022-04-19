<table>
    <tr style="vertical-align:middle; text-align:left;word-break:keep-all">
        <th tyle="ertical-align:middle; text-align:left;word-break:keep-all;wide=100%">作用</th>
        <th>操作</th>
    </tr>
    <tr>
        <td>展示表结构</td>
        <td>show create table table_name;</td>
    </tr>
    <tr>
        <td>查询表索引</td>
        <td>show index from table_name;</td>
    </tr>
    <tr>
        <td>创建普通 user</td>
        <td>use mysql; <br>         
        INSERT  INTO `user`(`Host`,`User`,`Password`,`Select_priv`,`Insert_priv`,`Update_priv`,`Delete_priv`,`Create_priv`,`Drop_priv`,`File_priv`,`References_priv`,`Index_priv`,`Alter_priv`,`Show_db_priv`,`Create_tmp_table_priv`,`Lock_tables_priv`,`Execute_priv`,`Create_view_priv`,`Show_view_priv`,`Create_routine_priv`,`Alter_routine_priv`,`Event_priv`,`Trigger_priv`) VALUES ('%','blb','blb','Y','Y','Y','Y','Y','Y','Y','Y','Y','Y','Y','Y','Y','Y','Y','Y','Y','Y','Y','Y'); 
        </td>
    </tr>
    <tr>
        <td>数据库导入导出表结构</td>
        <td>导出：<br>
            mysqldump -h10.107.42.56 -P3306 -ubcc -pbcc -d meta_server >meta_server.sql; <br>
            导入：<br>
            mysql -h10.136.32.34 meta_server -P7010 -ubce-sandbox -p2BGgkVZzEeimX2BGgkVZzEeiSXxBcgQV < meta_server.sql
        </td>
    </tr>
    <tr>
        <td>对比表结构差异</td>
        <td><b>安装：</b><br>
            wget https://ylybucket.su.bcebos.com/tools%2Fmysql-utilities-1.6.5.tar.gz<br>
            tar -zxvf mysql-utilities-1.6.5.tar.gz<br>
            cd mysql-utilities-1.6.5<br>
            python setup.py build<br>
            python setup.py install<br>
            mysqldiff --version<br>
            mysql-connector-python 安装<br>
            下载地址：https://dev.mysql.com/downloads/connector/python/<br>
            <b>mysql-utilities 安装</b><br>
            下载地址：http://downloads.mysql.com/archives/utilities/
            mysqldiff --server1=root:password@127.0.0.1:3306 --server2=root:password@127.0.0.1:3306 --force --difftype=sql db1:db2<br>
            安装以后执行查看版本命令，如果能显示版本表示安装成功<br>
            mysqldiff --version<br>
            MySQL Utilities mysqldiff version 1.6.5<br>
            License type: GPLv2<br>
            <b>mysqldiff 使用方法</b><br>
            命令：<br>
            mysqldiff --server1=root:password@host1:port --server2=root:password@host2:port --force --difftype=sql db1(.table1):db2(.table3)<br>
            参考：https://blog.csdn.net/fdipzone/article/details/78884518<br>
        </td>
    </tr>
    <tr>
        <td>查看建表语句</td>
        <td>SHOW CREATE TABLE tbl_name;</td>
    </tr>
    <tr>
        <td>改变表约束</td>
        <td>ALTER TABLE table_name ADD UNIQUE (name);</td>
    </tr>
    <tr>
        <td>改变表增加主键</td>
        <td>alter table elb_instance add primary key(id); <br>
            alter table elb_cert change column id id int(11) not null default null auto_increment; 
        </td>
    </tr>
