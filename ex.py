import string
import sys

class ClassEx():
    firstName = ""
    lastName = ""
    
    def setFirstName(self, name):
        self.firstName = name 

        
    def setLastName(self, name):
        self.lastName = name
        
    def getFullName(self):
        return self.firstName + " " + self.lastName
        
    def getLastName(self):
        return self.lastName    

    def convertFirstNameToLowerCase(self):
        return string.lower(self.firstName)
    
name = ClassEx()
name.setFirstName("STAVros")
name.setLastName("Man")
myname = name.getFullName()
print myname
lastname = name.getLastName()
print lastname
lowername = name.convertFirstNameToLowerCase()
print lowername
