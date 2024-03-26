def colored(original_str, color='black', attrs=['normal']):
  ''' This function returns the provided original_str printed with the color and attribute options
  color should be an option from - black, white, grey, green, yellow, red, blue
  attrs should be a list with just one entry from - bold, light, normal, italicized, underlined
  e.g. 
  colored_string = colored('hello', color='white', attrs=['light'])
  colored_string = colored('hello', color='green', attrs=['bold'])
  The colored string returned by the fn is only displayed in color when displayed with the print function.
  print(colored_string)
  ''' 

  attribute_dict = {
      'bold'        : 1,
      'light'       : 2,
      'normal'      : 0,
      'italicized'  : 3, 
      'underlined'  : 4,
  }
  bold_code = attribute_dict[attrs[0]]
  
  colors_dict = {
      'black'   : 30,
      'red'     : 31,
      'green'   : 32,
      'yellow'  : 33,
      'blue'    : 34,
      'white'   : 37,
      'grey'    : 37,
      'gray'    : 37,
  }
  color_code = colors_dict[color]
  
  result = '\033['+ str(bold_code) + ';' + str(color_code) + 'm' + original_str + '\033[0;0m'
  return result

print(colored('hello', color='green', attrs=['bold']))
print(colored('hello', color='yellow', attrs=['light']))
print(colored('hello', color='white', attrs=['normal']))
print(colored('hello', color='gray', attrs=['bold']))

import random
import requests
import json
def colored(original_str, color, attrs):
  ''' This function returns the provided original_str printed with the color and attribute options
  color should be an option from - black, white, grey, green, yellow, red, blue
  attrs should be a list with just one entry from - bold, light, normal, italicized, underlined
  e.g. 
  colored_string = colored('hello', color='white', attrs=['light'])
  colored_string = colored('hello', color='green', attrs=['bold'])
  The colored string returned by the fn is only displayed in color when displayed with the print function.
  print(colored_string)
  ''' 

  attribute_dict = {
      'bold'        : 1,
      'light'       : 2,
      'normal'      : 0,
      'italicized'  : 3, 
      'underlined'  : 4,
  }
  bold_code = attribute_dict[attrs[0]]
  
  colors_dict = {
      'black'   : 30,
      'red'     : 31,
      'green'   : 32,
      'yellow'  : 33,
      'blue'    : 34,
      'white'   : 37,
      'grey'    : 37,
      'gray'    : 37,
  }
  color_code = colors_dict[color]
  result = '\033['+ str(bold_code) + ';' + str(color_code) + 'm' + original_str + '\033[0;0m'
  return result

def update_qwerty(self, input):
  #updates the self.qwerty_str with the right colors - green(correct letter and position so far)
  #and yellow(correct letter so far) and ‘white’(no occurrence in self.correct_word) for all the letters that have been tried by the user so far

  for i in range(0,len(input)):
    for j in range(0,len(self.qwerty_lis)):
      if input[i] == self.qwerty_lis[j]:
        self.qwerty_colors[j] = self.colors[i]
        self.qwerty_desc[j] = ['bold']

  for i in range(0,len(self.qwerty_lis)):
    temp = colored(self.qwerty_lis[i], color=self.qwerty_colors[i], attrs=self.qwerty_desc[i])
    print(temp, end=' ')

def display_word(self, input):
  let1 = colored(input[0], color=self.colors[0], attrs=['bold'])
  let2 = colored(input[1], color=self.colors[1], attrs=['bold'])
  let3 = colored(input[2], color=self.colors[2], attrs=['bold'])
  let4 = colored(input[3], color=self.colors[3], attrs=['bold'])
  let5 = colored(input[4], color=self.colors[4], attrs=['bold'])
  print('{}{}{}{}{}'.format(let1,let2,let3,let4,let5))
  update_qwerty(self, input)

def check_letter(self,input, correct):
  #checks whether the letter and position of the letter against the self.correct_word to determine whether the 
  #letter should be green(correct letter and correct position), yellow(correct letter and wrong position) or grey(letter not present in self.correct_word)
  
  found = []

  for j in range(0,len(input)):  
    count1 = 0 #green
    count2 = 0 #yellow

    for i in range(0,len(correct)):
      if(correct[i] == input[j]) and i == j:
        count1 = count1 + 1
      elif(correct[i] == input[j]):
        count2 = count2 + 1

    if count1 != 0:
      self.colors.append('green')
    elif count2 > 0:
      self.colors.append('yellow')
    elif(count1 == 0 and count2 == 0):
      self.colors.append('grey')
   
  
  display_word(self, input)
  
 
    

def break_letters(self):
    #breaks the self.this_word into its individual letters and uses self.check_letter(letter, position) to figure out what color the letter should be assigned.
    input_letters = list(self.this_word)
    correct_letters = list(self.correct_word)
    #print(input_letters)
    #print(correct_letters)
    
    check_letter(self,input_letters,correct_letters)

def is_word(self):
    #returns true if the self.this_word is a real word. It makes a call to the dictionary api to determine this.
    #the url is coming back as a string despite it looking like a dictionary
    rand = random.randint(0,len(self.words_list))
    temp2 = self.words_list[rand]
    temp2 = temp2.upper()
    self.correct_word = temp2
    print('You have 6 tries, good luck!')
    while(self.tries < 7):
      print()
      self.colors = []
      temp = input('Enter your five letter guess - Trial {}: '.format(self.tries))
      temp = temp.upper()
      self.this_word = temp
    

      url = 'https://api.dictionaryapi.dev/api/v2/entries/en/' + self.this_word 
      data = requests.get(url).text
      if len(self.this_word) > 5 or len(self.this_word) < 5 :
        print('Not correct length, you lost a turn!')
        self.tries = self.tries + 1
      elif (data[10] == 'N' and data[11] == 'o' and data[12] == ' '):
        print('Not a real word, try again!')
      elif (len(self.this_word) ) == 5:
        self.tries = self.tries + 1
        break_letters(self)
      count = 0
      for i in self.colors:
        if i == 'green':
          count = count+1
      if count > 4:
        print('You guessed correct!')
        self.tries = 7
    print('The correct word is {}!'.format(self.correct_word))

def wordle(self):
 #calling this method runs the entire game - sets a new correct word, gets input from user, shows output to user
  print()

class WordleGame(object):
  def __init__(self):
    self.words_list = []
    self.correct_word = ''
    self.this_word = ''
    self.colors = []
    self.tries = 1
    self.qwerty_lis = ['Q', 'W','E','R','T','Y','U','I','O','P','A','S','D','F','G','H','J','K','L','Z','X','C','V','B','N','M']
    self.qwerty_colors = ['black','black','black','black','black','black','black','black','black','black','black','black','black',
                          'black','black','black','black','black','black','black','black','black','black','black','black','black',]
    self.qwerty_desc = [['normal'],['normal'],['normal'],['normal'],['normal'],['normal'],['normal'],['normal'],['normal'],['normal'],['normal'],['normal'],['normal'],
                        ['normal'],['normal'],['normal'],['normal'],['normal'],['normal'],['normal'],['normal'],['normal'],['normal'],['normal'],['normal'],['normal']]
    self.filename = 'words.txt'

    self.api_url = 'https://api.dictionaryapi.dev/api/v2/entries/en/'
  def load_file(self):
    #loads the file into self

    fh = open('words.txt')
    data = fh.readlines()
    fh.close()
    for item in data:
      item = item.rstrip('\n')
      self.words_list.append(item)
    #print(self.correct_word)
    is_word(self)


w1 = WordleGame()
w1.load_file()

