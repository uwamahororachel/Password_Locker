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
