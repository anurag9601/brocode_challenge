def factor_sort(nums):
    factor_dict = {}
    result = []
    for num in nums:
        factor_count = 0
        for i in range(1,num + 1):
            if num % i == 0:
                factor_count += 1
        factor_dict[factor_count] = num
    value_lst = list(factor_dict.keys())
    return value_lst

# print(factor_sort([9, 7, 13, 12]))

def nearest_chapter(chapter_obj, find_page_no):
    closest_chapter = ""
    closest_page = None

    for chapter,pageNo in chapter_obj.items():
        pageDifference = abs(pageNo - find_page_no)
        if not closest_page:
            closest_page = pageDifference
            closest_chapter = chapter
        elif closest_page > pageDifference:
            pageDifference = closest_page
            closest_chapter = chapter
    return closest_chapter


# print(nearest_chapter({
#   "Chapter 1" : 1,
#   "Chapter 2" : 15,
#   "Chapter 3" : 37
# }, 10))

# print(nearest_chapter({
#   "New Beginnings" : 1,
#   "Strange Developments" : 62,
#   "The End?" : 194,
#   "The True Ending" : 460
# }, 200))

def same_vowel_group(words):

    def get_present_vowel(word):
        vowels = "aeiou"
        present_vowels = ""
        for letter in vowels:
            if letter in word:
                present_vowels += letter
        return sorted(present_vowels)
    
    result = [words[0]]
    common_vowel = get_present_vowel(words[0])

    for i in range(1, len(words)):
        current_word_vowel = get_present_vowel(words[i])
        if current_word_vowel == common_vowel:
            result.append(words[i])
    
    return result

# print(same_vowel_group(["toe", "ocelot", "maniac"]))
# print(same_vowel_group(["many", "carriage", "emit", "apricot", "animal"]))
# print(same_vowel_group(["hoops", "chuff", "bot", "bottom"]))
        


