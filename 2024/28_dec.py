def interview(input_lst, taken_time):
    attempt_questions = 0
    total_time = 0
    for i in input_lst:
        attempt_questions += 1
        total_time += i
    total_time += 20 #Interview buffer time
    
    if(attempt_questions == 8 and total_time <= 120 and taken_time <= 120):
        return "qualified"
    else:
        return "disqualified"

# print(interview([5, 5, 10, 10, 15, 15, 20, 20], 120))
# print(interview([2, 3, 8, 6, 5, 12, 10, 18], 64))
# print(interview([5, 5, 10, 10, 25, 15, 20, 20], 120))
# print(interview([5, 5, 10, 10, 15, 15, 20], 120))
# print(interview([5, 5, 10, 10, 15, 15, 20, 20], 130))

#Binary search algorithms
primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
def is_prime(primes, n):
    left, right = 0, len(primes) - 1

    while(left <= right):
        mid = (left + right) // 2
        if(primes[mid] == n):
            return "yes"
        elif(primes[mid] < n):
            left = mid + 1
        else:
            right = mid - 1
    return "no"

# print(is_prime(primes, 3))
# print(is_prime(primes, 36))



            



