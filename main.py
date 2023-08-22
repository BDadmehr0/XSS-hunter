import platform
from colorama import Fore as F

def system_guard():
    sys = platform.system()
    if sys == 'Linux':
        print(F.GREEN+'\nWelcome To XSS-Hunter.\n')
    else:
        print(F.RED+f'\nScript Not Support Your System: {sys}\n')

if __name__ == '__main__':
    system_guard()
