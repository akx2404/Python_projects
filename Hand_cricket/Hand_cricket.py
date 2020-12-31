import turtle
import random
import time

pscore = 0
cscore = 0
player = ''
comp = ''
count = 1
key = 'on'

scoreboard = turtle.Turtle()
scoreboard.hideturtle()
scoreboard.penup()

def exit_app():
    global key
    key = 'off'

def comp_won():
    global count
    global pscore
    global cscore

    count = 1
    pscore = 0
    cscore = 0
    
    window.clearscreen()
    window.bgcolor('red')
    text = turtle.Turtle()
    text.penup()
    text.hideturtle()
    text.write("Comp won!!", align = 'center', font=("Comic Sans MS", 35, 'bold'))

    text.goto(0,-35)
    text.write("~~~~~Press 'Enter' to restart the game~~~~~", align='center', font=("Comic Sans MS", 25, 'bold'))
    text.goto(0,-45)
    text.write("~~~~~Press 'Escape' to exit the game~~~~~", align='center', font=("Comic Sans MS", 25, 'bold'))

    window.listen()
    window.onkey(game, 'Return')
    window.onkey(exit_app, 'Escape')
    


def player_won():
    global count
    global pscore
    global cscore

    count = 1
    pscore = 0
    cscore = 0
    
    window.clearscreen()
    window.bgcolor('chartreuse')
    text = turtle.Turtle()
    text.penup()
    text.hideturtle()
    text.write("You won!", align = 'center', font=("Comic Sans MS", 35, 'bold'))

    text.goto(0,-35)
    text.write("~~~~~Press 'Enter' to restart the game~~~~~", align='center', font=("Comic Sans MS", 25, 'bold'))
    text.goto(0,-45)
    text.write("~~~~~Press 'Escape' to exit the game~~~~~", align='center', font=("Comic Sans MS", 25, 'bold'))

    window.listen()
    window.onkey(game, 'Return')
    window.onkey(exit_app, 'Escape')
    
    
def player_bat():
    global count
    global pscore
    global cscore


    plr = turtle.Turtle()
    plr.hideturtle()
    plr.penup()
    plr.goto(40,0)

    cmp = turtle.Turtle()
    cmp.hideturtle()
    cmp.penup()
    cmp.goto(-40,0)

    scoreboard.clear()
    scoreboard.penup()

    if count == 1:
        scoreboard.goto(0,35)
        scoreboard.write("~~ Your score - {} ~~".format(pscore), align = 'center', font=("Comic Sans MS", 20, 'bold'))
        
        while True:
            plr.hideturtle()
            cmp.hideturtle()
            cruns = random.randint(1,6)
            pruns = int(window.textinput('Hey!' , '---- Enter runs ----'))
            plr.showturtle()
            cmp.showturtle()
            plr.shape('{}.GIF'.format(pruns))
            cmp.shape('{}.GIF'.format(cruns))
            if pruns != cruns:
                pscore = pscore + pruns
                scoreboard.clear()
                scoreboard.write("~~ Your score - {} ~~".format(pscore), align = 'center', font=("Comic Sans MS", 20, 'bold'))
            else:
                count = 2
                scoreboard.clear()
                scoreboard.write("OUT!! --- Your turn to bowl!".format(pscore), align = 'center', font=("Comic Sans MS", 30, 'bold'))
                time.sleep(2)
                plr.hideturtle()
                cmp.hideturtle()
                comp_bat()
                break
                
            time.sleep(1)

    elif count == 2:
        scoreboard.goto(0,35)
        scoreboard.write("~~ Your score - {} ~~".format(pscore), align = 'center', font=("Comic Sans MS", 20, 'bold'))
        scoreboard.goto(0,25)
        scoreboard.write("Target - {} ~~".format(cscore), align = 'center', font=("Comic Sans MS", 20, 'bold'))
        
        
        while pscore <= cscore:
            plr.hideturtle()
            cmp.hideturtle()
            cruns = random.randint(1,6)
            pruns = int(window.textinput('Hey!' , '---- Enter runs ----'))
            plr.showturtle()
            cmp.showturtle()
            plr.shape('{}.GIF'.format(pruns))
            cmp.shape('{}.GIF'.format(cruns))
            if pruns != cruns:
                pscore = pscore + pruns
                scoreboard.clear()
                scoreboard.goto(0,35)
                scoreboard.write("~~ Your score - {} ~~".format(pscore), align = 'center', font=("Comic Sans MS", 20, 'bold'))
                scoreboard.goto(0,25)
                scoreboard.write("Target - {} ~~".format(cscore), align = 'center', font=("Comic Sans MS", 20, 'bold'))
            else:
                scoreboard.clear()
                scoreboard.write("OUT!!".format(pscore), align = 'center', font=("Comic Sans MS", 30, 'bold'))
                time.sleep(2)
                plr.hideturtle()
                cmp.hideturtle()
                comp_won()
                break
            time.sleep(1)
            
        else:
            time.sleep(2)
            player_won()
        time.sleep(1)

def comp_bat():
    global pscore
    global cscore
    global count

    plr = turtle.Turtle()
    plr.hideturtle()
    plr.penup()
    plr.goto(40,0)

    cmp = turtle.Turtle()
    cmp.hideturtle()
    cmp.penup()
    cmp.goto(-40,0)

    scoreboard.clear()
    scoreboard.penup()


    if count == 1:
        
        scoreboard.goto(0,35)
        scoreboard.write("~~ Opponent's score - {} ~~".format(cscore), align = 'center', font=("Comic Sans MS", 20, 'bold'))
        
        while True:
            plr.hideturtle()
            cmp.hideturtle()
            cruns = random.randint(1,6)
            pruns = int(window.textinput('Hey!' , '---- Enter runs ----'))
            plr.showturtle()
            cmp.showturtle()
            plr.shape('{}.GIF'.format(pruns))
            cmp.shape('{}.GIF'.format(cruns))
            if cruns != pruns:
                cscore = cscore + cruns
                scoreboard.clear()
                scoreboard.write("~~ Opponent's score - {} ~~".format(cscore), align = 'center', font=("Comic Sans MS", 20, 'bold'))
            else:
                count = 2
                scoreboard.clear()
                scoreboard.write("OUT!! --- Your turn to bat!".format(pscore), align = 'center', font=("Comic Sans MS", 30, 'bold'))
                time.sleep(2)
                plr.hideturtle()
                cmp.hideturtle()
                player_bat()
                break
                
            time.sleep(1)

    elif count == 2:
        scoreboard.goto(0,35)
        scoreboard.write("~~ Opponent's score - {} ~~".format(cscore), align = 'center', font=("Comic Sans MS", 20, 'bold'))
        scoreboard.goto(0,25)
        scoreboard.write("Target - {} ~~".format(pscore), align = 'center', font=("Comic Sans MS", 20, 'bold'))
        
        
        while cscore <= pscore:
            plr.hideturtle()
            cmp.hideturtle()
            cruns = random.randint(1,6)
            pruns = int(window.textinput('Hey!' , '---- Enter runs ----'))
            plr.showturtle()
            cmp.showturtle()
            plr.shape('{}.GIF'.format(pruns))
            cmp.shape('{}.GIF'.format(cruns))
            if cruns != pruns:
                cscore = cscore + cruns
                scoreboard.clear()
                scoreboard.goto(0,35)
                scoreboard.write("~~ Opponent's score - {} ~~".format(cscore), align = 'center', font=("Comic Sans MS", 20, 'bold'))
                scoreboard.goto(0,25)
                scoreboard.write("Target - {} ~~".format(pscore), align = 'center', font=("Comic Sans MS", 20, 'bold'))
            else:
                scoreboard.clear()
                scoreboard.write("OUT!!".format(pscore), align = 'center', font=("Comic Sans MS", 30, 'bold'))
                time.sleep(2)
                plr.hideturtle()
                cmp.hideturtle()
                player_won()
                break

            time.sleep(1)
        else:
            time.sleep(2)
            comp_won()
        time.sleep(1)
        



        
            
def game():
    global pscore
    global cscore
    global player
    global comp 
    window.clearscreen()
    window.bgpic('ground.gif')
    
    text = turtle.Turtle()
    text.penup()
    text.hideturtle()

    text.right(90)
    text.goto(0,30)
    text.write("Starting a new game....", align = 'center', font=("Comic Sans MS", 15, 'bold'))
    time.sleep(2)
    text.forward(10)
    text.write(".....", align = 'center', font=("Comic Sans MS", 15, 'bold'))
    time.sleep(2)
    text.forward(10)
    text.write("Mowing grass....", align = 'center', font=("Comic Sans MS", 15, 'bold'))
    time.sleep(2)
    text.forward(10)
    text.write(".....", align = 'center', font=("Comic Sans MS", 15, 'bold'))
    time.sleep(2)
    text.forward(10)
    text.write("Preparing the pitch....", align = 'center', font=("Comic Sans MS", 15, 'bold'))
    time.sleep(2)
    text.forward(10)
    text.write(".....", align = 'center', font=("Comic Sans MS", 15, 'bold'))
    time.sleep(2)
    text.forward(10)
    text.write("Opponent team getting ready....", align = 'center', font=("Comic Sans MS", 15, 'bold'))
    time.sleep(2)
    text.clear()
    text.goto(0,0)
    text.write("3", align = 'center', font=("Comic Sans MS", 35, 'bold'))
    time.sleep(1)
    text.clear()
    text.write("2", align = 'center', font=("Comic Sans MS", 35, 'bold'))
    time.sleep(1)
    text.clear()
    text.write("1", align = 'center', font=("Comic Sans MS", 35, 'bold'))
    time.sleep(1)
    text.clear()

    text.write(".....", align = 'center', font=("Comic Sans MS", 35, 'bold'))
    time.sleep(1)
    text.clear()
    text.write(".....", align = 'center', font=("Comic Sans MS", 35, 'bold'))
    time.sleep(1)
    text.clear()

    text.write("And it's time for the toss !", align = 'center', font=("Comic Sans MS", 35, 'bold'))
    time.sleep(3)
    text.clear()
    toss = window.textinput('Hey!' , '---- heads or tails? ----')
    tosslist = ['heads', 'tails']
    randtoss = random.randint(0,1)
    if toss == tosslist[randtoss]:
        text.write("{} it is!".format(toss), align='center', font=("Comic Sans MS", 20, 'bold'))
        time.sleep(2)
        text.clear()
        selection = window.textinput('Hey!' , '---- bat or field? ----')
        if selection == 'bat':
            player = 'bat'
        elif selection == 'field':
            comp = 'bat'
            
        text.write("You opted to {} first".format(selection), align='center', font=("Comic Sans MS", 20, 'bold'))
        time.sleep(2)
        text.clear()
        
    else:
        text.write("You lost!", align='center', font=("Comic Sans MS", 20, 'bold'))
        time.sleep(2)
        text.clear()
        selectlist = ['bat', 'field']
        randselect = random.randint(0,1) #bat or field
        if randselect == 0:
            comp = 'bat'
        elif randselect == 1:
            player = 'bat'
            
        text.write("Opponent opted to {} first".format(selectlist[randselect]), align='center', font=("Comic Sans MS", 20, 'bold'))
        time.sleep(2)
        text.clear()    
            
    text.goto(0,-47)
    text.write("~~~~~Press 'Escape' to go back~~~~~", align='center', font=("Comic Sans MS", 15, 'bold'))

    plabel = turtle.Turtle()
    plabel.hideturtle()
    plabel.penup()
    plabel.speed(-10)
    plabel.goto(40, -27)
    plabel.write("(You)", align='center', font=("Comic Sans MS", 10, 'bold'))
    plabel.goto(-40, -27)
    plabel.write("(Comp)", align='center', font=("Comic Sans MS", 10, 'bold'))

    if player == 'bat':
        player_bat()
    elif comp == 'bat':
        comp_bat()
    
    
    window.listen()
    window.onkey(main_page, 'Escape')

def main_page():
    global key

    if key == 'off':
        turtle.bye()
        
    window.clearscreen()
    window.bgpic('mainpage.GIF')
    player_name = window.textinput('Hey!' , 'Enter your name please..')

    text = turtle.Turtle()
    text.penup()
    text.hideturtle()
    text.goto(0,35)
    text.color('DarkOrange')
    text.write("Welcome {} !".format(player_name), align = 'center', font=("Broadway", 50, 'underline'))

    text.goto(-90,20)
    text.right(90)
    text.color('Black')
    text.write("Instructions for the game -- ", font=("Comic Sans MS", 25, 'underline', 'bold'))
    text.color('black')
    
    instructions = ['This is the classic hand cricket game', 'You can enter a value from 1 to 6',
                    'You will compete with the computer', 'If you both play the same value, you get out!']

    for i in range(len(instructions)):
        text.forward(10)
        text.write("{}) {}.".format(i+1, instructions[i]), move=False, font=("Comic Sans MS", 16, 'bold'))

    text.color('yellow')
    text.goto(0,-45)
    text.write("~~~~~Press 'Enter' to start the game~~~~~", align='center', font=("Comic Sans MS", 25, 'bold'))

    window.listen()
    window.onkey(game, 'Return')


window = turtle.Screen()
window.title('Welcome to Hand-Cricket !')
window.setup(1000,500)
window.setworldcoordinates(-100, -50, 100, 50)
turtle.register_shape('1.GIF')
turtle.register_shape('2.GIF')
turtle.register_shape('3.GIF')
turtle.register_shape('4.GIF')
turtle.register_shape('5.GIF')
turtle.register_shape('6.GIF')
if key == 'off':
    turtle.bye()
main_page()



window.mainloop()
