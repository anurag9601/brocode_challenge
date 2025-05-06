def mine_run(run_list):
    speed_up = 2.67
    slow_down = 2.67
    un_power = 1

    speed = 0

    if run_list[0][0] == "-" and run_list[0][-1] == ">":
        speed += speed_up
    else:
        return 0
    
    for i in range(1, len(run_list)):
        current_run = run_list[i]
        if current_run[0] == "-" and current_run[-1] == ">":
            speed += speed_up
        elif current_run[0] == "<" and current_run[-1] == "-":
            speed -= slow_down
        elif current_run[0] == "-" and current_run[-1] == "-":
            speed -= un_power
        if speed != None and speed <= 0 and i != len(run_list) - 1:
            return i
        
    return True

print(mine_run(["-->", "-->", "-->", "<--", "<--", "<--"]))
print(mine_run(["-->", "<--", "-->", "-->", "<-->", "---"]))
