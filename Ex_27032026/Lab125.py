# Web Automation - Selenium
# Page - You are going automate

# class VWOLoginPage:
#
#     def __init__(self, email_arg, password_arg):
#         self.email = email_arg
#         self.password = password_arg
#
#     def login_confirm(self):
#         if self.email == "pramod@gmail.com" and self.password == "Pass123":
#             print("Allowed to enter")
#         else:
#             print("Not allowed")
#
#
# # This is the end of the class
#
# email = input("Enter the email \n")
# password = input("Enter the password \n")
# amit = VWOLoginPage(email, password)
# amit.login_confirm()
#
#
# email = input("Enter the email \n")
# password = input("Enter the password \n")
#
# pramod = VWOLoginPage("pramod@gmail.com", "Pass123")
# pramod.login_confirm()







class Login:
    email: None
    password: None

    def __init__(self, email, password):
        self.email = email
        self.password = password

    def check_login(self):
        if self.password == "Pass123":
            print(self.email, "Login Successful")
        else:
            print(self.email, "Login Failed")


lucky = Login("lucky@email.com", "Pass123")
lucky.check_login()

lucky1 = Login("lucky1@email.com", "Pass1234")
lucky1.check_login()

# amit = Login("amit@gmail.com", "Pass1234")
user = Login(input("Email: "), input("Password: "))
user.check_login()









