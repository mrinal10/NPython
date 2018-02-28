'''
Created on 28-Feb-2018

@author: mailm
'''

class StringReverse:
    stringValue=""


    def __init__(self, stringVal):
        self.stringValue = stringVal
    
    def reverseString(self):
        stringV = ""
        for i in self.stringValue:
            stringV = i + stringV
        return stringV

newStringObj = StringReverse("lanirM")
  
reversedString = newStringObj.reverseString();
print(reversedString)
