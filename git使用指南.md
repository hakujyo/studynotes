## 创建版本库
### 创建一个空目录
> ``` git bash
> $ mkdir learngit
> $ cd learngit
> $ pwd
> /d/learngit
> ```

### 把这个目录变成Git可以管理的仓库
> ``` git bash
> $ git init 
> Initialized empty Git repository in D:/learngit/.git/
> ```

### .git目录是Git来跟踪管理版本库的,不能随便修改删除
> ``` git bash
> $ ls -ah
> ./  ../  .git/
> ```

## 提交版本与版本回退
### 将读我把添加到版本暂存区
> ``` git bash
> $ git add readme.txt
> ```

### 一次性把暂存区的所有修改提交到分支
> ``` git bash
> $ git commit -m "wrote a readme file"
> [master (root-commit) 8e09117] wrote a readme file
>  1 file changed, 2 insertions(+)
>  create mode 100644 readme.txt
> ```

### 修改readme，查看状态，会提示把改动添加到版本库或者丢弃
> ``` git bash
> $ git status
> On branch master
> Changes not staged for commit:
>   (use "git add <file>..." to update what will be committed)
>   (use "git checkout -- <file>..." to discard changes in working directory)
> 
>         modified:   readme.txt
> 
> no changes added to commit (use "git add" and/or "git commit -a")
> ```

### 对比上一个版本修改的内容
> ``` git bash
> $ git diff readme.txt
> diff --git a/readme.txt b/readme.txt
> index 46d49bf..9247db6 100644
> --- a/readme.txt
> +++ b/readme.txt
> @@ -1,2 +1,2 @@
> -Git is a version control system.
> +Git is a distributed version control system.
>  Git is free software.
> ```

### 查看所有日志
> ``` git bash
> $ git log
> commit 9e51fdd8c92aa09bf8a9eaed2479f61f7591da22
> Author: yoruneko <hakujyo0518@gmail.com>
> Date:   Sun Aug 19 16:58:15 2018 +0800
> 
>     add distributed
> 
> commit 8e09117453ce6f62c2b1b79160681643b8af239b
> Author: yoruneko <hakujyo0518@gmail.com>
> Date:   Sun Aug 19 14:45:53 2018 +0800
> 
>     wrote a readme file
> 
> ```

### 回退到上一个版本
> ``` git bash
> git reset --hard HEAD^
> ```

### 重置到任一版本
> ``` git bash
> git reset --hard [commitid]
> ```

### 查看head指针历史记录
> ``` git bash
> $ git reflog
> 8e09117 HEAD@{0}: reset: moving to HEAD^
> 9e51fdd HEAD@{1}: commit: add distributed
> 8e09117 HEAD@{2}: commit (initial): wrote a readme file
> ```

### 让工作区文件回到最近一次git commit或git add时的状态
> ``` git bash
> $ git checkout -- [file]
> ```

### 让已经添加到暂存区的文件回到head指针指向的版本
> ``` git bash
> $ git reset HEAD [file]
> ```

### 上传到github服务器
> ``` git bash
> $ git push -u origin master   
> ```

## 小结
> * 场景1：当你改乱了工作区某个文件的内容，想直接丢弃工作区的修改时，用命令git checkout -- &lt;file&gt;。
> * 场景2：当你不但改乱了工作区某个文件的内容，还添加到了暂存区时，想丢弃修改，分两步，第一步用命令git reset HEAD &lt;file&gt;，就回到了场景1，第二步按场景1操作。
> * 场景3：已经提交了不合适的修改到版本库时，想要撤销本次提交，用命令git reset --hard HEAD^，不过前提是没有推送到远程库。



注意 这里如果是第一次提交，需要先设置本地仓库
> ``` git bash
> git remote add origin git@github.com/…blablabla
> ```
上一步要注意的是不要选择https方式上传代码

如果不幸选择了，可以remote，然后重新添加远程github仓库
> ```shell
> git remote rm origin            
> ```
为了不每次都密码登陆，我们选择创建rsa密钥
> ```shell
> ssh-keygen -t rsa -C “your e-mail”
> ```
这样密钥和公钥就产生啦，默认的钥匙位置在~/.ssh
上面这步windows用户可能会出错，文件目录的锅，所以推荐还是在类unix的git bash下进行git操作啦0w0
将公钥交给github！
> ```shell
> cat ~/.ssh/id_rsa.pub  
> ```
这样就能愉快的在gayithub里玩耍了！
从github服务器下载代码
> ```shell
> git  pull                                             
> ```
如果是多人协作写代码的话，上一步之前，要先pull别人的代码下来看
但是又不想更改自己的代码，先 git stash存储一下
git pull，然后再git stash pop，拿出来
