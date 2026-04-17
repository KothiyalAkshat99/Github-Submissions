"""
Problem Name: Design Twitter
Difficulty: Medium
Tags: Hash Table, Linked List, Design, Heap (Priority Queue)
"""

"""
Submission 1
Language: python3
Runtime: 0 ms
Memory: 27.9 MB
"""
class Twitter:

    time = 0
    
    def __init__(self):

        # Need to check if tweetIDs are in asc order, to make minHeap using tweetIDs
        # TWEETIDs ARE NOT IN GLOBAL ASC ORDER

        self.followers = {} # followerId : [followeeId]. Which all users does this user follow
        
        self.userTweets = {} # userId : [[Twitter.time, tweetId]]


    def postTweet(self, userId: int, tweetId: int) -> None:
        Twitter.time = Twitter.time + 1
        #heapq.heappush(tweets, [Twitter.time, userId, tweetId])

        if userId not in self.userTweets:
            self.userTweets[userId] = []
        self.userTweets[userId].append([Twitter.time, tweetId])


    def getNewsFeed(self, userId: int) -> List[int]:
        ret = []
        userlist = [] # to keep a list of all users whose tweets need to be fetched

        if userId in self.userTweets:
            userlist.append(userId)
        
        if userId in self.followers:
            for Id in self.followers[userId]:
                if Id in self.userTweets:
                    userlist.append(Id)
        
        maxHeap = []

        # self.userTweets = {userId : [[Twitter.time, tweetId]]}

        if userlist:
            for Id in userlist:
                for tweet in self.userTweets[Id]:
                    heapq.heappush(maxHeap, [-tweet[0], tweet[1]])
        
        n = 10
        
        while n > 0 and maxHeap:
            ret.append(heapq.heappop(maxHeap)[1])
            n -= 1

        return ret
        

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.followers:
            self.followers[followerId] = []
        
        if followeeId not in self.followers[followerId]:
            self.followers[followerId].append(followeeId)


    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.followers:
            if followeeId in self.followers[followerId]:
                self.followers[followerId].remove(followeeId)
        return


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)

"""
Submission 2
Language: python3
Runtime: 11 ms
Memory: 28.7 MB
"""
class Twitter:

    def __init__(self):
        self.timestamp = 0
        self.userTweets = {}       # {userId: [[time, tweetId]]}
        self.userFollows = {}      # {followerId: (followeeId)}. Which other users does this user follow

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.timestamp -= 1
        if userId not in self.userTweets:
            self.userTweets[userId] = []
        self.userTweets[userId].append([self.timestamp, tweetId])

    def getNewsFeed(self, userId: int) -> List[int]:
        ret = [] # List of tweets, ordered starting from recent
        minHeap = []

        # Need to consider user's own tweets as well
        if userId not in self.userFollows:
            self.userFollows[userId] = set()
        self.userFollows[userId].add(userId)

        # For all followees of this user
        for followeeId in self.userFollows[userId]:
            if followeeId in self.userTweets:
                index = len(self.userTweets[followeeId]) - 1
                
                # Getting last/lastest tweet from followeeId
                time, tweetId = self.userTweets[followeeId][index]
                
                minHeap.append([time, tweetId, followeeId, index - 1])
        
        heapq.heapify(minHeap)
        
        while minHeap and len(ret) < 10:
            time, tweetId, followeeId, index = heapq.heappop(minHeap)
            ret.append(tweetId)
            if index >= 0:
                # Next tweet by this user/followee
                # We already decremented index by 1 while inserting into minheap
                time, tweetId = self.userTweets[followeeId][index]
                heapq.heappush(minHeap, [time, tweetId, followeeId, index - 1])

        return ret


    def follow(self, followerId: int, followeeId: int) -> None:
        # If followerId currently does not follow anyone
        if followerId not in self.userFollows:
            self.userFollows[followerId] = set()
        
        if followeeId != followerId:
            self.userFollows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.userFollows:
            if followeeId in self.userFollows[followerId]:
                self.userFollows[followerId].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)

