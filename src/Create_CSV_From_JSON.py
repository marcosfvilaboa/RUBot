'''        -------------------------
Project:     RUBot: humano o bot
           -------------------------
@author: Marcos F. Vilaboa
   Degree in CS (Universitat Oberta de Catalunya)
   -Open Data: Capture, analysis and visualisation - area
                                                    Created on 10 abr. 2018            
'''
from fileProcessing.JSONFile import JSONFile
from fileProcessing.CSVFile import CSVFile
from twitter.CollectUserInfo import CollectUserInfo
import sys
import time
   

if __name__ == '__main__':
    
    start_time = time.time()
    
    # result CSV filename passed by first parameter
    usersCSV = '../data/results/' + sys.argv[1]    
    # source JSON filename passed by second parameter
    fileJSON = '../data/temp/' + sys.argv[2]    
    # date of the info user data collection passed by third parameter
    dateOfCollection = sys.argv[3]
    
    fileReader = JSONFile()
    fileWriter = CSVFile()
    
    # Create CSV with user info from JSON
    usersListFromJSON = fileReader.readJson(fileJSON)
    userList = list()
    usersNum = 0
    for user in usersListFromJSON:
        usersNum += 1
        CollectUserInfo().addUsersInfoToList(user, userList, dateOfCollection)
        
    fileWriter.writeCSV(usersCSV,userList)
    print("Number of users in file: {0}".format(usersNum))
    print("Details of user '{0}':".format(userList[5]['screen_name']))  
    for y in userList[5]:
        print ('    -',y,'->',userList[5][y])
    
    print("--- %s seconds ---" % round((time.time() - start_time), 2))    
    