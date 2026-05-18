# class car:
#     def move(self):
#         print("Car is moving")

# d1 = car()
# d1.move()


# class mobile:
#     def show(self):
#         print("This is a Mobile")

# d1 = mobile()
# d1.show()

# class calculator:
#     def add(self,x,y):
#         print("Sum of the numers:",x+y)

# d1 = calculator()
# d1.add(3,2)

# class fan:
#     def on(self):
#         print("The fan is on")

# d1 = fan()
# d1.on()


# class tv:
#     def watch(self):
#         print("I am Watching TV")

# d1 = tv()
# d1.watch()


# class book:
#     def read(self):
#         print("I am Reading")

# d1 = book()
# d1.read()

# class person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

# p1 = person("unnikuttan", 19)
# print(p1.name)
# print(p1.age)


class person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print("Hello , my name is " + self.name)

p1 = person("Unnikuttan kir")
p1.greet()
      