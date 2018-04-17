'''        -------------------------
Project:     RUBot: humano o bot
           -------------------------
@author: Marcos F. Vilaboa
   Degree in CS (Universitat Oberta de Catalunya)
   -Open Data: Capture, analysis and visualisation - area
                                                    Created on 10 abr. 2018            
'''

import json

class JSONFile:
    '''
    classdocs
    '''
    
    def __init__(self, filePath={}):
        self.fileObj = filePath
         
    ''' 
    readJson read a JSON file from filePath composed by one dictionary field 
    with 'content' as a KEY and a list of diccionaries as a VALUE
    
    @return contentList with a list of lists
    '''   
    def readJson(self, filePath):
        with open(filePath, 'r', encoding='utf8') as self.fileObj: 
            jsonTree = json.load(self.fileObj)
            contentList = jsonTree['content']
        return contentList
