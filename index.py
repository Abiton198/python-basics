#VARIABLES

# failed_subjects='2'
# name='John'

# print('Dear Mrs Badger')
# print('Your son ' + name + 'is failing ' + failed_subjects + ' subjects')
# print(name +  ' will need to redo ' + failed_subjects +  ' courses.')
# name ='Peter'
# print(name +' is doing well in geography.')

# item = 'microwaves'
# price = '200'
# stock = '10'

# print('we have ' + stock, item + ' costing R' + price )

# ARITHMETICS

# a=10
# b=3
# print('Addition : ', a + b) #13
# print('Subtraction : ', a - b) #7
# print('Multiplication : ', a * b) #30
# print('Division (float) : ', a / b) #3.333333335
# print('Division (floor) : ', a // b)#3 does not count decimals
# print('Modulus : ', a % b) # records remainder only in division
# print('Exponent : ', a ** b)# 10 x 10 x 10 

#PYTHON STRINGS BASICS
# name = 'Michelle Tinevimbo'
# msg = 'I love you so much ' + name
# print(msg,msg) #duplicate msg
# print(msg + msg)
# # print(msg*2)
# print(msg.upper()) #uppercase / capital letters
# print(msg.lower()) #lowercase / small letters
# print(msg.capitalize()) #only 1st letter begining of sentence
# print(msg.title()) #capitalize each word
# print(len(msg)) #length of the string
# print(msg.count('love')) #count instance of word occurance in a string or letter

#SLICING
# print(msg[3]) #retain letter on 5 index, starting from 0
# print(msg[-1]) #retains the last letter
# print(msg[3:9]) # : retains every word after the number before upto number specified (not including the num 9 position)
# print(msg[:5]) #blank assumed to be zero (0)

# # #making a new string from a string
# msg='welcome to Python 101: Strings'
# message = msg[18] + ' '+ msg[:8] + msg[25:-1] +msg[7:-19] + msg[13] + msg[12] + msg[2
# ] + msg[1] + msg[25]
  
# print(message.title()) #"1 Welcome To Ring Tyler"
# print(message[::-1].title())# Reverse / backward print


#MAKING ONE LINE FROM MULTIPLE LINES
# msg = """ Dear Terry,,
# You must cut down the mightiest 
# tree in the forest with…
# a herring! <3 """
# print(msg)

# #FIND()
# msg = 'Welcome to Python 101: Strings'
# print(msg.find('o')) #retains position of the letter or word

# #REPLACE()
# msg='Welcome to Python 101: Strings'
# print(msg.replace('Python', 'Java')) #replaces the word - 1st written
# msg1 = msg.replace('Python', 'C') #using a variable is the best practise
# print(msg)

# #MEMBERSHIP
# print('Python' in msg) #check if it exist -True
# print('Python' not in msg) #check if not exist - False

#STRING FORMATTING
# name='TERRY'
# color = 'RED'
# msg = '[' + name + '] loves the color ' + color.lower() + '!'
# msg1 = f'[{name.capitalize()}] loves the color {color.lower()}!' #best practise to concatnat
# print(msg)
# print(msg1)

#USER INPUT
#When yo run code an input text box will pop-up and fill in
# name = input('What is your name?:')
# age = input('What is your age?')
# input('Hello ' + name + '! ' + 'You are ' + age + ' years old now.') 

# num1 = input('Enter a digit: ')
# num2 = input('Enter second number: ')
# answer= float(num1) + float (num2)
# print(answer)

# - Create a distance converter converting Km to miles
# - Take two inputs from user: Their first name and the distance in km
# - Print: Greet user by name and show km, and mile values
# - 1 mile is 1.609 kilometers
# - hint: use correct types for calculating and print
# - Did you capitalize the name


# name = input('What is your name?:')
# distance_km = input('How many km did you travel?:')
# distance_mi = float(distance_km)/1.609
# messge = (f'Hi {name.title()} you have travelled  {round(distance_mi,1)} miles so far!') #round() - to decimal number
# print(messge)

#LISTS
# friends = ['Michelle', 'Travis','Cherise','Abiton','Tyris','Tinevimbo'] #creating a list
# cars = [911,130,328,535,740,308] 
# print(friends)
# print(friends[2], friends[-1]) #looping 
# print(friends.count('Tyris'))
# friends.sort()#sort() in ascending order (A-Z)
# print(friends)
# friends.sort(reverse=True) #sort in descending order(Z-A)
# print(friends)
# friends.reverse() #original string reversed order
# print(friends)
# print(max(cars)) # max number or use min(cars)
# print(sum(cars)) #add num
# friends.append('Michelle T') #append() or use insert()
# friends.insert(2,'Cherise Nenyasha') #position in the list
# friends[2]= 'Cheris Nenyasha' #insert and remove the value item at the number / replace
# friends.extend(cars) #adding another list 
# friends.remove('Cherise') #removes from list
# friends.pop(4) #pop() removes item but can be used later
# # friends.clear() #remove everything from list / del remove permanently
# friends_new = friends[:]#creates a copy of the same list / friend.copy() / list(friends)
# print(friends_new)
# print(friends)

# sales_w1 = [7,3,42,19,15,35,9]
# sales_w2 = [12,4,26,10,7,28]
# sales = []
# another_day = input('Sale of new day:')
# sales_w2.append(int (another_day)) #adding another day a& make it interger/number from a string
# sales = sales_w1 + sales_w2 #joining 2 sales list
# print(sales)
# sales.sort() #or can use max & min
# best_day = f'Best Day Profit:$ {sales[-1]*1.50}' #calculate profit on best day
# print(best_day)
# worst_day =  f'Worst Day Profit:$ {sales[0]*1.50}' #calculate profit on worst day
# print(worst_day)
# combined_profit = best_day + worst_day
# print(f'Combined profit:${combined_profit}')

############## SPLIT() & JOIN() ########################

# msg ='Welcome to Python 101: Split and Join'
# csv = 'Eric,John,Michael,Terry,Graham'
# friends_list = ['Eric','John','Michael','Terry','Graham']
# print(msg.split()) #make a string into a list of items
# print(msg.split(' ')) #includes spaces
# print(csv.split(',')) #seperate into a list from a qoma
# print(' '.join(friends_list)) #list to string

# csv = 'Eric,John,Michael,Terry,Graham:TerryG;Brian'
# friends_list = ['Exercise: fill me with names']
# # From the list above fill a list(friends_list) properly
# # with the names of all the friends. One per "slot"
# # you may need to run same command several times
# # use print() statements to work your way through the exercise

# print((','.join(','.join(csv.split(';')).split(':'))).split(','))
# print('replace', csv.replace(';',',').replace(':',',').split(','))
# friends_list= ','.join(','.join(csv.split(';')).split(':')).split(',')
# print(friends_list)

##### TURPLES####### - faster Lists you can't change
# friends = ['John','Michael','Terry','Eric','Graham']
# friends_tuple = ('John','Michael','Terry','Eric','Graham') # cant be changed - immutable

# print(friends)

#########SETS ##########
#Sets - blazingly fast unordered Lists 
# friends = ['John','Michael','Terry','Eric','Graham']
# friends_tuple = ('John','Michael','Terry','Eric','Graham')
# friends_set = {'John','Michael','Terry','Eric','Graham','Eric'} #sets do not duplicate items of same name
# my_friends_set = {'Reg','Loretta','Colin','Eric','Graham'}

# print(friends_set.difference(my_friends_set)) #gives the difference between 2
# print(friends_set.union(my_friends_set)) # all without duplicate
# print(friends_set.intersection(my_friends_set)) #whats common

# #Sets - blazingly fast unordered Lists 
# #empty Lists
# empty_list = []
# empyt_list = list()

# #empty Tuple
# empty_tuple = ()
# empty_tuple = tuple()

# #empty Set
# empty_set = {} # this is wrong, this is a dictionary
# empty_set = set()


#1. Check if ‘Eric’ and ‘John’ exist in friends
#2. combine or add the two sets 
#3. Find names that are in both sets
#4. find names that are only in friends
#5. Show only the names who only appear in one of the lists
#6. Create a new cars-list without duplicates

# friends = {'John','Michael','Terry','Eric','Graham'}
# my_friends = {'Reg','Loretta','Colin','John','Graham'}
# cars =['900','420','V70','911','996','V90','911','911','S','328','900']

# print('Eric' in friends and 'John' in friends) #1
# print(friends.union(my_friends)) #2 or use = friends | my_friends
# print(friends.intersection(my_friends)) #3
# print(friends.difference(my_friends)) #4 or use (friends - my_friends)
# print(friends.symmetric_difference(my_friends)) #or use (friends ^ my_friends)
# print(set(cars))#6 or use = list (set(cars))

##########FUNCTIONS##################
#def = defining a function
# def greetings(name, age=30, color = 'red'): #parameter - what we we sending in the function
#     message = f'Hey Love {name.title()}! you will be {age + 1}  this year!' # f - formatted strings
#     favorites = f'We hear you like the color {color}!'
#     print(message) #indent print() use Tab
#     print(favorites)


# name = input('What is your name?:')
# color = input('What is your favorite color? :')

# greetings(name='Michelle',age = '32',color='blue') #argument - what we send to ====use name notation so that its easy to read
# greetings('Cherise')#default age is used if not specified

# 1. Add new print statement - on a new line
#    which says 'We hear you like the color xxx! xxx is a string with color 
# 2. extend the function with another  input parameter 'color', that defaults to 'red'
# 3. Capture the color via an input box as variable:color 
# 4. Change the 'You are xx!' text to say 'you will be xx+1 years old next birthday 
#  adding 1 to the age
# 5. Capitalize first letter of the 'name', and rest are small caps 
# 6. Favorite color should be in lowercase  

######## RETURN STATEMENTS #########
# def value_added_tax(amount):
#     tax = amount * 0.25
#     total_amount = amount * 1.25
#     return amount, tax ,total_amount
    #f'' = string
    #{}  = set
    #()  = turple
    #[]  = list (index based)
# price = value_added_tax(100)    
# print(price, type(price))


######### COMPARISONS AND BOOLEANS   
# a = 7
# b = 3
# print(a == b) # = assign operator
# != not equal to
# 'o' in 'John'  === in / not in 
# a is b = checks identity of each
# #print('o in John is ','o' in 'John') #membership
# print('o in John is ','o' not in 'John') #non membership
# print('John is John ','John' is 'John') #identity
# print('John is not John is ','John' is not 'John') # negative identity
#! Boolean = 0 & '' evaluates to FALSE / 0 
#all other values in Boolean evaluates to TRUE / 1

########## CONDITIONALS --- IF, IFELSE, ELSE
# is_raining = False
# is_cold = True
# print("Good Morning")
# if is_raining and is_cold: # and expects 2 conditions to be met
#     print("Bring Umbrella and jacket")
# elif is_cold or is_raining: # only expects 1 condition to be met
#     print('Bring either jacket or umbrella')
# elif is_raining and not(is_cold):
#     print('Bring Umbrella')
# elif is_cold and not(is_raining):
#     print('Bring a jacket')
# else:
#     print("Umbrella or jacket is optional")

# purchase = 51
# is_pin = 2010
# if purchase <= 50:
#     print('Purchase Approved')
# else:
#     input('Enter a pin:')

# if is_pin != is_pin:
#     print('Sorry! Your purchase has been declined!')
# else:
#     print(f'Pin correct! your purchase approved!')
#! Project - Wadrobe suggestor (work with next day weather predictions)
#######print('if elif else - Exercise')
# Create a calculator which handles +,-,*,/ and outputs answer based on the mode/ operator used
# Hint: use 3 separate inputs 
# Bonus: Extend functionality with extra mode so it also does celsius to fahrenheit conversion
# formula is: temp in C*9/5 + 32 = temp in f

# mode = input('Enter math operator:(+,-,/,* or f for Celcius to fahrenheit)')
# a = float(input('Enter number:'))
# if mode.lower() == 'f':
#     print(f'{a} Degrees Celcius is equal to {(a*9/2) + 32} Ferhrenheit')
# else:
#     b = float(input('Enter another number:'))
# # wrap input into float(input(...)) - to change string into number
# #1st if statement is to prevent double input of number if want to convert dEGREES Celcius to Ferhrenheit
# #indent the other if conditional statement

#     if mode == '+':
#         print(f'The answer is : {int(a) + int (b)}')
#     elif mode == '-':
#         print(f'The answer is: {int(a) - int(b)}')
#     elif mode == '*':
#         print(f'The answer is : {int(a) * int (b)}')
#     elif mode == '/':
#         print(f'The answer is : {int(a) / int (b)}')
#     else:
#         print('Input error!')

# def num_days(month):
#     days = 31
#     # if month == 'apr' or month =='jun' or month =='sep' or month =='nov':
#     if month in {'apr', 'jun' , 'sep', 'nov'}: # can use [] or turple () , in - checks membership
#         days = 30
#     elif month == 'feb':
#         days = 28
#     print('number of days in',month,'is',days)

# num_days('may')
# # optimize/shorten the code in the function
# # reduced number of conditionals 

######### WHILE LOOPS ###############
# Three Loop Questions:
#1. What do I want to repeat?
#  -> message
#2. What do I want to change each time? 
#  -> stars
#3. How long should we repeat?
#  -> 5 times

# print("1.*Loops are great*")
# print("2.**Loops are great**")
# print("3.***Loops are great***")
# print("4.****Loops are great****")
# print("5.*****Loops are great*****")

#using loops to achieve the same result
# i = 0
# while i < 5:
#     i += 1
#     print(f'{i}.' + '*'* i + 'Loops are awesome' + '*' * i)
#     # i = index

######LOOPS EX. ==== GUESSING GAME
# print('Guessing game') 
# Guess the correct number in 3 guesses. If you don’t get it right after 3 guesses you lose the game. 
# Give user input box: 1. To capture guesses, 
# print(and input boxes) 1. If user wins 2. If user loses
# Tip:( remember you won’t see  print statements durng execution, so If you want to see prints during whle loop, then print to the input box

#Modification 1: number 1-100, tell user if guess is too high/low ,and let them have 5-10 guesses.
# Tip:( remember you won’t see  print statements during execution, so If you want to see prints during whle loop, print to the input box (This is specific to this platform)
# Three Loop Questions:
#1. What do I want to repeat?
#  -> guesses
#2. What do I want to change each time?
#  -> winner or loser
#3. How long should we repeat?
#  -> 100
#! Project - Guessing game 
# guess = 0
# guess_limit = 5
# num = 55
# guess_num = 0 
# guess = int(input(f'guess # 1-100 :')) #int - to make it a number # 1st guessed number 
# guess_num += 1 

# while guess_num < guess_limit:

#     if guess != num: # 1st condition of guess
#         guess_num += 1 #keeping track of count num of guesses
#         if guess > num : #guiding the player of guessed number
#             guess = int(input(f'{guess} guess too high!'))
#         else:
#             guess = int(input(f'{guess} Guess too low!'))

#     if guess == num: #correct guess 
#         print(f'Your guessed {guess} is correct! Congrats!') 
#         break # means now outside the scope of if loop

# if guess!= num: #reaching limit with wrong guesses
#         print(f'You lose! guess number is {num}')

################# FOR LOOPS AND LOOPING #######################
# for letter in 'Anniversary': #for loop - loops every item in a string
#     print(letter)
# for numbers in range(5,60,12): # in range - prints from 5, skips according to 3rd number 12 upto 60
#     # ['Terry', 'John', 'Mark', 'Ann'] - list === use for names in [...]
#     print(numbers)
friends = ['Terry', 'John', 'Eric', 'Mark', 'Ann']
# for index in range(len(friends)): #len - length; index- contents of array
#     print(friends[index])
# print('For loop when done')
################## break / continue
# for friend in friends:
#     if friend == 'Eric':
#         print('found ' + 'Eric')
#         # break #stops when it gets to condition 
#         continue # continue even if condition is met
#     #if no break or continue it duplicates 'Eric'
# #     print(friend)

# ######nested loops
# for friend in friends:
#     for number in [1,2,3]:
#         print(friend, number)
########## Exercise - party invitation ####
# names = ['john ClEEse','Eric IDLE','michael']
# names1 = ['graHam chapman', 'TERRY', 'terry jones']
# # 1 - create message for all names to be received
# msg = 'you are invited to party on saturday.'
# # 2 - join the 2 list to 1 list
# names += names1 #to join the list
# # names.extend(names1)
# # 3 - add 2 names in the list through append in input box
# for index in range(2):
#     names.append(input('Enter name:'))
# # 4 - loop over the new list and add msg
#     for name in names:
#         message = f'{name.title()} {msg}'
#         print(message)

############## ENUMERATOR ####################
# friends = ['Terry', 'John', 'Eric', 'Mark', 'Ann']
# #numbering items in a list starting from 1 ---turns string into a turple
# for num,friend in enumerate(friends,start=10): #num for numbers #1 - where to start from 
#     print(num, friend)

############# SORT() & SORTED()
#sorted() - retrns an ascending order array or list
# my_list = [1,-5,3,7,-2]
# my_dict = {'car':4,'dog':2,'add':3,'bee':1}
# my_tuple = ('d','c','e','a','b')
# my_llist=[['car',4,65],['dog',2,30],['add',3,10],['bee',1,24]]

# print(sorted(my_list), 'new') # sort the list in ascending order
# print(my_list[::-1]) #reverses the order of the list only / reverse()
# print(my_tuple, key = abs) #returns absolute value of a list
# print(my_llist, key = lambda item: item[1])

####### DICTIONARIES ############
# movie = {
#     'title' : 'Life of Brian',
#     'year' : 1979,
#     'cast' : ['John','Eric','Michael','George','Terry']
# }
# movie['budget'] = '24 000' #adding an item (key and value in a list)
# movie.update({'title': 'titanic', 'year' : '1987'}) #updating the movie object
# del movie['year'] #deleting an item permanently
# year = movie.pop('cast') #remove item and save it into new variable
# print(movie) #retains everything in movie
# print(movie.get('year')) # value of a list from a specified key - year
# print(year)
# print(movie.keys()) #keys
# print(movie.values())#values

# for key,value in movie.items(): #get list key and values 
# #     print(key,value)

# python = {'John':35,'Eric':36,'Michael':35,'Terry':38,'Graham':37,'TerryG':34}
# holy_grail = {'Arthur':40,'Galahad':35,'Lancelot':39,'Knight of NI':40, 'Zoot':17}
# life_of_brian = {'Brian':33,'Reg':35,'Stan/Loretta':32,'Biccus Diccus':45}

# #membership test
# if 'Abiton' not in python: #in / not in ---checks existance
#     print('he\'s not here!')

# #updating membership
# people = {}
# people1 = {}
# people3 = {}

# #method 1 - update
# people.update(python)
# # people.update(holy_grail)
# people.update(life_of_brian)
# print(sorted(people.items()))

# #method 2 - comprehension
# for groups in (python,holy_grail,life_of_brian): people1.update(groups)
# print(sorted(people1.items()))

# #method 3 - unpacking
# people3 = {**python, **holy_grail, **life_of_brian}
# print(sorted(people3.items()))

# #sum value
# print('The sum is: ',sum(people.values()))

##############EXERCISE  ----DICTIONARIES##########
#It’s...not really an adventure game...#Ver 1.0
#Your village is being attacked by 'a germanic tribe' and you need to run to the stores and get the right things to save your village, and probably some good looking girl or boy you want to marry. All prices in gold pieces excl. VAT... chop chop!! ze germanz are coming!
#The code should allow you to get 1 thing from each store and each item you get should be removed from the store inventory, then do same for next store...
# one way to buy by typing the key 'newt' in an input box...or something
# at end you should print the 'items' you have taken..in this version you don't have to pay for stuff or add it up
#ver 1.2 add ability to exit a store without buying and go to next by typing 'exit', and to exit if a nonexistant item is bought(typed)
#Add purse with 1000 gold pieces and payment for the items during or at end of code and show a message about total cost and how much gold you have left
#ver 1.4 random bug fix, ' browser compatability', refactoring code... basically being lazy ..stop scrolling TikTok/Facebook! ;-)
#Ver 1.5 print inventory before and after purchases as one department_store of stuff(combine inventories from all stores into one...pretend Big Biz bought all the local stores, and want constant reporting for inventory management...)
# as in all games there is a special way to do this that actually makes money and solves the problem...can you find 'them'? Do you know why? May require knowledge of actual python 'lore'
#create stores

freelancers = {'name':'freelancing Shop','brian': 70, 'black knight':20, 'biccus diccus':100, 'grim reaper':500, 'minstrel':-15}
antiques = {'name':'Antique Shop','french castle':400, 'wooden grail':3, 'scythe':150, 'catapult':75, 'german joke':5}
pet_shop = {'name':'Pet Shop','blue parrot':10, 'white rabbit':5, 'newt': 2}

#morning inventory -updating the inventory before the purchases
department_store = {}
for department in (freelancers, antiques, pet_shop) :department_store.update(department)
department_store.pop('name')
print('Morning inventory of stores', sorted(department_store.items()))
print('-----------------')

#create an dempty shopping cart
cart = {}
#create a purse
purse = 1000

buy_item1 = ''
#loop through stores/dicts
for shop in (freelancers, antiques, pet_shop):
    #inputbox  to show what you can buy...capture textstring of what was bought...make lowercase
    buy_item = input(f'Welcome to {shop["name"]}! what do you want to buy: {shop}').lower()
    # Condition when one try to buy nonexistant product- should allow  to exit to next shop
    if buy_item == 'exit':
        continue
    if buy_item not in shop:
        continue

    #update the string
    buy_item1 = buy_item1 + f'{buy_item}:{shop[buy_item]} Gp,'
    #update the cart
    cart.update({buy_item:shop.pop(buy_item)}) # use pop...
    # item = ", ".join(list(cart.keys())) #only for keys but with no values

print(f'You Purchased: {buy_item1}. Your total amount is {sum(cart.values())}Gp. Your change is {purse - sum(cart.values())}Gp. Have a nice day of mayhem!')
#evening inventory ---after all purchases done and items removed
department_store_after = {**freelancers, **antiques, **pet_shop} #pyth 3.5
department_store_after.pop('name')
print('-----------------')
print('Evening inventory of stores', sorted(department_store_after.items()))