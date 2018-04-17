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
def myprint(d):
    for k, v in d.iteritems():
        if isinstance(v, dict):
            myprint(v)
        else:
            print('{0} : {1}'.format(k, v))
      
if __name__ == '__main__':
    
    filePathIn = '../data/' + sys.argv[1]
    filePathOut = '../data/' + sys.argv[2]
    fileReader = JSONFile()
    fileWriter = CSVFile()
    
    date = 'Wed Mar 07 23:04:55 +0000 2018'
    parsed_date = parser.parse(date)
    
    
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
    
    print("Number of conversations in file: {0}".format(conversationsNum))
    print("Number of tweet data (retweets): {0}".format(tweetsNum))
    print("Number of diferent users who twited: {0}".format(len(screenNames)))
    print("Number of authors of tweets retweeted: {0}".format(len(tweetAuthors)))
    print("Sample of 10 users who retweeted: {0}".format(screenNames[0:10])) 
    print("Sample of 5 retweeted tweets and its author username {0}".format(tweetTexts[0:5]))
    print("Details of user '{0}': {1}".format(userDetailsList[10]['screen_name'], userDetailsList[10]))
    
    # import data of the dictionaries list of users details to csv
    fileWriter.writeCSV(filePathOut,userDetailsList)