import sys, random, os, math, atexit, signal, re
#figure out terminal colouring later
import time as t
#try:
#    from sound import play_sound
#except Exception as e:
#    print(e)
from multiprocessing import Process
from threading import Thread
from playsound import playsound

#shift + numpad 0 to fix block cursor issue


#py -m PyInstaller "C:\Users\Sam Knight\OneDrive\Documents\Coding\beyondbelief\beyondbelief.py"
#py -m PyInstaller "C:\Users\Sam Knight\OneDrive\Documents\Coding\beyondbelief\beyondbelief.py" --add-data="C:\Users\Sam Knight\OneDrive\Documents\Coding\beyondbelief\sound.py":main

music = Process()
current_song = 0
songs = {
    "home": "einekleine.wav",
    "walking": "bachprelude3.wav",
    "school": "mozart9_1.wav",
    "luna": "lovesorrow.wav",
    "action": "bachaminorconcerto.wav",
    "action2": "crybaby.wav",
    "creative": "origdmajor.wav",
    "jazzy": "universe.wav",
    "jovial": "mozartvconcerto3_1.wav",
    "goofy": "buddyholly.wav",
    "debate": "scriabinetude8_12.wav",
    "chase": "chopin10_4.wav",
    "innerthought": "chopin25_5.wav",
    "resolved": "shukumei.wav",
    "grand": "rach2.wav",
    "intimidating": "rachprelude5.wav"
}

class Player:
    typing_speed = 60 #wpm
    name = " "
    current_line = 0
    chapter = 1
    luna_opinion = 0

chars = {   #add more chars when needed
    "main": Player.name,
    "luna": "Luna",
}


attr_names = [
    "typing_speed",
    "name",
    "current_line",
    "chapter",
    "luna_opinion",
]
    
title_card = [
    "*                                                                **         *                  ***                          ***   ",
    "**                                                                **      **                    ***      *                ** ***  ",
    "**                                                                **      **                     **     ***              **   *** ",
    "**                                                                **      **                     **      *               **       ",
    "**                   **   ****         ****                       **      **                     **                      **       ",
    "** ****       ***     **    ***  *    * ***  * ***  ****      *** **      ** ****       ***      **    ***        ***    ******   ",
    "*** ***  *   * ***    **     ****    *   ****   **** **** *  *********    *** ***  *   * ***     **     ***      * ***   *****    ",
    "**   ****   *   ***   **      **    **    **     **   ****  **   ****     **   ****   *   ***    **      **     *   ***  **       ",
    "**    **   **    ***  **      **    **    **     **    **   **    **      **    **   **    ***   **      **    **    *** **       ",
    "**    **   ********   **      **    **    **     **    **   **    **      **    **   ********    **      **    ********  **       ",
    "**    **   *******    **      **    **    **     **    **   **    **      **    **   *******     **      **    *******   **       ",
    "**    **   **         **      **    **    **     **    **   **    **      **    **   **          **      **    **        **       ",
    "**    **   ****    *   *********     ******      **    **   **    **      **    **   ****    *   **      **    ****    * **       ",
    " *****      *******      **** ***     ****       ***   ***   *****         *****      *******    *** *   *** *  *******  **       ",
    "  ***        *****             ***                ***   ***   ***           ***        *****      ***     ***    *****    **      ",
    "                        *****   ***                                                                                               ",
    "                     ********  **                                                                                                 ",
    "                    *      ****                                                                                                   ",
]

c1_card = [
    "             *                                                                                                   ",
    "           **                                  *                                                                 ",
    "           **                                 **                                                                 ",
    "           **                                 **                                                                 ",
    "           **                      ****     ********           ***  ****          ****                           ",
    "   ****    **  ***      ****      * ***  * ********     ***     **** **** *      * ***  * ***  ****       ***    ",
    "  * ***  * ** * ***    * ***  *  *   ****     **       * ***     **   ****      *   ****   **** **** *   * ***   ",
    " *   ****  ***   ***  *   ****  **    **      **      *   ***    **            **    **     **   ****   *   ***  ",
    "**         **     ** **    **   **    **      **     **    ***   **            **    **     **    **   **    *** ",
    "**         **     ** **    **   **    **      **     ********    **            **    **     **    **   ********  ",
    "**         **     ** **    **   **    **      **     *******     **            **    **     **    **   *******   ",
    "**         **     ** **    **   **    **      **     **          **            **    **     **    **   **        ",
    "***     *  **     ** **    **   *******       **     ****    *   ***            ******      **    **   ****    * ",
    " *******   **     **  ***** **  ******         **     *******     ***            ****       ***   ***   *******  ",
    "  *****     **    **   ***   ** **                     *****                                 ***   ***   *****   ",
    "                  *             **                                                                               ",
    "                 *              **                                                                               ",
    "                *                **                                                                              ",
    "               *                                                                                                 ",
]

stall_log = [
    "Are you gonna play the game or not?",
    "You're here for a game, aren't you?",
    "Is this appealing for you?",
    "Really?",
    "Why?",
    "There's a good game here, you know.",
    "Good content.",
    "Mid programming.",
    "Bad writing.",
    "You could disagree if you played the game.",
    "...",
    "Fine.",
    "No more entertainment for you.",
]

##############################################################################################################
##############################################################################################################



#################################################################################################################
#################################################################################################################

def slow_type(sentence, sleep=1, dialogue=False, color="purple"):
    dims = list(os.get_terminal_size())
    spacing = math.floor((dims[0]-len(sentence))/2)
    for space in range(0, spacing):
        print(' ', end='')
    for char in sentence:
        #sys.stdout.write(colored(f'{char}', color))
        if dialogue == True:
            sys.stdout.write(f'{char.upper()}')
        else:
            sys.stdout.write(f'{char}')
        sys.stdout.flush()
        t.sleep(random.random()*10.0/(Player.typing_speed))
    t.sleep(sleep)  #variable sleep between every statement
    print ('')

def set_resolution(y_dis=0):
    os.system('cls||clear')
    dims = list(os.get_terminal_size())
    y_dis = math.floor(dims[1]/2)-2-y_dis
    for line in range(0, y_dis):
        print()

def sound_check(current_song, term=False):
    global music
    if play_music == False:
        #print("Music isn't turned on.")
        return 0
    try:
        if term == True:
            #print("here")
            music.terminate()
            #music.join()
        try:
            if music.is_alive():
                pass
            else:
                #print("here mus 1")
                #t.sleep(2)
                music = Process(target=playsound, daemon=True, args=[str("sounds/"+current_song)])
                music.start()
                #print("here mus 3")
                #t.sleep(2)
        except UnboundLocalError as e:
            #print("here mus 2")
            #print(e)
            #t.sleep(2)
            music = Process(target=playsound, daemon=True, args=[str("sounds/"+current_song)])
            music.start()
    except Exception as e:
        #print(e)
        #t.sleep(20)
        #print("Your music isn't installed.")   # if music isn't installed
        pass

def settings():
    global typing_speed
    while True:
        try:
            print()
            speed = int(input(f"Enter word speed (default is 60, range 20-120, current is {Player.typing_speed}): ".rjust(list(os.get_terminal_size())[0]//2)))
            print()
            if speed < 20:
                slow_type("That is below the minimum of 20.")
            elif speed > 120:
                slow_type("That is above the maximum of 120.")
            else:
                Player.typing_speed = speed
                slow_type(f"Set typing speed to {Player.typing_speed}.")
                print()
                break
        except:
            print()
            slow_type("Your input isn't valid.")

def saving():
    if os.path.isfile("save.txt"):
        os.remove("save.txt")
    file = open("save.txt", "w")
    for param in range(0, len(attr_names)):
        file.write(str(getattr(Player, attr_names[param]))+"\n")
    file.close()
    t.sleep(2)

def load_game():
    file = open("save.txt", "r")
    lines = file.readlines()
    for line in range(0, len(lines)):
        data = lines[line].split()
        if line == 1:   #special exception for name cuz im tired of making expandable systems for now
            Player.name = str(data[0])
        else:
            exec_line = f'Player.{attr_names[line]} = {int(data[0])}'
            exec(exec_line)

def if_load_exists():
    return os.path.exists("save.txt")

def load_chapter():
    while True:
        match Player.chapter:
            case 1:
                chapter_1()
                content_finish()
                break
            case 2:
                chapter_2()
            case 3:
                chapter_3()

def name_chr():
    global Player
    set_resolution(5)
    slow_type("What would you like to name your character? (only lowercase/uppercase letters)")
    slow_type(" ", 0.05)
    while True:
        name = input("name -> ".rjust(list(os.get_terminal_size())[0]//2)).strip()
        if re.findall("[a-zA-Z]", name):
            if "luna" in name.lower():
                slow_type(" ", 0.05)
                slow_type("No.")
                slow_type(" ", 0.05)
            else:
                Player.name = name
                #print(Player.name)
                break
        else:
            slow_type("Your name must only contain lowercase or uppercase letters.")

###################################################################################################################
###################################################################################################################

def title_card_menu(loaded_game):
    stall_val = 0
    set_resolution(15)
    for line in title_card: #tempered version of the slow type algorithm
        dims = list(os.get_terminal_size())
        print(f'{line: ^{dims[0]}}')
        t.sleep(random.random()*10.0/50)
    t.sleep(3)
    #print(loaded_game)
    for temp in range(0, 5):    #prints new lines
        print()
    if loaded_game == False: #finish the loaded game case
        slow_type("New game, settings, or quit?")
        while True:
            print()
            choice = input("(ng/settings/quit): ".rjust(list(os.get_terminal_size())[0]//2)).strip().lower()    #i stole this ehe, it has to redo dims if you changed the size
            match choice:   #anything not based on slow_type has to adapt to dimensions
                case "ng":
                    print()
                    slow_type("Beginning Chapter 1...", sleep=2)
                    load_chapter()
                    #content_finish()
                    break
                case "quit":
                    print()
                    slow_type("Quitting...", sleep=1)
                    exit()
                case "settings":
                    settings()
                    slow_type("New game, settings, or quit?")
                case _:
                    if stall_val >= 10:
                        try:
                            slow_type(stall_log[stall_val-10], sleep=2)
                            stall_val += 1
                        except:
                            pass
                    else:
                        slow_type("...", sleep=2)
                        stall_val += 1
    elif loaded_game == True:
        slow_type("Load game, new game, settings, or quit?")
        while True:
            print()
            choice = input("(lg/ng/settings/quit): ".rjust(list(os.get_terminal_size())[0]//2)).strip().lower()    #i stole this ehe, it has to redo dims if you changed the size
            match choice:   #anything not based on slow_type has to adapt to dimensions
                case "lg":
                    print()
                    slow_type("Loading game...")
                    load_game()
                    load_chapter()
                    break
                    #content_finish()
                case "ng":
                    print()
                    slow_type("Beginning Chapter 1...", sleep=2)
                    try:
                        os.remove("save.txt")
                    except:
                        pass
                    load_chapter()
                    break
                    #content_finish()
                case "quit":
                    print()
                    slow_type("Quitting...", sleep=1)
                    exit()
                case "settings":
                    settings()
                    slow_type("Load game, new game, settings, or quit?")
                case _:
                    if stall_val >= 10:
                        try:
                            slow_type(stall_log[stall_val-10], sleep=2)
                            stall_val += 1
                        except:
                            pass
                    else:
                        slow_type("...", sleep=2)
                        stall_val += 1

def chapter_1():
    global current_song
    set_resolution(9)
    for line in c1_card: #tempered version of the slow type algorithm
        dims = list(os.get_terminal_size())
        print(f'{line: ^{dims[0]}}')
        t.sleep(random.random()*10.0/50)
    t.sleep(1)
    slow_type("A solitary beginning", sleep=2)
    if Player.current_line == 0:
        current_song = songs["home"]
    for item in range(Player.current_line, len(c1_content)):
        sound_check(current_song)
        #print(Player.name)
        if type(c1_content[item]) != str:
            set_resolution(c1_content[item])
        else:
            if c1_content[item] == "name_chr()":    #i know its bad okay stop laughing
                name_chr()
            elif c1_content[item] == " ":
                slow_type(c1_content[item], 0.01)
            elif c1_content[item] == "save":
                saving()
            elif c1_content[item].split()[0] == "change":
                print(songs[str(c1_content[item].split()[1])], c1_content[item])
                print(play_music)
                t.sleep(2)
                current_song = songs[str(c1_content[item].split()[1])]
                print(current_song)
                sound_check(current_song, True)
                sound_check(current_song)   #it waits till another to redo the song, so do it twice
                #print("here 2")
            elif c1_content[item].split()[0] == "*":
                #print(Player.name)
                chars["main"] = Player.name
                #print(chars["main"], Player.name)
                slow_type(chars[c1_content[item].split()[1]], 0, True)
            elif c1_content[item][-1] == "$":
                slow_type(c1_content[item[0:-1]], 3)
                #Player.current_line += 1
            elif c1_content[item][-1] == "£":
                slow_type(c1_content[item[0:-1]], 0.4)
                #Player.current_line += 1
            else:
                slow_type(c1_content[item])
        Player.current_line += 1 

def chapter_2():
    pass

def chapter_3():
    pass

def content_finish():
    set_resolution(2)
    slow_type("That is the end of the demo.")
    slow_type(" ", 0.05)
    slow_type("I hope you enjoyed.")
    slow_type(" ", 0.05)
    slow_type("More coming soon!")
##############################################################################################################################
##############################################################################################################################

c1_content = [    #ALWAYS put saves before change resolution
    1,
    "I woke to an alarm clock blaring on a warm spring day.",
    5,
    "The sun shone through the small gaps in my closed blinds.",
    " ",
    "The ambience of a few vehicles and some people walking quietly filled my ears.",
    #"change jazzy",    #ALWAYS put change music before spaces
    " ",
    "I slammed the alarm clock with an absent-minded arc of the arm.",
    " ",
    "It fell on the floor and kept blaring, a little muted now.",
    " ",
    "I sighed with frustration as I forced myself to lean up.",
    "name_chr()",
    "save", #ALWAYS put saves before change resolution
    2,
    "* main",    #dont use spaces between character dialogue
    "'Ugh...'",
    " ",
    "I suspected the demo was about to end."
]

# dollar sign used for a long sleep, pound for short sleep
        
#every time you need to add 2 line (plus 1) (2n+1) you decrease the displacement by 1 (n), from math.floor(dims[1]/2)-2
#eg 1dis -> 1-3lines, 2dis -> 3-5lines, 3dis -> 5-7 lines, etc

#atexit.register(saving)
os.system("title " + "Beyond Belief")
if __name__ == '__main__':
    if os.path.isfile(f'sounds/einekleine.wav'):
        play_music = True
        #print("it exists???")
        #t.sleep(5)
    else:
        #print("it doesn't exist???")
        #t.sleep(5)
        play_music = False
    state = if_load_exists()
    os.system('cls||clear')
    title_card_menu(state)
    t.sleep(20)