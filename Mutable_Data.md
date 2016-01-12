###2.4.9 传输约束
可变数据允许我们模拟改变中的系统。同时也让我们可以构建新一种抽象。
在这个拓展例子中，我们结合nonlocal 赋值，lists，dict 来构建一个**基于约束的系统**，它支持计算多种指令。用约束条件来表达程序是一种**声明式编程**。编程者声明一个要被解决的问题，抽离出了解决这个问题的具体细节。

计算机程序通常被组织成单向的计算。它执行提前指定的操作参数，来产生需要的输出。也就是说，我们根据数量之间的关系建立模型系统。举个例子，我们之前考虑的气体法则，它关系到压力(p)、体积(v)、质量(n)、温度(t)，理想的气体通过Boltzmann 法则(k)：
> p * v = n * k * t

这个等式不是单向的。给出任意四个量，我们可以计算出第五个。但是，将这个等式翻译成传统的计算语言，将会迫使我们从4个量中选出一个，然后根据其他的量来计算出它。因此，一个计算压力的函数不能被用来计算温度，即使所有的量的计算出现在一个公式中。

在这一节，我们勾勒出一个通用的线性设计模型。我们定义一个基本的约束条件来保持量之间的关系，如adder(a,b,c)约束一个强制数学关系a + b = c。

我们也定义一种结合方式，使基本的约束条件可以结合起来表达复杂的关系。在这里，我们的程序类是于一个编程语言。我们构造一个将约束条件通过connectors连接的网状结构，用它来结合约束条件。连接器是一个拥有数值并且参与多个约束条件中。

举个例子，我们知道Fahrenheit和Celsius温度的关系：
> 9 * c = 5 * (f - 32)

这个公式在c和f之间有着复杂的约束。每一个约束可以被认为是一个网状结构(通过基本的约束adder,multiplier,constant组成的)

![](http://i.imgur.com/R6eYoau.png)

在这个图中，我们看到左边的乘法盒子有三个端口，标记为a,b,c。这个乘法器连接网状结构的其他部分如下：a端口连接一个celsius的连接器(它将会持有摄氏度)。b端口连接一个w连接器(它也连接一个持有9的常数盒子)。c端口是通过乘法盒子约束中a和b产生的，它连接到另一个乘法盒子的c端口，另一个盒子的b端口连接一个持有5的常量盒子，它的a连接到和的约束条件盒子的一个端口。

用这种网状结构的好处有：当一个连接器获得一个值(通过用户或者另一个它连接的约束盒子)，它通过传送值唤醒了它所连接的约束(除了那个唤醒它的约束)。每个被唤醒的约束盒子去检测它的连接器们，看他们是否有足够的信息去决定一个连接器的值。如果可以，这个盒子设置那个连接器，这个连接器接着唤醒所有它所连接的约束，等等。举个例子，在华氏度和摄氏度的转换中，w,x和y是立即被设置成常数盒子9，5，32。连接器唤醒了乘法和加法，他们决定这儿没有足够的信息进行下去。如果有人设置celsius连接器一个值(25)，最左边的乘法器将被唤醒，然后它设置u为25 * 9 = 225。然后 u 唤醒第二个乘法器，它设置v为45，v唤醒加法器，它设置fahrenheit连接器为77。

**使用约束系统**。使用约束系统计算上面的温度转换，我们第一步通过connector的构造函数创建两个命名的连接器，celsius和fahrenheit。

	>>>celsius = connector('Celsius')
	>>>fahrenheit = connector('Fahrenheit')

然后，我们连接这些连接器到一个网状结构中。converter函数聚集各种连接器和约束条件。

	>>>def converter(c,f):
	       """Connect c to f with constraints to convert from Celsius to Fahrenheit"""
	       u,v,w,x,y = [connector() for _ in range(5)]
           multiplier(c,w,u)
           multiplier(v,x,u)
           adder(v,y,f)
           constant(w,9)
           constant(x,5)
           constant(y,32)
    >>>converter(celsius,fahrenheit)

我们将用一个信息传送系统来确定约束器和连接器。约束器是一个不持有他们自己状态的字典。它对信息的回馈不是一个纯函数，因为将会改变它约束的连接器。

连接器持有当前值的并且回应信息操作值。约束器不会直接改变连接器的值，它将会传信息来改变值，并且让连接器通知其他约束器回应改变。在这里，一个连接器表现为一个数字，但是也可以抽象这种行为。

我们可以给连接器发出一个信息是设置它的值。这里，我们('user')设置celsius为5

	>>> celsius['set_val']('user',25)
	Celsius = 25
    Fahrenheit = 77.0

不只有celsius的值变成了25，它的值传到了整个网状结构，所以，fahrenheit的值也改变了。这个改变被打印出来了，因为我们在构造他们的时候取了名字。

现在我们可以尝试设置fahrenheit为一个新的值212。

	>>>fahrenheit['set_val']('user',212)
	Contradiction detected:77.0 vs 212

连接器报错了:它的值是77，有人想设置为212，如果我们真的想重用网状结构，我们可以告诉celsius忘了它的旧值:

    >>>celsius['forget']('user')
    Celsius is forgotten
    Fahrenheit is forgotten

连接器celsius找到最开始设置这个值的user，现在取消那个值，所以celsius同意丢掉它的值，同时通知网状结构的其他部分。这个信息最后传到fahrenheit。fahrenheit没有理由继续持有77，因此它也丢弃了它的值。

现在fahrenheit没有值，我们可以自由的设置它为212:

    >>>fahrenheit['set_val']('user',212)
    Fahrenheit = 212
    Celsius = 100.0

这个新的值传遍了网状结构，使celsius有了100这个值。我们用非常相像的网状结构来通过fahrenheit结算celsius和通过celsius来计算
fahrenheit。这个非直接的计算是基于约束系统的指导特性。

**实现约束系统**。我们看到，连接器是映射信号名到函数和数据值。我们会实现反馈这些信息的一个连接器：

+ connector['set_val'](source,value\) 这个指令是source是一个请求设置它的当前值为value
+ connector['has_val'](\)返回是否连接器有一个值
+ connector['val']是连接器当前的值
+ connector['forget'](source\)通知连接器source请求丢弃它的值
+ connector['connect'](source\)通知连接器加入新的约束器source

约束器也是字典，它接受从连接器来的信息:

+ constraint['new_val'](\)指示连接到这个约束器的连接器有新的值。
+ constraint['forget'](\)指示连接到这个约束器的连接器丢弃它的值。

当约束器得到这些信息，他们传送信息到其他的连接器。

adder函数通过三个连接器构造一个加法约束器，这里前两个相加形成第三个：a + b = c。为了支持多方向的约束传送，adder也必须指定c - a = b和 c - b = a

	>>>from operator import add,sub
	>>>def adder(a,b,c):
	       """The constraint that a + b = c"""
           return make_ternary_constraint(a,b,c,add,sub,sub)

我们会实现一个通用的三元约束，它使用三个连接器和三个函数，创建一个约束器接收new_val 和forget信息。信息的回复是一个放在字典中被称为constraint的本地函数。

    >>>def make_ternary_constraint(a,b,c,ab,ca,cb):
           """The constraint that ab(a,b)=c and ca(c,a)=b and cb(c,b)=a."""
           def new_value():
               av,bv,cv = [connector['has_val']() for connector in (a,b,c)]
               if av and bv:
                   c['set_val'](constraint,ab(a['val'],b['val']))
               elif av and cv:
                   b['set_val'](constraint,ca(c['val'],a['val']))
               elif bv and cv:
                   a['set_val'](constraint,cb(c['val'],b['val']))
           def forget_value():
               for connector in (a,b,c):
                   connector['foget'](constraint)
           constraint = {'new_val':new_value,'forget':forget_value}
           for connector in (a,b,c):
               connector['connect'](constraint)
           return constraint

constraint是一个调度字典，也是约束对象本身。它回应两个接收的信息，但它也传作为source的参数到它的连接器中。

约束器的本地函数new_value不论何时，当连接器有了值，都会被调用。这个函数首先检查是否a,b有值，如果有，则告诉c设置它的值来返回函数ab的值。约束器传它自己作为source参数到连接器(它是adder对象)。如果a和b没有同时有值,约束器检查a,c,等等。

如果一个约束器被告知，它的一个连接器需要丢弃值，它请求它所有的连接器丢弃值。

乘法约束器很像加法约束器。

	>>>from operator import mul,truediv
	>>>def multiplier(a,b,c):
	       """The constraint that a * b = c """
           return make_ternary_constraint(a,b,c,mul,truediv,truediv)

