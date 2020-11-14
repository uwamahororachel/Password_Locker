#!/usr/bin/env python3.6
from credentials import Credentials
from user import User
import string
import random
# ...................................credentials...................................
def create_credentials(pfacebook,pcanvas,ptwitter,pemail):
    '''
    Function to create a new contact
    '''
    new_credentials = Credentials(pfacebook,pcanvas,ptwitter,pemail)
    return new_credentials

def save_credentials(credentials):
    '''
    Function to save credentials
    '''
    credentials.save_credentials()
def display_credentials():
    '''
    Function that returns all the saved credentials
    '''
    return Credentials.display_credentials()
def del_credentials(credentials):
    '''
    Function to delete a credentials
    '''
    credentials.delete_credentials()

def check_existing_credentials(name):
    '''
    Function that check if an account exists with that name and return a Boolean
    '''
    return Credentials.credentials_exist(name)  
def find_credentials(name):
   '''
   Function that finds a credential by username and returns the user credential
   '''
   return Credentials.find_by_name(name)

def pw_gen(size = 8, chars=string.ascii_letters + string.digits + string.punctuation):
	return ''.join(random.choice(chars) for _ in range(size))

# print(pw_gen(int(input('How many characters in your password?'))))


#     ........................................................USER..............................
def create_user(user_name,password):
    '''
    Function to create a new account
    '''
    new_user = User(user_name,password)
    return new_user

def save_user(user):
    '''
    Function to save user
    '''
    user.save_user()    

def del_user(user):
    '''
    Function to delete a account
    '''
    user.delete_user()    


def find_user(name):
    '''
    Function that finds a account by nane and returns the account
    '''
    return User.find_by_name(name)    

def check_existing_user(name):
    '''
    Function that check if an account exists with that name and return a Boolean
    '''
    return User.user_exist(name)    

def display_user():
    '''
    Function that returns all the saved accounts
    '''
    return User.display_user()  
def main():

    print(" Welcome to PassWord Locker App. What is your name?")
    user_name = input()
#     print(f"Hello {user_name}, create  your account.")
    print('\n')
    while True:
        print(f" WELCOME {user_name} PLEASE SELECT ACCORDING TO WHAT YOU WANT TO DO :\n S -> To create your account.\n D -> Display your account.\n L ->For you to log in.\n ex ->To exit password locker. ")
        print("*"*50)
        short_code = input().lower()
        if short_code == 's':
            print("CREATE PASSWORD LOCKER ")
            print("*"*50)
            user_name= input('USERNAME:')
            print ('\n')
            password = input('PASSWORD:')
            print ('\n')
           
            save_user(create_user(user_name,password)) 
            print ('\n')
            print(f"THE ACCOUNT HAS BEEN CREATED WITH USERNAME {user_name} AND PASSWORD {password}.")
            print ('\n')
            
        elif short_code == 'd':
             if display_user():
                 print("HERE IS YOUR USERNAME AND PASSWORD")
                 print("*"*50)
                 print('\n')
                 for user in display_user():
                     print(f"PASSWORD:{user.password}  USERNAME: {user.user_name} ")
                     print('\n')
             else:
                 print('\n')
                 print("PLEASE CREATE ACOUNT FIRST")
                 print('\n')
        elif short_code == "ex":
                            print("Bye .......")
                            break
        elif short_code == 'l':
            print(f"PLEASE {user_name} ENTER YOUR PASSWORD TO LOG IN.")
            print ('\n')
            search_user = input()
            if check_existing_user(search_user):
                search= find_user(search_user)
                print("\033[1;32;1m   \n")
                print(f"You are now logged in to your {user_name} account")
                print("\033[1;37;1m   \n")
            else:
                print('Wrong password')    
                break

            while True:
                    print("FOLLOW THIS SHORTCODE ACCORDING TO WHAT YOU WANT TO DO : \n cc - create credentials,\n dc - display credentials, \n fc -delete credentials,\n ft -generate password new acount,\n f- find  \n ex -exit Password Locker ")

                    short_code = input().lower()
        
                    if short_code == 'cc':
                            print("PLEASE ENTER THE PASSWORD YOU WANT TO SAVE ACORDING TO YOUR ACCOUNT")
                            print("-"*10)

                            print ("PASSWORD FOR FACEBOOK :")
                            pfacebook = input()
                            print("\n")

                            print("PASSWORD FOR CANVAS :")
                            pcanvas= input()
                            print("\n")

                            print("PASSWORD FOR TWITTER :")
                            ptwitter= input()
                            print("\n")

                            print("PASSWORD FOR YOUR EMAIL :")
                            email = input()
                            print("\n")


                            save_credentials(create_credentials(pfacebook,pcanvas,  ptwitter,email)) 
                            print ('\n')
                            print(f"FACEBOOK PASSWORD  {  pfacebook} ")
                            print ('\n')
                            print(f"CANVAS PASSWORD { pcanvas} ")
                            print ('\n')
                            print(f"TWITTER PASSWORD {  ptwitter}" )
                            print ('\n')
                            print(f"EMAIL PASSWORD {  email}")
                            print ('\n')

                    elif short_code == 'dc':

                            if display_credentials():
                                    print("HERE IS THE LIST OF YOUR  CREDENTIALS")
                                    print('\n')

                                    for  credentials in display_credentials():
                                            print(f" TWITTER:{credentials.twitter} \n FACEBOOK:{credentials.facebook} \n CANVAS:{credentials.canvas} \n EMAIL:{credentials.email}")

                                    print('\n')
                            else:
                                    print('\n')
                                    print("You dont seem to have any credentials saved yet")
                                    print('\n')
                    elif short_code == 'ft' :
                              print(pw_gen(int(input('How many characters in your password?'))))
                              print("your password has bees created")
                    elif short_code == 'fc':     
                              for  credentials in display_credentials():
                                      
                                credentials.delete_credentials()
                                print("deleted" )

                    # elif short_code == 'f':

                    #         print("Enter the number you want to search for")

                    #         search_name = input()
                    #         if check_existing_credentials(search_name):
                    #                 search_credentials = find_credentials(search_name)
                    #                 print(f"{search_credentials} {search_credentials.canvas}")
                    #                 print('-' * 20)

                    #                 print(f"facebook.......{search_credentials.facebook}")
                    #                 print(f"Email address.......{search_credentials.email}")
                    #         else:
                    #                 print("That contact does not exist")            
                    elif short_code == "ex":
                        print("Bye ....")
                        break
                        
        else:
             print("I don't get that Shortcode you have used. Please select the other one")
             print("\n")    
#     handle.close()                             
if __name__ == '__main__':

    main()
