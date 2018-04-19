'''        -------------------------
Project:     RUBot: humano o bot
           -------------------------
@author: Marcos F. Vilaboa
   Degree in CS (Universitat Oberta de Catalunya)
   -Open Data: Capture, analysis and visualisation - area
                                                    Created on 18 abr. 2018            
'''
from twitter.ParsedDate import ParsedDate

class Info(dict):
    '''
    classdocs
    '''
    
    def idInTweetList(self, tt, ttList):
        for i in ttList: 
            if i['id'] == tt: 
                return True
        return False

    def addTweetInfoToTweetMap(self, twt):
        twtMap = {}
        
        #Calculate the number of chars in the screen name and the name
        chars_in_screen_name = len(twt['user']['screen_name'])
        chars_in_name = len(twt['user']['name'])
        # Calculate the number of digits in the screen name
        digits_in_screen_name = sum(char.isdigit() for char in twt['user']['screen_name'])
        
        # Add all the information to the Map
        twtMap['id'] = twt['id']    
        twtMap['quote_count'] = twt['quote_count']
        twtMap['contributors'] = twt['contributors']
        twtMap['text'] = twt['text']
        twtMap['reply_count'] = twt['reply_count']
        twtMap['lang'] = twt['lang']
        twtMap['created_at'] = twt['created_at']    
        twtMap['user_id'] = twt['user']['id']
        twtMap['user_screen_name'] = twt['user']['screen_name']
        twtMap['user_chars_in_screen_name'] = chars_in_screen_name
        twtMap['user_digits_in_screen_name'] = digits_in_screen_name
        twtMap['user_name'] = twt['user']['name']
        twtMap['user_chars_in_name'] = chars_in_name
        twtMap['user_statuses_count'] = twt['user']['statuses_count']
        twtMap['user_followers_count'] = twt['user']['followers_count']
        twtMap['user_friends_count'] = twt['user']['friends_count']
        twtMap['user_listed_count'] = twt['user']['listed_count']
        twtMap['user_lang'] = twt['user']['lang']
        twtMap['user_created_at'] = twt['user']['created_at'] 
        
        print('twt MAP: ', twtMap)
        input('Press enter...')
        
        return twtMap
  
    def addTweetInfoToUserMap(self, tt):
        userMap = {}
        
        userMap.id = tt['id']
        userMap.screen_name = tt['screen_name']
        userMap.statuses_count = tt['statuses_count']
        userMap.followers_count = tt['followers_count']
        userMap.friends_count = tt['friends_count']
        userMap.listed_count = tt['listed_count']
        userMap.lang = tt['lang']
        userMap.created_at = tt['created_at']
        
        return userMap

    def addRetweetInfoToRetweetMap(self, twt):
        retwtMap = {}
        
        # Calculate the difference between the date of the original tweet and the retweet
        retwtDate = twt['created_at']
        twtDate = twt['retweeted_status']['created_at']
        diff_time_after_twt = (ParsedDate().substractStringDates(retwtDate, twtDate))
        #Calculate the number of chars in the screen name and the name
        chars_in_screen_name = len(twt['user']['screen_name'])
        chars_in_name = len(twt['user']['name'])
        # Calculate the number of digits in the screen name
        digits_in_screen_name = sum(char.isdigit() for char in twt['user']['screen_name'])
        
        # Add all the information to the Map
        retwtMap['id'] = twt['id']    
        retwtMap['quote_count'] = twt['quote_count']
        retwtMap['contributors'] = twt['contributors']
        retwtMap['text'] = twt['text']
        retwtMap['reply_count'] = twt['reply_count']
        retwtMap['lang'] = twt['lang']
        retwtMap['created_at'] = twt['created_at']    
        retwtMap['seconds_after_twt'] = diff_time_after_twt
        retwtMap['user_id'] = twt['user']['id']
        retwtMap['user_screen_name'] = twt['user']['screen_name']
        retwtMap['user_chars_in_screen_name'] = chars_in_screen_name
        retwtMap['user_digits_in_screen_name'] = digits_in_screen_name
        retwtMap['user_name'] = twt['user']['name']
        retwtMap['user_chars_in_name'] = chars_in_name
        retwtMap['user_statuses_count'] = twt['user']['statuses_count']
        retwtMap['user_followers_count'] = twt['user']['followers_count']
        retwtMap['user_friends_count'] = twt['user']['friends_count']
        retwtMap['user_listed_count'] = twt['user']['listed_count']
        retwtMap['user_lang'] = twt['user']['lang']
        retwtMap['user_created_at'] = twt['user']['created_at']   
        
        return retwtMap
    