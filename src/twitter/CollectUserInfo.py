'''        -------------------------
Project:     RUBot: humano o bot
           -------------------------
@author: Marcos F. Vilaboa
   Degree in CS (Universitat Oberta de Catalunya)
   -Open Data: Capture, analysis and visualisation - area
                                                    Created on 6 may. 2018
'''
from twitter.Config import Config
import tweepy
from tweepy import OAuthHandler
import json
import time
from utils.Calcs import Calcs

class CollectUserInfo:       
    
    auth = OAuthHandler(Config.consumer_key, Config.consumer_secret)
    auth.set_access_token(Config.access_token, Config.access_secret)         
    api = tweepy.API(auth) 
    max_query_size = 900
    
    def catchMyFriendsListFromTwitter(self):
        count = 0
        data = {}  
        data['content'] = []  
        for friend in tweepy.Cursor(self.api.friends).items():
            data['content'].append(friend._json)
            self.processOrStore(friend._json)
            count += 1
        print("Number of friends catched in my friends list = {0}".format(count))
        return data
    '''
    Code from http://www.erinshellman.com/bot-or-not/
    adapted to this case
    '''
    def getTwitterUsersInfoFromList(self, usersList):
        data = {}  
        data['content'] = []
        errorsCount = 0
        correctsCount = 0
        if len(usersList) > self.max_query_size:
            chunks = self.blowChunks(usersList, self.max_query_size)
            while True:
                try:
                    currentChunk = next(chunks)
                    for user in currentChunk:
                        try:
                            userData = self.api.get_user(user)
                            data['content'].append(userData._json)
                            correctsCount += 1
                        except:
                            # if the user doesn't exist
                            print("  ERROR collecting data from user '{0}' ".format(user))
                            errorsCount += 1
                            pass
                    print("\nIt's time to take a break due the Twitter API rate limits!\n")
                    time.sleep(60 * 16)
                    continue
                except StopIteration:
                    break  
        else:
            for user in usersList:
                try:
                    user_data = self.api.get_user(user)
                    data['content'].append(user_data._json)
                    correctsCount += 1
                except:
                    # if the user doesn't exist
                    print("  ERROR collecting data from user '{0}' ".format(user))
                    errorsCount += 1
                    pass
        print("\n----Information collected correctly from {0} users".format(correctsCount))
        print("----It was not possible to collect information from {0} users".format(errorsCount))
        return data
    '''
    Code from http://www.erinshellman.com/bot-or-not/
    adapted to this case
    '''
    def blowChunks(self, data, max_chunk_size):
        for i in range(0, len(data), max_chunk_size):
            yield data[i:i + max_chunk_size]
    
    def processOrStore(self,tweet):        
        print(json.dumps(tweet))
    
    def addUsersInfoToList(self, userDict, userList, dateOfMakeCollection):
        try:
            # Catch info from original tweet if its a retweet        
            if userDict['id']:
                userMap = self.addNewUser(userDict, dateOfMakeCollection)
                userList.append(userMap)   
        except KeyError:
            # Key is not present
            pass 
        
    def addNewUser(self, user, dateOfMakeCollection):
        userMap = {}
        
        # Calculate the timedelta difference between the creation of the user and 
        # the date of the data collection in seconds
        diff_time_collection_user_creation = Calcs().substractStringDates(dateOfMakeCollection, user['created_at'])
        # Convert the difference into days
        diff_time_collection_user_creation /= (24 * 60 * 60)
        #Calculate the number of chars in the screen name and the name
        charsInScreenName = len(user['screen_name'])
        charsInName = len(user['name'])
        # Calculate the number of digits in the screen name
        digitsInScreenName = Calcs().digitsInString(user['screen_name'])
        
        # Add all the information to the Map
        userMap['id'] = user['id']
        userMap['screen_name'] = user['screen_name']
        userMap['chars_in_screen_name'] = charsInScreenName
        userMap['digits_in_screen_name'] = digitsInScreenName
        userMap['name'] = user['name']
        userMap['chars_in_name'] = charsInName
        userMap['statuses_count'] = user['statuses_count']
        userMap['statuses_percentage'] = Calcs().calcPercentage(user['statuses_count'])
        userMap['tweets_per_day'] = (userMap['statuses_count'] / diff_time_collection_user_creation)
        userMap['followers_count'] = user['followers_count']
        userMap['followers_count_percentage'] = Calcs().calcPercentage(user['followers_count'])
        userMap['friends_count'] = user['friends_count']
        userMap['friends_count_percentage'] = Calcs().calcPercentage(user['friends_count'])
        userMap['friends_followers_rate'] = 1 -(userMap['followers_count_percentage'] - userMap['friends_count_percentage'])
        userMap['listed_count'] = user['listed_count']
        userMap['favourites_count'] = user['favourites_count']
        if (user['verified'] == True):
            userMap['verified'] = 1
        else:
            userMap['verified'] = 0
        if (user['contributors_enabled'] == True):
            userMap['contributors_enabled'] = 1
        else:
            userMap['contributors_enabled'] = 0 
        if (user['profile_use_background_image'] == True):
            userMap['profile_use_background_image'] = 1
        else:
            userMap['profile_use_background_image'] = 0 
        if (user['has_extended_profile'] == True):
            userMap['has_extended_profile'] = 1
        else:
            userMap['has_extended_profile'] = 0 
        if (user['default_profile'] == True):
            userMap['default_profile'] = 1
        else:
            userMap['default_profile'] = 0 
        if (user['default_profile_image'] == True):
            userMap['default_profile_image'] = 1
        else:
            userMap['default_profile_image'] = 0
        userMap['favourites_count'] = user['favourites_count']
        userMap['lang'] = user['lang']
        userMap['created_at'] = user['created_at']         
          
        
        return userMap