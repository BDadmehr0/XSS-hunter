import argparse
import platform
import os
from colorama import Fore as F


def banner():
    os.system('clear')
    ascii_b = f'''
 __  _____ ___     _  _          _           
 \ \/ / __/ __|___| || |_  _ _ _| |_ ___ _ _  Find XSS Bugs
  >  <\__ \__ \___| __ | || | ' \  _/ -_) '_| github.com/BDadmehr0
 /_/\_\___/___/   |_||_|\_,_|_||_\__\___|_|   V1.0.0\n'''
    print(ascii_b,F.WHITE)

def system_guard():
    sys = platform.system()
    if sys == 'Linux':
        print(F.GREEN+'\nWelcome To XSS-Hunter.\n')
    else:
        print(F.RED+f'\nScript Not Support Your System: {sys}\n')

def main():
    parser = argparse.ArgumentParser(description='XSS Hunter Script')
    parser.add_argument('-d', metavar='URL', help='Provide a URL')
    args = parser.parse_args()

if __name__ == '__main__':
    system_guard()
    banner()
    main()

