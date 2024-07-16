from collections import defaultdict

def group_anagrams(words):
    anagrams = defaultdict(list)
    for word in words:
        sorted_word = ''.join(sorted(word))
        anagrams[sorted_word].append(word)
    return list(anagrams.values())

if __name__ == "__main__":
    words = input("Enter a list of words (comma separated): ").split(',')
    words = [word.strip() for word in words]
    print(group_anagrams(words))
