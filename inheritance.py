class User:

    def login(self):
        print('Login')

    def register(self):
        print('Register')

class Student(User):

    def enroll(self):
        print('Enrol')

    def review(self):
        print('Review')

stu1 = Student()

stu1.enroll()
stu1.review()
stu1.login()
stu1.register()

u1 = User()
u1.enroll()
u1.review()
u1.login()
u1.register()



