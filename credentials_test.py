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


    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_credentials.facebook,"tttttTTTTDWEW12")
        self.assertEqual(self.new_credentials.canvas,"Uwamahoro@ws")
        self.assertEqual(self.new_credentials.twitter,"eaeaeeatgg")
        self.assertEqual(self.new_credentials.email,"TTTFGGEHJGHSRTMN")

    def test_save_credentials(self):
        '''
        test_save_contact test case to test if the credentials object is saved into
         the contact list
        '''
        self.new_credentials.save_credentials() # saving the new contact
        self.assertEqual(len(Credentials.credentials_list),1)

    def test_delete_credentials(self):
            '''
            test_delete_contact to test if we can remove a contact from our contact list
            '''
            self.new_credentials.save_credentials()
            test_credentials = Credentials("Test","user","0712345678","test@user.com") # new contact
            test_credentials.save_credentials()

            self.new_credentials.delete_credentials()# Deleting a contact object
            self.assertEqual(len(Credentials.credentials_list),1)
    def test_find_credentials_by_name(self):
        '''
        test to check if we can find a contact by phone number and display information
        '''

        self.new_credentials.save_credentials()
        test_credentials = Credentials("tttttTTTTDWEW12","Uwamahoro@ws","eaeaeeatgg","TTTFGGEHJGHSRTMN") # new contact
        test_credentials.save_credentials()

        found_credentials = Credentials.find_by_name("facebook")

        self.assertEqual(found_credentials,test_credentials.facebook)
if __name__ ==  '__main__':
    unittest.main()