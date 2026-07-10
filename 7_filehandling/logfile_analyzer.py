
print("=========LOG FILE ANALYZER PROJECT==========")

class LogParseError(Exception):
    pass

 
#generator func
def read_log(filename):
    try:
        with open(filename, "r") as file:
            for i in file:
                i = i.strip()

                parts = i.split(" ", 3)

                if len(parts) != 4:
                    raise LogParseError("Invalid Log Format")

                date = parts[0]
                time = parts[1]
                level = parts[2]
                message = parts[3]

                timestamp = date + " " + time

                yield timestamp, level, message

    except FileNotFoundError:
        print("File not found.")
        return

    except LogParseError as e:
        print(e)
        return


# Count Log Levels
def count_levels(filename):
    counts = {
        "INFO": 0,
        "WARNING": 0,
        "ERROR": 0,
        "CRITICAL": 0
    }

    total = 0

    for timestamp, level, message in read_log(filename):
        total += 1

        if level in counts:
            counts[level] += 1

    return counts, total


#searching keyword
def search_keyword(filename, keyword):
    print("Keyword Search:", keyword)

    for timestamp, level, message in read_log(filename):
        if keyword.lower() in message.lower():
            print(f"[{timestamp}] {level} : {message}")


#first and last timestamp

def first_last(filename):
    first = ""
    last = ""

    for timestamp, level, message in read_log(filename):

        if first == "":
            first = timestamp
        last = timestamp

    return first, last


# Print Errors
def print_errors(filename):

    print("Errors and Critical Entries")
    for timestamp, level, message in read_log(filename):

        if level == "ERROR" or level == "CRITICAL":
            print(f"[{timestamp}] {level} : {message}")


#MAIN()
def summary(filename):

    counts, total = count_levels(filename)
    first, last = first_last(filename)

    print("LOG FILE ANALYZER")

    print("Total Entries :", total)
    print()

    for level in counts:
        print(level, ":", counts[level])

    print("First Entry :", first)
    print("Last Entry  :", last)

    search_keyword(filename, "Database")

    print_errors(filename)


summary("log.txt")