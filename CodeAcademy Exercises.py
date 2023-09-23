#CodeAcademy Exercises 

#Problem 1: 
#Write a function called digit_sum that takes a positive integer n as input and returns the sum of all that number’s digits. For example: digit_sum(1234) should return 10 which is 1+2+3+4. Assume that the number you are given will always be positive.

def digit_sum(n): 
  sum = 0 
  n = str(n) # conver to a string so that it can be iterable through a for loop
  for i in n: 
    i = int(i) #convert the first character in the string into a number so that it can be used to add to "sum"
    sum = sum + i 
  return sum 

#Problem #2
#Calculate the factorial of a number x. Factorials are determined by multiplying all the integers from 1 through x. Ex. Is factorial(4) == 24 and factorial(1) == 1

def factorial(x): 
  total = 1
  while x >0: 
  #can't deal with integers ==0 or less than 0 when doing factorials 
    if x == 0: 
    #have the breaking condition first so it breaks out of the for loop whenever the if statement becomes true. 
      break 
    total = total*x
    x = x-1 
    #how you do the factorial. Decrease x in steps of 1. 
  return total

#Problem #3
#Determine input x as a prime number or not. Your code should account for negative numbers, 0, and 1 as well. 

def is_prime(x):
  if x <=1: 
  #need the case for x ==0 and x ==1 and x == negative numbers. Need this because 0 and 1 are not prime numbers. 
      return False
  for n in range (2, x): 
  #works x ==2 because  range (2,2) doesn't output a number. It goes straight to the else statement. 
    if x % n ==0: 
      return False 
  else: 
    return True

#Problem #4
#Input is a string, and the output is the reverse of the string. 

def reverse(text): 
  count = len(text)-1
  string = '' 
  #have to put this outside because this is the base. Can't have it in the for loop or else it'll reset to an empty string 
  for i in range(len(text)): 
  #ranges are exclusive of the last number, so it actually goes from 0 to len(text)-1 
    string = string + text[count] 
    #accessing the last index of text and concatenating it to the empty string
    count = count -1 
    #can't do -i because the first i is 0. Basically, with -i, round 2 would print out the last character twice. 
  return string

#Problem #5
#Define a function called anti_vowel that takes one string, text, as input and returns the text with all of the vowels removed. 

def anti_vowel(text): 
  string = ''
  vowel = ['A', 'a', 'E', 'e', 'I', 'i', 'O', 'o', 'U', 'u']
  for char in text: 
    if char not in vowel: 
      string = string + char
  return string 

#Problem 6
#Define a function scrabble_score that takes a string word as input and returns the equivalent scrabble score for that word. 
# Assume your input is only one word containing no spaces or punction. 
# As mentioned, no need to worry about score multipliers! 
# Your function should work even if the letters you get are uppercase, lowercase, or a mix 
# Assume you’re given non-empty strings. 

def scrabble_score(word):
  score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2, 
         "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3, 
         "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1, 
         "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4, 
         "x": 8, "z": 10}
  total = 0 
  for char in word: 
    char = char.lower() 
    #make the character lowercase so that you can access the values in the score dictionary 
    total = total + score[char]
  return total 

#Problem 7
#Write a function called censor that takes two strings, text and word, as input. It should return the text with the word you chose replaced with asterisk. 
#Example is if you want to censor the string ('this hack is wack hack') and you wan tto censor the word 'hack' then the return should be 'this **** is wack ****'
# Assume your input strings won’t contain punctuation or upper case letters 
# The number of asterisk you put should correspond to the number of letters in the censored word. 

def censor(text,word): 
  length = len(word)
  asterik = '*' * length 
  #prints the appropriate asteriks * because the * symbol gets multiplied by the len of the word 
  new_text = text.replace(word,asterik)
  return new_text

#Problem 8
#Define a function called count that has two arguments called sequence and item. 
#Return the number of times the item occurs in the list 
#for exapmle: count([1,2,1,1]) should return 3 because 1 appears 3 times in the list 
#There is a list method in Python that you can use for this, but you should do it in the long way for practice. 
#Your function should return an integer 
#The item you input may be an integer, string, float, or even another list! 
#Be careful not to use list as a variable name in your code

def count(sequence,item): 
  total = 0 
  for i in sequence: 
    if i == item: 
      total = total +1 
  return total 

#Problem 9 
#Define a function called purify that takes in a list of numbers, removes all odd numbers in the list, and returns the result. For example purify)[1,2,3]) should return [2]. 
#Do not directly modify the list you are given as a input; instead return only the even numbers. 

def purify(number_list): 
  new_list = []
  for number in number_list: 
    if number % 2 == 0: 
      new_list.append(number)
  return new_list 

#Problem 10 
#Define a function called product that takes a list of integers as input and returns the product of all the elements in the list. For example product)[4,5,5]) should return 100 because 4*5*5 = 100. 
#Don't worry about the list being empty 
#Your function should return an integer 

def product(number_list): 
  total = 1
  for number in number_list: 
    total = total * number
  return total  

#Problem 11
#Write a function remove_duplicates that takes in a list and removes elements of the list that are the same. 
#For example: remove_duplicates([1,1,2,2]) should return [1,2]
# Don’t remove every occurrence, since you need to keep a single occurrence of a number 
# The order in which you present your output does not matter. So returning [1,2,3] is the same as returning [3,2,1]
# DO NOT modify the list you take as an input! Return a new list instead. 

def remove_duplicates(list): 
  new_list = []
  for element in list: 
    if element not in new_list: 
      new_list.append(element) 
  return new_list

#Problem 12
#Write a function called median that takes a list as an input and returns the median value of the list. For example: median([1,1,2]) should return 1. 

def median(num_list):
    new_num_list = sorted(num_list)
    x = len(num_list)
    y = len(num_list)-1 
    #to access the list based off of indices since indexes go from 0 to len(list)-1
    if x % 2 != 0: 
    #means if the length of the num_list is not readily divisible by 2
        med = new_num_list[int(y/2)] 
        #Have to do integer conversion because // is division to a whole number. / is division that leads to a float. Don't need a case for when the list has one element because this if statement handles it. 
    else: 
        total = new_num_list[int((x/2)-1)]+new_num_list[int(x/2)] 
        #Note: Round() function in python always rounds down, so you can't depend on using y to access indexes. 
        med = total/2
    return med




