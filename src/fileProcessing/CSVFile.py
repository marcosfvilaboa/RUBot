'''        -------------------------
Project:     RUBot: humano o bot
           -------------------------
@author: Marcos F. Vilaboa
   Degree in CS (Universitat Oberta de Catalunya)
   -Open Data: Capture, analysis and visualisation - area
                                                    Created on 11 abr. 2018            
'''
import csv
class CSVFile:
    '''
    classdocs
    '''
    def __init__(self, filePath={}):
        self.fileObj = filePath
    
    def writeCSV(self, filePath, dictsList):
        keys = dictsList[0].keys()
        with open(filePath, 'w', newline='', encoding='utf-8') as output_file:
            dict_writer = csv.DictWriter(output_file, keys)
            dict_writer.writeheader()
            dict_writer.writerows(dictsList)