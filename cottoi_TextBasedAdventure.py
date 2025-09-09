#Isabella Cottone
#cottoi@rpi.edu
#Text based adventure due 9/8
#8/28-1 got eveyrthing functional except quiz. Things to do left is quiz, text animation, polish, extra
#8/28-2 did the quiz so everything functions expect for any bugs... Things to do left is text animation, polish, extra
#8/28-3 got my roomate Savanna to bug test and fixed some bugs and added some text. Things to do left is text animation, polish, extra
#8/29-1 Looked up how to do the txt animation and tested it in another file and put it here. Need to turn all my text into this function now. Things to do left is text animation, polish, extra
#9/1 Andrew playtested no bugs, but some grammer mistakes to fix, and then when adding extra text he suggested i found some bugs with cast spells that would have broken after using a spell in a place it doesnt do anything. Things left to do extra
#9/4 I added a turns count

#words text animation
#https://stackoverflow.com/questions/20302331/typing-effect-in-python
#credit to Jon Vorcak and user12327406 on stack overflow specifically
import sys
import time

def type(words):
    for char in words:
        time.sleep(0.02)
        sys.stdout.write(char)
        sys.stdout.flush()


#info and intro
print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
type("You are a trainee wizard trying to learn some spells. \nUnfortunately, Xarelf (your mentor) keeps using you for menial tasks, so in an effort to learn some real spells (and maybe find some treasure) you have gone to nearby ruins in the forest.\n")
type("You approach the ancient ruins inside a small cave and enter the first room.\n")
type("Type 'actions' to see the actions you can take\n")


#variables
room = "entrance"
vines = True
fountainDry = True
doorLocked = True
fireballUnlocked = False
waterUnlocked = False
unlockUnlocked = False
quizComplete = False
#arson
libraryBurned = False
studyWet = False
turns = 0

#bunch of functions needed
#fireball makes fire and burns vines in cave room also burns any other plants in rooms
def fireball(v, lb):
    type("A fireball forms and blasts the room with heat and flames.\n")

    if room == "cave":
        type("The fire burns the vines revealing a hidden door.\n")
        return False, lb
    #god why do they all want to burn this library i swear if i have to add ANOTHER check for burning a room down
    elif room == "library":
        if lb == False:
            type("You have successfully burnt down the library. \nI wonder what else would burn this well?\n")
            return v, True
        else:
            type("Bro stop burning down the library its already gone\n")
            return v, lb
    elif room == "deep cave":
        type("Sorry rocks and tiles are not affected by fire so therefore you must acually do the puzzle.\n")
        return v, lb
    else:
        return v, lb


#water fills fountain or just splashes
def water(w, sw):
    type("A ball of water forms in front of you before splashing onto the floor.\n")
    if room == "fountain":   
        type("The water fills the empty fountain and the mechanism starts working. A spell scroll is spit out from the top as water flows through it.\n")
        return False, sw
    elif room == "study":
        type("Now all the couches are wet. Great job. Awesome. Love it. Thanks so much.\n")
        return w, True
    else:
        return w, sw

#unlock can be used on the door
def unlock(u):
    if room == "study":
        type("You cast unlock on the door causing a click and the door to creak open.\n")
        return False
    else:
        type("You cast unlock... which does nothing here. Were you trying to unlock like the secrets of the universe or something? Pro tip its 42\n")
        return u

#list of all the actions the player can type to do something, will update auto when they get new action
def actions():
    type("Here is a list of actions you can take: \n\n")
    type("go left\n")
    type("go right\n")
    type("go back\n")
    type("describe\n")
    type("open door\n")
    type("learn spell\n")
    type("cat\n")
#cant ruin the suprise until they are unlocked
    if fireballUnlocked:
        type("cast fireball\n")
    if waterUnlocked:
        type("cast water\n")
    if unlockUnlocked:
        type("cast unlock\n")
    
#ok crazy bug here cant figure out whyyyy but for go left, right, back, and open door i can't use if room == ""?????? like whyyy it works in describe
#anyways can't fix it shrug but i did find a work around with using parameters
#ok never mind it fixed the error but it wont do what i want it to do now uhhhghghghh
#reacserch
#ok so python is stupid and keeps treating these room as new room variables within the function so im gonna have to use return and parameters but thats sooooo mch work arhhgsags
#ok it wasn't that bad just had to use returns alot like everywhere but yay i think it wrks now
def goLeft():

    if room == "entrance":
        type("You go through the tall red door which leads into a room full of statues.\n")
        return "statue"
    elif room == "statue":
        type("You go through the left door which leads into a library.\n")
        return "library"
    else:
        type("You walk left until you bump into the wall and fall on your butt. haha\n")
        return room

def goRight():
    if room == "entrance":
        type("You go through the blue door which leads into a room with a fountain.\n")
        return "fountain"
    elif room == "statue":
        type("You go through the right door which leads to another room with lots of furniture.\n")
        return "study"

    else:
        type("You walk right until you slam your face into the wall. haha\n")
        return room

def goBack():
    if room == "entrance":
        type("To go back is to leave entirely, which is not how you're getting the treasure. So I forbid it.\n")
        return "entrance"
    elif room == "fountain":
        type("You walk back through the blue door into the entrance\n")
        return "entrance"
    elif room == "cave":
        type("You walk back through door into the fountain room\n")
        return "fountain"
    elif room == "deep cave":
        type("You walk back to the first part of the cave\n")
        return "cave"
    elif room == "statue":
        type("You walk back through the red door into the entrance\n")
        return "entrance"
    elif room == "library":
        type("You walk back through the door to the statue room\n")
        return "statue"
    elif room == "study":
        type("You walk back through the door to the statue room\n")
        return "statue"

def openDoor(d):
    #entrance has to be weird cuz 2 doors and also statue room too
    if room == "entrance":
        type("Which one???????\n")
        choice = input("Left or right? ").lower()
        if choice == "left":
            return goLeft()
        elif choice == "right":
            return goRight()
        else:
            type("Thats not a choice dude\n")
            return "entrance"

    elif room == "fountain":
        type("You open the door and walk through to a more cave looking room.\n")
        return "cave"
    
#aw man relised this needs a check if has been found yet 
    elif room == "cave":
        if vines == False:
            type("You open the door and walk further into the cave where it gets dimmer.\n")
            return "deep cave"
        else:
            type("What door? There's no door here.\n")
            return "cave"

#ewwwwww weird choices make code not uniform with everything else noooooo
    elif room == "statue":
        type("Which one???????\n")
        choice = input("Left or right? ").lower()
        if choice == "left":
            return goLeft()
        elif choice == "right":
            return goRight()
        else:
            type("Thats not a choice dude\n")
            return "statue"

#uhggg needs check as well for unlock spell thing
    elif room == "study":
        if doorLocked == False:
            type("You walk through the now unlocked door.\n")
            return "end"
        else:
            type("You try opening the door but it won't move. It seems locked due to the lock on the door.\n")
            return "study"
    else:
        type("There are no doors in front of you.\n")
        return(d)
 

#description of room your in
def describe(q):
    if room == "entrance":
        #two doors
        type("The entrance room of these underground ruins is worn with age filled cracks, moss, and a few missing bricks in the walls. \nYou try to look at the celing but it reaches farther than even the candle light can. \nA tall red door stands on the left and the grand blue one on the right in front of you.\n")
        return q
    elif room == "fountain":
        #unlock scroll in the dry fountain also a new door maybe 2 descriptions for before and after
        if fountainDry:
            type("This room is covered in mold and moss with a medium stone fountain standing in the middle. \nTime has left any water which was once in it evaporated and the fountain dry. \nLooking closer at the top you see a scroll stuck in the spout, but it is stuck unless perhaps you got the fountain working again. \nThere is a door on the other side of the room\n")
            return q
        else:
            type("The water spell from earlier has fixed the fountain, so now it is spewing water in an infinite loop until the water evaporates again. \nThe other door is still there.\n")
            return q
    elif room == "statue":
        #make up clues for quiz using the statue also 2 door
        type("There are many statues in this room some of which you noticed are colored. \nA blue statue is doing the splits, \na yellow one is mid jumping jack, \nthe orange and purple ones are high fiving, \nthe green statue is in some sort of crab pose, \nand finally a red statue seems to be drowning in a solid pool of concrete.\nThere are also two doors in front of you.\n")
    elif room == "cave":
        #lots of vines maybe i need two description sfor after fireball
        if vines:
            type("The cave-ish area has both stalagmites and tites around, and a chill runs up your spine. \nVines have overgrown almost covering an entire wall, while any man-made walls here have mostly collapsed like how walls look after the kool-aid man is done with them.\n")
            return q
        else:
            type("The vines have been completely burnt away releaving that hidden door. \nThe absence of any green now has left the cave quite grey.")
            return q
    elif room == "deep cave":
        #wow a quiz here and a scroll for water maybe 2 descriptions for before and after
        if q == False:
            type("Inside there are symbols on the walls and tiles on the floor. \nIt seems like a matching puzzle with colors. \nThere is also a locked compartment in the wall.\n")
            choice = input("Do you want to try it? Yes or no: ").lower()
            if choice == "yes":
                return quizActivate()
            else:
                return q
        elif waterUnlocked == False:
            type("The compartment is now open thanks to the quiz being solved. \nInside is a scroll.\n")
            return q
        else:
            type("The compartment is now empty. \nThere is nothing left in this room aside from the remains of the puzzle.\n")
            return q
    
    elif room == "study":
        #new door but lock on it looks normals
        if doorLocked == True:
            if studyWet == False:
                type("The study looks like one of the best preserved places yet with probably functional chairs and bookcases. \nThere is a door, however it has a comically large lock on the handle.\n")
                return q
            else:
                type("The study no longer looks like one of the best preserved places because it is soaking wet. \nThere is a door, however it has a comically large lock on the handle.\n")
                return q
        else:
            type("The once locked door is now open. Pro-tip: You should go through it\n")
            return q
    elif room == "library":
        #wow i bet you could learn like fireball here with all th eboooks
        #people want this libray to burn so now i have to add checksssssss argggggg
        if libraryBurned == False:
            type("The library is full of bookshelves some of which still have books on them. \nThe smell of old books permeates the whole room (I wonder why).\n")
            if fireballUnlocked == False:
                type("Perhaps if one was willing to look through these books they might find something magical.\n")
                return q
            else:
                return q
        else:
            type("Piles of ash and smoke is all that remain.\nThe smell of smoke permeates the whole room (I wonder why).\n")
            return q

def quizActivate():
    type("\nThe first picture on the wall shows someone doing the spilts.\n")
    one = input("Do you put the red, yellow, or blue tile in the slot? ").lower()

    if one == "blue":
        type("\nThe second picture on the wall shows a crab-ish contortion.\n")
        two = input("Do you put the green, orange, or yellow tile in the slot? ").lower()

        if two == "green":
            type("\nThe third picture on the wall shows a high five.\n")
            three = input("Do you put the red and yellow or purple and orange tiles in the slots? (RY or PO): ")

            if three == "PO":
                type("\nWith the last two tiles put in place the compartment slides open revealing a scroll.\n")
                return True
            else:
                type("ERRRR wrong\n")
                return False
        else:
            type("ERRRR wrong\n")
            return False
    else:
        type("ERRRR wrong\n")
        return False


#main loop to keep game going
while room != "end":
    type("\n")
    type("You are in the " + room + " room\n")
    action = input("What will you do? ").lower()
#all actions to functions plus nonsense checker

    if action == "cast fireball":
        if fireballUnlocked == True:
            vines, libraryBurned = fireball(vines, libraryBurned)
        else:
            type("heyyyy you shouldn't know that yet\n")

    elif action == "cast unlock":
        if unlockUnlocked == True:
            doorLocked = unlock(doorLocked)
        else:
            type("heyyyy you shouldn't know that yet\n")

    elif action == "cast water":
        if waterUnlocked == True:
            fountainDry, studyWet = water(fountainDry, studyWet)
        else:
            type("heyyyy you shouldn't know that yet\n")

    elif action == "actions":
        actions()
#this is stupid why does python think i want to make a NEW variable of the same name so i have to do these tihngs
    elif action == "describe":
        quizComplete = describe(quizComplete)
    elif action == "go left":
        room = goLeft()
    elif action == "go right":
        room = goRight()
    elif action == "go back":
        room = goBack()
    elif action == "open door":
        room = openDoor(room)
    elif action == "learn spell":

#this could be a function but then i would have to do returns again because python keeps thinking im making new variables when i just want to refrence the original one
        #agrgar need to put cases in for when its not propers line because people do things agrgrag
        #the more i add to tihs the more i either think it would be better as a funciton but then i remember id have to make more returns and parameters and i just dont want to
        if room == "library":
            if fireballUnlocked == False:
                type("The secrets of flame come to you as you read a book. Fireball unlocked.\n")
                fireballUnlocked = True
            else:
                type("The rest of the books are unreadable.\n")

        elif room == "fountain":
            if fountainDry == False:
                if unlockUnlocked == False:
                    type("The mechanisms of locks come to your mind as you read the scroll. Unlock unlocked.\n")
                    unlockUnlocked = True
                else:
                    type("You stare deeply into the rippling water. \nThe rest of the room fades away as you stare even deeper into the dark water. \nIt seems to become dark, darker, yet darker. \nSuddenly, you jolt and everything seems back to normal. \nDespite all this you have not learned another spell.\n")
            else:
                type("Staring deeply into the dry fountain brings no spell to mind.\n")

        elif room == "deep cave":
            if quizComplete == True:
                if waterUnlocked == False:
                    type("You decipher the flow of water as you read the scroll. Create water unlocked.\n")
                    waterUnlocked = True
                else:
                    type("The scroll was used up.\n")
            else:
                type("No matter how hard you stare into those walls, no spell comes to your mind.\n")
        else:
            type("Despite studying the pebbles on the floor and eating the moss, no spell comes to your mind.\n")
    elif action == "cat":
#credit to Felix Lee for making the cat ascii art
#https://www.asciiart.eu/animals/cats
        print("      |\      _,,,---,,_")
        print("ZZZzz /,`.-'`'    -.  ;-;;,_")
        print("     |,4-  ) )-,_. ,\ (  `'-'")
        print("    '---''(_/--'  `-'\_)  Felix Lee ")
    else:
        type("what? huh? idk what that is\n")
    turns += 1
    


#end after loop cutsceen text
type("As you enter the final room you see a large treasure chest in the middle of the room.\n")
choice = input("Do you try to open it? Yes or no? ").lower()

if choice == "yes":
    type("UH OH IT WAS A MIMIC ARGHGRAHG.\n")
    fireOrNot = input("WHAT DO YOU DO???? ").lower()
#apparently people love fire ball too much and i had to add this
    if fireOrNot == "cast fireball":
        type("You cast fireball at the mimic killing it instantly. \nThankfully you have survived this trap and decide to learn your lesson and head back home to your wizard tower apartment.\n")
    else:
        #DEATH WOOOOOOO
        type("OH NOOOO it doesn't work and so ends the story of the poor greedy wizard mentee.\n")
elif choice == "no":
    #good ending
    type("Deciding that the spells you've gained were enough of a prize, or a perhaps a gut feeling, you leave the chest alone and head back to your wizard tower apartment.\n")

type("You completed this adventure in "+ str(turns) + " turns.\n")
type("The End!")