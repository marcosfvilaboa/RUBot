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
from dateutil import parser
import sys
from datetime import datetime
      
if __name__ == '__main__':
    
    filePathIn = '../data/' + sys.argv[1]
    filePathOut = '../data/' + sys.argv[2]
    fileReader = JSONFile()
    fileWriter = CSVFile()
####### Trying to operate with dates
    date1 = 'Wed Mar 07 23:03:14 +0000 2018'
    date2 = 'Wed Mar 07 23:04:14 +0000 2018'
    date3 = 'Wed Mar 07 23:03:14 +0000 2018'
    date4 = 'Thu Mar 08 23:05:55 +0000 2018'
    parsed_date1 = parser.parse(date1) 
    parsed_date2 = parser.parse(date2)  
    parsed_date3 = parser.parse(date3) 
    parsed_date4 = parser.parse(date4)  
    # Second parsed date has to be later than first 
    parsed_dateA = parsed_date2 - parsed_date1
    parsed_dateB = parsed_date4 - parsed_date3
    parsed_date = list()
    
    parsed_date.append(parsed_dateB.total_seconds())
    parsed_date.append(parsed_dateA.total_seconds())
    
    parsed_date.sort()
#######
    conversationList = fileReader.readJson(filePathIn)
    conversationsNum = 0
    tweetsNum = 0
    mentionsNum = 0
    
    screenNames = list()
    userDetailsList = list()
    
    tweetTexts = list()
    tweetAuthors = list()
    for conversation in conversationList:
        conversationsNum += 1
        for tweets in conversation:
            tweetsNum += 1
            try:
                # Catch users of original tweet
                if tweets['retweeted_status']:
                    if tweets['retweeted_status']['user']['screen_name'] not in tweetAuthors:
                        tweetTexts.append({tweets['retweeted_status']['user']['screen_name'] : tweets['retweeted_status']['text']})
                        tweetAuthors.append(tweets['retweeted_status']['user']['screen_name'])
            except KeyError:
                # Key is not present
                pass
            # Catch users
            if tweets['user']['screen_name'] not in screenNames:                
                screenNames.append(tweets['user']['screen_name'])
                userDetailsList.append(tweets['user'])
    print("Date parsed: {0}".format(parsed_date))
    print("Number of conversations in file: {0}".format(conversationsNum))
    print("Number of tweet data: {0}".format(tweetsNum))
    print("Number of diferent users who twited: {0}".format(len(screenNames)))
    print("Number of authors of tweets retweeted: {0}".format(len(tweetAuthors)))
    print("Sample of 10 users who retweeted: {0}".format(screenNames[0:10])) 
    print("Sample of 5 retweeted tweets and its author username {0}".format(tweetTexts[0:5]))
    print("Details of user '{0}': {1}".format(userDetailsList[10]['screen_name'], userDetailsList[10]))
    
    # import data of the dictionaries list of users details to csv
    #fileWriter.writeCSV(filePathOut,userDetailsList)
    