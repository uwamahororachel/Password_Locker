import unittest # Importing the unittest module

from credentials import Credentials
import pyperclip
    
class TestCredentials(unittest.TestCase):

    '''
    Test class that defines test cases for the contact class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''
    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_credentials = Credentials("tttttTTTTDWEW12","Uwamahoro@ws","eaeaeeatgg","TTTFGGEHJGHSRTMN")
 # create contact object

