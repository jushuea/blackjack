import random
import os
from hardvalues import items,numbers,balance,cards,menu,good_items,bad_items,multi
def cls():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Window, use cls
        command = 'cls'
    os.system(command)
print("Black jack By joshua\nyes i did write this ;(\n\n")
name = input("Username: ")
cityc = {1:"Las Vegas 🎰🤑",2:"San Jose 🎉💸",3:"Singapore 😎💵"}
print("Here is a list of the available cities:\n1: Las Vegas\n2: San Jose\n3: Singapore\n")
choice = input("Enter a number: ")[0]
choice = int(choice)
city = cityc[choice]
inventory = ["🎲","💎","🎱"]
a_variable_i_had_to_create_lol = [1,2,3,4,5,6]


def money(balance,multi):
  if balance < 5000:
    print("\n\nLOL ngl ur broke :P\n\n")
  else:
    pass
  card1 = random.choice(cards)
  card2 = random.choice(cards)
  card3 = random.choice(cards)
  card4 = random.choice(cards)
  random_item = random.choice(items)
  super_item = random.choice(good_items)
  bad_item = random.choice(bad_items)
  player_value = card1 + card2
  player_hand = [card1,card2]
  dealer_value = card3 + card4
  dealer_hand = [card3,card4]
  if balance <= 0:
    print("You have lost the game... Balance: ",balance)
    exit()
  def dice_roll(balance):
    rigged_cards = [0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,3,3,3,3,3,2,2,2,2,6,5,9,10,10]
    start_rig = [10,9]
    rcard1 = random.choice(start_rig)
    rcard2 = random.choice(start_rig)
    card3 = 8
    card4 = 4
    random_item = random.choice(items)
    player_value = rcard1 + rcard2  
    player_hand = [rcard1,rcard2]
    dealer_value = card3 + card4
    dealer_hand = [card3,card4]
    print("!Hello ",name,", WELCOME TO ",city.upper())
    print("Available Balance: ",balance)
    x = input("\n1: Go to the casino \n2: Access Inventory\n3: Go to the Bank\n4: Go to Sleep\n5: Go to the Merchant\n6: Dictionary\n> ")
    while True:
      try:
        x = int(x)
      except ValueError:
        x = input("Please enter a number\n> ")
      else:
        break

    if x == 2:
      cls()
      print("Devil's layer. One Gamble. You can only use Casino here. Good Luck.")
      dice_roll(balance)

    elif x == 6:
      cls()
      print("Devil's layer. One Gamble. You can only use Casino here. Good Luck.")
      dice_roll(balance)
    
    elif x == 1:
      cls()
      print("Welcome to the Casino! Get ready to gamble your life savings\n away!\n")
      bet = input("Enter Bet: ")
      bet = int(bet)
      while bet > balance:
        print("You can't bet more than you have!\n",balance)
        bet = input("Enter Bet: ")
        bet = int(bet)
      while bet <= 0:
        print("You cant bet negatives idiot!\n> ")
        bet = input("Enter Bet: ")
        bet = int(bet)
      while player_value < 22:
    #Player Turn
        print("----------------------\n","\nDealer Hand: ",card3,"X")
        print("Player Hand Value: ",player_value)
        print("Player Hand: ",player_hand)
        a = input("Hit or Stand: ")
        a = a.lower()
        if a == "hit":
          draw_card = random.choice(rigged_cards) 
          player_value += draw_card
          player_hand.append(draw_card)
          if player_value > 21:
            print("You Bust!!!!\n-----------------------")
            balance -= bet
            print("New Balance: ",balance)
            print("---------------------")
            money(balance,multi)
          continue
        elif a == "stand":
      #Dealer Turn
          pass
          print("----------------------")
          print("Player Hand Value ", player_value)
          dealer_hand = [card3, card4]
          print("Dealer hand: ", dealer_hand)
          if dealer_value > player_value:
            print("---------------------\n-Dealer Stands-")
            print("You have lost.😏💦")
            balance -= bet
            print("New Balance: ",balance)
            print("Lucky!!!\nItem Received: ",random_item)
            inventory.append(random_item)
            print("---------------------")
            money(balance,multi)
        
          elif dealer_value <= player_value:
            while dealer_value <= player_value: #DEALER VALUE IS DEALERS TOTAL CARD VALUE
              print("------------------")
              dealer_hand = [card3,card4]
              draw = random.choice(cards)
              dealer_hand.append(draw)
              print("Dealer Hand: ",dealer_hand)
              dealer_value += draw
              print("Dealer Card Value: ",dealer_value)

              if dealer_value > 21:
                print("------------")
                print("DEALER BUSTED!!! 🍆")
                print("You win!!!")
                old = balance
                balance += bet
                balance = balance*multi
                profit = balance - old
                print("Profit made: ",profit)
                print("New Balance: ",balance)
                pity = [1,2,3,4]
                helps = random.choice(pity)
                if helps > 0:
                  print("Item Received!!!\nItem: ",super_item)
                  inventory.append(super_item)
                print("---------------------")
                money(balance,multi)
              elif dealer_value > player_value and player_value < 21:
                print("------------------")
                print("You have lost.😏💦")
                balance -= bet
                print("New Balance: ",balance)
                print("Lucky!!!\nItem Received: ",random_item)
                inventory.append(random_item)
                print("---------------------")
                money(balance,multi)
  print("Hello ",name,", WELCOME TO ",city.upper())
  print("Available Balance: ",balance)
  x = input("\n1: Go to the casino\n2: Access Inventory\n3: Go to the Bank\n4: Go to Sleep\n5: Go to the Merchant\n6: Dictionary\n> ")
  while True:
    try:
      x = int(x)
    except ValueError:
      x = input("Please enter a number\n> ")
    else:
      break
  if x == 4:
    print("Haven't Decided what sleeping does lol")
    money(balance,multi)
  elif x == 2:
    cls()
    print("-----------------------\nHere is your inventory!\n\nIF YOU WANT THE NAME OF A ITEM GO TO DICTIONARY\nLOCATED IN MENU!!!!\n\n",inventory)
    usage = input("Do you wish to use an item?\nyes/no\n> ").lower()
    if usage == "yes":
      use_item = input("Which item would you like to use?\n> ").lower()
      if use_item == "dice":
        if "🎲" in inventory:
          print("Your chances of winning have increased for now... 😈 ... enjoy!\n")
          inventory.remove("🎲")
          dice_roll(balance) 
        else:
          print("Item was not found!!!\n\n")
      elif use_item == "card":
        if "🃏" in inventory:
          print("As you hold the card, a dark cloud manifests around you.\nDo you want to make a deal with the devil? \nThere is a chance your life may be at risk 💀")
          devil = input("Yes or No\n> ").lower()
          if devil == "yes":
            inventory.remove("🃏")
            fate = random.choice(numbers)
            if fate > 1:
              print("...money...")
              balance += 100000
              dice_roll(balance) 
            else:
              print("*You feel a sense of impending doom*")
              balance -= 100000
              money(balance,multi)
        else:
          print("Item was not found!!!\n\n")
      elif use_item == "cigar":
        if "🚬" in inventory:
          print("DONT DO DRUGS KIDS!!!!\n\n")
          balance -= 100
          inventory.remove("🚬")
          money(balance,multi)
      elif use_item == "beer":
        if "🍺" in inventory:
          inventory.remove("🍺")
          print("You start to feel DIZZZZY!!!")
          drunk = random.choice(numbers)
          if drunk > 1: 
            print("While you fell asleep you went gambling!!\nYou doubled your money!\n> ")
            balance += balance
            money(balance,multi)
          else:
            print("While you fell asleep you went gambling!!\nYou lose NEARLY all of your money!\n> ")
            balance -= balance-1
            money(balance,multi)
    
      elif use_item == "diamond":
        if "💎" in inventory:
          inventory.remove("💎")
          eval = [10069,10000,100069,100000,1696969,696969]
          print("Welcome to the Diamond Dealer!\nHere we evaluate the prices of diamonds ;)")
          print("Highest valued diamond: 1696969")
          price = random.choice(eval)
          print("\n\nPrice of your diamond: ",price)
          balance += price
          print("Diamond sold!\n\n")
          money(balance,multi)
      elif use_item == "hat":
        if "🎩" in inventory:
          inventory.remove("🎩")
          quiz = input("What day of October was Joshua Born in?\n(ex. 10,23,30)\nPURE NUMBER VALUES\n> ")
          quiz = int(quiz)
          if quiz == 24:
            print("Thanks! Here's a few bucks :D")
            balance += balance
            money(balance,multi)
          else:
            print("Nice try. >:(")
            balance -= balance/2
        else:
          print("you do not own the item")
          money(balance,multi)
      elif use_item == "bag":
        if "💰" in inventory:
          inventory.remove("💰")
          half = balance/2
          balance += half
          money(balance,multi)
        else:
          print("you do not own the item")
          money(balance,multi)
      elif use_item == "cash":
        if "💸" in inventory:
          inventory.remove("💸")
          quarter = balance/4
          balance += quarter
          money(balance,multi)
        else:
          print("You do not have this item!")
      elif use_item == "ball":
        if "🎱" in inventory:
          inventory.remove("🎱")
          youre = [1,2,3,4]
          roll = random.choice(youre)
          balance += balance/roll
          print("You roll a ", roll)
          bonus = [0.1,0.2,0.1,0.2,0.3,0.4,0.5]
          multi += random.choice(bonus)
          print("Multi increased by ???")
          money(balance,multi)
        else:
          print("Item not found!!!")
      elif use_item == "shit":
        if "💩" in inventory:
          print("You have shat\n\nYou now have two shits!\n")
          inventory.append("💩")
          money(balance,multi)
        else:
          print("Item not owned")
        
          
    else:
        money(balance,multi)
    back = input("Do you wish to return?\n> ").upper()
    while back != "YES":
      print("\nEnter yes to exit")
      print("Here is your inventory!\n",inventory)
      back = input("Do you wish to return?\n> ").upper()
    money(balance,multi)

  elif x == 3:
    cls()
    print("\n\nYour Current Coin Muliplier: ",multi)
    print("WELCOME TO THE BANK!\nBALANCE: ",balance,"\nHere you can increase your multiplier by a tiny bit, move to other cities for great multipliers and other known benefits!!! \n\n")
    bank = input("1: Multiplier Store\n2: Train Ticket\n3: Return\n> ")
    while True:
      try:
        bank = int(bank)
      except ValueError:
        bank = input("Please enter a number\n> ")
      else:
        break
    if bank == 1:
      print("\nWelcome to the Muliplier Store!\n BALANCE: ",balance,"\n\n1: +0.1x multi = 2.5k\n2: +0.5x multi = 11.5k!\n3: +1.0x multi = 22k\n4: +2.0x multi =  43k\n")
      shop = input("\n> ")
      shop = int(shop)
      if shop == 1:
        print("\n\nYOUR BALANCE: ",balance)
        smol = input("How many 0.1x multi's would you like to buy?\n> ")
        smol = int(smol)
        add = 0.1*smol
        cost = 2500*smol
        if balance < cost:
          print("You don't have enough money!")
          money(balance,multi)
        balance -= cost
        multi += add
        money(balance,multi)
      if shop == 2:
        print("\n\nYOUR BALANCE: ",balance)
        smol = input("How many 0.5x multi's would you like to buy?\n> ")
        smol = int(smol)
        add = 0.5*smol
        cost = 11500*smol
        if balance < cost:
          print("You don't have enough money!")
          money(balance,multi)
        balance -= cost
        multi += add
        money(balance,multi)
      if shop == 3:
        print("\n\nYOUR BALANCE: ",balance)
        smol = input("How many 1x multi's would you like to buy?\n> ")
        smol = int(smol)
        add = 1*smol
        cost = 11500*smol
        if balance < cost:
          print("You don't have enough money!")
          money(balance,multi)
        balance -= cost
        multi += add
        money(balance,multi)
      if shop == 4:
        print("\n\nYOUR BALANCE: ",balance)
        smol = input("How many 2x multi's would you like to buy?\n> ")
        smol = int(smol)
        add = 2*smol
        cost = 43000*smol
        if balance < cost:
          print("You don't have enough money!")
          money(balance,multi)
        balance -= cost
        multi += add
        money(balance,multi)
    elif bank == 2:
      print("Haven't finished the train ticket thing just yet :( ")
      money(balance,multi)
    elif bank == 3:
      print("Adios!\n")
      money(balance,multi)
    else:
      print("YOU CANT TYPE THAT YOU DUMBDUMB!\n\n")
      money(balance,multi)
    
  elif x == 6:
    cls()
    print("\n\nDictionary of Items\n\nIN ORDER TO USE AN ITEM TYPE IN THE NAME OF ITEM (EX. Dice) or (Ex. Bag)")
    print("🎲 - Dice - Increases Luck\n🃏- Card - Lose ~XXX~ or gain ~XXX~ and Increase Luck Greatly\n🚬 - Cigar - Unknown \n🍺- Beer - Double or Nothing\n💎 - Diamond - It's a diamond -_-\n💰 - Bag - A bag of money\n💸 - Cash - litterily cash >:| \n🎩 - Hat - Asked a random question for a chance of cash\n🎱 - ball - Increases money by XXX amount\n💩 - shit - Disease.\n\n")
    money(balance,multi)
  elif x == 5:
    cls()
    print("Welcome the Merchent!!!\nPerfect for gambling adicts like you!\nBuy items for all benefits OR sell pesky items you never wanted!\nYour Current Balance: ",balance)
    ops = input("\n\n1: Enter Store\n2: Enter Pawn Shop\n> ")
    
    while True:
      try:
        ops = int(ops)
      except ValueError:
        ops = input("Please enter a number\n> ")
      else:
        break
    if ops == 1:
      print("Welcome to the Store!\nHere are the items available!\n\na: 🎲 - Dice - 80k\nb: 💎 - Diamond - 100.569k\nc: 🃏 - Card - 150k\nd: 🚬 - Cigar - 7k\ne: 🎩 - Magic Hate - 2,000,000,000,000\nf: 🍺 - Beer - 7k\ng: 🎱 - Magic 8 Ball - 25k\nh: RETURN TO MENU")
      buy = input("\n>").lower()
      if buy == "a":
        print("80K each Dice\nBALANCE: ",balance)
        dice = input("How many Dice Do you want to buy?\n> ")
        dice = int(dice)
        cost = 80000*dice
        if balance < cost:
          print("You're broke get out of here.")
          money(balance,multi)
        while dice > 0:
          inventory.append("🎲")
          dice -= 1
        balance -= cost
        money(balance,multi)
        
      if buy == "b":
        print("100.569k for each Diamond\nBALANCE: ",balance)
        diamond = input("How many Diamonds do you want to buy?\n> ")
        diamond = int(diamond)
        cost = 100569*diamond
        if balance < cost:
          print("BROKE LOL!\n\n")
          money(balance,multi)
        while diamond > 0:
          inventory.append("💎")
          diamond -= 1
        balance -= cost 
        money(balance,multi)
          
      if buy == "c":
        print("150k for each Card\nBALANCE: ",balance)
        card = input("How many Cards do you want to buy?\n> ")
        card = int(card)
        cost = 150000*card
        if balance < cost:
          print("BROKE LOL!\n\n")
          money(balance,multi)
        while card > 0:
          inventory.append("🃏")
          card -= 1
        balance -= cost 
        money(balance,multi)
      if buy == "d":
        print("6.9k for each cigar\nBALANCE: ",balance)
        cigar = input("How many cigars do you want to buy?\n> ")
        cigar = int(cigar)
        cost = 100569*cigar
        if balance < cost:
          print("BROKE LOL!\n\n")
          money(balance,multi)
        while cigar > 0:
          inventory.append("🚬")
          cigar -= 1
        balance -= cost 
        money(balance,multi)
      if buy == "e":
        print("2,000,000,000,000 for each hat\nBALANCE: ",balance)
        hat = input("How many Hats do you want to buy?\n> ")
        hat = int(hat)
        cost = 2000000000000*hat
        if balance < cost:
          print("BROKE LOL!\n\n")
          money(balance,multi)
        while hat > 0:
          inventory.append("🎩")
          hat -= 1
        balance -= cost 
        money(balance,multi)
      if buy == "f":
        print("7k for each beer\nBALANCE: ",balance)
        beer = input("How many Beers do you want to buy?\n> ")
        beer = int(beer)
        cost = 7000*beer
        if balance < cost:
          print("BROKE LOL!\n\n")
          money(balance,multi)
        while beer > 0:
          inventory.append("🍺")
          hat -= 1
        balance -= cost 
        money(balance,multi)
      if buy == "g":
        print("25k for each 8 Ball\nBALANCE: ",balance)
        ball = input("How many 8 balls do you want to buy?\n> ")
        ball = int(ball)
        cost = 25000*ball
        if balance < cost:
          print("BROKE LOL!\n\n")
          money(balance,multi)
        while ball > 0:
          inventory.append("🎱")
          ball -= 1
        balance -= cost 
        money(balance,multi)
      if buy == "h":
        money(balance,multi)

    
    elif ops == 2:
      print("WELCOME TO THE PAWN SHOPPPP!\nGET ready to BARGAINN!\nBALANCE: ",balance)
      bargain = {1:20000,2:95000,3:500,4:7000,5:80000,6:15000,7:70000}
      ballz = 20000
      hat = 95000
      cigar = 500
      beer = 7000
      card = 80000
      diamond = 15000
      dice = 70000
      sell = input("Which item would you like to sell?\nHere are the items available!\n\n7: 🎲 - Dice\n6: 💎 - Diamond\n5: 🃏 - Card\n3: 🚬 - Cigar\n2: 🎩 - hat\n4: 🍺 - Beer\n1: 🎱 - ballz\nh: RETURN TO MENU")
      sell = int(sell)
      TRUE_VALUE = bargain.get(sell)
      TRUE_VALUE = int(TRUE_VALUE)
      BEGIN_VALUE = TRUE_VALUE/2
      x = input("Enter Ask Price for Object: ")
      x = int(x)
      if x > TRUE_VALUE:
        print("PAWN PRICE: ",BEGIN_VALUE)
        PROCESS = input("OH HELL NO!\n\nYes or No?\n> ").lower()
        if PROCESS == "yes":
          print("LOL scammed :P\n\n")
          balance += BEGIN_VALUE
          money(balance,multi)
        while BEGIN_VALUE <= TRUE_VALUE:
          BEGIN_VALUE += BEGIN_VALUE/2
          print("NEW PAWN PRICE: ",BEGIN_VALUE)
          loop = input("\nYes or No?").lower
          if loop == "yes":
            balance += BEGIN_VALUE
            money(balance,multi)
          else: 
            may = random.choice(numbers)
            if may > 1:
              continue
            if may < 2:
              balance += BEGIN_VALUE
              break
        money(balance,multi)
          
        
      
      
      
  elif x == 1:
    cls()
    print("Welcome to the Casino! Get ready to gamble your life savings\n away!\n")
    bet = input("Enter Bet: ")
    bet = int(bet)
    while bet > balance:
      print("You can't bet more than you have!\n",balance)
      bet = input("Enter Bet: ")
      bet = int(bet)
    while bet <= 0:
      print("You cant bet negatives idiot!\n> ")
      bet = input("Enter Bet: ")
      bet = int(bet)

    while player_value < 22:
    #Player Turn
      print("----------------------\n","\nDealer Hand: ",card3,"X")
      print("Player Hand Value: ",player_value)
      print("Player Hand: ",player_hand)
      a = input("Hit or Stand: ")
      a = a.lower()
      if a == "hit":
        draw_card = random.choice(cards) 
        player_value += draw_card
        player_hand.append(draw_card)
        if player_value > 21:
          print("You Bust!!!!\n-----------------------")
          balance -= bet
          print("New Balance: ",balance)
          print("---------------------")
          money(balance,multi)
        continue
      elif a == "stand":
      #Dealer Turn
        pass
        print("----------------------")
        print("Player Hand Value ", player_value)
        dealer_hand = [card3, card4]
        print("Dealer hand: ", dealer_hand)
        if dealer_value > player_value:
          print("---------------------\n-Dealer Stands-")
          print("You have lost.😏💦")
          balance -= bet
          print("New Balance: ",balance)
          print("---------------------")
          money(balance,multi)
          
        
        elif dealer_value <= player_value:
          while dealer_value <= player_value: #DEALER VALUE IS DEALERS TOTAL CARD VALUE
            print("------------------")
            dealer_hand = [card3,card4]
            draw = random.choice(cards)
            dealer_hand.append(draw)
            print("Dealer Hand: ",dealer_hand)
            dealer_value += draw
            print("Dealer Card Value: ",dealer_value)

            if dealer_value > 21:
              print("------------")
              print("DEALER BUSTED!!! 🍆")
              print("You win!!!")
              old = balance
              balance += bet
              balance = balance*multi
              profit = balance - old
              print("Profit made: ",profit)
              print("New Balance: ",balance)
              helpo = [1,2,3,4]
              pity = random.choice(helpo)
              randomvar = balance/4
              if pity < 4:
                if bet > balance/2:
                  print("Item Received!!!\nItem: ",random_item)
                  inventory.append(random_item)
                elif bet < balance/4:
                  print("Item Received!!!\nItem: ",bad_item)
                  inventory.append(bad_item)
                elif bet > balance/2 + randomvar:
                  print("Godly Item Received!!!\nItem: ",super_item)
                  inventory.append(super_item)
                
                print("---------------------")
              money(balance,multi)
            elif dealer_value > player_value and player_value < 21:
              print("------------------")
              print("You have lost.😏💦")
              balance -= bet
              print("New Balance: ",balance)
              print("---------------------")
              if balance < 30000:
                help = random.choice(numbers)
                if help < 2:
                  money(balance,multi)
                elif help > 1:
                  dice_roll(balance)
    money(balance,multi)
money(balance,multi)

  
