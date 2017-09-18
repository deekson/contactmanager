class NewContact:
          def __init__(self, name, phone, email, website, notes):

	          self.name =  name
	          self.phone = phone
	          self.email = email
	          self.website = website
	          self.notes = notes

          def create_contact(self):
               self.name =  input('Enter your name \n')
               self.phone = int((input('Enter your phone \n')))
               self.email = input('Enter your email \n')
               self.website = input('Enter your website \n')
               self.notes = input('Enter your notes \n')

          def list_contact(self):

               contacts = (self.name,self.phone,self.email,self.website,self.notes)
               print(contacts)

name = str(input('Enter name: '))
phone = int(input('Enter your phone \n'))
email = str (input('Enter your email \n'))
website = str (input('Enter your website \n'))
notes = str(input('Enter your notes \n'))


contact = NewContact(name,phone,email, website,notes)

# contact.create_contact()

contact.list_contact()