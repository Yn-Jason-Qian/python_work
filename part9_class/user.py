class User():
    """用户"""
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hello(self):
        print("hello, my name is " + self.name + ", " + str(self.age) + " is my age")

class Admin(User):
    """管理员"""
    def __init__(self, name, age, privileges):
        super().__init__(name, age)
        self.privileges = privileges

    def show_privileges(self):
        i = 0
        privilege_str = ""
        while i < len(self.privileges):
            if i == len(self.privileges) - 1:
                privilege_str += self.privileges[i]
            else:
                privilege_str += self.privileges[i] + ", "
            i+= 1 
        print("Admin: " + self.name + ", Privileges: " + privilege_str)

user = User("qian.yang", 28)
user.say_hello()
admin = Admin("qian.yang", 28, ["can add post", "can delete post", "can ban user"])
admin.show_privileges()
