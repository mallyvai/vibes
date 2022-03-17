#!/usr/bin/env python

import sys
import subprocess
import random

successes = '''Success! On this command!
Go get 'em tiger!
Your hair probably smells nice.
This result is successful. Just like you.
Success! I appreciate you.
This command worked. You are loved. 
Nice job getting this working!'''.strip().split('\n')

failures = '''It didn't work. That's okay..
You'll do better next time.
Failure is just the beginning.
Unsuccessful? Take a break. You've earned it.
Fail ten times. Succeed on the 11th.
Sorry it didn't work out, but it'll get better.'''.strip().split('\n')


def main():
    returncode = subprocess.run(sys.argv[1:]).returncode

    if returncode is 0:
        print(random.choice(successes))
    else:
        print(random.choice(failures))
    sys.exit(returncode)


if __name__ == '__main__':
    main()


