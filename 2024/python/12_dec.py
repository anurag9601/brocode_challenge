def sort_dates(lst, mode):
    format_lst = []

    passed_i = []

    result = []

    for i in lst:
        split_date_time = i.split("_")
        split_date = split_date_time[0].split("-")[::-1]
        split_time = split_date_time[1].split(":")
        format_lst.append(split_date + split_time)
    
    for i in range(len(lst)):
        max_i = -1
        prev_i = -1
        get_result = False
        for j in range(len(format_lst[0])):
            for k in range(len(format_lst)):
                if(k not in passed_i and prev_i > 0):
                    prev_i = k
                    max_i = k
                elif(k not in passed_i):
                    if(format_lst[prev_i][j] > format_lst[k][j]):
                        max_i = prev_i
                        prev_i = k
                        break
                    elif(format_lst[prev_i][j] < format_lst[k][j]):
                        max_i = k
                        prev_i = k
                        break
        passed_i.append(max_i)
        result.append(lst[max_i])

    if(mode == "ASC"):
        return result[::-1]
    else:
        return result

# print(sort_dates(["10-02-2018_12:30", "10-02-2016_12:30", "10-02-2018_12:15"], "ASC"))

# print(sort_dates(["10-02-2018_12:30", "10-02-2016_12:30", "10-02-2018_12:15"], "DSC"))

def time_adjust(string, hr, mint, sec):
    format_time = []

    props_lst = [hr, mint, sec]

    for i in (string.split(":")):
        format_time.append(int(i))

    for j in range(len(props_lst)):
        if(j == 0):
            remain = props_lst[j]//24
            if(remain == 0):
                format_time[j] = format_time[j] + props_lst[j]
        elif(j == 1):
            remain = (props_lst[j] + format_time[j]) //60
            if(remain > 0):
                format_time[0] = format_time[0] + remain
                format_time[j] = (props_lst[j] + format_time[j]) % 60
        elif(j == 2):
            remain = (props_lst[j] + format_time[j]) // 60
            if(remain > 0):
                format_time[1] = format_time[1] + remain
                format_time[j] = (props_lst[j] + format_time[j]) % 60
    
    result = ""
    for i in range(len(format_time)):
        if(format_time[i] == 0):
            result += "00"
            if(i != len(format_time)-1):
                result += ":"
        else:
            str_num = str(format_time[i])
            if(len(str_num) == 1):
                str_num = "0" + str_num
            result += str_num
            if(i != len(format_time)-1):
                result += ":"

    return result

# print(time_adjust("18:22:30", 4, 60, 30))

print(time_adjust("00:00:00", 72, 120, 120))









                

