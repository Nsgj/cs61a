##无需监控的学习
餐厅趋向出现在聚类中，在这一节，我们将猜想一个方法去聚集那些相互靠近的餐厅。

**K平均值算法**是一个发现聚类中心的方法。它是一个无需监管的学习方法，因为算法不告诉什么聚类是正确的，它只单独从数据来推断。

K平均算法通过匹配输入的聚类，来发现几何的的中心。为了达成这点，K平均算法开始随机选择k的几何中心，然后重复执行下面两步：

1. 靠近同一个几何中心的所有餐厅包含在一个聚类中，聚集所有餐厅到聚类中。
2. 计算每个新的聚类获得一个新的几何中心（平均位置）

这个图显示了工作原理[http://tech.nitoyon.com/en/blog/2013/11/07/k-means/](http://tech.nitoyon.com/en/blog/2013/11/07/k-means/)

##术语

当你完成下面的问题，你将会遇到下面的术语，当你遇到不懂得问题，可以重回这里查阅

+ 地址：横纵坐标
+ 几何中心：一个聚类的中心
+ 餐厅：定义在abstractions.py中餐厅的抽象
+ 聚类：餐厅的列表
+ 用户：定义在abstractions.py中的用户抽象
+ 评论：定义在abstractions.py中的评论抽象
+ 特性函数：获得餐厅返回一个数字的单参函数，比如排名的平均值和或者价格。

##问题3（1pt）

实现find_closest，它获得一个位置和一列几何中心（一些位置）。它返回最靠近这个位置的，几何中心的元素。

你需要用到distance函数（utils.py），来测量位置间的距离。这个函数计算两个位置的直线距离。

如果两个几何中心同样的靠近，返回最先出现在几何中心队列的那个。

提示：使用min函数

##问题4（2pt）

实现group_by_centroid函数，它获得一系列餐厅和一系列几何中心点，返回一个聚类列表。每个结果聚类是一个餐厅的列表，这些餐厅都最靠近一个特定的几何中心。返回的聚类列表顺序不重要。

如果一个餐厅同等的靠近两个几何中心，返回第一个。

提示：使用group_by_first函数来聚集同一个键所有的值。

##问题5（2pt)

实现find_centroid函数，它找到一个聚合类的几何中心，根据餐厅的位置。经纬度通过餐厅位置的平均数计算。

提示：使用mean函数（utils.py)来计算平均数。

##问题6（1pt）

完成k平均算法，在while语句的每个迭代中。

1. 聚合restaurants到聚合类中，每个聚合类包含靠近同一个几何中心的所有餐厅（用group_by_centroid)
2. 将几何中心绑定到新的所有的聚合类的几何中心列表（用find_centroid)

##干预学习

这一部分，你将会预测用户对餐厅的排名。你将会实现一个干预学习算法，从已知的正确排名归纳。通过分析用户过去的排名，我们可以预测用户可能给一个新的餐厅的排名。当你完成这一部分，你的图形将包含所有的餐厅，而不是已经被评价的餐厅。

为了预测排名，你将会实现**简单的最小平方线性回归**，一个广泛的统计学方法，一些近似的关系，在输入特性（如价格）然后输出一排排名的值。这个算法获得一系列输入输出对，然后计算斜率和截距，来最小化线和输出的平均方差。

##问题7（3pt）

实现find_predictor函数，获得一个user，一列餐厅，和一个feature function 调用feature_fn。find_predictor 返回两个值：一个predictor函数和一个r_squared 值。

用最小平方线性回归来计算predictor和r_squared。这个方法，如下所述，计算a和b对于predictor 线 y = a + bx 的系数。r_squared值测量这个线段对原始数据描述的准确度。

一个通过算平方的和来计算这些值的方法，S_xx,S_yy,S_xy:

##问题8（2pt）

实现best_predictor函数，它获得user，一列restaurants，一列featuer_fns。它用每个feature函数去计算一个预测函数。然后返回预测中有最高r_squared值的。所有预测因子通过餐厅的排名的子集学习。

提示：max函数可以像min的key参数一样

##问题9（2pt）
实现rate_all函数，它获得user和一列restaurant。返回一个dictionary，它的键是每个餐厅的名字。它的价值被排名。

如果一个餐厅已经被用户排名了，rate_all将会用最佳的预测来赋值所有的餐厅。最佳的预测通过用feature_fns列来选出来

提示：你可能发现user_rating函数很有用（在abstractions.py）

##预测你自己的打分

一旦你完成了，你可以用你的项目去预测你自己的打分，这里展示：

1. 在users文件夹，你将会看到一对.dat文件。复制其中的一个，然后重命名为新的yourname.dat
2. 在新的文件中，你会看到下面的：
 
	make_user(
         'john DoeNero'
         [
             make_review('Jasmine Thai',4.0),
             ...
         ]

替换第二行你的名字

3. 替换已经存在的评价

。。。。