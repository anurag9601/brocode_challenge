def find_anagrams(s, p):
    result = []

    def appear_count_dic(subs):
        count_dic = {}
        for i in range(len(subs)):
            count = 0
            if subs[i] not in list(count_dic.keys()):
                for j in range(i, len(subs)):
                    if subs[i] == subs[j]:
                        count += 1
                count_dic[subs[i]] = count
        return count_dic
    
    p_count = appear_count_dic(p)

    p_keys = list(p_count.keys())

    len_p = len(p)

    for i in range(len(s) - len_p + 1):
        matched = True
        curr_str = s[i : i + len_p]
        curr_str_dic = appear_count_dic(curr_str)
        for key, value in curr_str_dic.items():
            if key not in p_keys or p_count[key] != value:
                matched = False
                break
        if matched:
            result.append(i)
    return result

# print(find_anagrams("cbaebabacd", "abc"))
# print(find_anagrams("abab", "ab"))