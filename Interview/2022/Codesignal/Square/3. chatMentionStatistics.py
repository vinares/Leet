import collections
import re

def chatMentionStatistics(messages):
    hashtable = collections.defaultdict(int)
    ans = []
    for message in messages:
        message = message.replace('.',' ')
        x = message.replace('!',' ').split()
        hasht = set()
        for y in x:
            if y[0] == "@":
                ids = re.split(',|@',y[1::])
                for id in ids:
                    if id[0:2] == 'id' and id[2::].isnumeric():
                        hasht.add(id)
        for id in hasht:
            hashtable[id] += 1
    for i, j in sorted(hashtable.items(),key=lambda x : (x[1],x[0]), reverse=False):
        ans.append(i + '=' + str(j))
    return ans

messages = ["@id123,id456,di789 only first two mentions will work",
 "@id123,id456.id789 only first two mentions will work",
 "@idNotDigits is not a mention"]
print(chatMentionStatistics(messages))