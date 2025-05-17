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

def bar_chart(char_val):
    keys = list(char_val.keys())
    values = list(char_val.values())

    for i in range(len(values)):
        max_num_i = i
        for j in range(i, len(values)):
            if values[j] > values[max_num_i]:
                max_num_i = j
        values[i],values[max_num_i] = values[max_num_i],values[i]
        keys[i],keys[max_num_i] = keys[max_num_i],keys[i]
    
    for i in range(len(keys)):
        if values[i] == 0:
            print(f"{keys[i]} | {values[i]}")
        else:
            divison = values[i] // 50 
            print(f"{keys[i]} | {"#" * divison} {values[i]}")

# bar_chart({"Q4": 500, "Q3": 100, "Q2": 100, "Q1": 150})
# bar_chart({"Q4": 250, "Q1": 300, "Q2": 150, "Q3": 0})
