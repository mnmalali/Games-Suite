import math
import random as ra


#the main part of the program that calls all games
def main():
    while True:
        print('\t\tCHOOSE A GAME\t\t')
        print("==============================")
        print('1- 2-player guess the number \n2- hang man game \n3- math practice\n4- Exit ')
        print("==============================")
        choice=int(input('Enter your choice: '))
        if choice==1:
            main_guessnumber()
        elif choice==2:
            main_hangman()
        elif choice==3:
            main_mathp()
        elif choice==4:
            break
        else:
            print("Invalid option. Please enter a valid option (1-4).")



#this is the part for the dice game
def main_guessnumber():
    total=0
    iden1=0
    iden2=0
    score1=0
    score2=0
    score=f'{score1}X{score2}'
    print('this is a 2-player 3-round dice game. \nthere will be two dice and you must guess the number that is closer to the sum of the numbers given by the two dice')
    print('the person whose guess is closer gets a point')
    for i in range(1,4):
        print(f'Round{i}')
        p1=int(input('player 1 guess(2-12): '))
        p2=int(input('player 2 guess(2-12): '))
        dice1=ra.randint(1,6)
        dice2=ra.randint(1,6)
        total=dice1+dice2
        iden1=math.fabs(total-p1)
        iden2=math.fabs(total-p2)

        if iden1<iden2:
            score1+=1
            score=f'{score1}X{score2}'
        elif iden1>iden2:
            score2+=1
            score=f'{score1}X{score2}'
        else:
            score1+=1
            score2+=1
            score=f'{score1}X{score2}'
        print(f'Dice1={dice1} Dice2={dice2} Total={total} Score= {score}')
        print('-----------------------------------------------------------------------')
    if score1>score2:
        print('Player1 won  :)')
    else:
       print('Player2 won  :)')






#this is the part for the hang-man game
WORD=''
totindex=0
def is_valid(letter):  #validates the input the user gave
    if len(letter)>1 or letter=='':
        return False, 'letter cant be empty or more than one letter!!!'
    if not letter.isalpha():
        return False, "letter must be an alphabetic number!!!"
    return True,''



def getting_word(): #gets a random word from file
    with open('words.txt','r') as wordsfile:
        lines=wordsfile.readlines()
        num_line=len(lines)
        rand_number=ra.randint(1,num_line)
        wordsfile.seek(0)
        for i in range(rand_number):
            word_used=wordsfile.readline().strip('\n')
    global WORD
    WORD=word_used
    return  word_used



dash_list=[]
def display():  #this parts displays the same number of underscores as letters in the word chosen from the file
    for i in range(len(WORD)):
        dash_list.append('_')
    for i in dash_list:
        print(i,end='')


def display2(letter): #this function checks the users guess and displays correctly gussed letters instead of underscores
    global totindex
    indices = [i for i, char in enumerate(WORD) if char == letter]
    for indret in indices:
        if dash_list[indret] == '_':
            del dash_list[indret]
            dash_list.insert(indret, letter)
            totindex += 1
            break  # Stop after revealing one occurrence
    for i in dash_list:
        print(i, end='')




def main_hangman():  #the main part of the program that is used to play this game
    itr=0
    maxtries=6
    getting_word()
    display()
    while totindex<len(WORD) and itr<maxtries :
       itr+=1
       print()
       letter=input('Guess the letter in the word: ').lower()
       valid,massege=is_valid(letter)
       if valid:
            display2(letter)

       else:
            print(massege)
    if itr==maxtries:
        print('Sorry you have lost :(')







#this is the part for the math game

def cont():
    condition=input('Do you want to continue: ').lower()
    if condition=='y' or condition=='yes':
        return True
    else:
        return False



def main_mathp():
    while True:
        print('this game is simple, you will choose an operation two perform on two numbers,\nif you perform the operation correctly you get a point \n')
        print('CHOOSE OPERATION: ')
        print('----------------------------')
        print('1-Addition(+) \n2-Subtraction(-) \n3-Multiplication(*) ')
        choice=int(input('Enter your choice of operation: '))
        if choice==1:
            addition()
            print('Total points= ',totpoint)
            if not cont():
                break

        elif choice==2:
            subtraction()
            print('Total points= ',totpoint)
            if not cont():
                break
        elif choice==3:
            mutiplication()
            print('Total points= ',totpoint)
            if not cont():
                break

        else:
            print("Invalid option. Please enter a valid option (1-4).")
            if not cont():
                break

totpoint=0
num1=ra.randint(1,10)
num2=ra.randint(1,10)
def addition():
    print(f'what is the sum of {num1} + {num2}')
    guess=int(input('Enter your guess: '))
    if guess==(num1+num2):
        print(':) CORRECT!!!!!!!!!')
        global totpoint
        totpoint+=1
    else:
        print(":( SORRY you're incorrect!!!!!")


def subtraction():
    print(f'what is the subtraction of {num1} - {num2}')
    guess=int(input('Enter your guess: '))
    if guess==(num1-num2):
        print(':) CORRECT!!!!!!!!!')
        global totpoint
        totpoint+=1
    else:
        print(":( SORRY you're incorrect!!!!!")


def mutiplication():
    print(f'what is the product of {num1} x {num2}')
    guess=int(input('Enter your guess: '))
    if guess==(num1*num2):
        print(':) CORRECT!!!!!!!!!')
        global totpoint
        totpoint+=1
    else:
        print(":( SORRY you're incorrect!!!!!")


main()
