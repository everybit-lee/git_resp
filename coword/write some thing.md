研究目标：信息技术已经成为社会发展的重要引擎。信息技术在教育领域有着深入而广泛的应用。该怎样去评估信息技术在教育领域的应用程度？信息技术在教育领域中有哪些研究路径和趋势？
材料和方法：对研究领域中知名的12个期刊在web of science核心库中被收录的8131篇文献进行关键词

The use of IT in education represents a promising tool to facilitate the communication as a whole in educational progress. Most of the studies focus on the specific impact of IT in the educational process, e.g., gamification makes the educational process more intuitive and interesting, e-learning remove communication barriers among participants, social network breaks the time barrier, etc..
Nevertheless, little research has focused on providing a comprehensive literature review, which will help researchers to better understand how this stream of research

信息技术在教育中的应用，是促进教育整体传播的一种很有前途的工具。大多数的研究集中在教育过程中，例如它的具体影响，游戏化，使教育过程更直观和有趣，学习消除沟通障碍的参与者，社会网络打破了时空的阻隔，等。

Nevertheless, little research has focused on providing a comprehensive literature review, which will help researchers to better understand how this stream of research has evolved over latest decade.
In this study, we use TF/IDF and co-occurrence analysis in order to provide useful up-to-date information to picture the state of the art about current research and evolution of the topic. Analysis on Data sets obtained from titles and abstracts extracted from 8131 articles published in 12 journals over the last decade (2007–2017) allowed identifying relevant
authors and institutions, key constructs and themes involved, and trends of knowledge development. Main findings suggest an increasing academic interest on the topic over the last 5 years and a wide variety of constructs that were clustered in four main themes that we named: (i) effectiveness, (ii) acceptance, (iii) engagement and (iv) social interactions. Future research lines are also addressed.

###[干货！详述Python NLTK下如何使用stanford NLP工具包](http://www.cnblogs.com/baiboy/p/nltk1.html) 

#20171115

###有哪些主要的共用术语？

> tfidf 这个数据是怎么来的？高频词tfidf?是直接的文本，将每个期刊的所有文本放在一起，文档名，tens-12.txt
>
> n选举1000，中的数据进行聚类



###co-word: 计算机或IT技术应用于教育领域，有哪些主要的研究主题？

> Gamification中使用词频

这里用TF/IDF+co-word确定研究主题

	n选举1000，中的数据进行聚类
	这个聚类，既代表各种主题，也代表不同期刊对不同主题的倾向
	如何评价，到底要选举多少个关键词？
	12个期刊的关键词数的平均值？或其他指标？

###在十年间，这些主题有哪些变化和发展？这些主题的文献量发生了哪些变化

year by year td/idf+coword

###各个主题有哪些主要的研究者？

简单统计+social network

###有哪些研究方法？

##【已完成】

1. 词频统计
2. TF/IDF统计
3. 词同现矩阵
4. 将作者姓名分离出来，并存放到数据库中，下一步进行统计
5. 还需要关键词/通用关键术语
6. 高频词或通用术语对应的文章数、年份统计

----

#20171116

tf/idf用于确定公共术语时，应该用术语在各自期刊的排位还是值本身？

用排位，位置信息取代了原始值，会掩盖什么吗?----但起码比较难说服别人；很难说清为何要用排位
用值，直接得到平均值，不会有太大争议

### 难题

在TF/IDF选举结果中如何构造统计量？

接下来：

1. 得到关键词统计排名；
2. 对tf/idf选举结果进行聚类，这里本身就可以得到研究方向的初步结果
3. 取得排名靠前的关键词，并在co-word矩阵中查找相关的语境
4. 关键词/术语与作者的关联统计
5. （待定）作者合著网络

####关于聚类的资料

1. [关于聚类的学习资料整理+思维导图](http://blog.csdn.net/basica/article/details/78534516)
2. [分类和聚类的区别及各自的常见算法](http://blog.csdn.net/basica/article/details/78532003) 
3. [从比较基础讲起的--->数据挖掘之聚类算法](http://blog.csdn.net/private_void/article/details/46363091)
4. 关于tf/idf发展及其使用的较全面的介绍: [TF-IDF 加权及其应用](https://www.cnblogs.com/chenny7/p/4002368.html) 以及详尽的解释 [TF-IDF及其算法](https://www.cnblogs.com/biyeymyhjob/archive/2012/07/17/2595249.html)
5. [哪种聚类算法可以不需要指定聚类的个数，而且可以生成聚类的规则？](https://www.zhihu.com/question/20977382) 其中提到[非参数贝叶斯模型](http://blog.csdn.net/workerwu/article/details/8131009)


# 20171120

1. [pandas处理矩阵数据;  ](https://www.cnblogs.com/chaosimple/p/4153083.html) [另一个资料](http://pandas.pydata.org/pandas-docs/stable/io.html#io-excel)
2. [标准化或去除均值和方差缩放](https://www.cnblogs.com/chaosimple/p/4153167.html)
3. [文献关键词共现矩阵python实现](http://blog.csdn.net/basica/article/details/78532179)

### 评估co-word和聚类技术的作用

> 参看： [关键词、共现矩阵及聚类](http://blog.sciencenet.cn/blog-82196-292267.html)

高频词co-word主要是为进一步分析做准备，即**聚类**；

> 聚类分析是一种重要的人类行为。它是指将物理或抽象对象的集合分组，使其成为由类似的对象组成的多个类的分析过程。从数据的角度讲，聚类是通过计算分类对象在各个属性上的相似程度，将对象分类到不同的类或者簇的过程，使得同一个类中的对象有很大的相似性，不同类间的对象有很大的相异性。聚类与分类的不同在于聚类所要求划分的类预先是未知的。

上面文献用SPSS做模糊层次聚类

[sklearn kmeans的详细解释](http://blog.csdn.net/qq_25040013/article/details/52574962)

**今天的（未解决的）问题：kmeans的具体实现**

-------

#20171121

1. [python中pandas和matplotlib画图](http://blog.csdn.net/luoyexuge/article/details/49069225) 

2. [[Python 数据分析包：pandas 基础](http://www.cnblogs.com/sumuncle/p/5719006.html)] **非常详尽地解释了dataframe**

3. [将pandas dataframe转为numpy的narray](https://stackoverflow.com/questions/13187778/convert-pandas-dataframe-to-numpy-array-preserving-index) 

   1. df=df.values

   2. Pandas has something built in...

      numpyMatrix = df.as_matrix()

4. [Python Numpy的数组array和矩阵matrix](http://blog.csdn.net/zhihaoma/article/details/51002742)  另一个[Python: NumPy中的多维数组ndarray](http://blog.sciencenet.cn/home.php?mod=space&uid=3031432&do=blog&id=1064033)

5.  [numpy ndarray官方指南](https://docs.scipy.org/doc/numpy/reference/arrays.ndarray.html) 

6. numpy ndarray 最大值求法

   >  a = np.arange(4).reshape((2,2))
   >  aarray([[0, 1],       [2, 3]])
   >  np.amax(a)           # Maximum of the flattened array
   >  3



# 20171122

搞清楚：

1. 先用画图方法，将现有矩阵画出来，判断是用kmeans还是其他聚类方法（kmeans适用于球状簇聚类；[kmeans聚类中的那些坑](http://blog.sciencenet.cn/blog-556556-860647.html) ,否则可以采用层次聚类）

2. sklearn的聚类算法接受的输入，是numpy类型的矩阵、narray还是pandas的dataframe? 以numpy narray为主

3. [sklearn 数据归一化/标准化/正则化](https://www.cnblogs.com/chaosimple/p/4153167.html) 

4. [python实现数据归一化](http://blog.csdn.net/lenovojxn/article/details/53768537) 

直接进行kmeans聚类？

​	1.[Python_sklearn机器学习库学习笔记（五）k-means（聚类）](http://www.cnblogs.com/wuchuanying/p/6264025.html) （金秀：里边有说明画图以及肘部法则确定K值）

2. [Kmeans文本聚类算法+PAC降维+Matplotlib显示聚类图像](http://blog.csdn.net/eastmount/article/details/50545937) (**比较综合的实验，推荐**)
3. [matplotlib pyplot快速绘图](http://hyry.dip.jp/tech/book/page/scipy/matplotlib_fast_plot.html) 
4. [pyplot-subplot](https://www.cnblogs.com/Frandy/archive/2012/09/27/python_pyplot_subplot.html)

---

###今天工作小结：

基本搞清楚了kmeans用法以及如何输出图形，代码：tryplot.py、 trypandas.py

基本确定了，使用tf/idf选举结果进行聚类，来确定研究领域，该部分代码已经基本确定，但由于选举数据尚未运行完成，所以聚类代码trypandas.py尚未开始工作。

tf/idf的结果，来自将每个期刊的数据（预处理后）当成一个类别，用sklearn计算出来的。因此，并没有做截断操作

---

#[python做科学计算教程的总目录](http://hyry.dip.jp/tech/book/page/scipy/index.html#)

# 20171123 kmeans聚类

###好嗨森，一段简单的代码，查看到数据及绘图

> import pandas as pd
> import numpy as np
> import matplotlib.pyplot as plt
> xlsx=pd.ExcelFile('F:\\03 other\\git_resp\\data\\journals\\selectdata.xlsx')
> df=pd.read_excel(xlsx,"n-20",index_col=0)
> print df
>          J1  J2  J3  J4  J5  J6  J7  J8  J9  J10  J11  J12
>     word
>     student         1   2   1   1  23   1   1   1   2    1    1    4
>     use             2   3   2   4   3   5   3   5   6    8    3    2
>     ...            ..  ..  ..  ..  ..  ..  ..  ..  ..  ...  ...  ...
>     parameter       0   0   0   0  20   0   0   0   0    0    0    0
> df.columns  #输出  Index([u'J1', u'J2', u'J3', u'J4', u'J5', u'J6', u'J7', u'J8', u'J9', u'J10', u'J11', u'J12'], dtype='object')
> df.index  输出 Index([u'student', u'use', u'study', u'learning', ..., u'parameter'], dtype='object', name=u'word')
> df.index.name # word
> nf=df.values  #输出除了colunms 和index之外的纯数字的矩阵，因此，用nf进行聚类、画图等操作
> nf.shape  # (87,12)  即87行，12列 nf.shape[0]=87
> np.amax(nf)  #49  即矩阵中最大值
> %以下画图
> plt.figure()
> plt.axis([0,nf.shape[0],0,np.amax(nf)])  # 横轴起点，终点，纵轴起点，终点
> plt.grid(True)
> plt.plot(nf,"k.") **这里k后面的点不能省**
> plt.show()
>
> ![test01](F:\03 other\git_resp\data\journals\results\test01.png)

### 开始聚类

1. ndarray的补齐。用np.zeros((行数，列数),dtype=nf.dtype)生成多维的零值矩阵；用np.hstack((左矩阵，右矩阵))来向右扩展；用np.vstack((上矩阵，下矩阵))来向下扩展，例子(原始一维矩阵p(2,)，向右扩展为(10,)再向下扩展为(10,10))：

>p=np.zeros((2,),dtype=nf.dtype)
    p
    array([0, 0], dtype=int64)  #(2,0)矩阵
> k=np.zeros((8,),dtype=nf.dtype)
> nt=np.hstack([p,k])
     nt
     array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0], dtype=int64)
> nt.shape
    (10,)
> z=np.zeros((9,10),dtype=nf.dtype)    # （9,10）矩阵
> rt=np.vstack((nt,z))
> rt.shape
    (10, 10)  #扩展得到一个10*10 的矩阵rt
2. ​ 本机内存不够，GPU服务器有问题。已经得到一部分图像，可以做出初步的判断。但还需要细致的判断。

3. 几个坑：

[matplotlib中文字体问题](https://www.cnblogs.com/taceywong/p/5468224.html)

      	Linux中可以使用命令——`fc-list :lang=zh`来查看我们系统安装的中文字体系统识别的名称
[matplotlib在Linux和Windows显示的问题](https://www.lookfor404.com/%E8%BF%90%E8%A1%8Cggplot%E5%87%BA%E7%8E%B0%E9%97%AE%E9%A2%98no-display-name-and-no-display-environment-variable/)

​	先更改matplotlib的后端模式为”Agg”。直接贴代码吧！

```
%do this before importing pylab or pyplot``
Import matplotlib``
matplotlib.use('Agg')
import matplotlib.pyplot asplt`
```
4. [mysql数据库迁移](https://www.cnblogs.com/advocate/archive/2013/11/19/3431606.html) 

---

### 今日小结：

1. tf/idf选举计算的结果已出来。可以使用两个指标来确定，用n-1000是比较理想的（9个以上期刊使用的kw比例，选举值和9个以上期刊期刊使用kw数的比例）
2. 代码和数据文件夹在 F:\03 other\git_resp\
3. 开始聚类，诸多小坑已填平。已提交gpu服务器计算；计算中....
4. mysql数据库迁移进行中....
5. mysql服务可使用，但 root密码需重新设定

---

# 20171127聚类意义的重新思考

1. 是否需要按期刊来计算TFIDF。

  ​原因：现在按期刊进行统计TF/IDF，选举后进行聚类。貌似聚类结果就是分成12类，这是巧合？

2. 重新计算TFIDF。

3. 重置MYSQL---好像还是搞不定，数据转换不过来旧的数据库

4. [mysql密码重置](https://www.cnblogs.com/forever-cjs/p/4975860.html) 其中 [MySQL5.7中password 改为authentication_string](http://blog.csdn.net/u010603691/article/details/50379282) 

   1. 没成功；
   2. [4楼服务器mysql服务器远程](https://www.cnblogs.com/fnlingnzb-learner/archive/2016/09/01/5830661.html)连接成功

5. 先考虑将1的结果，即聚类的结果输出，再做其他打算。

6. trypandas-gpu.py当前是对n-1000的前1586个数据，也就是9个及以上期刊所共同采用的术语进行聚类，其数据文件selectdata.xlsx中，
```
n-1000基本上是排序后的原始数据
n2-1000已删除重复数据
n3-1000仅保留1586个关键词，即9个以上的词
```

7. [python社交网络分析](http://computational-thinking.farbox.com/blog/2014-08-03-study-osn-using-python#toc_8) 
8. [pyquery爬虫神器]([python爬虫神器PyQuery的使用方法](https://segmentfault.com/a/1190000005182997))

# 20171129聚类结果整理+作者合著网络

1. 从kmeans聚类效果来看，全集分成7类/1586kw集合分成5类是最好的（[结果位置](F:\03 other\git_resp\data\journals\results\gpu-res\1127) 这些文件中，有n2-前缀的，是全体kw的分类结果，其他则是1586个kw的结果）

   ![两者比较](F:\03 other\git_resp\data\journals\results\gpu-res\1127\两者比较.png)

2. [Matplotlib绘制论文需要的图片](http://www.jb51.net/article/115168.htm)  这个详细：[基于matplotlib高质量矢量图输出](https://www.ibm.com/developerworks/cn/linux/l-matplotlib/) 

3. [matplotlib绘制各种图形集合](https://blog.mythsman.com/2016/01/24/1/) （填充图、散点图、三维图....）[这篇的解释更加详尽一些](http://blog.csdn.net/ikerpeng/article/details/20523679)

4. [Python matplotlib高级绘图详解](http://blog.csdn.net/matrix_laboratory/article/details/50698239) 

5. [matplotlib极坐标绘图详解](https://www.cnblogs.com/kallan/p/6738577.html)

###接下来：
1. 评估分类结果；
2. svg保存有问题（gpu上）