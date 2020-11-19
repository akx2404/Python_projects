import turtle
import random
import time

flag=1

def game():
    global flag
    window.clearscreen()
    window.bgcolor('gold')

    text = turtle.Turtle()
    text.penup()
    text.hideturtle()

    text.write("The computer is thinking of a number ....", align = 'center', font=('Comic Sans MS',25, 'bold'))
    time.sleep(3)
    text.clear()
    text.write("3", align = 'center', font=('Comic Sans MS',30, 'bold'))
    time.sleep(0.5)
    text.clear()
    text.write("2", align = 'center', font=('Comic Sans MS',30, 'bold'))
    time.sleep(0.5)
    text.clear()
    text.write("1", align = 'center', font=('Comic Sans MS',30, 'bold'))
    time.sleep(0.5)
    text.clear()
    text.write("All the best !", align = 'center', font=('Comic Sans MS',30, 'bold'))
    time.sleep(0.5)
    text.clear()

    text.goto(0,230)
    text.write("Guess the number !", align = 'center', font=("Broadway", 50, 'underline'))

    def giveup():
        window.clearscreen()
        window.bgcolor('red')
        ans = turtle.Turtle()
        ans.hideturtle()
        ans.penup()
        ans.goto(0,50)
        ans.write("You Lost :(".format(n), align = 'center', font=('Comic Sans MS',60, 'bold'))
        ans.goto(0,0)
        ans.write("The number was - {} ".format(n), align = 'center', font=('Comic Sans MS',40, 'bold'))

    def win():
        window.clearscreen()
        window.bgcolor('chartreuse')
        ans = turtle.Turtle()
        ans.hideturtle()
        ans.penup()
        ans.goto(0,50)
        ans.write("You win :)".format(n), align = 'center', font=('Comic Sans MS',60, 'bold'))
        ans.goto(0,0)
        ans.write("The number was - {} ".format(n), align = 'center', font=('Comic Sans MS',40, 'bold'))

    
    text.goto(0,-275)
    text.color('maroon')
    text.write("~~~~~Press 'G' to giveup~~~~~", align='center', font=("Comic Sans MS", 25, 'bold'))
    window.listen()
    window.onkey(giveup, 'g')
    window.onkey(giveup, 'G')

    n = random.randint(0, 100)
    print(type(n))
    
    #clue1-----------------------------
    for i in range(2,n,1):
        if n%i==0:
            flag = 0

    if flag ==0:
        
        if n>50:
            clue1="The number is a composite number greater than 50"
        else:
            clue1="The number is a composite number less than 50"
            
        if n%2==0:
            clue2="The number is an even number"
            if n%3==0:
                clue4="The number is divisible by 6 as well"
            elif n%4==0:
                clue4="The number is divisible by 4 as well"
            else:
                clue4="The number is neither divisble by 4 nor by 6"
        else:
            clue2="The number is an odd number"
            if n%7==0:
                clue4="The number is divisible by 7 as well"
            elif n%5==0:
                clue4="The number is divisible by 5 as well"
            else:
                clue4="The number is neither divisble by 7 nor by 5"
                
    else:
        clue1="The number is a prime number"
        if n>50:
            clue2="The number is greater than 50"
            if n>75:
                clue4="The number is greater than 75"
            else:
                clue4="The number is less than 75"
        else:
            clue2="The number is less than 50"
            if n>25:
                clue4="The number is greater than 25"
            else:
                clue4="The number is less than 25"

    nn= n%10
    clue3="the number has {} in ones place".format(nn)
    
    
    

    
    
    text.goto(-320,135)
    text.right(90)
    num1 = int(window.textinput('1' , 'Enter your first guess..'))
    text.color('black')
    text.write("Your first guess -- {}".format(num1), font=("Comic Sans MS", 16, 'bold'))
    if num1!=n:
        text.forward(20)
        text.color('red')
        text.write("You are wrong :( ", font=("Comic Sans MS", 16, 'normal'))
        text.forward(60)
        text.color('black')
            
        text.write("Clue 1: {} ".format(clue1), font=("Comic Sans MS", 16, 'normal'))
        num2 = int(window.textinput('2' , 'Enter your second guess..'))
        text.color('black')
        text.forward(20)
        text.write("Your second guess -- {}".format(num2), font=("Comic Sans MS", 16, 'bold'))                                                
        if num2!=n:
            text.forward(20)
            text.color('red')
            text.write("You are wrong :( ", font=("Comic Sans MS", 16, 'normal'))
            text.forward(40)
            text.color('black')

            text.write("Clue 2: {} ".format(clue2), font=("Comic Sans MS", 16, 'normal'))
            num3 = int(window.textinput('3' , 'Enter your third guess..'))
            text.color('black')
            text.forward(20)
            text.write("Your third guess -- {}".format(num3), font=("Comic Sans MS", 16, 'bold'))                                                
            if num3!=n:
                text.forward(20)
                text.color('red')
                text.write("You are wrong :( ", font=("Comic Sans MS", 16, 'normal'))
                text.forward(40)
                text.color('black')

                text.write("Clue 3: {} ".format(clue3), font=("Comic Sans MS", 16, 'normal'))
                num4 = int(window.textinput('4' , 'Enter your fourth guess..'))
                text.color('black')
                text.forward(20)
                text.write("Your fourth guess -- {}".format(num4), font=("Comic Sans MS", 16, 'bold'))                                                
                if num4!=n:
                    text.forward(20)
                    text.color('red')
                    text.write("You are wrong :( ", font=("Comic Sans MS", 16, 'normal'))
                    text.forward(40)
                    text.color('black')

                    text.write("Clue 4: {} ".format(clue4), font=("Comic Sans MS", 16, 'normal'))
                    num5 = int(window.textinput('5' , 'Enter your fifth guess..'))
                    text.color('black')
                    text.forward(20)
                    text.write("Your fifth guess -- {}".format(num5), font=("Comic Sans MS", 16, 'bold'))                                                
                    if num5!=n:
                        text.forward(20)
                        text.color('red')
                        text.write("You are wrong :( ", font=("Comic Sans MS", 16, 'normal'))
                        text.forward(40)
                        text.color('black')
                        giveup()

                    else:
                        win()
                else:
                    win()
            else:
                win()
        else:
            win()
    else:
        win()
                                                         
                              
                                                                                        

def mainwindow():
    window.clearscreen()
    window.bgcolor('DarkOrange')
    player_name = window.textinput('Hey!' , 'Enter your name please..')

    #text on first window
    text = turtle.Turtle()
    text.penup()
    text.hideturtle()
    text.goto(0,230)
    text.color('navy')
    text.write("Welcome {} !".format(player_name), align = 'center', font=("Broadway", 50, 'underline'))

    text.goto(-320,135)
    text.right(90)
    text.color('maroon')
    text.write("Instructions for the game -- ", font=("Comic Sans MS", 25, 'underline', 'bold'))
    text.color('black')
    
    instructions = ['The theme of the game is that you have to guess the number (0-100)', 'You will get only 5 chances and 4 clues',
                    'With every clue you use, you lose 20 points', 'You can earn a maximum of 100 points']

    for i in range(len(instructions)):
        text.forward(80)
        text.write("{}) {}.".format(i+1, instructions[i]), font=("Comic Sans MS", 16, 'normal'))

    text.color('maroon')
    text.goto(0,-275)
    text.write("~~~~~Press 'Enter' to start the game~~~~~", align='center', font=("Comic Sans MS", 25, 'bold'))

    window.listen()
    window.onkey(game, 'Return')
    

#create window
window = turtle.Screen()
window.title('Number guessing')
window.screensize(450,450)
mainwindow()



window.mainloop()
