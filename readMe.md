**后台环境配置**

- 安装pipenv：在终端中输入```brew install pipenv(需要先安装brew)```。
  常用指令：```pipenv graph```查看已安装的依赖
- 进入```/backend/newapi```：```cd backend/newapi```
- 安装django：```pipenv install django```
- 开启虚拟环境：```pipenv shell```
- 开启后台服务：```(newapi) bash-3.2$ python manage.py runserver```


---

**后台启动**
- 安装python配置，运行```pipenv install```（该步骤建议在vpn环境下运行，因为资源库在国外）
- 运行推荐模板生成模块，输入```python recommendController.py```
- 另起一个terminal，用于运行后台系统，输入```python manage.py makemigrations```,回车后再输入```python manage.py migrate```,
上述两个命令用于数据库的更新与格式化，最后输入```python manage.py runserver```启动数据库。
- 后台系统运行在`127.0.0.1:8000`，用户可通过`127.0.0.1:8000/admin`查看管理员系统


**后台调试前置条件**

- 修改```host```文件：<a href="https://blog.csdn.net/dingqk/article/details/77982910">如何修改mac的host文件</a>
- 开启微信小程序本地调试：点击菜单栏```设置/项目设置```，勾选最下面的一个选项，不校验http证书和合法域名
