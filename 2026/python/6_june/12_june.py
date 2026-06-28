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

    
print(longest_consecutive([
    "2026-06-01",
    "2026-06-02",
    "2026-06-04",
    "2026-06-05",
    "2026-06-06"
]))


