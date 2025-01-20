index = '''
<html>
<head>
    Hi! I'm a text in the head.
    I probably shouldn't be here.
    <title>edabit.com</title>
</head>
<body>
    Hi! I'm a text in the body.
    <p>This is a parragraph and <a href="https://edabit.com">this is a link</a>.</p>
    Here comes a fake tag: <>.
</body>
</html>
'''

class re:
    def findall(tagTaget, index):
        result = []
        temp = ""
        add_content = False
        for i in index:
            if(i == "<"):
                add_content = True
            if(i == ">"):
                add_content = False
                temp += i
                if(len(temp) > 2):
                    result.append(temp)
                temp = ""
            if(add_content == True):
                if(tagTaget == "opening_tags"):
                    if(len(temp) == 1 and i == "/"):
                        add_content = False
                        temp = ""
                elif(tagTaget == "closing_tags"):
                    if(len(temp) == 1 and i != "/"):
                        add_content = False
                        temp = ""
                temp += i
        return result


# print(re.findall("opening_tags", index))
# print(re.findall("closing_tags", index))
# print(re.findall("all_tags", index))

                    
