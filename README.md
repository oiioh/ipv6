<div align="center">

# 获取ipv6地址
通过python代码，利用QQ邮箱或者企业微信机器人实现获取ipv6地址的目的。

</div>

# 📋 教程

## 1.下载python
### 1.1下载地址：
https://www.python.org/downloads/

### 1.2配置环境
通过Win+R输入CMD打开命令提示符，输入以下命令
```
pip install requests
```

## 2.下载python代码
下载qq.py.txt或wx.py.txt文件，下载后将后缀.txt去除。
![](https://github.com/oiioh/ipv6/releases/tag/0.0.1)

## 3.自动运行
### 3.1任务计划程序
在任务计划程序中，添加触发器与操作实现自动运行。
#### 第一步
![](https://github.com/oiioh/ipv6/blob/main/image/IMG_20241226_001646.png)

#### 第二步
![](https://github.com/oiioh/ipv6/blob/main/image/IMG_20241226_002043.png)

#### 第三步
![](https://github.com/oiioh/ipv6/blob/main/image/IMG_20241226_002414.png)

#### 第四步
![](https://github.com/oiioh/ipv6/blob/main/image/IMG_20241226_002545.png)

#### 第五步
![](https://github.com/oiioh/ipv6/blob/main/image/IMG_20241226_003116.png)



### 3.2脚本运行
#### 3.2.1新建一个bat文件
新建一个qq-ipv6.bat文件，输入以下内容
```
.\qq.py server
```

或新建一个wx-ipv6.bat文件，输入以下内容
```
.\wx.py server
```
由于bat文件运行时存在命令框，因此需要新建一个vbs文件

#### 3.2.2新建一个vbs文件
新建一个qq-ipv6.vbs文件，输入以下内容
```
set ws=WScript.CreateObject("WScript.Shell")
ws.Run "qq-ipv6.bat",0
```

或新建一个wx-ipv6.vbs文件，输入以下内容
```
set ws=WScript.CreateObject("WScript.Shell")
ws.Run "wx-ipv6.bat",0
```

#### 3.2.3开机自启
将上面的vbs文件创建快捷方式，将快捷方式放入下面的文件夹
```
C:\Users\hhh\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup
```
