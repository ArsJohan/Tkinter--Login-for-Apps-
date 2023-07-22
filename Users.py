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
    

