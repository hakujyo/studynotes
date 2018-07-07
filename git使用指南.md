要使用git工具，首先你需要一个服务器，一般为github，我们在上面建一个仓库
在本地建立git文件夹
> ```shell
> git init 
> ```
检查有没有 .git文件夹 ，注意不要随意更改这个文件夹，里面存储着git版本信息
> ```shell
> ls -ah 
> ```
写一个读我把：D
> ```shell
> vim readme.txt
> ```
将读我把添加到本地仓库
> ```shell
> git add readme.txt
> ```
提交该版本
> ```shell
> git commit -m “commit info”
> ```
上传到github服务器
> ```shell
> git push -u origin master   
> ```
注意 这里如果是第一次提交，需要先设置本地仓库
> ```shell
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
