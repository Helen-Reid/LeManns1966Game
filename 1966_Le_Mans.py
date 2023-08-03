import time
import random
import sys
import webbrowser






# Log in function
def log_in():
    global time
    global username
    while True:
        username = input("Please enter your username: ")
        time.sleep(1)
        password = input("Please enter the password: ")
        
        if password.lower () == "race":
            time.sleep(1)
            print("""
██╗     █████╗  █████╗  ██████╗ ██╗███╗  ██╗ ██████╗
██║     ██╔══██╗██╔══██╗██╔══██╗██║████╗ ██║██╔════╝
██║     ██║  ██║███████║██║  ██║██║██╔██╗██║██║  ██╗
██║     ██║  ██║██╔══██║██║  ██║██║██║╚████║██║  ╚██╗
███████╗╚█████╔╝██║  ██║██████╔╝██║██║ ╚███║╚██████╔╝
╚══════╝ ╚════╝ ╚═╝  ╚═╝╚═════╝ ╚═╝╚═╝  ╚══╝ ╚═════╝ """ + """██╗   
                                                     ╚═╝""")
            time.sleep(3)
            break
        else:
            time.sleep(1)
            print("Wrong Password! Try again")
            time.sleep(1)
log_in()


# Function that delays the prints letter by letter
def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.03)

count = 0

# Video game title visual
def Le_mans():
    global count
    def history_of_le_mans ():
        global hol
        hol = (input ("\n\nWould you like more information on the history of Le Mans race? "))
        if hol.lower () == "yes" or hol.lower () == "y":
            webbrowser.open ("https://www.amazon.co.uk/Mans-Official-History-Greatest-1960-69/dp/0992820952/ref=sr_1_3?crid=1OVJP5MAR7DCD&keywords=%22le+mans+official+book&qid=1679408495&sprefix=le+mans+official+book%2Caps%2C109&sr=8-3")
            webbrowser.open_new_tab ("https://www.youtube.com/watch?v=7rrVOVuwPV0")
            delay_print("\nThank you for playing!")
            quit()
        else:
            delay_print("\nThank you for playing!")
            quit()

    def play_again ():
        global count
        restart = input ("\n\nWould you like to play again? ")
        if restart.lower () == "yes" or restart.lower () == "y":
            time.sleep (2)
            count = 0
            Le_mans ()
            quit ()
        else: 
            count = 0
            history_of_le_mans()
            quit ()
        
    def you_lose ():
        print ("""\033[0;31m

                            ________¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶__________
                            ______¶¶¶¶¶¶_____________¶¶¶¶¶¶________
                            _____¶¶¶¶¶_________________¶¶¶¶¶¶______
                            ____¶¶¶¶_____________________¶¶¶¶¶_____
                            ___¶¶¶¶_______________________¶¶¶¶¶____
                            __¶¶¶¶_____¶¶¶¶_______¶¶¶¶______¶¶¶____
                            __¶¶¶_____¶¶¶¶¶¶_____¶¶¶¶¶¶_____¶¶¶¶___
                            _¶¶¶¶_____¶¶¶¶¶¶_____¶¶¶¶¶¶______¶¶¶___
                            _¶¶¶_______¶¶¶¶_______¶¶¶¶_______¶¶¶¶__
                            _¶¶¶______________________________¶¶¶__
                            _¶¶¶______________________________¶¶¶__
                            _¶¶¶______________________________¶¶¶__
                            _¶¶¶____________¶¶¶¶¶____________¶¶¶¶__
                            _¶¶¶¶________¶¶¶¶¶¶¶¶¶¶¶_________¶¶¶___
                            __¶¶¶______¶¶¶¶¶_____¶¶¶¶¶______¶¶¶¶___
                            __¶¶¶¶____¶¶¶___________¶¶¶____¶¶¶¶____
                            ___¶¶¶¶___¶¶_____________¶¶___¶¶¶¶_____
                            ____¶¶¶¶____________________¶¶¶¶¶______
                            _____¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶_______
                            _______¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶_________


            '||' '|'  ..|''||   '||'  '|'    '||'       ..|''||    .|'''.|  '||''''|
              || |   .|'    ||   ||    |      ||       .|'    ||   ||..  '   ||  .
               ||    ||      ||  ||    |      ||       ||      ||   ''|||.   ||''|
               ||    '|.     ||  ||    |      ||       '|.     || .     '||  ||
              .||.    ''|...|'    '|..'      .||.....|  ''|...|'  |'....|'  .||.....|\x1B[0m""")
        play_again()
        quit ()
        
        
    print("""\033[0;36m
                                                              
                                                             ███    █████╗    █████╗   █████╗
                                                            ████║   ██╔══██  ██╔═══╝  ██╔═══╝
                                                            ██╔██║  ╚██████║ ██████╗  ██████╗
                                                            ╚═╝██║   ╚═══██║ ██╔══██╗ ██╔══██╗
                                                            ███████╗ █████╔╝ ╚█████╔╝ ╚█████╔╝
                                                            ╚══════╝ ╚════╝   ╚════╝   ╚════╝  \x1B[0m""")

    print("""\033[0;36m

                                                ██╗     ███████╗  ███╗   ███╗ █████╗ ███╗  ██╗ ██████╗  
                                                ██║     ██╔════╝  ████╗ ████║██╔══██╗████╗ ██║██╔════╝
                                                ██║     █████╗    ██╔████╔██║███████║██╔██╗██║╚█████╗ 
                                                ██║     ██╔══╝    ██║╚██╔╝██║██╔══██║██║╚████║ ╚═══██╗
                                                ███████╗███████╗  ██║ ╚═╝ ██║██║  ██║██║ ╚███║██████╔╝
                                                ╚══════╝╚══════╝  ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚══╝╚═════╝ 
                                                                                                    \x1B[0m""")



    time.sleep(2)

    # Game starts
    delay_print(f"""\n
Welcome to Le Mans {username.capitalize ()}, this year Ford has decided to join the competition with their new build, \x1B[1;3mTHE FORD GT 40\x1B[0m.
In case you didn't know, this race will go on for 24 hours to test the driver's durability and skills; testing the company's engineering team's composure to the 
limits.
    Will Ford be able to win over the prestigious Ferrari Automobile company?
    There's only one way to find out!
    Drivers, please take your positions...\n\n""")
    time.sleep(3)

    print("""\033[1;31m
         #######  ##    ##    ##    ##  #######  ##     ## ########     ##     ##    ###    ########  ##    ##  ######
        ##     ## ###   ##     ##  ##  ##     ## ##     ## ##     ##    ###   ###   ## ##   ##     ## ##   ##  ##    ##
        ##     ## ####  ##      ####   ##     ## ##     ## ##     ##    #### ####  ##   ##  ##     ## ##  ##   ##
        ##     ## ## ## ##       ##    ##     ## ##     ## ########     ## ### ## ##     ## ########  #####     ######  ####
        ##     ## ##  ####       ##    ##     ## ##     ## ##   ##      ##     ## ######### ##   ##   ##  ##         ## ####
        ##     ## ##   ###       ##    ##     ## ##     ## ##    ##     ##     ## ##     ## ##    ##  ##   ##  ##    ##  ##
         #######  ##    ##       ##     #######   #######  ##     ##    ##     ## ##     ## ##     ## ##    ##  ######  ##  \x1B[0m\n""")
    time.sleep(2)
                                                                                                                                                                                                                                            
                                                                                                                            
    print ("""\033[1;33m
         ######   ######## ########     ######  ######## ######## ####                                                      
        ##    ##  ##          ##       ##    ## ##          ##    ####                                                      
        ##        ##          ##       ##       ##          ##    ####                                                      
        ##   #### ######      ##        ######  ######      ##     ##                                                      
        ##    ##  ##          ##             ## ##          ##                                                     
        ##    ##  ##          ##       ##    ## ##          ##    ####                                                      
         ######   ########    ##        ######  ########    ##    #### \x1B[0m\n""")
    time.sleep(2)                                      

                                                                                                                    
    print ("""\033[1;32m
         ######    #######  #### ####                                                                                       
        ##    ##  ##     ## #### ####                                                                                       
        ##        ##     ## #### ####                                                                                       
        ##   #### ##     ##  ##   ##                                                                                       
        ##    ##  ##     ##                                                                                       
        ##    ##  ##     ## #### ####                                                                                       
         ######    #######  #### ####  \x1B[0m\n""")
    time.sleep(3)



    #First decision
    delay_print("""\nYou start to race towards your vehicle and notice a puddle in your way.
    What do you do?:
    1) Jump over
    2) Go through
    3) Hold back and go around \n""")

    def decision1():
        global count
        answer1 = (input("Choose an option: "))
        if answer1 == "1" or answer1.lower () == "jump over" or answer1.lower() == "jump":
            delay_print("""\nYou trip and fall. Everyone gets ahead of you. You will think again next time before taking a risk.\n""")
            count -= 15
        elif answer1 == "2" or answer1.lower () == "go through":
            delay_print("""\nYou slip and break your ankle. Try again next season!\n""")
            you_lose ()
            quit ()
        elif answer1 == "3" or answer1.lower () == "hold back and go around" or answer1.lower () == "hold back" or answer1.lower () == "go around":
            delay_print("""\nYou chose well, others tried to risk it and failed! Good luck, now go and win the race!\n""")
            count += 25
        else:
            delay_print("\nThis is not an option. Please try again!\n")
            decision1()

    decision1()

    #Second decision
    delay_print("""\nYou are now 3 hours into the race. Due to the hot weather the car's engine in front of you is overheating and is now leaking. The entire road is now slippery 
which could be dangerous. You want to overtake but a corner is coming.
    What do you do?:
    1) Over-take
    2) Wait for the corner \n""")

    def decision2():
        global count
        answer2 = (input("Choose an option: "))
        if answer2 == "1" or answer2.lower () == "overtake" or answer2.lower () == "over-take" or answer2.lower () == "over take":
            delay_print("\n Well done! That was risky but you made it. \n")
            count += 35
        elif answer2 == "2" or answer2.lower () == "wait for the corner" or answer2.lower () == "wait" or answer2.lower () == "wait for corner":
            delay_print("\nThe car's engine stops, causing you to brake and lose time. \n")
            delay_print ("Coach:\033[1;34m\"Rookie move Champ, get your head in the game!\"\x1B[0m\n")
            count -= 5
        else:
            delay_print("\nThis is not a playable option. Please try again!\n")
            decision2()

    decision2()


    #Third decision
    delay_print(f"""\nYou are doing amazing, {username.capitalize ()}! Keep your nerve!
    """)
    delay_print("""\nBut wait, what is that sound? I think it's coming from the front right wheel. The car is also understeering and the balancing is out.
    What should I do?:
    1) Go to pitstop
    2) Continue to accelerate to win time \n""")

    def decision3():
        global count
        answer3 = (input("Choose an option: "))
        if answer3 == "1" or answer3.lower () == "go to pitstop" or answer3.lower () == "pitstop":
            delay_print("""\nGood call, due to intensive use one of the axles was damaged!\n""")
            count += 30
        elif answer3 == "2" or answer3.lower () == "continue to accelerate to win time" or answer3.lower () == "continue to accelerate" or answer3.lower () == "accelerate" or answer3.lower () == "win time":
            delay_print("""\nOh no! The Ford has crashed! The car is in flames. This is the worse accident in the history of Le Mans\n""")
            you_lose ()
            quit()
        else:
            delay_print("\nThis is not a playable option. Please try again!\n")
            decision3()

    decision3()


#Fourth Decision

    delay_print ("""\nNight time is drawing in and you're starting to feel a little tired. With all that excitement, who can blame you?\n""")
    delay_print ("""\n\033[1;34m"Hey Boss, Coach here. Well done dealing with that tyre situation, heart-pounding stuff, huh?
    Listen buddy, you don't look too good. A little more rough on the eyes than usual.
    Do you want to sub?"\x1B[0m

    1. No way! Victory is mine!
    2. A good driver knows when to quit. Get me out of here!
    3. I'll just rest my eyes for a moment, noone will notice  
    """)

    def decision4 ():
            global count
            answer4 = (input("Choose an option: "))
            if answer4 == "1" or answer4.lower() == "no way! victory is mine!" or answer4.lower() == "no way!" or answer4.lower() == "no way" or answer4.lower() == "victory is mine!" or answer4.lower() == "victory is mine":
                delay_print ("\nYour move is a bold one, some might say reckless. Your opponent has made a different choice, can you stand up to fresh blood?\n")
                delay_print ("\nCoach:\033[1;34m\"Just remember kid, on your head be it! WIN THIS THING\"\x1B[0m\n")
                count -= 35
            elif answer4 == "2" or answer4.lower() == "a good driver knows when to quit. get me out of here!" or answer4.lower() == "quit" or answer4.lower() == "get me out of here!" or answer4.lower() == "get me out of here":
                delay_print("\nCoach is pleased with your decision, wise move.\n")
                count += 20
            elif answer4 == "3" or answer4.lower() == "i'll just rest my eyes for a moment, noone will notice" or answer4.lower() == "rest my eyes" or answer4.lower () == "rest eyes":
                delay_print ("""\nUnfortunately, someone did notice...

                Infact, the whole section of front row audience members who are currently being checked by medics and given refunds \x1B[1;3mdefinitely\x1B[0m noticed.

Your racing days are over. \n""")
                you_lose() 
                quit()
            else:
                delay_print ("You have selected an invalid option, please try again:")
                decision4 ()

    decision4 ()

#Fifth Decision

    delay_print ("""\nIt's late in the day and with just 10 laps to go, we're on the final stretch folks. Who will be the winner? It's looking close!\n""")
    delay_print ("""\nYou are making good progress. A quick glance in your rear-view mirror shows a Ferrari driver hot on your tail, what do you do?

    1. Put the pedal to the metal! Force the engine to 7k RPM
    2. Do not allow the Ferrari driver to over-take
    3. Allow the Ferrari driver to over-take safely \n""")


    def decision5 ():
            global count
            answer5 = (input("Choose an option: "))
            if answer5 == "1" or answer5.lower() == "put the pedal to the metal! Force the engine to 7k RPM" or answer5.lower() == "put the pedal to the metal!" or answer5.lower () == "put the pedal to the metal" or answer5.lower() == "force the engine to 7k RPM" or answer5.lower() == "force the engine":
                delay_print ("\n\x1B[3mGenius\x1B[0m, no-one's seen such machine mastery before! Who knew an engine could maintain such RPM for so long?? YOU DID, that's who!\n ")
                count += 15
            elif answer5 == "2" or answer5.lower() == "do not allow the Ferrari driver to over-take" or answer5.lower () == "do not allow" or answer5.lower() == "do not allow the Ferrari driver to overtake" or answer5.lower () == "do not allow":
                delay_print("""\nDefinitely not a good move, Ferrari attempts the over-take and clips your back tyre.
                You spin out of control and the car bursts into a ball of flames.

                Atleast there's always next year! ....If you can face Coach after this\n""")
                you_lose ()
                quit()
            elif answer5 == "3" or answer5.lower () == "allow" or answer5.lower () == "allow the ferrari driver to over-take" or answer5.lower () == "allow the ferrari driver to overtake" or answer5.lower () == "allow the ferrari driver to over-take safely"or answer5.lower () == "allow the ferrari driver to overtake safely":
                print ("\nYour logic is sound, but your team are now behind. Ferari is gaining time!\n")
                count -= 25
            else:
                delay_print("\nThis is not a playable option. Please try again!\n")
                decision5()

    decision5()
#End 
    delay_print ("""\n"A special thanks to all our drivers competing in today's final race! The winners will be announced shortly.
    Please keep all dogs on leads, exits are located via the foyer. The café on site will remain open for precisely 23 minutes.

    Thank you all for your participation.\"\n\n
    """)
            
    def End_Race ():
        global count
        if count >= 80:
            delay_print (f"In \033[4mFirst place\x1B[0m, with a score of {count} points is Team FORD, with credit to driver {username.capitalize ()}""!")
            print ("""\033[1;33m

                    ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶ 
                    ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶ 
               ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶ 
             ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶ 
            ¶¶¶¶______¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶_______¶¶¶¶ 
            ¶¶¶_______¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶________¶¶¶ 
            ¶¶¶_______¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶________¶¶¶ 
            ¶¶¶_____¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶______¶¶¶ 
            ¶¶¶____¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶_____¶¶¶ 
            ¶¶¶¶___¶¶¶ ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶ ¶¶¶____¶¶¶¶ 
             ¶¶¶¶___¶¶¶_¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶_¶¶¶¶___¶¶¶¶ 
              ¶¶¶¶__¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶___¶¶¶¶ 
                ¶¶¶¶¶¶¶¶ ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶ ¶¶¶¶¶¶¶¶¶ 
                  ¶¶¶¶¶¶  ¶¶¶¶¶¶¶¶¶¶¶¶¶¶  ¶¶¶¶¶¶ 
                           ¶¶¶¶¶¶¶¶¶¶¶¶ 
                             ¶¶¶¶¶¶¶¶ 
                               ¶¶¶¶ 
                               ¶¶¶¶ 
                               ¶¶¶¶ 
                               ¶¶¶¶ 
                           ¶¶¶¶¶¶¶¶¶¶¶¶ 
                        ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶ 
                        ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶ 
                        ¶¶¶            ¶¶¶ 
                        ¶¶¶ 1st Place  ¶¶¶ 
                        ¶¶¶____________¶¶¶ 
                        ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶ 
                        ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶ 
                      ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶ 
                     ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶ \x1B[0m 
                     """)
            time.sleep (1)
            delay_print ("""
\033[1;37mWell done! You made 1st Place! Excellent driving!\x1B[0m 

\033[1;37mI don't think we've seen Coach cry before...\x1B[0m """)
        elif count >= 30 and count <= 79:
            delay_print (f"In \033[4mSecond place\x1B[0m, with a score of {count} points is Team FORD, with credit to driver {username.capitalize ()}! Ferrari have done it again! ")
            print ("""\033[1;30m

                    ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶ 
                    ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶ 
               ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶ 
             ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶ 
            ¶¶¶¶______¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶_______¶¶¶¶ 
            ¶¶¶_______¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶________¶¶¶ 
            ¶¶¶_______¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶________¶¶¶ 
            ¶¶¶_____¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶______¶¶¶ 
            ¶¶¶____¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶_____¶¶¶ 
            ¶¶¶¶___¶¶¶ ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶ ¶¶¶____¶¶¶¶ 
             ¶¶¶¶___¶¶¶_¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶_¶¶¶¶___¶¶¶¶ 
              ¶¶¶¶__¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶___¶¶¶¶ 
                ¶¶¶¶¶¶¶¶ ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶ ¶¶¶¶¶¶¶¶¶ 
                  ¶¶¶¶¶¶  ¶¶¶¶¶¶¶¶¶¶¶¶¶¶  ¶¶¶¶¶¶ 
                           ¶¶¶¶¶¶¶¶¶¶¶¶ 
                             ¶¶¶¶¶¶¶¶ 
                               ¶¶¶¶ 
                               ¶¶¶¶ 
                               ¶¶¶¶ 
                               ¶¶¶¶ 
                           ¶¶¶¶¶¶¶¶¶¶¶¶ 
                        ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶ 
                        ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶ 
                        ¶¶¶            ¶¶¶ 
                        ¶¶¶ 2nd Place  ¶¶¶ 
                        ¶¶¶____________¶¶¶ 
                        ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶ 
                        ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶ 
                      ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶ 
                     ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶ \x1B[0m
                     """)
            time.sleep (1)
            delay_print ("""
            \033[1;37mCongrats! You made 2nd Place!

            Next time you're sure to be golden!\x1B[0m """)
                
        elif count <= 30:
            delay_print (f"In \033[4mThird place\x1B[0m, with a score of {count} points is Team FORD, with credit to driver {username.capitalize ()}! ...Please, no Boo'ing.")
            print ("""\033[0;30m

                    ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶ 
                    ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶ 
               ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶ 
             ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶ 
            ¶¶¶¶______¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶_______¶¶¶¶ 
            ¶¶¶_______¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶________¶¶¶ 
            ¶¶¶_______¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶________¶¶¶ 
            ¶¶¶_____¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶______¶¶¶ 
            ¶¶¶____¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶_____¶¶¶ 
            ¶¶¶¶___¶¶¶ ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶ ¶¶¶____¶¶¶¶ 
             ¶¶¶¶___¶¶¶_¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶_¶¶¶¶___¶¶¶¶ 
              ¶¶¶¶__¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶___¶¶¶¶ 
                ¶¶¶¶¶¶¶¶ ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶ ¶¶¶¶¶¶¶¶¶ 
                  ¶¶¶¶¶¶  ¶¶¶¶¶¶¶¶¶¶¶¶¶¶  ¶¶¶¶¶¶ 
                           ¶¶¶¶¶¶¶¶¶¶¶¶ 
                             ¶¶¶¶¶¶¶¶ 
                               ¶¶¶¶ 
                               ¶¶¶¶ 
                               ¶¶¶¶ 
                               ¶¶¶¶ 
                           ¶¶¶¶¶¶¶¶¶¶¶¶ 
                        ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶ 
                        ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶ 
                        ¶¶¶            ¶¶¶ 
                        ¶¶¶ 3rd Place  ¶¶¶ 
                        ¶¶¶____________¶¶¶ 
                        ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶ 
                        ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶ 
                      ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶ 
                     ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶ \x1B[0m
                     """) 
            time.sleep (1)
            delay_print ("""
                    \033[1;37mYou came in 3rd Place! 

        There's always next season! ...just, maybe, don't mention this to Coach\x1B[0m""")
    End_Race ()

#Easter game
    time.sleep(1)
    def easter_egg ():
        global count2
        count2 = 0
        if count >= 100:
                delay_print("""\n\n\033[0;36mOh you have done it! Who would of thought. Because of this impressive performance I have something interesting for you! AN EASTER EGG
        Let's see your knowledge of the racing world!
            
            Question 1: What team has the most wins in Le Mans history?:
            1) Porsche
            2) Ford
            3) Ferrari\x1B[0m\n""")
        else:
            play_again ()
            quit ()
        def question1 ():
            global count2
            answer1ee = input("Choose an option: ")
            if answer1ee == "1" or answer1ee.lower () == "porsche":
                delay_print("\n\033[0;36mCorrect!\x1B[0m\n")
                count2 += 1
            elif answer1ee == "2" or answer1ee.lower () == "ford":
                delay_print("\n\033[0;36mWrong!\x1B[0m\n")
            elif answer1ee == "3" or answer1ee.lower () == "ferrari":
                delay_print("\n\033[0;36mWrong!\x1B[0m\n")
            else:
                delay_print("\033[0;36mThis is not an option. Please try again!\x1B[0m")
                question1()
        question1()
            
        delay_print("""\033[0;36m
            Question 2: When was the Le Mans race founded?:
            1) 1966
            2) 1923
            3) 1958 \x1B[0m\n""")
        def question2():
            global count2
            answer2ee = input("Choose an option: ")
            if answer2ee == "1" or answer2ee == "1966":
                delay_print("\n\033[0;36mWrong!\x1B[0m\n")
            elif answer2ee == "2" or answer2ee == "1923":
                delay_print("\n\033[0;36mCorrect!\x1B[0m\n")
                count2 += 1
            elif answer2ee == "3" or answer2ee == "1958":
                 delay_print("\n\033[0;36mWrong!\x1B[0m\n")
            else:
                delay_print("\033[0;36mThis is not an option. Please try again!\x1B[0m")
                question2()
        question2()

        delay_print("""\033[0;36m
            Questions 3: What is the legal amount of time a driver can race without stopping according to Le Mans rules?:
            1) 14 Hours
            2) 6 Hours
            3) 10 Hours \x1B[0m\n""")
        def question3():
            global count2
            answer3ee = input("Choose an option: ")
            if answer3ee == "1" or answer3ee == "14" or answer3ee.lower() == "14 hours":
                delay_print("\n\033[0;36mCorrect!\x1B[0m\n")
                count2 += 1
            elif answer3ee == "2" or answer3ee == "6" or answer3ee.lower() == "6 hours":
                delay_print("\n\033[0;36mWrong!\x1B[0m\n")
            elif answer3ee == "3" or answer3ee == "10" or answer3ee.lower() == "10 hours":
                delay_print("\n\033[0;36mWrong!\x1B[0m\n")
            else:
                delay_print("\033[0;36mThis is not an option. Please try again!\n\x1B[0m")
                question3()
                
            delay_print(f"\n\033[0;36mYou have scored {count2} out of 3\x1B[0m\n\n")
            play_again ()
            quit()
        question3()
    easter_egg ()

    play_again()

Le_mans ()

    











