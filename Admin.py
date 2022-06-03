import FoodsList

class Admin:

    list = FoodsList.FoodsList()
    
    username = 'alina'

    password = 'alina191095'

    def __init__(self):
        print(self.username,self.password)

    def login(self):
        entered_username = input("Please enter username: ")
        entered_password = input("Please enter password: ")
        
        if entered_username == self.username and entered_password == self.password:
            print(self.list.getAllItems())
        else:
            print('Please enter correct credentials')
            
        
        
admin = Admin()
admin.login()
