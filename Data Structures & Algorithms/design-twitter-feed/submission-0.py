class Twitter:

    def __init__(self):
        self.postMap = defaultdict(list)
        self.followMap = defaultdict(set)
        self.t = 0


    def postTweet(self, userId: int, tweetId: int) -> None:
        self.postMap[userId].append((self.t, tweetId))
        self.t += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        feed = self.postMap[userId][:]
        for followee in self.followMap[userId]:
            feed.extend(self.postMap[followee])
        
        # sort feed by t
        feed.sort(key = lambda x : -x[0])

        # return top 10 tweets in feed
        return [tweetId[1] for tweetId in feed[:10]]

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId is not followeeId:
            self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].discard(followeeId) 
        
