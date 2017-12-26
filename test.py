# encoding:utf-8
message = 'hello world';
print message;


# 这是一个注释
bicycles = ['1','cc','sss','d'];
print bicycles;

bicycles[1] = 'dudu'
print bicycles;

# 列表最后一项添加元素
bicycles.append(1)
print bicycles;

# 列表最后一项删除，并且返回删除的项
num =  bicycles.pop();
print bicycles;
print 'delete num ' + str(num);

# 列表中插入，第一个参数表示插入的位置，第二个是插入的东西
bicycles.insert(2,'ssss');
print bicycles;

# 随机删除
del bicycles[2];
print bicycles;

# pop(index) del 如何取舍？ 删除的东西有用，用pop(); 没有用， 用del

arr = ['a','b','c'];
for item in arr:
    print item;
print 'done'


#  range(1,5)
nums = range(1,6);
print nums;


#
square = [];
for item in range(1,11):
    square.append(item**item);

print square;
