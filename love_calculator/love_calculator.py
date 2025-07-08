def calculate_love_score(name1, name2):
    love_phrase = "TRUE LOVE"
    # print(love_phrase.split()[0])
    # print(love_phrase.split()[1])

    points_word1 = 0
    points_word2 = 0
    for name_letter in name1.lower() + name2.lower():
        # print(name_letter)
        for word_letter in love_phrase.split()[0].lower():
            # print(word_letter)
            if name_letter == word_letter:
                points_word1 += 1
                # print("si")
        for word_letter in love_phrase.split()[1].lower():
            # print(word_letter)
            if name_letter == word_letter:
                points_word2 += 1
                # print("si")
    # print(points_word1)
    # print(points_word2)
    love_score = str(points_word1) + str(points_word2)
    return print(love_score)

calculate_love_score("Angela Yu", "Keanu Reeves")