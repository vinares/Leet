def brokenKeyboard(text, letters):
    words = text.split()
    ans = 0
    letter = set()
    for l in letters:
        letter.add(l)
    for word in words:
        flag = True
        for x in word:
            if 'A' <= x <= 'Z':
                print(x)
                x = chr(ord(x) + 32)
            if 'a' <= x <= 'z' and x not in letter:
                flag = False
                break
        if flag:
            ans += 1
    return ans

text = "Hello, this is CodeSignal!"
letters = ['e', 'i', 'h', 'l', 'o', 's']
print(brokenKeyboard(text,letters))