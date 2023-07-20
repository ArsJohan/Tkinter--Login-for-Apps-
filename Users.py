class User:
    num_users = 0
    def __init__(self, name, password):
        self.name = name
        self.password = password
        self.Attempts = 3 
        self.is_logged_in = False
        User.num_users +=1
        
    def connect(self, password=None, name = None):
        if password == None:
            my_pass = input('Enter your password: ')
        else: 
            my_pass = password
    
        if my_pass == self.password:
            self.is_logged_in = True
            return True
        else:
            self.Attempts -=1
            if self.Attempts > 0:
                return 'Sorry, wrong password' + "\n" +f'You have {self.Attempts} more attempts'
            else:
                return 'Your account is now locked'
                
    def disconnect(self):
        if self.is_logged_in:
            self.is_logged_in = False
            print(self.name, 'is now logged out')
        else:
            print('You are not logged in')
        
        
    def __str__(self):
        if self.is_logged_in:
            status = 'online'
        else:
            status = 'offline'
        return f'Name: {self.name}, Password: {self.password}. Status: {status}'
    

