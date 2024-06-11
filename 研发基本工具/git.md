### 远程登录密钥发送
```
ssh-copy-id -i ~/.ssh/id_rsa.pub user@ip
```
### 删除暂存区或分支上的文件, 但本地又需要使用, 但不希望这个文件被版本控制,
```
git rm --cached filename
```
### 版本冲突问题
```
error: Your local changes to the following files would be overwritten by merge:
        xxx/xxx.xxx
Please, commit your changes or stash them before you can merge.
```
如果希望保留生产服务器上所做的改动,仅仅并入新配置项, 处理方法如下:
```
git stash
git pull
git stash pop
```
然后可以使用git diff -w +文件名 来确认代码自动合并的情况.

反过来,如果希望用代码库中的文件完全覆盖本地工作版本. 方法如下:
```
git reset --hard
git pull
```

### git upstream和origin的区别
https://blog.csdn.net/weixin_37646636/article/details/129778632
upstream是开源仓库，origin是你的仓库下fork开源仓库的远端仓库，local是你本地的仓库

### 基于upstream只提交一个commit的方法
https://www.cnblogs.com/xuejianbest/p/10285278.html
比如你开发过程中，upstream已经被别人pull request了，这样你本地分支commit就会落后于upstream。
```
git fetch upstream [branch]
git rebase upstream/[branch]
```
