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






                

