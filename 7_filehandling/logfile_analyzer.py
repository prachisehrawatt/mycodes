from collections import Counter

import sys
class LogParseError(Exception):
    pass

class LogFileNotFoundError(FileNotFoundError):
    pass

def read_log_file(filename):
    try:
        with open(filename, "r") as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue
                try:

                    p = line.split(maxsplit=3)

                    if len(p) < 4:
                        raise LogParseError("Invalid log format")

                    timestamp = p[0] + " " + p[1]
                    level = p[2]
                    message = p[3]
                    yield timestamp, level, message