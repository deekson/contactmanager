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
               contact.phone = int((input('Enter your phone \n')))
               # contact.email = str(input('Enter your email \n'))
               # contact.website = str(input('Enter your website \n'))
               # contact.notes = str(input('Enter your notes \n'))
               phonebook.append(contact)

     def search_contact():
          SearchTerm = input('Who are you searching for? \n')

          for item in phonebook:
               if SearchTerm == item.name:
                    print('Item was found')
                    pass
               
               else:
                    print ('Item was not found')


     def all_contacts():
          for item in phonebook:
               print(item)

phonebook = []

# ContactManager.create_contact()
# ContactManager.search_contact()
ContactManager.all_contacts()

