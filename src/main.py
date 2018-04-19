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
from twitter.Info import Info

import sys

def addTweetInfoToLists(twt, twtLst, iTwtLst):  
    
    try:
        # Catch info from original tweet if its a retweet        
        if twt['retweeted_status']:
            if not Info().idInTweetList(twt['id'], iTwtLst):
                retwtMap = Info().addRetweetInfoToRetweetMap(twt)
                iTwtLst.append(retwtMap)      
        #catch normal tweet instead
        else:
            if not Info().idInTweetList(twt['id'], twtLst):        
                # add tweet details to tweet map
                twtMap = Info().addTweetInfoToTweetMap(twt)
                twtLst.append(twtMap)
    except KeyError:
        # Key is not present
        pass    

if __name__ == '__main__':
    
    filePathIn = '../data/' + sys.argv[1]
    userCSV = '../data/results/' + sys.argv[2]
    twtsCSV = '../data/results/' + sys.argv[3]
    retwtsCSV = '../data/results/' + sys.argv[4]
    fileReader = JSONFile()
    fileWriter = CSVFile()

    conversationList = fileReader.readJson(filePathIn)
    conversationsNum = 0
    userList = list()
    tweetList = list()
    interactionsTwtList = list()
    
    for conversation in conversationList:
        conversationsNum += 1
        for tweet in conversation:
            addTweetInfoToLists(tweet, tweetList, interactionsTwtList)
            
    
    print("Number of conversations in file: {0}".format(conversationsNum))
#     print("Number of tweet data: {0}".format(len(tweetList)))    
#     print("Details of tweet '{0}' by {1} in 'tweetList': {2}".format(tweetList[5]['id'], tweetList[5]['user']['screen_name'], tweetList[5]))
#     print("3 tweets selected from 'tweetList' : {0}".format(tweetList[12:15]))
    
    print("Number of retweet data: {0}".format(len(interactionsTwtList)))
    print("Details of tweet '{0}' by {1} in 'tweetList': {2}".format(interactionsTwtList[5]['id'], interactionsTwtList[5]['user_screen_name'], interactionsTwtList[5]))
    print("3 tweets selected from 'interactionsTwtList' : {0}".format(interactionsTwtList[12:15]))
    
    # import data of the dictionaries list of users details to csv
    #fileWriter.writeCSV(twtsCSV,tweetList)
    fileWriter.writeCSV(retwtsCSV,interactionsTwtList)
    
    