from datetime import datetime, timedelta
from time import sleep
import PySimpleGUI as sg
from playsound import playsound
import threading

# long_timer_length = 1500
# short_timer_length = 300
long_timer_length = 1500 #change to debug
short_timer_length = 300 #change to debug
counter = 1
timer_type = None



def play_sound():
    playsound('service-bell-ring-14610.mp3')
    

sg.theme('DarkRed1')

layout = [[sg.Button('Start', key='-START-', size=(5, 1), font = ('Helvetica', 20))],
          [sg.Text('Remaining Time:', font=('Arial', 16))],
          [sg.Text("", size=(5, 1), font=('Arial', 60), key='-OUTPUT-')]]

window = sg.Window('Timer', layout)

while True:
    event, values = window.read(timeout=0.1)

    if event == '-START-':
        window['-START-'].update('Stop')
        while True:
            if counter % 2 == 1:
                timer_type = "long"
                start_time = datetime.now()
                end_time = start_time + timedelta(seconds=long_timer_length)
                sg.change_look_and_feel('Default')
            else:
                timer_type = "short"
                start_time = datetime.now()
                end_time = start_time + timedelta(seconds=short_timer_length)
                sg.change_look_and_feel('DarkGreen')
            while datetime.now() < end_time:
                if event == sg.WIN_CLOSED or event == 'Exit':
                    break

                remaining_time = end_time - datetime.now()

                window['-OUTPUT-'].update('{:02d}:{:02d}'.format(remaining_time.seconds // 60, remaining_time.seconds % 60))
                # Read user input again, with a timeout of 0.1 seconds
                event, values = window.read(timeout=0.1)

                if event == '-START-': #pausing
                    window['-START-'].update('Start')
                    while True:
                        event, values = window.read(timeout=0.1)
                        if event == '-START-':
                            window['-START-'].update('Stop')
                            break
                    if timer_type == "long":
                        end_time = datetime.now() + remaining_time
                    else:
                        end_time = datetime.now() + remaining_time

            if event == sg.WIN_CLOSED or event == 'Exit':
                break
            # play sound
            thread = threading.Thread(target=play_sound)
            thread.start()
            counter += 1

    if event == sg.WIN_CLOSED or event == 'Exit':
                break

window.close()