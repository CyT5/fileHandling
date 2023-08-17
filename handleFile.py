while True:
    fname = input("Which file you are interested in?\n")
    try:
        fhand = open(fname)
    except:
        print(f"Invalid file name: {fname}")
        quit()
    
    action = input("Would you like to read the file or count the lines that are in the file?\n").lower()
    lineCount = 0

    if action == "count":
        for line in fhand:
            lineCount +=1
        else:
            print(lineCount)
    elif action == "read":
        for line in fhand:
            line = line.rstrip()
            print(line)
    else:
        print("Invalid action.")
        again = input("Would you like to play again? (y/n)\n").lower()
        if again == "y":
            continue
        else:
            break

    again = input("Would you like to run this program again? (y/n)\n").lower()
    if again == "y":
        continue
    else:
        break