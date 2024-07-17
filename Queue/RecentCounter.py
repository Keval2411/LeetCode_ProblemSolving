from collections import deque

class Recentcounter(object):
    def __init__(self):
        self.request = deque()
        
    def ping(self, t):
        self.request.append(t)
        while self.request[0]< t-3000:
            self.request.popleft()
        return len(self.request)
recentcounter=Recentcounter()
print(recentcounter.ping(1))
print(recentcounter.ping(100))
print(recentcounter.ping(3001))
print(recentcounter.ping(3002))
        
        