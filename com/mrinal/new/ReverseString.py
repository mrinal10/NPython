'''
Created on 28-Feb-2018

@author: mailm
'''

class StringReverse:
    stringValue=""


    def __init__(self, stringVal):
        self.stringValue = stringVal
    
    def reverseString(self):
        str = ""
        for i in self.stringValue:
            str = i + str
        return str

newStringObj = StringReverse("lanirM")
  
reversedString = newStringObj.reverseString();
print(reversedString)
