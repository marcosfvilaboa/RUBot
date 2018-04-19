'''        -------------------------
Project:     RUBot: humano o bot
           -------------------------
@author: Marcos F. Vilaboa
   Degree in CS (Universitat Oberta de Catalunya)
   -Open Data: Capture, analysis and visualisation - area
                                                    Created on 18 abr. 2018            
'''
from utils.Calcs import Calcs

class Info(dict):
    '''
    classdocs
    '''
    
    def idInTweetList(self, twt, ttList):
        for i in ttList: 
            if twt['user']['id'] == i['id']:
                return True
        return False
    
    def timeBetweenTweets(self, numOfTwt, dtUserCreation, dtLastTwt):
        return (Calcs().substractStringDates(dtUserCreation, dtLastTwt) / numOfTwt)
    
    def uploadUserRetweetInfo(self, retwt, ttList):
        for i in ttList: 
            if i['id'] == retwt['user']['id']:
                i['retweets_count'] += 1
                i['retweet_response_total_seconds'] += Calcs().substractStringDates(retwt['created_at'], retwt['retweeted_status']['created_at'])
                i['retweet_response_time_mean'] = round(i['retweet_response_total_seconds'] / i['retweets_count'], 2)
                i['retweet_percentage'] = Calcs().calcPercentage(i['statuses_count'], i['retweets_count'])
                if (i['statuses_count'] < retwt['user']['statuses_count']):
                    i['time_between_tweets'] = round(self.timeBetweenTweets(retwt['user']['statuses_count'], i['created_at'], retwt['created_at']), 2)

    def addNewRetweet(self, retwt):
        retwtMap = {}
        
        # Calculate the difference between the date of the original tweet and the retweet
        retwtDate = retwt['created_at']
        twtDate = retwt['retweeted_status']['created_at']
        diff_time_after_twt = Calcs().substractStringDates(retwtDate, twtDate)
        #Calculate the number of chars in the screen name and the name
        chars_in_screen_name = len(retwt['user']['screen_name'])
        chars_in_name = len(retwt['user']['name'])
        # Calculate the number of digits in the screen name
        digits_in_screen_name = Calcs().digitsInString(retwt['user']['screen_name'])
        
        # Add all the information to the Map
        retwtMap['id'] = retwt['user']['id']
        retwtMap['screen_name'] = retwt['user']['screen_name']
        retwtMap['chars_in_screen_name'] = chars_in_screen_name
        retwtMap['digits_in_screen_name'] = digits_in_screen_name
        retwtMap['name'] = retwt['user']['name']
        retwtMap['chars_in_name'] = chars_in_name
        retwtMap['statuses_count'] = retwt['user']['statuses_count']
        retwtMap['followers_count'] = retwt['user']['followers_count']
        retwtMap['friends_count'] = retwt['user']['friends_count']
        retwtMap['listed_count'] = retwt['user']['listed_count']
        retwtMap['lang'] = retwt['user']['lang']
        retwtMap['created_at'] = retwt['user']['created_at']   
        retwtMap['tweets_count'] = 1 
        retwtMap['retweets_count'] = 1       
        retwtMap['retweet_response_total_seconds'] = diff_time_after_twt
        retwtMap['retweet_response_time_mean'] = round(diff_time_after_twt, 2)
        retwtMap['retweet_percentage'] = Calcs().calcPercentage(retwt['user']['statuses_count'], 1)
        retwtMap['time_between_tweets'] = round(self.timeBetweenTweets(retwt['user']['statuses_count'], retwt['user']['created_at'], retwt['created_at']), 2)   
        
        return retwtMap
    
    def addTweetInfoToList(self, twt, twtLst):   
        try:
            # Catch info from original tweet if its a retweet        
            if twt['retweeted_status']:
                if not self.idInTweetList(twt, twtLst):
                    twtMap = self.addNewRetweet(twt)
                    twtLst.append(twtMap)
                else:
                    self.uploadUserRetweetInfo(twt,twtLst)
            else:
            # if its not a retweet
            # for now not implemented because the JSON example file seems not to have them
                if not self.idInTweetList(twt, twtLst):
                    twtMap = self.addNewRetweet(twt)
                    twtLst.append(twtMap)     
        except KeyError:
            # Key is not present
            pass 
    