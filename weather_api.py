''' written by B.SasiVatsal on 22nd Jan,2022 '''

# importing all the required libraries
from tkinter import *
import tkinter,requests
from tkinter.font import BOLD
from urllib import response
from tkinter import BOTH
from PIL import ImageTk, Image
from io import BytesIO
from cv2 import FONT_HERSHEY_COMPLEX

''' defining the global varibales that are to be used throught the development '''
sky_blue = "#171010"
green_color = "#EC0101"
output_color = "#F7F6F2"
input_color = "#3D0000"
# defining font style and size, can be changed later
large_font = ('SimSun', 20)
small_font = ('Simsun', 15)

'''============='''
''' driver code '''
'''============='''

# creating an object of TK class
root = tkinter.Tk()
# making a title for the app
root.title("Know the weather")
# adding icon to the app
#root.iconbitmap(r'C:\Users\sasiv\OneDrive\Desktop\TKINTER PROJECT IDEAS\weather_forecast\weather.ico')
# defining dimensions of the appp
root.geometry('500x500')
# making the app non-reszable to avoid scaling issues
root.resizable(0,0)

'''==========='''
''' FUNCTIONS '''
'''==========='''

def get_current_weather():
    ''' grabbing the information requested from the 
        api and displaying it to the user'''
    # gathering data from API
    
    ''' upadating values of variables with the weather information recieved from  the https request to the api'''
    
    city_name = response['name']
    city_lat = str(response['coord']['lat'])
    city_lon = str(response['coord']['lon'])
    main_weather = response['weather'][0]['main']
    description = response['weather'][0]['description']
    tempf = response['main']['temp']
    tempc = (tempf - 32) * 5/9
    temp = str(tempf)
    feels_like = str(response['main']['feels_like'])
    temp_min = str(response['main']['temp_min'])
    temp_max = str(response['main']['temp_max'])
    humidity = str(response['main']['humidity'])

    # updating the gui using label.config() method
    
    test_canvas.itemconfig(city_info_label,text=city_name + " (" + city_lat + ", " + city_lon + ")")
    test_canvas.itemconfig(weather_label,text="Weather:  " + main_weather + ", " + description)
    test_canvas.itemconfig(temp_label,text='Temperature:  ' + temp + " °C")
    test_canvas.itemconfig(feels_label,text="Feels Like:  " + feels_like + " °C")
    test_canvas.itemconfig(temp_min_label,text="Min Temperature:  " + temp_min + " °C")
    test_canvas.itemconfig(temp_max_label,text="Max Temperature:  " + temp_max + " °C")
    test_canvas.itemconfig(humidity_label,text="Humidity:  " + humidity)

''' adding icons depending on climate condition for more user interactivity '''

def get_current_climate_icon():
    global icon
    # getting the icon from API response
    iconss = response['weather'][0]['icon']
    # requesting weather icon from the same api
    url = 'http://openweathermap.org/img/wn/{icon}.png'.format(icon=iconss)
    # after receving the desired icon we have to download it in order to display
    # its can be implemented by giving argument stream=TRUE 
    icon_response = requests.get(url, stream=True)
    img_data = icon_response.content  
    '''The ImageTk module contains support to create and modify 
        Tkinter BitmapImage and PhotoImage objects from PIL images'''
    icon = ImageTk.PhotoImage(Image.open(BytesIO(img_data)))
    #Update label
    test_canvas.create_image(212.5,285,image=icon)


# main function form which everything is operated
def submit_search():
    global response
    url = ' http://api.openweathermap.org/data/2.5/weather'
    api_key = '6127b0e5bba71ee6af34dcb909a5bec9'
    #  get: () -> str, to convert it into the string
    queryy = {"q":cityy_name.get(),'units':'metric','appid':api_key }
    '''Python requests module has several built-in methods to make 
    Http requests to specified URI using GET, POST, 
    PUT, PATCH or HEAD requests
    GET method is used to retrieve information from the given server using a given URI. The GET method sends the encoded user information appended to the page request. 
    The page and the encoded information are separated by the ? character.
    '''
    # calling the api using request method in request module
    response = requests.request("GET",url,params=queryy)
    response = response.json()

    get_current_weather()
    get_current_climate_icon()

'''================================='''
''' making graphical user interface '''
'''================================='''

# making frames using Frame() method in tkinter
up_frame = tkinter.Frame(root, bg=sky_blue, height=350)
down_frame = tkinter.Frame(root,  bg=green_color)
# pack() is method is used to simply pack the attributes we defined in frame()
up_frame.pack(fill=BOTH, expand=True)
down_frame.pack(fill=BOTH, expand=True)

# the weather is displayed in the output frame
'''A labelframe is a simple container widget. 
  Its primary purpose is to act as a spacer or 
  container for complex window layouts. 
  This widget has the features of a frame plus the 
  ability to display a label.'''
# here up_frame() has 1st arg instead of root, coz output is shown inside the upper frame

output_frame = tkinter.LabelFrame(up_frame,bg=output_color, width=425, height=325)
test_canvas = tkinter.Canvas(output_frame,width=425, height=325,bg='blue', highlightthickness=False)
imgg = PhotoImage(file="26383.png")
test_canvas.create_image(212.5,162.5,image=imgg)

''' This section contains the information this app is supposed to show
    things like city name,weather,temperature,min temp,humidity etc 
    which a functional typical weather app displays'''
    
city_info_label = test_canvas.create_text(210,40,text="City_Name",fill="#FF0000",font=(FONT_HERSHEY_COMPLEX,20,'bold'))
weather_label = test_canvas.create_text(212.5,100,text="Weather: ",fill=output_color,font=(FONT_HERSHEY_COMPLEX,15,'bold'))
temp_label = test_canvas.create_text(212.5,130,text='Temperature: ',fill=output_color,font=(FONT_HERSHEY_COMPLEX,15,'bold'))
feels_label = test_canvas.create_text(212.5,160,text="Feels Like: ",fill=output_color,font=(FONT_HERSHEY_COMPLEX,15,'bold'))
temp_max_label = test_canvas.create_text(212.5,190,text="Min Temperature: ",fill=output_color,font=(FONT_HERSHEY_COMPLEX,15,'bold'))
temp_min_label = test_canvas.create_text(212.5,220,text="Max Temperature: ",fill=output_color,font=(FONT_HERSHEY_COMPLEX,15,'bold'))
humidity_label = test_canvas.create_text(212.5,250,text="Humidity: ",fill=output_color,font=(FONT_HERSHEY_COMPLEX,15,'bold'))

input_frame = tkinter.LabelFrame(down_frame, bg=input_color, width=425)
output_frame.pack(pady=30)
'''pack_propagate(0) tells tkinter to let the parent control 
   its own size, rather than letting it's size be determined 
   by the children of the widget when using pack to manage 
   the children.'''
output_frame.pack_propagate(0)
# u know pad is used for passing y for y-side and x for x-side
input_frame.pack(pady=15)
# packing all teh attributes defined in the create_textl() method together
test_canvas.pack()

''' This section contains text field to take user input '''
# The Entry Widget is a Tkinter Widget used to Enter 
# or display a single line of text. 
heading = tkinter.Label(input_frame,text="Enter City name:",font=('SimSun', 15,BOLD), bg=input_color,fg=output_color)
cityy_name = tkinter.Entry(input_frame, width=25, font=('SimSun', 17))
# submit button using button() in tkinetr
submit_button = tkinter.Button(input_frame, text='Search', font=('SimSun', 15,BOLD), bg=input_color,fg=output_color, command=submit_search)
cityy_name.grid(row=1, column=0, padx=(25,0), pady=(0,20))
submit_button.grid(row=1, column=1, padx=20,pady=(0,20))
heading.grid(row=0, column=0,pady=(5,5))


# mainloop() is reason for app to run
root.mainloop()
