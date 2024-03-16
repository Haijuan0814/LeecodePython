class User:
    def __init__(self , userId):
        self.userId = userId
        self.tweets = {}
        self.following = set()
        self.followers = set()


class Twitter:

    def __init__(self):
        self.users = {}
        self.time = 0
    
    def createUser(self , userId):
        if userId not in self.users:
            self.users[userId] = User(userId)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.createUser(userId)
        self.users[userId].tweets[tweetId] = self.time
        self.time += 1


    def getNewsFeed(self, userId: int) -> List[int]:
        self.createUser(userId)
        res = []
        # 找出self发的tweets
        for t in self.users[userId].tweets:
            res.append([t[0],t[1]])
        # 找出following的人发的tweets
        for f_uid in self.users[userId].following:
            for tw ,ti  in self.users[f_uid].tweets:
                res.append([tw,ti])
        # 按照时间倒序输出10个
        res = sorted(res[0], key = lambda x : (x[1]) , reverse = True)
        return res[:10]
        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.createUser(followerId)
        self.users[followerId].following.add(followeeId)

        self.createUser(followeeId)
        self.users[followeeId].followers.add(followerId)
        
    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.createUser(followerId)
        self.users[followerId].following.remove(followeeId)

        self.createUser(followeeId)
        self.users[followeeId].followers.remove(followerId)
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)