FREQUENCY = {
    "a": 8.4966,
    "b": 2.0720,
    "c": 4.5388,
    "d": 3.3844,
    "e": 11.1607,
    "f": 1.8121,
    "g": 2.4705,
    "h": 3.0034,
    "i": 7.5448,
    "j": 0.1965,
    "k": 1.1016,
    "l": 5.4893,
    "m": 3.0129,
    "n": 6.6544,
    "o": 7.1635,
    "p": 3.1671,
    "q": 0.1962,
    "r": 7.5809,
    "s": 5.7351,
    "t": 6.9509,
    "u": 3.6308,
    "v": 1.0074,
    "w": 1.2899,
    "x": 0.2902,
    "y": 1.7779,
    "z": 0.2722,
}

def calculate_score(s):
    score = 0.0
    for char in s:
        score += FREQUENCY[char]

    return score


def highestScoring(word_list):
    best = {"score": 0, "word": ""}
    
    print(len(word_list))
    for word in word_list: 
        score = calculate_score(word)
        score = score if "ee" not in word else score - 11

        if score > best["score"]: 
            best["score"] = score
            best["word"] = word

    return best["word"]


def calculate_score_new(s):
    score = 0.0
    used = []
    for char in s:
        score += FREQUENCY[char] if char not in used else 0
        used.append(char)

    return score

def starter(word_list):
    best = {"score": 0, "word": ""}
    
    print(len(word_list))
    for word in word_list: 
        score = calculate_score_new(word)

        if score > best["score"]: 
            best["score"] = score
            best["word"] = word

    return best["word"]