#
# @lc app=leetcode id=535 lang=python3
#
# [535] Encode and Decode TinyURL
#

# @lc code=start
class Codec:
    memory = dict()
    memory_rev = dict()
    counter = 0
    prefix = 'https://shortURL.com/'
    

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        if longUrl not in self.memory:
            Uid = str(hex(self.counter)[2:])
            self.counter += 1
            self.memory[longUrl] = Uid
            self.memory_rev[Uid] = longUrl
        return self.prefix+self.memory[longUrl]


    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self.memory_rev.get(shortUrl[len(self.prefix):])
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
# @lc code=end

