import sys, random, os, math
import time as t

#py -m PyInstaller (file directory)

typing_speed = 50 #wpm
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

def slow_type(sentence, sleep=1):
    dims = list(os.get_terminal_size())
    spacing = math.floor((dims[0]-len(sentence))/2)
    for space in range(0, spacing):
        print(' ', end='')
    for char in sentence:
        sys.stdout.write(f'{char}')
        sys.stdout.flush()
        t.sleep(random.random()*10.0/typing_speed)
    t.sleep(sleep)  #variable sleep between every statement
    print ('')

def set_resolution(y_dis=0):
    os.system('cls||clear')
    dims = list(os.get_terminal_size())
    y_dis = math.floor(dims[1]/2)-2-y_dis
    for line in range(0, y_dis):
        print()

def title_card_menu():
    stall_val = 0
    set_resolution(15)
    for line in title_card: #tempered version of the slow type algorithm
        dims = list(os.get_terminal_size())
        print(f'{line: ^{dims[0]}}')
        t.sleep(random.random()*10.0/50)
    t.sleep(3)
    for temp in range(0, 5):    #prints new lines
        print()
    slow_type("Begin Chapter 1?")
    while True:
        print()
        choice = input("(y/n): ".rjust(dims[0]//2)).strip().lower()    #i stole this ehe
        match choice:
            case "y":
                slow_type("Beginning Chapter 1...", sleep=2)
                chapter_1()
                break
            case "n":
                slow_type("Oh, right.", sleep=2)
                exit()
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
    set_resolution(9)
    for line in c1_card: #tempered version of the slow type algorithm
        dims = list(os.get_terminal_size())
        print(f'{line: ^{dims[0]}}')
        t.sleep(random.random()*10.0/50)
    t.sleep(3)
    set_resolution(1)
    slow_type("There's nothing here yet >.<", sleep=3)
    
"""
intro_dialogue = [
    1, 
    "I sat at my desk and typed some words on my VS Code window.",
    " ",
    "While usually I had a lot of story ideas to experiment with, this time I was kind of out.",
    2,
    "I knew the purpose of this one was to test iterating through a bunch of dialogue in a list.",
    " ",
    "Of course I needed to set the resolutions and add some blank spaces, but with some ifs in a for loop it should work.",
    " ",
    "Then theoretically I could make a game just using this cool concept.",
    2,
    "In the middle of writing this I realised that I would need to clear the screen every time I reset the resolution.",
    " ",
    "Every little paragraph needed to be a separate point, after all.",
    " ",
    "After this I'd just need to add some interface, and some options.",
    1,
    "Assuming you're seeing this, it worked.$",
    1,
    "BOO£"
]
# dollar sign used for a long sleep, pound for short sleep
def monologue():
    #length 15 lines
    set_resolution(6)
    slow_type("22nd November, 2024. 8:11pm.")
    slow_type(" ")
    slow_type("Ultraclicker was writing this very monologue.")
    slow_type("He was watching 'WHO'S MORE LIKELY TO...?' by PewDiePie.")
    slow_type("But he was also thinking of changing video.")
    slow_type("Only because of his shitty attention span, rather than any disinterest.")
    slow_type(" ")
    slow_type("He thought this concept could make a cool game idea.")
    slow_type("Finally he could make a cool novel game without needing to learn GUI.")
    slow_type("He started watching 'Every TikTok I've Ever Liked' by Markiplier.")
    slow_type("(banger)")
    slow_type("Anyway, what do you think?")
    slow_type("Oh wait, for this to be properly symmetrical the monologue needs to have a length of 2n+1 lines where n is an integer.")
    slow_type("Now it's 14, so I need to say another thing.")
    slow_type("Bye bye!")

def boo():
    set_resolution(1)
    slow_type("BOO")
    t.sleep(2)
        
#every time you need to add 2 line (plus 1) (2n+1) you decrease the displacement by 1 (n), from math.floor(dims[1]/2)-2

slow_type("Hey.")
t.sleep(2)
slow_type("Does this feel cinematic?")
t.sleep(2)
slow_type("Apart from the flashing cursor showing you where you should be...")
t.sleep(2)
slow_type("Do you feel focused on this?")
t.sleep(2)
slow_type("Could this be scary? Spooky scary?")
t.sleep(2)
slow_type("It's dark in here.")
t.sleep(2)
"""
intro_dialogue = []

os.system("title " + "Beyond Belief")
os.system('cls||clear')
title_card_menu()

for item in intro_dialogue:
    if type(item) != str:
        set_resolution(item)
    else:
        if item == " ":
            slow_type(item, 0.01)
        elif item[-1] == "$":
            slow_type(item[0:-1], 3)
        elif item[-1] == "£":
            slow_type(item[0:-1], 0.4)
        else:
            slow_type(item)
t.sleep(20)