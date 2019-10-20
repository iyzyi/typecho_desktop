# Typecho博客管理姬

emmmm，说起来，这算是我写的第三个Typecho博客管理的程序了。

* 第一个程序（[typecho_post](https://github.com/iyzyi/typecho_post)）算是入门，功能仅限上传和创建分类。甚至当时没分析好token（因为当时没接触过PHP，实在读不懂源代码），所以被迫将token固定住。显然，这样很容易受到攻击。
* 第二个程序（[typecho_desktop_cmd](https://github.com/iyzyi/typecho_desktop_cmd)）于我而言，是MySQL学习的一大助推力。没错，我，使用pymysql，近似地写了个Typecho的Python后端。后悔死我了。因为初学数据库，各方面处理的都不到位，考虑的并不全面。因为是直接对数据库操作，所以可能插入一些奇奇怪怪的东西，这些东西我都不会处理。而且最最重要的是，我的处理机制和官方的处理机制可能不可能完全相同，一旦有一处不同（比如说少插入了一列数据），后期在web段处理的时候就可能导致错误。轻则显示异常，重则直接报数据库错误。
* 第三个程序就是这个啦。为防止自己写入数据出错，所以，所有涉及数据库改动的操作均模拟web端的操作发包，只有部分读取数据的操作使用pymysql获取。最最重要的是，这个是可视化的程序啦。

## 前排提示

本程序并不通用哦。

因为自定义字段的不同。

当然，如果你不需要自定义字段，忽略即可。也不影响正常使用就是了。

## 功能

* 上传文章：将本地MD文本上传。文本中本地图片自动上传并替换其url，非本站网络图片则先下载再上传。
* 更新文章：修改标题、分类、创建时间、自定义字段内容。当然也会再次上传文本内容。
* 快速更新文章：一键上传，不改动标题、分类等
* 上传独立页面：类比上传文章
* 更新独立页面：类比更新文章
* 快速更新独立页面：类比快速更新文章
* 创建目录
* 更新目录：修改目录名称、缩略名、父级目录
* 删除目录
* 下载文章：下载文章或独立页面
* 下载并打开：下载文章后自动打开文本
* 下载含图片：下载文本并扫描所有图片，并下载到缓存目录下的img文件夹内，完成后将图片url替换为本地相对路径
* 打开文件：打开缓存目录内的选中文章
* 打开缓存目录
* 删除文章：删除文章或独立页面
* 彩蛋：目前没有功能。TODO：打开选中文章的网页
* 全站备份：下载博客中所有的文章、独立页面，含图片。
* 客户端配置：配置参数。一堆bug修复，所以还是手动配置吧。

## 缺陷

胖虎我没有任何开发项目经验，而且也是刚开始学PyQt5，所以自认为本程序存在着很多严重的缺陷，但是碍于个人能力的原因，实在是没有解决的思路，因此将目前已知的缺陷罗列出来。

* 严重卡顿：初步认为原因是没有较好的检验登录状态的机制，导致每一个操作都要重新登录、连接数据库一次。这其实也实在是迫不得已，因为每次web端登录，都会导致登录信息地过期。
* 容错机制不完善。很多地方并没有捕捉异常防错，也有很多地方并没有检查文本框中内容是否合法就发包，导致很可能某一处出错后，程序就会崩溃。因为是我写的，所以可能我知道哪里需要注意，哪里可能出错。但是你们可能并不晓得。所以，如果真的时常崩溃，希望可以理解，毕竟我没有任何开发经验。

## 使用

不建议大家使用该程序哦。写的很烂。

如果真的想看看有多烂，可以按照下面的步骤

保证exe文件和typecho.conf在同一文件夹下，修改typecho.conf

```
[
    {
        "choose":0
    },
    [
        {
            "url":"http://blog3.com",
            "token1":"Vxz(ROBQbZKM)LsWL)!P001^XF5ipASL",
            "ip":"127.0.0.1",
            "user":"root",
            "password":"root",
            "database":"blog3",
            "localDir":"C:\\计算机\\Project\\typecho_desktop_cmd\\md"
        }
    ]
]
```

choose：选择第几个博客（是的，你没有看错，这么烂的项目居然支持多博客切换），从0开始

* url：博客url

* token1：token的来源之一

  typecho是带有token的，token由四部分组成，分别为长度为32的字符串（建站时初始化，之后不变），长度为32的字符串authCode（每次登录时随机化），user的id，一般admin为1，具体页面的referer。四部分以&连接，然后md5作为token。（代码在\var\Widget\Security.php，可自己去看一下）

  我们需要手动获取token1，token2和3连接数据库后程序自动获取，token4也已经写在程序里了，所以只需要获取token1

  搭建typecho一般都用宝塔吧，当然这不重要，只要你能用自己的方式打开网址目录下的`\var\Widget\Security.php`就行。

  打开后，找到

```php
public function execute()
{
    $this->_options = $this->widget('Widget_Options');
    $user = $this->widget('Widget_User');

    $this->_token = $this->_options->secret;
    if ($user->hasLogin()) {
    $this->_token .= '&' . $user->authCode . '&' . $user->uid;
    }
}
```

​	添加`echo "<script>alert('$this->_token')</script>";`,如下：

```php
public function execute()
{
    $this->_options = $this->widget('Widget_Options');
    $user = $this->widget('Widget_User');

    $this->_token = $this->_options->secret;
    echo "<script>alert('$this->_token')</script>";
    if ($user->hasLogin()) {
    	$this->_token .= '&' . $user->authCode . '&' . $user->uid;
    }
}
```

​	然后打开你的博客，刷新一下，会弹出一个窗口，文本内容就是token1。

​	**最后不要忘记删掉刚刚我们添加的那条语句**

* ip：数据库ip
* user：数据库用户名
* password：数据库密码
* database：数据库库名
* localDir：本地缓存目录，下载的文章和文章中的图片都会放在这里

配置完成后要开启mysql远程连接服务，具体参考我之前写的一篇笔记：[mysql外网连接](http://iyzyi.com/index.php/archives/82/)

然后就可以使用啦。

### 编译打包

如果需要重新编译并打包成exe的话，可以参考以下内容

环境win10 x86（虚拟机）， python 3.7

`pip install PyQt5==5.11.3`

`pip install PyQt5-tools==5.9.2.1.3`

`pip install PyQt5-sip==4.19.19`

`pip install pyinstaller`

然后在cmd(或PowerShell)中进入根目录，运行

`pyinstaller -i typecho.ico -F -w main.py`

成功后可再dist文件夹内看到exe文件 