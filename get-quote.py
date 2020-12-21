import random

def primary():
  #print("Keep it logically awesome.")

  f = open("quotes.txt")        #open file
  quotes = f.readlines()        #assign file array to variable quotes
  f.close()                     #close file
  #last = 13                     #variable holding highest index for array
  last = len(quotes) - 1
  rnd = random.randint(0, last) #generate random num between first and last quotes and store it in variable rnd

  print(quotes[rnd])             #print a selected quote based on rnd

if __name__== "__main__":
  primary()
