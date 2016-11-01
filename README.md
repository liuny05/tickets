# tickets_12306
这是我在实验楼的
[Python3 实现火车票查询工具](https://www.shiyanlou.com/courses/623)
实验中写的代码

用的语言是Python2而不是原来的Python3，另外改进了一些功能并修补了一些漏洞

运行在 gbk 编码的命令行中，win10 的 cmd 亲测成功

##功能

在命令行中输入以下命令，即可返回相应的火车时刻表

```
tickets [-gdtkz] <from> <to> <date>
```

其中`[-gdtkz]`代表火车类型

效果如下图

![最终效果](https://dn-simplecloud.shiyanlou.com/uid/9db2fd51abe7de1fbd1ceffc43ef0e22/1478012985150.png-wm)


##用法

本项目需要用到第三方库，可通过以下命令安装

```
pip install urllib3 prettytable docopt colorama
```

推荐将本项目作为包安装进Python中，之后即可在命令行任意目录运行。步骤如下：

切换到本项目所在目录，运行命令

```
python setup.py install
```

然后你就可以在任意目录通过以下命令进行火车票查询了 :)

```
tickets [-gdtkz] <from> <to> <date>
```

如果不希望将本项目作为package安装，则可切到项目所在目录，通过以下命令运行

```
python tickets.py [-gdtkz] <from> <to> <date>
```

**注意**

本项目假定所有字符均为 gbk 输入 utf-8 输出，因此需运行在以 gbk 为默认编码的命令行中，且需设定显示的编码为 utf-8 ，对于windows系统，通过以下命令进行设置

```
chcp 65001
```

###关于本项目及对应课程的更多内容，可参见[我的实验报告](https://www.shiyanlou.com/courses/reports/1247705)
