'''        -------------------------
Project:     RUBot: humano o bot
           -------------------------
@author: Marcos F. Vilaboa
   Degree in CS (Universitat Oberta de Catalunya)
   -Open Data: Capture, analysis and visualisation - area
                                                    Created on 18 abr. 2018            
'''
from dateutil import parser

class ParsedDate:
    
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
    