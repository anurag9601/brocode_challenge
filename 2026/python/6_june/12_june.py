# Find the longest consecutive login streak.

def longest_consecutive(date_list):
    longest_chain = 1
    temp_chain = 1
    calc_next_date = ""

    def next_date(curr_date):
        split_date = curr_date.split("-")
        month_days = 31

        year = int(split_date[0])
        month = int(split_date[1])
        date = int(split_date[2])

        if month < 8 and month % 2 != 0 or month == 8:
            month_days = 31
        elif month != 2 and month < 8 and month % 2 == 0:
            month_days = 30
        elif month == 2:
            if ((year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)):
                month_days = 29
            else:
                month_days = 28
        elif month >= 9 and month % 2 != 0:
            month_days = 30
        elif month >= 9 and month % 2 == 0:
            month_days = 31

        if month == 12 and date == month_days:
            year = year + 1

        if date == month_days:
            month += 1
        
        month = month % 12 if month > 12 else month

        date = 1 if date == month_days else date + 1

        return f"{str(year)}-{'0' + str(month) if month < 10 else str(month)}-{'0' + str(date) if date < 10 else str(date)}"
    
    for i in range(1,len(date_list)):
        calc_next_date = next_date(date_list[i - 1])
        if date_list[i] == calc_next_date:
            temp_chain += 1
        else:
            temp_chain = 1

        if longest_chain < temp_chain:
            longest_chain = temp_chain

    return longest_chain

    
# print(longest_consecutive([
#     "2026-06-01",
#     "2026-06-02",
#     "2026-06-04",
#     "2026-06-05",
#     "2026-06-06"
# ]))

# Most frequent word pair

def frequent_word_pair(sentence):
    split_word = sentence.split(" ")

    if len(split_word) == 1:
        return -1
    elif len(split_word) == 2:
        return sentence , 1
    
    most_fre_word_pair = 0
    fre_word_pair_count = 0
    pair_diary = {}
    
    for word_i in range(len(split_word) - 1):
        curr_word_pair = " ".join([split_word[word_i], split_word[word_i + 1]])
        if curr_word_pair in pair_diary.keys():
            pair_diary[curr_word_pair] = pair_diary[curr_word_pair] + 1
        else:
            pair_diary[curr_word_pair] = 1
        
        if pair_diary[curr_word_pair] > fre_word_pair_count:
            fre_word_pair_count = pair_diary[curr_word_pair]
            most_fre_word_pair = curr_word_pair

    return most_fre_word_pair, fre_word_pair_count

# print(frequent_word_pair("hello"))
# print(frequent_word_pair("hello world"))
# print(frequent_word_pair("i love coding and i love coding every day"))
# print(frequent_word_pair("a a a a"))

# Smart inventory merge

class merge_inventory:
    warehouse_store = {}

    def __init__(self):
        pass

    def warehouse(self, fruit_obj):
        for fruit, fruit_count in fruit_obj.items():
            if fruit in self.warehouse_store.keys():
                self.warehouse_store[fruit] = self.warehouse_store[fruit] + fruit_count
            else:
                self.warehouse_store[fruit] = fruit_count

        return self.warehouse_store
    

# inventory = merge_inventory()

# print(inventory.warehouse({
#     "apple": 10,
#     "banana": 5
# }))

# print(inventory.warehouse({
#     "apple": 8,
#     "orange": 12
# }))

# Message cooldown system problem

def cooldown_check(mess_list):
    mess_record = []
    mess_process_log = []

    for mess_tup in mess_list:
        sec, mess = mess_tup[0], mess_tup[1]

        if mess in mess_record:
            if sec <= 5:
                mess_process_log.append(False)
            else:
                mess_process_log.append(True)
        else:
            mess_record.append(mess)
            mess_process_log.append(True)

    return mess_process_log

"""print(cooldown_check([
    (1, "Hi"),
    (3, "Hi"),
    (7, "Hi")
]))"""


# Find missing ticket numbers

def find_miss_tickets(tickets):
    miss_tickets = []

    for i in range(1, len(tickets)):
        diff = tickets[i] - tickets[i - 1]

        if diff > 1:
            diff_list = [i for i in range(tickets[i - 1] + 1, tickets[i])]
            miss_tickets += diff_list

    return miss_tickets

# print(find_miss_tickets([101, 102, 104, 106, 107]))

# Build a mini search engine

def search_engine(keyword):
    docs = [
        "python is awesome",
        "i love python",
        "javascript and java",
        "python python python"
    ]

    result = []

    for doc in docs:
        if keyword in doc:
            result.append(doc)

    return result

# print(search_engine("python"))

# User session analyzer

def session_analyzer(activity_logs):
    login_data = {}
    session_time = {}

    for log in activity_logs:
        user = log[0]
        action = log[1]
        time = log[2]

        if action.lower() == "login":
            login_data[user] = time
        elif action.lower() == "logout":
            if user in login_data.keys():
                time_diff = int(time) - int(login_data[user])
                if user in session_time.keys():
                    session_time[user] = session_time[user] + time_diff
                else:
                    session_time[user] = time_diff
                del login_data[user]
    
    return session_time

# print(session_analyzer([
#     ("A", "login", 10),
#     ("A", "logout", 20),
#     ("A", "login", 30),
#     ("A", "logout", 50)
# ]))

# Circular queue rotation

def circular_rotation(num_l, rotation_count):

    length = len(num_l)

    rotation_count = rotation_count % length

    return num_l[-rotation_count:] + num_l[:-rotation_count]

# print(circular_rotation([1,2,3,4,5], 2))
