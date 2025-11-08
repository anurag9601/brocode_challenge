def farey(n, combination_list = []):
    def return_list_in_ascending_order(operation_list):
        #Using selection sorting
        for i in range(len(operation_list)):
            min_num , min_den = operation_list[i].split("/")
            min = int(min_num) / int(min_den)
            for j in range(i + 1, len(operation_list) - 1):
                curr_num , curr_den = operation_list[j].split("/")
                curr = int(curr_num) / int(curr_den)
                if min > curr:
                    operation_list[i],operation_list[j] = operation_list[j],operation_list[i]
                    min_num , min_den = operation_list[j].split("/")
                    min = int(min_num) / int(min_den)
        return operation_list


    def remove_dupicate(operation_list):
        clean_list = []

        for operation in operation_list:
            if operation not in clean_list:
                clean_list.append(operation)
        return clean_list

    if(n == 0):
        return return_list_in_ascending_order(remove_dupicate(combination_list))

    else:
        for i in range(n + 1):
            combination_list.append(f"{i}/{n}")
        return farey(n - 1, combination_list)

# print(farey(4))

class time_slot_of_start_time_end_time():
    def __init__(self, start_time, end_time, slot_gap):
        self.start_time = start_time
        self.end_time = end_time
        self.slot_gap = slot_gap
        self.slots = self.generate_time_slots()

    def time_in_min(self, time):
        hour, minute = time.split(":")
        return (60 * int(hour)) + int(minute)
    
    def convert_min_in_24_hour_format(self, minute):
        minutes = minute % 60
        hours = minute // 60
        return f"{hours:02}:{minutes:02}"

    def generate_time_slots(self):
        time_slots = []

        start_time_in_min = self.time_in_min(self.start_time)
        end_time_in_min = self.time_in_min(self.end_time)

        while(start_time_in_min <= end_time_in_min):
            if start_time_in_min + self.slot_gap <= end_time_in_min:
                curr_slot_start_time = self.convert_min_in_24_hour_format(start_time_in_min)
                curr_slot_end_time = self.convert_min_in_24_hour_format(start_time_in_min + self.slot_gap)
                time_slots.append(f"{curr_slot_start_time}-{curr_slot_end_time}")
            start_time_in_min += self.slot_gap
        return time_slots
    
# generated_time_slots = time_slot_of_start_time_end_time("10:00", "22:00", 45)
# print(generated_time_slots.slots)    