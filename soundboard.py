import simpleaudio as sa
import PySimpleGUI as sg
from sound import Sound


 
val = 0
volume = Sound.current_volume

def works_cited():
     layout1 = [[sg.Text('\t\t\t       Works Cited')],
     [sg.Text('In this project we utilized our resources and in the following \n list are some admirable websites we used\n https://pysimplegui.readthedocs.io/en/latest/cookbook/\nhttps://mixkit.co/free-sound-effects/funny/\n https://stackoverflow.com/questions/48830178/what-is-a-cookbook-and-how-is-it-used')],
     [sg.Input(key='-IN-', enable_events=True)],
     [sg.Submit()],
     [sg.Text(size=(25,1), key='-OUTPUT-')]]
     



              
               
     return sg.Window('Window Title', layout1, finalize=True)

slider = sg.Slider(range=(0, 100), default_value=Sound.current_volume, size=(10, 15), orientation="h",
    enable_events=True, key="slider")
   






button1 = [sg.Button("Beep")]

stopall = [sg.Button("Stop sound")]

close = [sg.Button("Close")]

button4 = {sg.Button("Clown")}

button5 = {sg.Button("Sad Trombone")} 

button6 = {sg.Button("Fart")}

playall = [sg.Button("Play All")]

sg.theme('Black')

layout = [[sg.Text("Welcome to the Soundboard")], button1, button4, button5, button6, playall, stopall, close,  [slider]]

window = sg.Window("Sounboard", layout)
window2 = sg.Window(works_cited())



while True:
    event, values = window.read()

    # window2.move(window2.current_location()[0], window2.current_location()[1]+2200)

    
    if event == "Beep":
        filename = 'beep-02.wav'
        sound1 = sa.WaveObject.from_wave_file(filename)
        play_obj = sound1.play()
        
        
    
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

    if volume %2 != 0: 
        volume += 1

    Sound.volume_set(volume)

    print(volume)
    
    if event == "Stop sound": 
        sa.stop_all()

    if event == "Close" :
        window.close()
        break 
    if event == sg.WIN_CLOSED:
        break
        
        

window.close()