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
from twitter.ParsedDate import ParsedDate

import sys
      
if __name__ == '__main__':
    
    filePathIn = '../data/' + sys.argv[1]
    userCSV = '../data/results/' + sys.argv[2]
    fileReader = JSONFile()
    fileWriter = CSVFile()
    
####### Trying to operate with dates

    date1 = 'Wed Mar 07 23:03:14 +0000 2018'
    date2 = 'Wed Mar 07 23:04:14 +0000 2018'
    date3 = 'Thu Mar 08 23:05:55 +0000 2018' 
    parsed_dates = list()
    
    parsed_dates.append(ParsedDate().substractStringDates(date1, date2))
    parsed_dates.append(ParsedDate().substractStringDates(date3, date3))
    parsed_dates.append(ParsedDate().substractStringDates(date3, date1))
    parsed_dates.append(ParsedDate().substractStringDates(date2, date3))
    
    #parsed_dates.sort()
    
#######
    conversationList = fileReader.readJson(filePathIn)
    conversationsNum = 0
    tweetsNum = 0
    mentionsNum = 0
    
    idList = list()
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
            if tweets['user']['id'] not in idList:                
                idList.append(tweets['user']['id'])
                userDetailsList.append(tweets['user'])
    
    print("Date parsed: {0}".format(parsed_dates))
    print("Number of conversations in file: {0}".format(conversationsNum))
    print("Number of tweet data: {0}".format(tweetsNum))
    print("Number of diferent users who twited: {0}".format(len(idList)))
    print("Number of authors of tweets retweeted: {0}".format(len(tweetAuthors)))
    print("Sample of 10 users who retweeted: {0}".format(idList[0:10])) 
    print("Sample of 5 retweeted tweets and its author username {0}".format(tweetTexts[0:5]))
    print("Details of user '{0}': {1}".format(userDetailsList[10]['screen_name'], userDetailsList[10]))
    
    # import data of the dictionaries list of users details to csv
    fileWriter.writeCSV(userCSV,userDetailsList)
    
    