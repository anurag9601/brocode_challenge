def reverse_integer(int):
    temp_int = int if int >= 0 else -int
    reverse_int = 0
    while temp_int != 0:
        lst_dig = temp_int%10
        temp_int = temp_int//10

        #32-bit range 
        #maximum value = 2^31 - 1 = 2147483647
        #minimum value = -2^31 = -2147483647

        if (reverse_int > 2147483647 // 10 or (reverse_int == 2147483647 // 10 and lst_dig > 7)):
            return 0

        if (reverse_int < -2147483648 // 10 or (reverse_int == -2147483648 // 10 and lst_dig < -8)):
            return 0 

        reverse_int = reverse_int * 10 + lst_dig

    if(int < 0):
        return reverse_int * -1
    else:
        return reverse_int

# print(reverse_integer(120))
# print(reverse_integer(-123))

def time_around_word(city_a, timestamp, city_b):
    adding_time = "00:00"

    split_timestamp = timestamp.split(" ")
    time_split = split_timestamp[3].split(":")

    year = split_timestamp[2]
    month = split_timestamp[0]
    day = split_timestamp[1][:-1]
    hour = time_split[0]
    minute = time_split[1]

    cities_time_gap = {
        "Los Angeles" : "-08:00",
        "New York" : "-05:00",
        "Caracas" : "-04:30",
        "Buenos Aires" : "-03:00",
        "London" : "+00:00",
        "Rome" : "+01:00",
        "Moscow" : "+03:00",
        "Tehran" : "+03:30",
        "New Delhi" : "+05:30",
        "Beijing" :"+08:00",
        "Canberra" : "+10:00",
    }

    city_a_time_gap = cities_time_gap[city_a]
    city_b_time_gap = cities_time_gap[city_b]

time_around_word("Los Angeles", "April 1, 2011 23:23", "Canberra")
    