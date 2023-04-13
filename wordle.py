from letterfrequency import highestScoring, starter

F = open("wordleList.txt", "r")
wordList = F.read().split(" ")


print("loaded")

status = "_____"
guess = ""
lettersIn = []
lettersNotIn = []
LIindexes = []


def addLetters(char, i):
    if char not in lettersIn:
        lettersIn.append(char)
        LIindexes.append([i])
    else:
        LIindexes[lettersIn.index(char)].append(i)



def usedPosition(char, i):
    if char not in lettersIn: return False
    if i in LIindexes[lettersIn.index(char)]:
        return True
    return False


guess = starter(wordList)

print("1)", guess)
status = input("Enter Status:\t").strip()

filteredWords = wordList.copy()
for i in range(2, 7):

    for j in range(len(status)):

        letters = {guess[j]: guess.count(guess[j])}

        if status[j] == "_" and guess[j] not in lettersNotIn and letters[guess[j]] < 2:
            lettersNotIn.append(guess[j])

        elif status[j] == "+" and guess[j]:
            addLetters(guess[j], j)

    print(lettersIn, lettersNotIn)

    for word in wordList:

        removeIt = False
        for l in range(len(word)):
            if ((word[l] in lettersNotIn) or ( usedPosition(word[l], l))) and (word in filteredWords): 
                removeIt = True
        
        for letter in lettersIn:
            if letter not in word and word in filteredWords: 
                removeIt = True

        for k in range(len(status)):
            try:
                if status[k] not in "+_" and status[k] != word[k] and word in filteredWords: 
                    removeIt = True
            except IndexError:
                removeIt = True
        
        try:
            if removeIt:
                filteredWords.remove(word)
        except ValueError:
            print(word)


    guess = highestScoring(filteredWords)
    print(i, ")", guess)
    status = input("Enter Status:\t").strip()

    if status == 'list':
        print(filteredWords)
        status = input("Enter Status:\t").strip()

    if status == guess:
        print("GG EZ MODE")
        break
