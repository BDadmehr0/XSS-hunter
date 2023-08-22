import argparse
import platform
import os
import re
import requests

from core.process import attack
from colorama import Fore as F

def validate_URL(url):
    """Sends a request with a timeout.

    Args:
        url: The URL to send the request to.
        timeout: The timeout in seconds.

        Returns:
        The response object.
    """

    response = requests.get(url, timeout=5)
    return response


def banner():
    ascii_b = F.GREEN+f'''
 __  _____ ___     _  _          _           
 \ \/ / __/ __|___| || |_  _ _ _| |_ ___ _ _  Find XSS Bugs
  >  <\__ \__ \___| __ | || | ' \  _/ -_) '_| github.com/BDadmehr0
 /_/\_\___/___/   |_||_|\_,_|_||_\__\___|_|   V1.0.0\n'''
    print(ascii_b,F.WHITE)

def system_guard():
    sys = platform.system()
    if sys == 'Linux':
        # print(F.GREEN+'\nWelcome To XSS-Hunter.\n')
        pass
    else:
        print(F.RED+f'\nScript Not Support Your System: {sys}\n')
        exit()

def main():
    parser = argparse.ArgumentParser(description='XSS Hunter Script')
    parser.add_argument('-t', "--target-URL", type=str, help='Provide a Target URL exampel: https://www.example.com/?q=')
    args = parser.parse_args()
    url = str(args.target_URL)

    if args.target_URL:
        res = str(validate_URL(url=url))
        if res == '<Response [200]>':
            # print(f"{url} is a standard URL.")
            a = attack(input_b=url)
            print(a)
        else:
            print(F.RED+f'The request failed with status code {res}.')
    else:
        print(F.RED+'Error: please see HELP with "-h" flag')

if __name__ == '__main__':
    system_guard()
    banner()
    main()

