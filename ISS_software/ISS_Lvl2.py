'''
1) create a window    X
2) create a func to display a main menu   X
    - Designing the window X
    - writing the window tile X
    - Writing the menu contents X
3) Create a function to GET the astronaut names. X
    - Designing the window X
    - get the data(names) from the web service X
    - extract the data(names) X
    - display it in the window. X
    - Connecting it to the main window/menu. X 
4) Create a function to GET the ISS passtimes
    - Designing the window
    - Inputs (longitude and latitude)
    - GET the data from the web service.
    - extract the data(times)
    - display it in the window.
    - Connect to the main window.
5) Create a function to get the ISS location.
    - Designing the window
    - GET the data from the web service.
    - extract the data(location)
    - display it in the window.
    - Connect to the main window.
    - Store the data
6) Create a database
    - Insert data
    - store data
    - get data
7) Create a function to track the ISS
Designing the window
    - GET the data from the web service.
    - extract the data(location)
    - display it in the window.
    - Connect to the main window.

'''

import turtle
import requests
from datetime import datetime
import sqlite3


#------------------------------------------------------------------------------------
#create a databse
conn = sqlite3.connect('ISSHeadQuarters.db')

#create a cursor
c= conn.cursor()

#create a table in our database
c.execute('create table if not exists ISSdata (Time text, Latitude float, Longitude float, Place text)')

def insert_data(time, latitude, longitude, place):
    with conn:
        c.execute('insert into ISSdata values(?,?,?,?)', (time, latitude, longitude, place))

def delete_data():
    with conn:
        c.execute('delete from ISSdata')
    track_ISS()

def get_data():
    c.execute('select * from ISSdata')
    return c.fetchall()

#-------------------------------------------------------------------------------------
def exitapp():
    window.clearscreen()
    window.bgpic('space.gif')
    window.title('Exit_screen')

    
    ISS = turtle.Turtle()
    ISS.color('white')
    ISS. penup()
    ISS.hideturtle()
    ISS.write('Thank you!', align = 'center', font=('Courier',25,'bold'))
    ISS.goto(0,-20)
    ISS.color('yellow')
    ISS.write('(click anywhere to exit)', align = 'center', font=('Courier',15,'bold'))

    window.exitonclick()

#-------------------------------------------------------------------------------------
def display_message():
    ISS = turtle.Turtle()
    ISS.color('red')
    ISS. penup()
    ISS.hideturtle()
    ISS.goto(0,-80)
    ISS.write('Press M for main menu', align = 'center', font=('Courier',20,'bold'))



#-------------------------------------------------------------------------------------
def track_ISS():
    window.clearscreen()
    window.bgpic('map.gif')
    window.title('tracking ISS')

    ISS = turtle.Turtle()
    ISS.color('red')
    ISS.penup()
    ISS.hideturtle()
    ISS.goto(0,80)
    
    data = get_data()

    if len(data) ==0:
        ISS.write('Database empty!', align = 'center', font = ('Courier',20,'bold'))

    else:
        ISS.write('Press R to reset data', align = 'center', font = ('Courier',20,'bold'))
        
        for i in data:
            time= i[0]
            latitude = i[1]
            longitude = i[2]
            place = i[3]

            
            ISS.goto(longitude, latitude)
            ISS.pendown()
            ISS.dot(6)
            ISS.write("{} {} ".format(time, place), font = ('Courier',10,'bold'))

    display_message()
    window.listen()
    window.onkey(main_menu,'m')
    window.onkey(delete_data, 'r')
#-------------------------------------------------------------------------------------    
def current_location():
    window.clearscreen()
    window.bgpic('map.gif')
    window.title('Current location')

    ISS = turtle.Turtle()
    ISS.color('red')
    ISS.penup()
    ISS.goto(0,80)
    ISS.hideturtle()
    ISS.write('~~Current location of ISS~~', align = 'center', font=('Comic Sans+',20,'bold'))    

    url1 = 'http://api.open-notify.org/iss-now.json'
    response1 = requests.get(url1)
    data1 = response1.json()

    t= data1['timestamp'] #epoch
    time = datetime.fromtimestamp(t)
    longitude = float(data1['iss_position']['longitude'])
    latitude = float(data1['iss_position']['latitude'])

    url2= 'https://us1.locationiq.com/v1/reverse.php?key=316aed2e9d379d'

    dictionary = {'lat' : latitude, 'lon' : longitude, 'format': 'json'}

    response2 = requests.get(url2, params = dictionary)
    data2 = response2.json()
    place = ''

    if response2.status_code == 200:
        place = data2['address']['country']
    else:
        place='( Ocean )'

    ISS.goto(longitude, latitude)
    ISS.dot(8)
    ISS.write('I am here!', align = 'center', font=('Comic Sans+',10,'bold'))
    ISS.right(90)
    ISS.forward(15)
    ISS.write(place, align = 'center', font=('Comic Sans+',10,'bold'))
    

    insert_data(time, latitude, longitude, place)

    
    display_message()
    window.listen()
    window.onkey(main_menu,'m')



#-----------------------------------------------------------------------------------
def ISS_passtimes():
    window.clearscreen()
    window.bgpic('map.gif')
    window.title('Find when I visit you')

    ISS =  turtle.Turtle()
    ISS.penup()
    ISS.color('red')
    ISS.hideturtle()
    ISS.right(90)
    ISS.goto(0,75)

    latitude = window.numinput('Latitude', 'Enter the latitude- ')
    longitude = window.numinput('Longitude', 'Enter the longitude- ')
    
    dictionary = {'lat': latitude, 'lon': longitude}
    
    url2 = 'http://api.open-notify.org/iss-pass.json'
    response = requests.get(url2, params = dictionary)
    
    if response.status_code != 200:
        ISS.write('Invalid Coordinates !', align = 'center', font=('Courier',20,'bold'))
    else:
        data = response.json()
        passtimes = []

        for i in data['response']:
            passtimes.append(i['risetime'])

        ISS.write('Following are the passtimes for the given loaction--', align = 'center', font=('Courier',15,'bold'))
        ISS.goto(longitude, latitude)
        ISS.dot(8)
        for j in passtimes:
            ISS.write(datetime.fromtimestamp(j), font=('Courier',10,'bold'))
            ISS.forward(15)
       

    display_message()
    window.listen()
    window.onkey(main_menu, 'm')




#------------------------------------------------------------------------------------
def  astronaut_names():
    window.clearscreen()
    window.bgpic('space.gif')
    window.title('Astronauts in ISS')
    
    ISS = turtle.Turtle()
    ISS.color('yellow')
    ISS. penup()
    ISS.hideturtle()
    ISS.right(90)
    ISS.goto(0,65)
    ISS.write('The following astronauts are in the ISS :', align = 'center', font=('Courier',20,'bold'))
    
    url = 'http://api.open-notify.org/astros.json' # API to GET the data
    response = requests.get(url)
    data = response.json()


    astronaut_names = []
    for i in data['people']:
        astronaut_names.append(i['name'])

    
    ISS.goto(-150, 50)
    for i in range(len(astronaut_names)):
        ISS.forward(30)
        ISS.color('white')
        ISS.write(" {}. {}".format(i+1,astronaut_names[i]), font=('Courier',20,'bold'))
    

    display_message()
    window.listen()
    window.onkey(main_menu,'m')
    
 

#-------------------------------------------------------------------------------
def main_menu():
    window.clearscreen()
    window.bgpic('space.gif')
    window.title('ISS application- HOME')

    ISS = turtle.Turtle()
    ISS.color('red')
    ISS. penup()
    ISS.hideturtle()
    ISS.goto(0,65)
    ISS.right(90)
    ISS.write('~~~ISS Data station~~~', align = 'center', font=('Courier',26,'bold'))

    ISS.goto(-150,50)
    ISS.color('white')
    ISS.forward(20)
    ISS.write('A. Astronauts in ISS', font=('Courier',18,'bold'))

    ISS.forward(20)
    ISS.write('B. ISS passtimes', font=('Courier',18,'bold'))

    ISS.forward(20)
    ISS.write('C. Check the current location', font=('Courier',18,'bold'))

    ISS.forward(20)
    ISS.write('D. Track the ISS', font=('Courier',18,'bold'))

    ISS.forward(20)
    ISS.write('E. Exit', font=('Courier',18,'bold'))
    
    window.listen()
    window.onkey(astronaut_names, 'a')
    window.onkey(current_location, 'c')
    window.onkey(ISS_passtimes, 'b')
    window.onkey(track_ISS, 'd')
    window.onkey(exitapp, 'e')
    


#create window
window = turtle.Screen()
window.setup(720,360)
window.setworldcoordinates(-180, -90, 180, 90)
main_menu()



window.mainloop()




















