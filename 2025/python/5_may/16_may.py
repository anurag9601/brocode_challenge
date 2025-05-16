def staircase(n):
    start_i = n - 1
    end_i = -1
    iterate = -1

    if 0 > n:
        start_i = 0
        end_i = abs(n)
        iterate = 1
        

    for i in range(start_i, end_i, iterate):
        for j in range(abs(n)):
            if j >= i:
                print("#", end="")
            else:
                print("_", end="")
        print()
    
# staircase(3)
# staircase(7)
# staircase(-8)