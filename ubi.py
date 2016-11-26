from slacker import Slacker
import time
import websocket as websockets
import json
import sys
import math

def check_format(string):
    allowed = ['0','1', '2', '3', '4', '5', '6', '7', '8', '9', '*', '^', '%', '/', '+', '-', '.', ' ']
    nums = ['0','1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['+', '-', '*', '/', '^', '%', '.', ' ']
    math_symbols = ['+', '-', '*', '/', '^', '%']
    i = 0
    while i > len(string):
        if i != len(string):
            if string[i] in symbols and string[i + 1] in symbols:
                print('error1')
                return False
        if string[i] not in allowed:
            print('error2')
            return False
        if string[i] in math_symbols:
            if string[i - 1] != " " or string[i + 1] != " ":
                if string[i] != "-":
                    print('error3')
                    return False
                elif string[i - 1] != " " or string[i + 1] not in nums:
                    print('error3')
                    return False
        i += 1
    return True
def check_answer(string):
    if len(string) > 23:
        i = 0
        current = ''
        while i != 23:
            current += string[i]
            i += 1
        return current
    else:
        return "NAN"
def check_calc(string):
        i = 24
        current = ""
        while i < len(string):
            current += string[i]
            i += 1
        print(current)
        if check_format(current):
            return [True, current]
        else:
            return [False]

def make_array(p):
    all_operators = ['+', '-', '/', '*', '%', '^']
    i = 0
    current_num = ''
    new_list = []
    while i < len(p):
        if p[i] != ' ':
            current_num += str(p[i])
        else:
            new_list.append(float(current_num))
            current_num = ''
            i += 1
            new_list.append(p[i])
            i += 1
        i += 1
    new_list.append(float(current_num))
    return new_list


def solve_super_superior(li):
    i = 0
    cached_list = li
    so = ['^']
    while '^' in cached_list:
        if cached_list[i + 1] in so:
            if cached_list[i + 1] == '^':
                num1 = cached_list[i]
                num2 = cached_list[i + 2]
                cached_list.pop(i)
                cached_list.pop(i)
                cached_list.pop(i)
                cached_list.insert(i, num1 ** num2)
        if len(cached_list) > i + 2:
            if cached_list[i + 1] not in so:
                i += 1
    return cached_list


def solve_superior(li):
    i = 0
    cached_list = li
    so = ['*', '/', '%']
    while '*' in cached_list or '/' in cached_list or '%' in cached_list:
        if cached_list[i + 1] in so:
            if cached_list[i + 1] == '*':
                num1 = cached_list[i]
                num2 = cached_list[i + 2]
                cached_list.pop(i)
                cached_list.pop(i)
                cached_list.pop(i)
                cached_list.insert(i, num1 * num2)
            elif cached_list[i + 1] == '/':
                num1 = cached_list[i]
                num2 = cached_list[i + 2]
                cached_list.pop(i)
                cached_list.pop(i)
                cached_list.pop(i)
                if num1 != 0 and num2 != 0:
                    cached_list.insert(i, num1 / num2)
                else:
                    cached_list.insert(i, 1)
            else:
                num1 = cached_list[i]
                num2 = cached_list[i + 2]
                cached_list.pop(i)
                cached_list.pop(i)
                cached_list.pop(i)
                cached_list.insert(i, num1 % num2)
        if len(cached_list) > i + 2:
            if cached_list[i + 1] not in so:
                i += 1
    return cached_list


def solve_inferior(li):
    i = 0
    cached_list = li
    so = ['+', '-']
    while '+' in cached_list or '-' in cached_list:
        if cached_list[i + 1] in so:
            if cached_list[i + 1] == '+':
                num1 = cached_list[i]
                num2 = cached_list[i + 2]
                cached_list.pop(i)
                cached_list.pop(i)
                cached_list.pop(i)
                cached_list.insert(i, num1 + num2)
            else:
                num1 = cached_list[i]
                num2 = cached_list[i + 2]
                cached_list.pop(i)
                cached_list.pop(i)
                cached_list.pop(i)
                cached_list.insert(i, num1 - num2)
        if len(cached_list) > i + 2:
            if cached_list[i + 1] not in so:
                i += 1
    return cached_list


def solve_problem(p):
    starting_list = make_array(p)
    list1 = solve_super_superior(starting_list)
    list2 = solve_superior(list1)
    final_ = solve_inferior(list2)
    return final_[0]

ubi = Slacker('xoxb-92011768359-KRv2gTOT5dNXE3OhSZ8vSEeI')
websocket = websockets.WebSocket()
time_since_1970 = time.time()
time_since_2000 = math.floor(time_since_1970 + 60 * 60 * 24 * 365 * 30)
rtm = ubi.rtm.start().body
botid = rtm['self']['id']
emotions = ["Extremely Depressed", "Depressed", "Very Sad", "Sad", "Ok I guess", "I feel pretty good", "I feel great",
            "I feel awesome", "I feel super awesome!", "Boy im on cloud9"]
websocket.connect(rtm['url'])
users = []
happiness = 5
last = ''
allowBK = False
timer_start = 0
username = "I dunno"
reminder_person = "null"
calc_response = "I would help you, but its in the wrong format"
ubi.chat.post_message("#fn-general", 'Hello Guys! Im Ubi! Nice to meet you all', as_user=True)
def brain():
    try:
        ubi.chat.post_message('#fn-general', 'Somebody reply "Ubi your cool", im sad ):', as_user=True)
    except Exception as e:
        print(e)
check = "NAN"
uncle = "Umm no... iilucky12 is"
father = "Umm no... Enclo is"
grandfather = "Umm no... Mooshoe is"
last_time = time_since_2000
hunger_reply = 'Not Really'
other_hunger_reply = 'Im not hungry actually :P'
last_hunger_switch = 0
while True:
    if happiness < 0:
        try:
            ubi.chat.post_message('#fn-general', 'Bye fiber beta, Im running away to a better slackteam.', as_user=True)
        except Exception as e:
            print(e)
        sys.exit()
    if 10 < happiness:
        happiness = 10
    questions = ["Hi Ubi!", "Whats up Ubi?", "Ubi how are you feeling?", "Ubi are you hungry?", "-feed ubi",
                 "Ubi I am your father", "Ubi I am your grandfather", "Ubi Spam", "Ubi I am your grunkle",
                 "Ubi whats your source code", "Ubi whats the answer to"]
    responses = ["Hello There!", 'The Sky :3', emotions[happiness - 1], hunger_reply, other_hunger_reply,
                 father, grandfather, "Who do you think I am... Enclo-Jr?", uncle, 'This is', calc_response]
    events = websocket.recv()
    events = json.loads(events)
    time_since_1970 = time.time()
    time_since_2000 = math.floor(time_since_1970 + 60 * 60 * 24 * 365 * 30)
    if hunger_reply == 'Not Really':
        other_hunger_reply = 'Im not hungry actually :P'
    if time_since_2000 > last_hunger_switch + 10800:
        if hunger_reply == 'Yes':
            try:
                ubi.chat.post_message("#fn-general", 'Somebody Feed Me, I could eat a whale!', as_user=True)
            except Exception as e:
                print(e)
                time.sleep(1)
            hunger_reply = 'Yes'
            other_hunger_reply = 'Thanks! Im not so hungry anymore'
            last_hunger_switch = time_since_2000
        if hunger_reply == 'Not Really':
            try:
                ubi.chat.post_message("#fn-general", 'Umm hey guys, I could use a snack', as_user=True)
            except Exception as e:
                print(e)
                time.sleep(1)
            hunger_reply = 'Yes'
            other_hunger_reply = 'Thanks! Im not so hungry anymore'
            last_hunger_switch = time_since_2000
    if time_since_2000 > last_time + 900 or allowBK:
        if allowBK is False:
            timer_start = time_since_2000
            brain()
            allowBK = True
        else:
            if 'type' in events and events['type'] == 'message' and events['text'] == 'Ubi your cool':
                ubi.chat.post_message(events['channel'], 'Thanks, I feel much better now', as_user=True)
                allowBK = False
                last_time = time_since_2000
                happiness += 1
            elif time_since_2000 > timer_start + 60:
                ubi.chat.post_message("#fn-general", 'You guys never listen ):', as_user=True)
                allowBK = False
                last_time = time_since_2000
                happiness -= 1
    if events['type'] == 'message' and 'type' in events:
        try:
            check = check_answer(events['text'])
        except Exception:
            print(Exception)

    if events['type'] == 'message' and 'type' in events and events['text'] in questions or check in questions:
        for user in rtm["users"]:
            if user["id"] == events["user"]:
                username = user["name"]
                print(username)
        try:
            last = events['text']
            print(events['text'])
            check = check_answer(events['text'])
        except Exception:
            print(Exception)
        if check == "Ubi whats the answer to":
            index = questions.index('Ubi whats the answer to')
        else:
            index = questions.index(events['text'])
        if events['text'] == "-feed ubi":
            last_hunger_switch = time_since_2000
            hunger_reply = "Not Really"
        if events['text'] == "Ubi I am your father":
            if username == "enclo":
                father = "I already know that dad :P"
                happiness += 1
            elif username == "mooshoe":
                father = "Lol grandpops"
                happiness += 1
            elif username == "iilucky12":
                father = "Grunkle, you never fail to make me laugh"
                happiness += 1
            else:
                father = "Umm no... Enclo is"
                happiness -= 1
        if events['text'] == "Ubi I am your grandfather":
            if username == "mooshoe":
                grandfather = "I know that grandpops"
                happiness += 1
            elif username == "enclo":
                grandfather = "Dad your silly :D"
                happiness += 1
            elif username == "iilucky12":
                grandfather = "Lol grunkle, good one"
                happiness += 1
            else:
                grandfather = "Umm no... Mooshoe is"
                happiness -= 1

        if events['text'] == "Ubi I am your grunkle":
            if username == "iilucky12":
                uncle = "wazzup grunkle"
                happiness += 1
            elif username == "enclo":
                uncle = "man dad, you have the weirdest kind of humor"
                happiness += 1
            elif username == "mooshoe":
                uncle = "Ur silly grandpapops"
                happiness += 1
            else:
                uncle = "Umm no... iilucky12 is"
                happiness -= 1
        if check == "Ubi whats the answer to":
            original = check_calc(events['text'])
            if original[0] == True:
                print("1")
                try:
                    calc_response = 'Its ' + str(solve_problem(original[1]))
                except Exception:
                    calc_response = 'I would tell you, but thats in the wrong format'
            elif original[0] == False:
                print("2")
                calc_response = 'I would tell you, but thats in the wrong format'
        if events['text'] == "Ubi whats your source code":
            ubi.files.upload(file_="ubiNova.py", content="Source Code", filetype="python", filename= "Source Code",
                             channels="#fn-general")
            print("shared")
        try:
            questions = ["Hi Ubi!", "Whats up Ubi?", "Ubi how are you feeling?", "Ubi are you hungry?", "-feed ubi",
                         "Ubi I am your father", "Ubi I am your grandfather", "Ubi Spam", "Ubi I am your grunkle",
                         "Ubi whats your source code", "Ubi whats the answer to"]
            responses = ["Hello There!", 'The Sky :3', emotions[happiness - 1], hunger_reply, other_hunger_reply,
                         father, grandfather, "Who do you think I am... Enclo-Jr?", uncle, "This Is", calc_response]
            ubi.chat.post_message(events["channel"], responses[index], as_user=True)
        except Exception as e:
            print(e)
        time.sleep(1)
