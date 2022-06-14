#!/usr/bin/python3
import hashlib
import getpass
import urllib.request
import argparse
import sys

def process_line(line):
    line_split = line.strip().decode().split(":")
    return (line_split[0], int(line_split[1]))  

if(__name__ == "__main__"):

    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--password", type=str, default=None,help="Password to check. Not passing this option will prompt for password")
    args = parser.parse_args()

    if(args.password is None):
        if(sys.stdin.isatty()):
            passwd = getpass.getpass(prompt="Password: ")
        else:
            passwd = sys.stdin.readline().strip()
    else:
        passwd = args.password

    shahash = hashlib.sha1(passwd.encode()).hexdigest().upper()

    first5chars = shahash[:5]

    with urllib.request.urlopen("https://api.pwnedpasswords.com/range/" + first5chars) as res:
        contents = [process_line(l) for l in res.readlines()]

    for partial_hash, num_occurances in contents:
        full_hash = first5chars + partial_hash
        if(full_hash == shahash):
            if(num_occurances > 1):
                print("That password sucks! It has been seen {:,} times".format(num_occurances))
            else:
                print("That password sucks! It has been seen {:,} time".format(num_occurances))
            exit(1)

    print("Your password does not suck!")
