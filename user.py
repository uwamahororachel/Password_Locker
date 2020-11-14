import pyperclip
class User:
    """
    Class that generates new instances of users.
    """
    user_list = [] #empty account list

    def __init__(self,user_name,password):
     
        self.user_name = user_name
        self.password = password
      
    

    def save_user(self):

        '''
        save_user account 
        '''

        User.user_list.append(self)


    def delete_user(self):

        '''
        delete_account method deletes a saved account from the account_list
        '''

        User.user_list.remove(self)   

    @classmethod
    def find_by_name(cls,name):
        for user in cls.user_list:
            if user.user_name == name:
                return user   
    

    @classmethod
    def user_exist(cls,name):
        '''
        Method that checks if a account exists from the user list.
        Args:
            name: Acc name to search if it exists
        Returns :
            Boolean: True or false depending if the account exists
        '''
        for user in cls.user_list:
            if user.password == name:
                    return user

        return False
    @classmethod
    def display_user(cls):
        '''
        method that returns the account list
        '''
        return cls.user_list    

   