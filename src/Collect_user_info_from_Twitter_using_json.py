'''        -------------------------
Project:     RUBot: humano o bot
           -------------------------
@author: Marcos F. Vilaboa
   Degree in CS (Universitat Oberta de Catalunya)
   -Open Data: Capture, analysis and visualisation - area
                                                    Created on 29 may. 2018            
'''

from fileProcessing.JSONFile import JSONFile
from twitter.CollectUserInfo import CollectUserInfo
import time   

if __name__ == '__main__':
    
    start_time = time.time()
    
    fileJsonIn = './data/jornada_8_marzo.json'
    fileJsonOut = './data/temp/usuarios_info_8M.json'
    
    fileReader = JSONFile() 
    
    # Collect user data from JSON file with tweets
    conversationList = fileReader.readJson(fileJsonIn)
    tweetList = list()
         
    usersNamesList = list()
  
    for conversation in conversationList:
        for tweet in conversation:
            if tweet['user']['screen_name'] not in usersNamesList:
                usersNamesList.append(tweet['user']['screen_name'])
    
    print("Number of users in list: {0}".format(len(usersNamesList)))
    print("First 5 users screen names in list: {0}".format(usersNamesList[0:5]))
    
    # Collect user data from json file with tweets
    fromTwitterAPI = CollectUserInfo() 
    print("\nSearching information of the users...\n")
    usersDict = fromTwitterAPI.getTwitterUsersInfoFromList(usersNamesList)
    
    # Import data of the twitter API from list of users id's and write them into JSON file
    fileReader.writeJSON(usersDict, fileJsonOut)
    
    print("--- %s seconds ---" % round((time.time() - start_time), 2))