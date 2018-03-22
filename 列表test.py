---
title: CentOS6.9桌面系统安装VMware tools实例
date: 2018-03-21 
---

今天的笔记全是一些看书做的练习，看起来会比较乱，各位看官海涵！

第一部分：
1.小编的几个朋友好久不见，小编主动给他们发送了一条问候语
```bash
$ name = ["wangtianlai","wangxiaomeng","wangyao"]
```

为每个朋友送上祝福
```bash
$ print("how are you" + "," + name[0] + "!" )
$ print("how are you" + "," + name[1] + "!" )
$ print("how are you" + "," + name[2] + "!" )
```

2.小编做饭手艺不错，要请三个朋友来吃晚饭
```bash
$ Guests = ["liuyifei","fanbingbing","zhangbiyi"]
```
3.把三个朋友的名字打印到纸上，省得忘记了
```bash
$ Guests_one = Guests[0]
$ Guests_two = Guests[1]
$ Guests_three = Guests[2]
````
4.然后给小编有基友发送邀请信息
```bash
$ print('诚意邀请',Guests_one + "," + Guests_two + "," + Guests_three,'来参加周五晚上的宴会')
```
5.突然小编接到电话，有一个基友晚上女朋友要来，需要在家收拾床铺，不能前来了
```bash
$ print(Guests_three,"在家伺候女朋友，不能来参加晚会了！")
```
6.少一个基友不行呀，再重新邀请一位日本的朋友，中文名字叫龙泽
```bash
$ Guests[2] = "longze"
```
7.重新把名字打印，向每位朋友发出邀请
```bash
$ Guests_one = Guests[0]
$ Guests_two = Guests[1]
$ Guests_three = Guests[2]
$ print('诚意邀请',Guests_one + "," + Guests_two + "," + Guests_three,'来参加周五晚上的宴会')
```
8.小编突然发现一张大桌子，可能坐下更多的人，所以小编决定再多邀请几个来吃饭
先在名单开头加一个好友
```bash
$ Guests.insert(0,"wangludan")
```
9.在名单的中间加一个好友
```bash
$ Guests.insert(2,"景德")
$ print(Guests)
```
10.把一个新朋友添加到名单结尾
```bash
$ Guests.append("神仙姐姐")
```
11.重新打印名单
```bash
$ print(Guests)
```
12.突然发现菜不够了，只能宴请两位朋友
```bash
$ print("对不起！我只能邀请两位朋友来参加宴会了!")
```
13.删除名单名字，每删除一次，向朋友说明情况
```bash
$ Guests.pop()
$ Guests_pop = Guests.pop()
$ print("不好意思",Guests_pop,"今天晚上不邀请你来参加晚宴了!")
$ Guests.pop()
$ Guests.pop()
```
14.再看看还有谁能来吃饭
```bash
$ print(Guests)
$ Guests_new_one = Guests[0]
$ Guests_new_two = Guests[1]
```
15.向剩下的两位朋友发送消息依然可以在邀请之列
```bash
$ print(Guests_new_one,Guests_new_two,"很高兴能继续邀请两位来参加宴会!")
```
16.大家吃完所了，都走了，名单成空的了
```bash
$ del Guests[0]
$ del Guests[0]
$ print(Guests)
```

第二部分：
1.朋友开了一个蛋糕店，有很多甜点
```bash
$ pisa = ["芝士","奶油","蛋糕","披萨",'面包','饼干']
```
2.我想吃店里的前三样甜点
```bash
$ print('前三个元素',pisa[0:3])
```
3.小姐姐想吃中间的三样甜点
```bash
$ print('中间三个元素',pisa[2:5])
```
4.老板娘想吃最的的三样甜点
```bash
$ print('后三个元素',pisa[-3:])
```
5.小编开了一个跟朋友一模一样的甜点店
```bash
$ friend_food = pisa[:]
```
6.小编自已创造的新产品
```bash
$ pisa.append("花生")
```
7.朋友也有祖传秘方，生产出一种受欢迎的产品
```bash
$ friend_food.append("大豆")
```
8.小编给顾客介绍所有的产品
```bash
$ print('here is my food list')
$ for f in pisa:
$ 	print(f)
$ print(pisa)
```
9.朋友也是极力推荐自己的产品
```bash
$ print('my friend food list')
$ for x in friend_food:
$	 print(x)
$ print(friend_food)
```
10.小编喜欢店里的每一样甜点
```bash
$ for pi in pisa:
$	 print("I like", pi)
$ print("I rellay like",pisa)
```
11.小编原来还是一个喜欢动物的爱心人士
```bash
$ animal = ['cat','dog','pig']
$ for x in animal:
$	 print(x ,'is good!')
$ print('I like animal!')
```
12.循环打印1-10的平方，并创建列表
```bash
$ squares = []
$ for squeare in range(1,11):
$	 value = squeare**2
$	 squares.append(value)
$ print(squares)
```

第三部分：

1.创建一个列表，循环打印1到10的数字
```bash
$ for x in range(1,21):
$	print(x)
```
2.把1-100的整数创建列表，并求最大，最小值，和所有数据之和
```bash
$ number = list(range(1,101))
$ print(number)
$ print(max(number))
$ print(min(number))
$ print(sum(number))
```

2.创建一个列表，包含1到20的奇数，并循环打印出来
方法一：
```bash
$ for y  in range(1,20):
$	if y%2 ==1:
$		print(y)
```
方法二：
```bash
$ number = list(range(1,20,2))
$ for x in number:
$	print(x)
$ print(number)
```

3.创建一个列表，包含3到30之间能被3整除的数字，然后循环打印出来 
```bash
$ num = list(range(3,30,3))
$ for n in num:
$	print(n)
$print(num)
```
4.创建一个列表，包含1到10整数的立方，并打印出来
方法一：
```bash
$ number = list((i**3 for i in range(1,11)))
$ for x in number:
$	print(x)
$print(number)
```
方法二:(解析表达式)
```bash
$ jiexi = [w**3 for w in range(1,11)]
$ print(jiexi)
```

5.创建一个元组,并打印元组元素
```bash
$ print('here is old foods')
$ foods = ('大虾','烤肉','鸡肝','哈利','海红')
$ for food in foods:
$	print(food)
```
6.修改其中的一个元素，系统报错.f元组元素不可修改
```bash
$ foods[0] = '河虾'
```
7.重新定义元组
```bash
$ print('here is new foods')
$ new_foods = ('虾皮','烤肉','鱿鱼','哈利','海红')
$ for x in new_foods:
$	print(x)
```
8.比较两个字符串是否相等
```bash
$ a = 'alex'
$ b = "alox"
print(a != b )
```
9.使用lower()进行比较
```bash
$ a = 'alEX'
$ b = "alx"
print(a.lower() == b)
```
第四部分：
1.判断外星人颜色-001
```bash
$ alien_color = "green"
$ if alien_color == 'green':
$	print('恭喜你，获得五个金点值!')
```
2.判断外星人颜色-002
```bash
$ alien_color = "red"
$ if alien_color == 'green':
$	print('恭喜你，获得五个金点值!')
```	
3.判断外星人颜色-003
```bash
$ alien_color = 'green'
$ if alien_color == 'green':
$	print("获得10个点")
$ else:
$	print('你没有射击外星人')
```
4.判断外星人颜色-004
```bash
$ alien_color = 'yellow'
$ if alien_color == 'green':
$	print("获得10个点")
$else:
$	print('你没有射击外星人')
```

5.判断外星人-005
```bash
alien_color = 'red'
if alien_color == 'green':
	print('你获得5个金点')
elif alien_color == 'yellow':
	print('你获得10个金点')
else:
	print('你获得15个金点')
```

6.判断人的一生阶段
```bash
age = 89
if age < 2:
	prin('you are baby!')
elif age >=2 and age <4:
	print('你正在蹒跚学步')
elif age >=4 and age <13:
	print('你是一个儿童')
elif age >=13 and age < 20:
	print('you are young!')
elif age >=20 and age <	65:
	print('你是成年人!')
else:
	print('你是老年人')
```

7.小姐姐喜欢吃的水果
```bash
favorite_fruits = ['apple','banane','orange'] 
if 'apple' in favorite_fruits:
	print('I like apple')
if 'banane' in favorite_fruits:
	print('i like banane')
if 'orange' in favorite_fruits:
	print('i like orange')
if 'taozi' in favorite_fruits:
	print('i like taozi')
if 'lizi' not in favorite_fruits:
	print('我不喜欢吃lii')
```


8.客人点菜系统
```bash
shoping = ['土豆丝','黄瓜','西红柿']
for shop in shoping:
	if shop == '土豆丝':
		print('sorry,tuousi is empty!')
	else:
		print("adding" + shop + '.')
print("finish the shoping ")
```


9.创建用户列表
```bash
user_list = ['join','jack','mike','admin','lily']
user_list = []
if user_list == []:
	print('we need some users!')
for user in user_list:
	if user == 'admin':
		print('you are admin user ,you can do anything!')

	else:
		print('welcome login!')
user_list.clear()
print(user_list)
```


10.判断注册用户是否有效
```bash
current_users = ['lucy','lily','black','mike','jack'] 
new_users = ['lucy','liuyifei','black','tangyan','jack'] 

for user in new_users:
	if user.lower() in current_users:
		print('username is userd!')
	else:
		print('username is not userd！')

print('login is finished!')
```

11.打印序数
```bash
number_list = [1,2,3,4,5,6,7,8,9]
for y in number_list:
	if y == 1:
		print(str(y)+ 'st')
	elif y == 2:
		print(str(y)+'nd')
	elif y ==3:
		print(str(y) + 'rd')
	else:
		print(str(y)+'th')
```
今天的笔记全部都在这了，算一算写了不少代码呀，哈哈。光整理就一个多小时，给自己加油，继续努力！
累了一天了，是时候让小姐姐出厂了，给小编按摩一下......
!['肚皮'](/images/肚皮.jpg)
