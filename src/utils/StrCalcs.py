'''        -------------------------
Project:     RUBot: humano o bot
           -------------------------
@author: Marcos F. Vilaboa
   Degree in CS (Universitat Oberta de Catalunya)
   -Open Data: Capture, analysis and visualisation - area
                                                    Created on 19 abr. 2018            
'''

class StrCalcs(object):

    '''
    classdocs
    '''
    def __init__(self):
        pass

    def numberOfCharsInString(self, strToParse):
        return len(strToParse)

    def digitsInString(self, strToParse):
        return sum(char.isdigit() for char in strToParse)
    
        