class password_manager:
    __old_password=[]
    def get_password(self):
        if(password_manager.__old_password):
            return password_manager.__old_password[-1]
        else:
            print("password list is empty")
    def set_password(self):
        passw=input("enter the password")
        if(passw not in password_manager.__old_password):
            password_manager.__old_password.append(passw)
            print("password updated successfully")
        else :
            print("this password has alread been used")
    def is_correct(self,passw):
        if(password_manager.__old_password):
            if(passw==password_manager.__old_password[-1]):
                return True
            else:
                return False
        else:
            print("password list is empty")
manager=password_manager()
manager.set_password()
print(manager.get_password())
print(manager.is_correct(input("enter the password to check")))

