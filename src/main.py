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

   

if __name__ == '__main__':
    
    filePathIn = '../data/' + sys.argv[1]
    twtsCSV = '../data/results/' + sys.argv[2]
    fileReader = JSONFile()
    fileWriter = CSVFile()

    conversationList = fileReader.readJson(filePathIn)
    conversationsNum = 0
    tweetList = list()
    
    for conversation in conversationList:
        conversationsNum += 1
        for tweet in conversation:
            Info().addTweetInfoToList(tweet, tweetList)
            
    
    print("Number of conversations in file: {0}".format(conversationsNum))    
    print("Number of retweet data: {0}".format(len(tweetList)))
    print("Details of tweet '{0}' by {1} in 'tweetList': {2}".format(tweetList[5]['id'], tweetList[5]['screen_name'], tweetList[5]))
    print("3 tweets selected from 'tweetList' : {0}".format(tweetList[12:15]))
    
    # import data of the dictionaries list of users details to csv
    fileWriter.writeCSV(twtsCSV,tweetList)
    
    