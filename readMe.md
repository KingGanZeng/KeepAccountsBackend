**后台环境配置**

- 安装pipenv：在终端中输入```brew install pipenv(需要先安装brew)```。
  常用指令：```pipenv graph```查看已安装的依赖
- 进入```/backend/newapi```：```cd backend/newapi```
- 安装django：```pipenv install django```
- 开启虚拟环境：```pipenv shell```
- 开启后台服务：```(newapi) bash-3.2$ python manage.py runserver```


---

**后台调试前置条件**

- 修改```host```文件：<a href="https://blog.csdn.net/dingqk/article/details/77982910">如何修改mac的host文件</a>
- 开启微信小程序本地调试：点击菜单栏```设置/项目设置```，勾选最下面的一个选项，不校验http证书和合法域名
