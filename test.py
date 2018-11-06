#Columbai Business School
#B9122 - Computing for Business Research
#Assignment 1
#
#Lukas Felix Fischer
#LFischer23@gsb.columbia.edu
#
#----------------------------------------------------------------------------------------------------------------------
# Question 1
word = 'aeiou'                          #create a string in which certain characters are to be changed
word_new = word.replace('a', 'i')       #replaces certain characters in the string that is handed over and stores it in new string
print(word_new)                         #print the result

#----------------------------------------------------------------------------------------------------------------------

# Question 2
def crazycalc(n):                       #define a fuction that does the desired computation
    i = 1                               #genreate variable that represents the element in the multiplications
    for x in range(0, n):               #loop over the values up to which the multiplications are to be printed
        j = 1                           #generate another variable which is the element. It is reset to one whenever the the loop finishes
        for x in range(0, n):           #nested for loop to do the computations
            p = i * j                   #define result as p
            print(i, "*", j, "=", p)    #print the result in a nice way
            j += 1                      #increment j s.t. in the next passt i*j+1 is computed
        i += 1                          #increment i when this loop finishes, i.e. i*j \forall j=[0,n] has been computed

crazycalc(3)                            #run this function for a value of 3 to show it works

#----------------------------------------------------------------------------------------------------------------------

# Question 3
sentence = 'this is a long sentence'                                    #store string in variable
sentence_split = sentence.split(' ')                                    #split the sentence at the blanks and store it
sentence_len = []                                                       #generate empty array to store word length
for x in range(0, len(sentence_split)):                                 #for all words in the original sentence do the following
    sentence_len.append(len(sentence_split[x]))                         #compute the length of each word and store in array
sentence_unsorted = list(zip(sentence_len, sentence_split))             #zip the two arrays together to generate new array that contains word,length pairs
sentence_sorted = sorted(sentence_unsorted, key=lambda tup: tup[0])     #sort this array by word length
print(sentence_sorted)                                                  #print the array
# words of same length appear in the same order as in the original string
#----------------------------------------------------------------------------------------------------------------------

# Question 4
fh = open("01b_Question 4.txt")                                 #open the txt file
txt = fh.read()                                                 #store content in variable

txt = txt.lower()                                               #make all words lowercase
txt = txt.replace('\n', ' ')                                    #replace linebreaks with spaces (to make handling easier)

txt_words = txt.split(" ")                                      #split it up into words and store in new variable

word_list = {}                                                  #generate variable for wordlist

for words in txt_words:                                         #for all words in the file store them in the array if not already in there and keep track of frequency
    if words not in word_list:
        word_list[words] = 0
    word_list[words] += 1

n = 5                                                           #set how many of the most freuqent ones are to be displayed
for i in range(0, n):                                           #loop over all of them and print one after the other
    x = sorted(word_list, key=word_list.get, reverse=True)[i]
    print(word_list[x], " ", x)

#----------------------------------------------------------------------------------------------------------------------

# Question 5
import re                                                       #import regular expressions

test_dob = "My Date of Birth isn't 1925-03-28"                  #generate test strings
test_zip5 = "10025 is my zip code"
test_zip9 = "More precisely it is 10025-4567"
test_email = "You can write an emil to lfischer23@gsb.columbia.edu"

# a. yyyy-mm-dd.
dob1=re.search(r'\b(\d{4}[-]\d{2}[-]\d{2})\b', test_dob)
print(dob1.group(1))
    #Easiest version that just looks for digit combinations of the form dddd-dd-dd
    #No check whether date actually makes sense
dob2=re.search(r'\b(\d{4}[-](1[012]|0[1-9])[-]\d{2})\b', test_dob)
print(dob2.group(1))
    #All years are possible but months have to be between 1 and 12, any day (no check for consistency between month and day)

dob3=re.search(r'\b(\d{4}[-](([10-12]|[0][1-9]))[-](([0-3][0-9])(?!-)))\b', test_dob)
print(dob3.group(1))
    #Improved version where only days between 00 and 39 are recognized.

dob4=re.search(r'(\d{4}-(0[1-9]|1[0-2])-(0[1-9]|1[0-9]|2[0-9]|3[0-1]))', test_dob)
print(dob4.group(1))
    #Further improved to consider only days between 01 and 31, not checked for consistency withthe month though
    #I considered that being overkill

# a. xxxxx or xxxxx-xxxx
zip5=re.findall(r'\d{5}', test_zip5)
print(zip5)
    #Simply looks for a combination of five numbers
    #one could add \b to ensure that the spaces before and after the zip are empty

zip9=re.search(r'\b(\d{5}[-]\d{4})\b', test_zip9)
print(zip9.group(1))
    #This assumes that the zip code is always stated in the layout specified above, separated by a -

zip_all5=re.search(r'((\d{5}[-]\d{4})|(\d{5}(?!-)))', test_zip5)
zip_all9=re.search(r'((\d{5}[-]\d{4})|(\d{5}(?!-)))', test_zip9)
print(zip_all5.group(1))
print(zip_all9.group(1))
    #looks for both zip5 and zip9

# a. localpart@domain.com
email=re.search(r'\b(\S+[@]\S+[.]\w+)\b', test_email)
print(email.group(1))
    #\S are used as email addresses can have numbers, dashes, dots etc. in them before as well as after the @
    #For the top level domain (TLD) \w is used as only [a-z] are possible characters
    #+ allows for a wide range of string lengths

#----------------------------------------------------------------------------------------------------------------------

# Question 6
import numpy as np                  #import nunpy

a = np.array([1, 2, 3, 2])          #generate the two arrays
b = np.array([2, 2, 3, 2])

input_len = max(len(a), len(b))     #store length of longer sequence in variable

output = []                         #create empty output

for i in range(1, input_len):       #compare element by element
    if a[i] == b[i]:                #if the same store number of position in array
        output.append(i)            #add this information element by element

print(output)                       #print the result
print("WHAT THE HELL")