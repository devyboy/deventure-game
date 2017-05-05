# I was really tired and rushed and couldn't give a fuck to make this look good, sorry to whoever is reading this (probably future me)
from time import sleep
from random import randint
from os import system

#########GLOBAL VARIABLES###################
goblinhp = 60
werewolfhp = 100
dragonhp = 200
playerdamdagger = [2,3,4,5]
playerdamsword = [5,6,7,8,9,10]
playerdamrapier = [4,6,8,12,16,20]
difficulty = ''
goblindam = [2,4,6,8,10]
werewolfdam = [5,10,15,20]
dragondam = [10,15,20,25]
hp = 50
mana = 100
armor = 0
bag = { 'gold': 300, 'potion': 1, 'dagger': 1}
hpthresh = 100
choice = None
talked1 = None
gobdead = False
given1 = False
############################################

#Clear screen function (Linux)

def clear():
  system('printf "\033c"')

#Resets variables if you play again

def resetvars():
    global goblinhp
    global hp
    global bag
    global werewolfhp
    goblinhp = 60
    werewolfhp = 100
    dragonhp = 200
    hp = 50
    mana = 100
    armor = 0
    bag = { 'gold': 300, 'potion': 1, 'dagger': 1}
    
#Choose difficulty

def choosediff():
    global difficulty
    print("\nWelcome to Deventure. This is a text based turn style role playing game. Just follow the on screen instructions and enter the number of your choice. Thanks for playing.")
    choice = input("\nChoose a difficulty.\
    \n1. Easy\
    \n2. Medium\
    \n3. Impossible\
    \n: ")
    if choice == '1':
      print("\nEasy difficulty selected...you baby.")
    elif choice == '2':
      print("\nMedium difficulty selected. Have fun.")
    elif choice == '3':
      print("\nImpossible difficulty selected. Good luck, you'll need it.")
    else:
      print("\nPlease select a valid difficulty.")
      choosediff()
    difficulty = choice
    
#End game screen

def gameend():
  print("\nThanks for playing. If you have any feedback just email me at dev@udel.edu. Keep up with further updates at www.udel.edu/~dev/. Please send money.")
  input("\nPress enter to play again.")
  clear()
  resetvars()
  gamestart()

#Checks to see if the goblin is dead

def isdead1():
  return bool(goblinhp <= 0)

#Checks to see if the werewolf is dead

def isdead2():
  return bool(werewolfhp <= 0)

#Checks to see if the dragon is dead

def isdead3():
  return bool(dragonhp <= 0)

#Goblin's attack turn, checks if you're dead after every attack

def goblinturn():
  global hp
  if difficulty == '1':
    attackdmg = (goblindam[randint(0,4)]*1)
  elif difficulty == '2':
    attackdmg = (goblindam[randint(0,4)]*2)
  elif difficulty == '3':
    attackdmg = (goblindam[randint(0,4)]*3)
  print("\nThe goblin attacks you for " + str(attackdmg) + " damage.")
  hp -= (attackdmg-armor)
  if hp <= 0:
    clear()
    print("\nYou have died. You suck (unless this is hard mode) at this game.")
    gameend()
  else:
    combat1()

#Werewolf attack turn

def werewolfturn():
  global hp
  if difficulty == '1':
    attackdmg = (werewolfdam[randint(0,3)]*1)
  elif difficulty == '2':
    attackdmg = (werewolfdam[randint(0,3)]*2)
  elif difficulty == '3':
    attackdmg = (werewolfdam[randint(0,3)]*3)
  print("\nThe werewolf slashes you for " + str(attackdmg) + " damage.")
  hp -= (attackdmg-armor)
  if hp <= 0:
    clear()
    print("\nYou have died. You suck (unless this is hard mode) at this game.")
    gameend()
  else:
    combat1()

#Main combat function for the first area

def combat1():
  global gobdead
  global hp
  global goblinhp
  print("\nYou have "+str(hp)+" health.")
  fight = input("\n1. Attack\
    2. Use potion\n:")
  if fight == '1':
    try:
      if bag['sword'] > 0:
        print("\nYou strike the goblin with your sword for "+str(playerdamsword[randint(0,5)])+" damage.")
        goblinhp -= playerdamsword[randint(0,5)]
        
        sleep(1)
    except KeyError:
      try:
        if bag['rapier'] > 0:
          print("\nYou stab the goblin with your rapier for "+str(playerdamrapier[randint(0,5)])+" damage.")
        goblinhp -= playerdamrapier[randint(0,5)]
      except KeyError:
          print("\nYou strike the goblin with your dagger for "+str(playerdamdagger[randint(0,3)])+" damage.")
          goblinhp -= playerdamdagger[randint(0,3)]
          sleep(1)
          clear()
    if isdead1() is False:
        sleep(1)
        clear()
        goblinturn()
    else:
      clear()
      print("\nThe goblin finally dies and falls to the ground as blood pours from its wounds. You deliver a final blow and decapitate him. Inside the cave you set the kidnapped women free and return to the village with the goblin's head as a trophy.")
      sleep(2)
      gobdead = True
      input("\nPress enter to continue.")
      intown1()
  elif fight == '2':
    if bag['potion'] > 0:
        print("\n40 health restored with potion.")
        bag['potion']-= 1
        hp += 40
        hpbal()
        sleep(1)
        clear()
        combat1()
    else:
        print("\nYou have no more potions!")
        sleep(1)
        clear()
        combat1()
  else:
      print("\nPlease choose an option.")
      combat1()
    
#Displays the player's inventory

def displayinv(inv):
    print("\nInventory:")
    for k, v in inv.items():
        if v > 1:
            if k == 'gold':
                print("\n", v, k)
            else:
                print("\n", v, k+"s")
        else:
            print("\n", v, k)
            
#Rest at the inn to fully restore your health

def rest():
  global hp
  sleepornah = input("\nWelcome to the inn, a room for the night costs 30 gold. You have " + str(bag['gold'])+" gold. \nWould you like to rent a room?: ")
  if sleepornah.lower() == 'yes' or sleepornah.lower() == 'y':
    if bag['gold'] < 30:
      print("\nYou don't have enough money.")
      intown1()
    else:
      print("\nEnjoy your stay and sweet dreams...")
      sleep(3)
      clear()
      hp = hpthresh
      bag['gold'] -= 30
      print("\nYou awaken feeling well rested. Your HP has been restored.")
      intown1()
  else:
    clear()
    intown1()

#Main function for being in town

def intown1():
  global talked1
  dowhat()
  if choice is '1':
    shop1()
  elif choice is '2':
    rest()
  elif choice is '3':
   print("\nYou decide to talk to the locals...")
   sleep(1.5)
   if gobdead is False:
     print("\nOld Lady: My, what a handsome young man you are! My daughter could use a husband like you. She doesn't want to marry any of the village boys. Perhaps a brave adventurer like you could woo her? But who can think about marriage when there is a goblin that comes into town every night and attacks our cattle and kidnaps our women! Please do something about it. We will be forever grateful. I would buy a better weapon from the shop and some potions too if you want to stand a chance!")
     talked1 = True
     input("\nPress enter to return to town.")
     clear()
     intown1()
   else:
     print("\nOld Lady: My goodness you did it! We will be forever grateful! Please, take this money as a taken of our gratitude. You deserve it.")
     if given1 is False:
       print("\nYou obtain 1000 gold")
       bag['gold'] += 1000
       input("\nPress enter to return to town.")
       clear()
       intown1()
     else:
       input("\nPress enter to return to town.")
       clear()
       intown1()
  elif choice is '4':
    clear()
    displayinv(bag)
    intown1()
  elif choice is '5':
    print("\nYou decide to venture out to kill the goblin that is terrorizing the village.\nEventually you find his cave on the mountainside. You step inside and light a torch. The walls are covered in scratches and blood. As you reach the inner sanctum, the goblin is patiently sitting on a pile of animal bones. 'I knew I smelled a human,' he says, eyeing you closely. 'I haven't tasted human flesh in quite a while...looks like it's back on the menu.' 'Come then, your meal awaits,' you say as you draw your weapon. He leaps down from his pile to meet you in combat.")
    combat1()
  else:
    print("Please select a number.")
    intown1()

#Broke down intown into another function for ease, asks player for action and sends to above function

def dowhat():
  global choice
  if talked1 is True:
    whatdo = input("\nWhat would you like to do?\
    \n1. Shop\
    \n2. Rest\
    \n3. Talk\
    \n4. View Inventory\
    \n5. Leave Town\n:")
    choice = whatdo
    clear()
  else:
    whatdo = input("\nWhat would you like to do?\
    \n1. Shop\
    \n2. Rest\
    \n3. Talk\
    \n4. View Inventory\n")
    choice = whatdo
    clear()

#Starts the game

def gamestart():
    choosediff()
    area1()
  
#Balances your HP, if you try to heal more than your total hp, cap it at the total

def hpbal():
  global hp
  if hp > hpthresh:
    hp = hpthresh

#Main shop function

def shop1():
    global bag
    stock = {'sword': 100, 'rapier': 75, 'mana potion': 30, 'potion': 50}
    print("\nWelcome to my shop. These are the items that I am selling today:\n\n1. Bronze Sword: 100 gold\n2. Bronze Rapier: 75 gold\n3. Mana Potion: 30 gold\n4. Potion: 50 gold\n5. Leave")
    prompt = input("\nWhich item would you like to purchase?: ")
    if prompt == '1' or prompt == '2' or prompt == '3' or prompt == '4':
      if prompt == '1':
        prompt = "sword"
      elif prompt == '2':
        prompt = 'rapier'
      elif prompt == '3':
        prompt = 'mana potion'
      elif prompt == '4':
        prompt = 'potion'
      prompt2 = int(input("\nHow many " + prompt + "s " + "would you like to buy?: "))
      if prompt2 < 0:
        print("\nYou can't buy negative things!")
        clear()
        shop1()
      else:
        goldowe = prompt2*stock[prompt]
        print("\nThat will be " + str(goldowe) + " gold.\nYou have " + str(bag['gold']) + " gold.")
        prompt3 = (input("\nConfirm purchase?: "))
        if prompt3.lower() == 'yes' or prompt3.lower() == 'y':
          if bag['gold'] < goldowe:
            print("\nYou don't have enough money!")
            input("Press enter to go back.")
            clear()
            shop1()
          else:
            try:
              bag[prompt] += prompt2
              bag['gold'] -= goldowe
              print("You bought " + str(prompt2) + " " + prompt)
              input("Press enter to keep shopping.")
              clear()
              shop1()
            except KeyError:
              bag[prompt] = 0
              bag[prompt] += prompt2
              bag['gold'] -= goldowe
              print("\nYou bought " + str(prompt2) + " " + prompt)
              input("Press enter to keep shopping.")
              clear()
              shop1()
        else:
          input("\nTransaction cancelled.\nPress enter to go back.")
          clear()
          shop1()
    elif prompt == '5':
      clear()
      intown1()
    else:
      print("\nI'm not selling that.")
      input("\nPress enter to go back")
      clear()
      shop1()

#First area function

def area1():
  name = input("\nWelcome to the Land of Devonia young traveller, my name is Jacob and i'll be your guide. His Majesty King Devon has decree that all travellers must be treated with utmost respect and kindness.\nMay I have your name please?: ")
  clear()
  print("\nGreetings, " + name + ". Follow me to the nearest village where you can rest and stock up on supplies. You seem injured, you're only at half hp! I would go to the inn and have a rest to restore your health.")
  sleep(3)
  print("\nWelcome to Dev-ville. This is my home village, i've lived here all my life! Why don't you have a look around? I highly recommend talking to the locals for jobs.")
  intown1()



#Clears the terminal and starts the game when the file is run directly.

if __name__ == "__main__":
    clear()
    gamestart()
    
