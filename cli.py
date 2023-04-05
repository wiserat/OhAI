from ohbot import *

while True:
    input_move = input("User input: ")
    input_move = input_move.lower()
    input_value = input("Value: ")
    input_value = int(input_value)
    
    match input_move:
        case "exit":
            break
        case "headnod":
            move(HEADNOD, input_value)
        case "headturn":
            move(HEADTURN, input_value)
        case "eyeturn":
            move(EYETURN, input_value)
        case "eyetilt":
            move(EYETILT, input_value)
        case "lidblink":
            move(LIDBLINK, input_value)
        case "toplip":
            move(TOPLIP, input_value)
        case "bottomlip":
            move(BOTTOMLIP, input_value)
        case "say":
            say(input_value)
        case "reset":
            reset()
        case _:
            print("Invalid input")