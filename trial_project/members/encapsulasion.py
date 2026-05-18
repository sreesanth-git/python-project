class person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    def get_age(self):
        return self.__age

p1 = person("Emil", 25)
print(p1.name)
# print(p1.__age) this will raise an error because __age is private
print(p1.get_age())
