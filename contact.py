import os
  # on windows


class Contact:
     def __init__(self, *args):

          name = 'Kofi'
          phone = '1234'
          email = 'kofi@mw.com'
          website = 'kofi.com'
          notes = 'None'

class ContactManager:

     def create_contact():

               contact = Contact()
               contact.name =  str(input('Enter your name \n'))
               contact.phone = str((input('Enter your phone \n')))
               # contact.email = str(input('Enter your email \n'))
               # contact.website = str(input('Enter your website \n'))
               # contact.notes = str(input('Enter your notes \n'))
               phonebook.append(contact)
               contact.all = (contact.name,contact.phone)
               # ,contact.email,contact.website,contact.notes


     def all_contacts():
          for item in phonebook:
               print(item.all)

     def search_contact():
          SearchTerm = input('Who are you searching for? \n')
          
          for index,item in enumerate(phonebook):
               if SearchTerm == item.name:
                    print(item.all)
                    return
               else:
                    print("Name doesn't exit")
                    return

     def delete_contact():
          SearchTerm = input('Type Contact to Delete \n')

          for index,item in enumerate(phonebook):
               if SearchTerm == item.name:
                    phonebook.pop(index)
                    return

               else:
                    print("Name doesn't exit")
                    return
 
def menu():
     print ("Do you want to \n")
     print ("1. Add new Contact \n")
     print ("2. Search Contact \n")
     print ("3. Delete Contact \n")
     print ("4. Quit \n")
     return input("Type corresponding digit and press Enter \n")


phonebook = []

choice = menu()

while choice != "4":
     if choice ==  "1":
          ContactManager.create_contact()
     return
     
     elif choice ==  "2":
          ContactManager.search_contact()
     return

     elif choice ==  "3":
          ContactManager.delete_contact()
     return
     
     elif choice ==  "4":
          pass

     else:
          os.system('clear')
          choice = menu()     