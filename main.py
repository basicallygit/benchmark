#!/usr/bin/env python3

import subprocess
import sys

def create_command(command: str):
    #command used to fetch the real time spent (user + kernel)
    return "(time " + command + """) 2>&1 | grep real | awk -F " " '{printf $NF}'"""

def usage(argv):
    print(f"Usage: {argv[0]} <command> <amount of times to run> [option number of decimal points to show]")
    exit(0)

def get_time_spent(command: str):
    return subprocess.check_output(create_command(command), shell=True).decode("ascii")

def calculate_average(times: list):
    total = 0.0
    for time in times:
        total += time
    return total / len(times)

def main(argv=sys.argv):
    times = []
    if len(argv) <= 2:
        usage(argv)
    
    dec_points = 5 #default
    if len(argv) >= 4:
        try:
            dec_points = int(argv[3])
        except:
            print("Invalid decimal point count")
            usage(argv)

    count = None
    try:
        count = int(argv[2])
    except:
        print("Invalid count")
        usage(argv)
    
    for i in range(count):
        time = get_time_spent(argv[1])
        times.append((int(time[0]) * 60) + float(time[2:7]))
        print(times)
    print(f"average time taken: {round(calculate_average(times), dec_points)} seconds")


if __name__ == "__main__":
    main()
