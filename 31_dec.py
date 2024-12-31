def getRunnerUpScore(arr):
    prev = float("-inf")
    max = float("-inf")
    for i in arr:
        if(i > max):
            prev = max
            max = i
        elif(i < max and i > prev):
            prev = i
    return prev