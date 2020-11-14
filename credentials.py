import pyperclip
import string

class Credentials:
    """
    Class that generates new instances of credentials.
    """

    credentials_list = [] # Empty contact list

    def __init__(self,facebook,canvas,twitter,email):

      # docstring removed for simplicity

        self.facebook= facebook
        self.canvas = canvas
        self.twitter = twitter
        self.email= email
    @classmethod
    def display_credentials(cls):
        '''
        method that returns the contact list
        '''
        return cls.credentials_list
    contact_list = [] # Empty contact list
 # Init method up here
    def save_credentials(self):

        '''
        save_credentials method saves credentials objects into credentials_list
        '''

        Credentials.credentials_list.append(self)
      
    def delete_credentials(self):

        '''
        delete_contact method deletes a save credentials from the credentials_list
        '''

        Credentials.credentials_list.remove(self)
    @classmethod
    def find_by_name(cls,name):
        for credentials in cls.credentials_list:
            if credentials.credentials_name == name:
                return Credentials  
    
    @classmethod
    def credentials_exist(cls,name):
        '''
        Method that checks if a credentials exists from the credentials list.
        Args:
            name: Acc name to search if it exists
        Returns :
            Boolean: True or false depending if the credentials exists
        '''
        for credentials in cls.credentials_list:
            if credentials.password == name:
                    return credentials

        return False      
