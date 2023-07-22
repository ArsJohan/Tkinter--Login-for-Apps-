#This class will be used to create a user object.
#If you have a other class of user or created a DATABASE class, you can delete this class.

class User:
    num_users = 0
    def __init__(self, name, password):
        self.name = name
        self.password = password 
        self.is_logged_in = False
        User.num_users +=1
        
    def connect(self,password):
        my_pass = password
        if my_pass == self.password:
            self.is_logged_in = True
            return True
        else:  
            return False
                
    def disconnect(self):
        if self.is_logged_in:
            self.is_logged_in = False
            return self.name +' is now logged out'
        else:
            return 'You are not logged in'
        
        
    def __str__(self):
        if self.is_logged_in:
            status = 'online'
        else:
            status = 'offline'
        return f'Name: {self.name}, Password: {self.password}. Status: {status}'
    

