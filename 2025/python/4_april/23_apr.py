def generate_nonconsecutive(n):
    if n == 1:
        return "0 1"
    
    result = []
    iterate = (2 ** n) - 1

    for i in range(iterate):
        bin_curr_n = str(bin(i))[2:]
        if "11" not in bin_curr_n:
            result.append(bin_curr_n)
        
    return " ".join(result)

# print(generate_nonconsecutive(3))
