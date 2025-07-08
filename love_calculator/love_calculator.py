name1 = input("Please, write your name: ")
name2 = input("Please, write the name of the person you love: ")

def calculate_love_score(name1, name2):
    love_phrase = "TRUE LOVE"

    points_word1 = 0
    points_word2 = 0
    for name_letter in name1.lower() + name2.lower():
        for word_letter in love_phrase.split()[0].lower():
            if name_letter == word_letter:
                points_word1 += 1
        for word_letter in love_phrase.split()[1].lower():
            if name_letter == word_letter:
                points_word2 += 1
    love_score = str(points_word1) + str(points_word2)
    return print(f"The Love Score of the couple is: {love_score}/100")

calculate_love_score(name1, name2)