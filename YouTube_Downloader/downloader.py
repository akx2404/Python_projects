#libraries
import turtle
from youtube_search import YoutubeSearch
from pytube import YouTube
import os
import time
import sqlite3

#global var
count = 7



#create a databse
conn = sqlite3.connect('songs.db')

#create a cursor
c= conn.cursor()

#create a table in our database
c.execute('create table if not exists songsdata (title text)')

def insert_data(title):
    with conn:
        c.execute('insert into songsdata values(?)', (title,))

def delete_data():
    with conn:
        c.execute('delete from songsdata')
    history()

def get_data():
    c.execute('select * from songsdata')
    return c.fetchall()



def display_message():
    t = turtle.Turtle()
    t.color('red')
    t. penup()
    t.hideturtle()

    t.goto(0,-290)
    t.write("~~ Press 'M' to go back ~~", align = 'center', font=('Fixedsys',20,'bold'))

    


def history():
    window.clearscreen()
    window.bgpic('background.GIF')
    
    text = turtle.Turtle()
    text.color('white')
    text.penup()
    text.hideturtle()
    text.goto(0,220)
    text.write('~~~ Your list of songs ~~~', align = 'center', font = ("Fixedsys", 30, 'bold'))
    
    data = get_data()
    text.goto(0,-250)
    text.color('red')
    if len(data) ==0:
        text.write('Song list Empty!', align = 'center', font = ('Fixedsys',20,'bold'))

    else:
        text.write('Press "W" to reset data', align = 'center', font = ('Fixedsys',20,'bold'))

    te = turtle.Turtle()
    #print(data)
    te.color('cyan')
    te.penup()
    te.hideturtle()
    te.goto(-400, 170)
    te.right(90)

    for i in range(len(data)):
        te.write('{}: {}'.format(i+1,data[i][0]), font = ('Fixedsys',10,'bold'))
        te.forward(20)

    window.onkey(main_menu, 'm')
    window.onkey(main_menu, 'M')
    window.onkey(delete_data, 'w')
    window.onkey(delete_data, 'W')
    
    display_message()
    
def linkdown():
    songname = ''
    link = ''
    home = os.path.expanduser('~')
    location = os.path.join(home, 'Downloads')
    
    window.clearscreen()
    window.bgpic('background.GIF')

    te = turtle.Turtle()
    te.color('yellow')
    te.speed(-100)
    te.hideturtle()
    te.penup()

    text = turtle.Turtle()
    text.color('white')
    text.speed(-100)
    text.hideturtle()
    text.penup()

    text.goto(0, 190)
    text.write('~~~ Download using YouTube link ~~~', align = 'center', font = ("Fixedsys", 30, 'bold'))

    text.goto(-250, 15)
    text.color('cyan')
    text.write("-> Press 'R' to enter link", align = 'center', font=('Fixedsys',15,'bold'))
    text.goto(-250, -65)
    text.write("->  Press 'D' to\n confirm and download", align = 'center', font=('Fixedsys',15,'bold'))

    #dotted line
    line = turtle.Turtle()
    line.color('green')
    line.speed(0)
    line.width(7)
    line.right(90)
    line.hideturtle()
    line.penup()
    line.goto(-13, 160)
    line.pendown()
    for i in range(10):
        line.forward(20)
        line.penup()
        line.forward(20)
        line.pendown()

    def search2():
        te.clear()
        te.color('yellow')
        te.goto(15, 0)
        global songname, link
        songurl = window.textinput('Search', 'Enter song URL--  ')
        link = songurl
        if 'https://www.youtube.com/' not in songurl:
            te.color('red')
            te.write("Enter valid URL", font=('Fixedsys',15,'bold'))
            te.goto(15, -50)
            te.write("Press 'N' to search again", font=('Fixedsys',15,'bold'))
            window.listen()
            window.onkey(search2, 'n')
            window.onkey(search2, 'N')
        else:
            try:
                te.clear()
                te.write("Fetching song..... Be patient ", font=('Fixedsys',15,'bold'))
                yt_obj = YouTube(link)
                te.clear()
                te.write("Is this the song? - \n{}".format(yt_obj.title), font=('Fixedsys',15,'bold'))
                te.goto(15, -50)
                te.write("Press 'N' to search again".format(yt_obj.title), font=('Fixedsys',15,'bold'))
                window.listen()
                window.onkey(search2, 'n')
                window.onkey(search2, 'N')
                window.onkey(search2, 'r')
                window.onkey(search2, 'R')
                window.onkey(download2, 'd')
                window.onkey(download2, 'D')
                
            except Exception as e:
                print(e)
    
    


    def download2():
        text.clear()
        line.clear()
        te.clear()
        global songname, link
        try:
            yt_obj = YouTube(link)
            te.write("Downloading....Be patient".format(yt_obj.title), align = 'center', font=('Fixedsys',20,'bold'))
            yt_obj.streams.get_audio_only().download(output_path=location, filename=yt_obj.title)
            te.clear()
            te.write("downloaded!".format(yt_obj.title), align = 'center', font=('Fixedsys',20,'bold'))
            insert_data(yt_obj.title)
            time.sleep(2)
            linkdown()
        except Exception as e:
            print(e)
    
    window.listen()
    window.onkey(search2, 'r')
    window.onkey(search2, 'R')
    window.onkey(download2, 'd')
    window.onkey(download2, 'D')
    window.onkey(main_menu, 'm')
    window.onkey(main_menu, 'M')

    display_message()



def search():
    songname = ''
    link = ''
    home = os.path.expanduser('~')
    location = os.path.join(home, 'Downloads')
    
    window.clearscreen()
    window.bgpic('background.GIF')

    te = turtle.Turtle()
    te.color('yellow')
    te.speed(-100)
    te.hideturtle()
    te.penup()

    text = turtle.Turtle()
    text.color('white')
    text.speed(-100)
    text.hideturtle()
    text.penup()

    text.goto(0, 190)
    text.write('~~~ Download by searching ~~~', align = 'center', font = ("Fixedsys", 30, 'bold'))

    text.goto(-250, 15)
    text.color('cyan')
    text.write("-> Press 'S' to Search", align = 'center', font=('Fixedsys',15,'bold'))
    text.goto(-250, -65)
    text.write("->  Press 'D' to\n confirm and download", align = 'center', font=('Fixedsys',15,'bold'))

    def search2():
        te.clear()
        te.color('yellow')
        te.goto(15, 0)
        global songname, link
        songname = window.textinput('Search', 'Enter the song name--  ')
        results = YoutubeSearch('{} song'.format(songname), max_results=10).to_dict()
        link = 'https://www.youtube.com/{}'.format(results[0]['url_suffix'])

        try:
            te.clear()
            te.write("Searching.... please wait ", font=('Fixedsys',15,'bold'))
            yt_obj = YouTube(link)
            te.clear()
            te.write("Is this the song? - \n{}".format(yt_obj.title), font=('Fixedsys',15,'bold'))
            te.goto(15, -50)
            te.write("Press 'N' to search again".format(yt_obj.title), font=('Fixedsys',15,'bold'))
            window.listen()
            window.onkey(search2, 'n')
            window.onkey(search2, 'N')
            window.onkey(search2, 's')
            window.onkey(search2, 'S')
            window.onkey(download2, 'd')
            window.onkey(download2, 'D')
            
        except Exception as e:
            print(e)

    def download2():
        text.clear()
        line.clear()
        te.clear()
        global songname, link
        try:
            yt_obj = YouTube(link)
            te.write("Downloading....Be patient".format(yt_obj.title), align = 'center', font=('Fixedsys',20,'bold'))
            
            yt_obj.streams.get_audio_only().download(output_path=location, filename=yt_obj.title)
            te.clear()
            te.write("downloaded!".format(yt_obj.title), align = 'center', font=('Fixedsys',20,'bold'))
            title = yt_obj.title
            insert_data(title)
            time.sleep(2)
            search()
        except Exception as e:
            print(e)

    window.listen()
    window.onkey(search2, 's')
    window.onkey(search2, 'S')
    window.onkey(download2, 'd')
    window.onkey(download2, 'D')
    window.onkey(main_menu, 'm')
    window.onkey(main_menu, 'M')

    #dotted line
    line = turtle.Turtle()
    line.color('green')
    line.speed(0)
    line.width(7)
    line.right(90)
    line.hideturtle()
    line.penup()
    line.goto(-13, 160)
    line.pendown()
    for i in range(10):
        line.forward(20)
        line.penup()
        line.forward(20)
        line.pendown()

    display_message()
    

def main_menu():
    global count
    window.clearscreen()
    window.bgpic('background.GIF')

    data = get_data()
    count = len(data)
    
    text = turtle.Turtle()
    text.color('white')
    text.speed(-100)
    text.hideturtle()
    text.penup()

    text.goto(0, 190)
    text.write('~~~ Youtube Downloader ~~~', align = 'center', font = ("Fixedsys", 40, 'bold'))

    text.goto(-250, 0)
    text.color('red')
    text.write('Download count-', align = 'center', font = ("Fixedsys", 20, 'bold'))
    text.goto(-250, -65)
    text.write('( {} )'.format(count), align = 'center', font = ("Fixedsys", 35, 'bold'))


    #dotted line
    line = turtle.Turtle()
    line.color('green')
    line.speed(0)
    line.width(7)
    line.right(90)
    line.hideturtle()
    line.penup()
    line.goto(-13, 160)
    line.pendown()
    for i in range(10):
        line.forward(20)
        line.penup()
        line.forward(20)
        line.pendown()


    text.color('yellow')
    text.goto(20, 60)
    text.write('(A). Download by searching', font = ("Fixedsys", 20, 'bold'))
    text.goto(20, 40)
    text.write("(press key 'A')", font = ("Fixedsys", 15, 'bold'))

    text.goto(20, -30)
    text.write('(B). Using Youtube link', font = ("Fixedsys", 20, 'bold'))
    text.goto(20, -50)
    text.write("(press key 'B')", font = ("Fixedsys", 15, 'bold'))

    text.goto(20, -120)
    text.write('(C). View history', font = ("Fixedsys", 20, 'bold'))
    text.goto(20, -140)
    text.write("(press key 'C')", font = ("Fixedsys", 15, 'bold'))

    window.listen()
    window.onkey(search, 'A')
    window.onkey(search, 'a')
    window.onkey(linkdown, 'B')
    window.onkey(linkdown, 'b')
    window.onkey(history, 'c')
    window.onkey(history, 'C')


#create window
window = turtle.Screen()
window.setup(1000, 600)
main_menu()



window.mainloop()


