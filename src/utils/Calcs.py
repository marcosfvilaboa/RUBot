'''        -------------------------
Project:     RUBot: humano o bot
           -------------------------
@author: Marcos F. Vilaboa
   Degree in CS (Universitat Oberta de Catalunya)
   -Open Data: Capture, analysis and visualisation - area
                                                    Created on 19 abr. 2018            
'''
from dateutil import parser

class Calcs:
    
    '''
     Getter to return the date in 'datetime' format
     @return: the string date parsed
    '''
    def parseDate(self, dt):
        return parser.parse(dt)
    '''
     substractStringDates function takes two String format parameters
     and return the 'timedelta' difference between them in seconds
     @param fstDate the first date to substract
     @param scndDate: the second date to substract 
     @return: the difference in 'timedelta' seconds
    '''  
    def substractStringDates(self, fstDate, scndDate):
        if((self.parseDate(fstDate) - self.parseDate(scndDate)).total_seconds() < 0):
            return (self.parseDate(scndDate) - self.parseDate(fstDate)).total_seconds()
        return (self.parseDate(fstDate) - self.parseDate(scndDate)).total_seconds()
    
    def isFirstNewer(self, fstDate, scndDate):
        if ((self.parseDate(fstDate) - self.parseDate(scndDate)).total_seconds() < 0):
            return scndDate
        return fstDate
    '''
    
    '''
    def digitsInString(self, strToParse):
        return sum(char.isdigit() for char in strToParse)
    
    def calcPercentage(self, X, Y):
        return Y*100/X
    