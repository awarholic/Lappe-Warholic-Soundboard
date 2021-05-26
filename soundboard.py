import simpleaudio as sa
import PySimpleGUI as sg 
from sound import Sound
# import modules 

 
val = 0
volume = Sound.current_volume

def works_cited():# this def sets up a pop up that shows you our work cited
     layout1 = [[sg.Text('\t\t\t       Works Cited')],
     [sg.Text('In this project we utilized our resources and in the following \n list are some admirable websites we used\n https://pysimplegui.readthedocs.io/en/latest/cookbook/\nhttps://mixkit.co/free-sound-effects/funny/\n https://stackoverflow.com/questions/48830178/what-is-a-cookbook-and-how-is-it-used\n Special thamks to ')],
     [sg.Input(key='-IN-', enable_events=True)],
     [sg.Submit()],
     [sg.Text(size=(25,1), key='-OUTPUT-')]] # establishes the size 
     



              
               
     return sg.Window('Window Title', layout1, finalize=True) # return this to the while loop

slider = sg.Slider(range=(0, 100), default_value=Sound.current_volume, size=(10, 15), orientation="h",
    enable_events=True, key="slider") #enables slider 
   






button1 = [sg.Button("Beep")]

stopall = [sg.Button("Stop sound")]

close = [sg.Button("Close")]

button4 = {sg.Button("Clown")} #this section stores the code for our buttons and text into a variable which makes it easier to read when put into the layout 

button5 = {sg.Button("Sad Trombone")} 

button6 = {sg.Button("Fart")}

playall = [sg.Button("Play All")]

sg.theme('Black') # gives us a nice black theme

layout = [[sg.Text("Welcome to the Soundboard")], button1, button4, button5, button6, playall, stopall, close,  [slider]] #this is the line of code that stores our layout plan. It includes things like where the buttons are and text.

window = sg.Window("Sounboard", layout)
window2 = sg.Window(works_cited())



while True:                 # this while loop keeps our program live, it constantly checks for "events" such as button presses and closing of the window
    event, values = window.read()

    

    
    if event == "Beep":
        filename = 'beep-02.wav'
        sound1 = sa.WaveObject.from_wave_file(filename)
        play_obj = sound1.play()
        #This hold true for the following functions alswell and it is in a loop to constantly checks if the user pressed the required sound button if triggered it plays it's assigned .wav
        
        
    
    if event == "Clown":
        filename = 'clownhrn.wav'
        sound1 = sa.WaveObject.from_wave_file(filename)
        play_obj = sound1.play()
        
    
    
    if event == "Sad Trombone":
        filename = 'tombone.wav'
        sound1 = sa.WaveObject.from_wave_file(filename)
        play_obj = sound1.play()
        

    
    if event == "Fart":
        filename = 'fart.wav'
        sound = sa.WaveObject.from_wave_file(filename)
        play_obj = sound1.play()
        

    if event == "Play All":
        filename = 'clownhrn.wav'
        sound1 = sa.WaveObject.from_wave_file(filename)
        play_obj = sound1.play()
        

        filename = 'beep-02.wav'
        sound1 = sa.WaveObject.from_wave_file(filename)
        play_obj = sound1.play()
        
   
        filename = 'fart.wav'
        sound = sa.WaveObject.from_wave_file(filename)
        play_obj = sound1.play()
        

        filename = 'tombone.wav'
        sound1 = sa.WaveObject.from_wave_file(filename)
        play_obj = sound1.play()
          
    

    
    volume = int(values["slider"])

    if volume %2 != 0: #the slider runs off of an emulation of a keystroke which turns up the volume, the keystroke only goes up by 2 so we have to keep the value set by the slider even
        volume += 1

    Sound.volume_set(volume)# sets the current volume to the slider value

    
    
    if event == "Stop sound": #checks if the stop sound button has been pressed
        sa.stop_all()

    if event == "Close" : #checks if the close button has been pressed
        window.close()
        break 
    if event == sg.WIN_CLOSED: # if the window is closed; break the loop
        break
        
        

window.close() #when the loop is broken the code after the loop is run, this line closes the window. 