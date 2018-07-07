## 0x00 引言

以前玩过集成php开发环境，phpstudy，wampServer什么的，但是傻瓜式的集成包让我有种无法掌控个人电脑的不安全感。。。所以还是推荐手工搭建PHP开发环境。=。=
顾名思义，wamp，windows+apache+mysql+php。

## 0x01 Apache http server的编译安装

Apache http server在windows上是没有直接安装包的，需要自己编译。（应用市场上可能有，不过都是很老的版本，个人不太喜欢，还是喜欢自己编译）

 Apache http server的下载地址：http://httpd.apache.org/docs/current/platform/windows.html#down

进入以后选择ApacheHaus，这个是Apache http server本体，WampServer跟XAMPP已经是傻瓜式集成环境包了=。=

下载完毕以后，进入conf文件夹，用记事本打开httpd.conf。

找到Define SRVROOT “baseroot\httpd-2.4.27-x64-vc14\Apache24″这行，将路径改为Apache24文件夹所在的当前目录。

另外Listenen 80这行也需要注意，在cmd下用命令netstat -a查看当前80端口是否被占用，被占用了的话换一个端口号。

修改完毕后保存，进行Apache主服务的安装。

用管理员身份打开cmd，输入命令：“baseroot\httpd-2.4.27-x64-vc14\Apache24\bin\httpd.exe” -k install -n apache

apache是Apache服务器的服务名，也可以是别的。

如果出现如：

The ‘apache’ service is successfully installed.
Testing httpd.conf….
Errors reported here must be corrected before the service can be started.

字样，并且Errors那行后面没有继续报错，那么安装成功。

进入浏览器测试：输入localhost，此时页面应该已变成ApacheHaus的欢迎界面，说明apache服务器已经可以运行

卸载apache，需要先卸载apache服务。在CMD命令窗口，输入sc delete apache

（apache是Apache服务器的服务名）

## 0x02 Php的安装配置

Php的下载地址：http://php.net/downloads.php

php解压后需要跟apache做一些绑定，用记事本打开apache的httpd.conf文件。

在文件最后添加：
> ```php
> # php7 support
> LoadModule php7_module baseroot/php-7.1.7-Win32-VC14-x64/php7apache2_4.dll
> AddType application/x-httpd-php .php .html .htm
> # configure the path to php.iniPHPIniDir “D:/php”
> ```
将php.ini-development更改为php.ini文件，打开：
> date.timezone = Asia/Shanghai
> extension_dir = “ext”去掉分号,并改为ext的完整路径
> extension=php_mysqli.dll，extension=php_mbstring.dll去掉分号（这几步是为了之后配置phpmyadmin做准备）
以上基本将配好了，测试一下，在baseroot\Apache\htdocs 文件夹下添加一个phpinfo.php文件，里面的内容设置为
> ```php
> <?php
> phpinfo();
> ?>
> ```
重启apache http server，在浏览器中打开localhost:/phpinfo.php，出现php信息页面则php+Apache的环境就配置完成了。

## 0x03 MySQL的安装配置

MySQL的下载地址：https://dev.mysql.com/downloads/windows/

跟apache http server相比，mysql的安装就显得非常容易，下载后跟着安装向导安装即可。而

需要注意的是如果下载mysql workbench，那么下载的还会带一个图形界面，对新手和记不住基本sql语句的用户更友好一些。

php和mysql的版本要么全选x64，要么全选x86，最好不要混搭。

将baseroot\MySQL\MySQL Server 5.7\bin；加入到环境变量。

进入cmd，mysqld -install

mysql -uroot -p进入mysql

## 0x04 PhpMyAdmin的安装配置

PhpMyAdmin的下载地址：https://www.phpmyadmin.net/downloads/

将压缩包解压到baseroot\htdocs目录下。

打开 libraries 目录下的 config.default.php 文件，配置：

配置访问网址：$cfg[‘PmaAbsoluteUri’] = ‘http://localhost/phpMyAdmin/’;，路径也可以是别的。

MySQL主机信息：

$cfg[‘Servers’][$i][‘host’] = ‘localhost’;，填写 localhost  或 MySQL  所在服务器的 ip 地址，如果 MySQL 和该 phpMyAdmin 在同一服务器，则按默认 localhost

$cfg[‘Servers’][$i][‘socket’] = ‘3306’;，MySQL 端口，默认为 3306，保留为空即可，如果安装 MySQL 时使用了其它的端口，需要在这里填写。

MySQL用户名和密码
> $cfg[‘Servers’][$i][‘user’] = ‘root’;
> $cfg[‘Servers’][$i][‘password’] = ‘123456’;

认证方法

> $cfg[‘Servers’][$i][‘auth_type’] = ‘cookie’

短语密码（blowfish_secret）的设置

$cfg[‘blowfish_secret’] = ”;如果认证方法设置为 cookie，就需要设置短语密码，设置为什么密码，由您自己决定，这里不能留空，否则会在登录 phpMyAdmin 时提示的错误。

测试：浏览器打开localhost/phpmyadmin，出现phpmyadmin的主页，则配置成。
