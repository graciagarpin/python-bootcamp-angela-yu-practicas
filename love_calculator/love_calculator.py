name1= input("Please, write your name: ")
name2= input("Please, write the name of the person you love: ")

def calculate_love_score(name1, name2):
    word1 = "TRUE"
    word2 = "LOVE"
    points_word1 = 0
    points_word2 = 0
    for name_letter in name1.lower() + name2.lower():
        # print(name_letter)
        for word_letter in word1.lower():
            # print(word_letter)
            if name_letter == word_letter:
                points_word1 += 1
                # print("si")
        for word_letter in word2.lower():
            # print(word_letter)
            if name_letter == word_letter:
                points_word2 += 1
                # print("si")
    # print(points_word1)
    # print(points_word2)
    love_score = str(points_word1) + str(points_word2)
    return print(f"The love score of the couple is: {love_score}/100")


calculate_love_score(name1, name2)