
class Student ():
    # 类变量
    name = 'dudu'
    age  = 12
    # def __init__(self, name, age):
    #      实例变量
    #     self.name = name
    #     self.age = age
    def say (self):
        print self.name
        print str(self.age)



# student = Student()
# student.say()
print(Student.name)