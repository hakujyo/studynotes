# 创建版本库
创建一个空目录
> ``` git bash
> $ mkdir learngit
> $ cd learngit
> $ pwd
> /d/learngit
> ```

把这个目录变成Git可以管理的仓库
> ``` git bash
> $ git init 
> Initialized empty Git repository in D:/learngit/.git/
> ```

.git目录是Git来跟踪管理版本库的,不能随便修改删除
> ``` git bash
> $ ls -ah
> ./  ../  .git/
> ```

# 提交版本与版本回退
将读我把添加到版本暂存区
> ``` git bash
> $ git add readme.txt
> ```

将文件从暂存区删除
> ``` git bash
> $ git rm --cached &lt;file&gt
> ```

 一次性把暂存区的所有修改提交到分支
> ``` git bash
> $ git commit -m "wrote a readme file"
> [master (root-commit) 8e09117] wrote a readme file
>  1 file changed, 2 insertions(+)
>  create mode 100644 readme.txt
> ```

修改readme，查看状态，会提示把改动添加到版本库或者丢弃
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

对比上一个版本修改的内容
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

查看所有日志
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

回退到上一个版本
> ``` git bash
> git reset --hard HEAD^
> ```

重置到任一版本
> ``` git bash
> git reset --hard [commitid]
> ```

查看head指针历史记录
> ``` git bash
> $ git reflog
> 8e09117 HEAD@{0}: reset: moving to HEAD^
> 9e51fdd HEAD@{1}: commit: add distributed
> 8e09117 HEAD@{2}: commit (initial): wrote a readme file
> ```

用版本库里的版本替换工作区的版本
> ``` git bash
> $ git checkout -- [file]
> ```

让已经添加到暂存区的文件回到head指针指向的版本
> ``` git bash
> $ git reset HEAD [file]
> ```

上传到github服务器
> ``` git bash
> $ git push -u origin master   
> ```

从版本库中删除文件
> ``` git bash
> $ git rm &lt;file&gt;
> $ git commit -m "remove file"
> ```

## 小结
> * 场景1：当你改乱了工作区某个文件的内容，想直接丢弃工作区的修改时，用命令git checkout -- &lt;file&gt;。
> * 场景2：当你不但改乱了工作区某个文件的内容，还添加到了暂存区时，想丢弃修改，分两步，第一步用命令git reset HEAD &lt;file&gt;，就回到了场景1，第二步按场景1操作。
> * 场景3：已经提交了不合适的修改到版本库时，想要撤销本次提交，用命令git reset --hard HEAD^，不过前提是没有推送到远程库。


# 远程仓库
## 密钥
1. 创建ssh key
> ```shell
> $ ssh-keygen -t rsa -C “your e-mail”
> ```
这样密钥和公钥就产生啦，默认的钥匙位置在~/.ssh
上面这步windows用户可能会出错，文件目录的锅，所以推荐还是在类unix的git bash下进行git操作啦0w0

2. 将公钥交给github！
> ```shell
> $ cat ~/.ssh/id_rsa.pub  
> ```
这样就能愉快的在g~~ay~~ithub里玩耍了！

## 添加远程仓库
1. 在github上“Create a new repo”，并将本地库关联远程仓库
> ```shell
> $ git remote add origin git@github.com:hakujyo/learngit.git
> ```

上一步要注意的是不要选择https方式上传代码，如果不幸选择了，可以remote，然后重新添加远程github仓库
> ```shell
> git remote rm origin            
> ```

把本地库的所有内容推送到远程库上（注意第一次一定要加-u）：
> ```shell
> $ git push -u origin master
> ```

## 小结
> * 要关联一个远程库，使用命令git remote add origin git@server-name:path/repo-name.git；
> * 关联后，使用命令git push -u origin master第一次推送master分支的所有内容；
> * 此后，每次本地提交后，只要有必要，就可以使用命令git push origin master推送最新修改；

## 从远程库克隆
> ```shell
> $ git clone git@server-name:path/repo-name.git
> ```

# 分支管理
创建+切换分支
> ```shell
> $ git checkout -b dev
> Switched to a new branch 'dev'
> ```

创建分支：
> ```shell
> $ git branch dev
> ```

切换分支：
> ```shell
> $ git checkout dev
> ```

查看当前分支
> ```shell
> $ git branch
> ```

合并指定分支到当前分支
> ```shell
> $ git merge [branchname]
> ```

删除分支
> ```shell
> $ git branch -d [branchname]
> ```

对于没有被合并的分支，需要强制删除分支
> ```shell
> $ git branch -D [branchname]
> ```

查看分支合并情况
> ```shell
> $ git log --graph --pretty=oneline --abbrev-commit
> ```

# bug分支
对于已经add到暂存区的内容，又要临时用别的分支完成任务，可以先stash保护现场：
> ```shell
> $ git stash
> ```

查看工作现场
> ```shell
> $ git stash list
> stash@{0}: WIP on dev: f52c633 add merge
> ```

等处理完毕，再切换到该分支，释放出来：
> ```shell
> $ git stash pop
> ```

这种方法约等于两个命令：
> ```shell
> $ git stash apply # 恢复工作区
> $ git stash drop  # 删除该stash
> ```

有多次stash的时候，就需要先git stash list查看，然后恢复指定工作区：
> ```shell
> $ git stash apply stash@{0}
> ```


## 小结
> * 修复bug时，我们会通过创建新的bug分支进行修复，然后合并，最后删除；
> * 当手头工没有完成时，先把工作现场git stash一下，然后去修复bug，修复后，再git stash pop，回到工作现场。

# 多人协作
查看远程库的信息
> ```shell
> $ git remote                                             
> ```

显示更详细的远程库信息
> ```shell
> $ git remote -v                                              
> ```

推送分支
> ```shell
> $ git push origin &lt;branch-name&gt;                                            
> ```

抓取分支
> ```shell
> $ git clone git@server-name:path/repo-name.git                                         
> ```

创建远程origin的dev分支到本地
> ```shell
> $ git checkout -b dev origin/dev                                        
> ```

如果没有指定本地dev分支与远程origin/dev分支的链接，要先设置dev和origin/dev的链接：
> ```shell
> $ git branch --set-upstream-to &lt;branch-name&gt;                                       
> ```

下拉远程库最新代码
> ```shell
> $ git pull                                       
> ```
   
## 多人协作的工作模式通常是这样：
> 1. 首先，可以试图用git push origin <branch-name>推送自己的修改；
> 2. 如果推送失败，则因为远程分支比你的本地更新，需要先用git pull试图合并；
> 3. 如果合并有冲突，则解决冲突，并在本地提交；
> 4. 没有冲突或者解决掉冲突后，再用git push origin <branch-name>推送就能成功！
> 5. 如果git pull提示no tracking information，则说明本地分支和远程分支的链接关系没有创建，用命令git branch --set-upstream-to &lt;branch-name&gt; origin/<branch-name>。

## 小结
> * 查看远程库信息，使用git remote -v；
> * 本地新建的分支如果不推送到远程，对其他人就是不可见的；
> * 从本地推送分支，使用git push origin branch-name，如果推送失败，先用git pull抓取远程的新提交；
> * 在本地创建和远程分支对应的分支，使用git checkout -b branch-name origin/branch-name，本地和远程分支的名称最好一致；
> * 建立本地分支和远程分支的关联，使用git branch --set-upstream branch-name origin/branch-name；
> * 从远程抓取分支，使用git pull，如果有冲突，要先处理冲突。

