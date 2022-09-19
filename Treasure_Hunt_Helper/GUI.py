import PySimpleGUI as sg

sg.theme('Black')


layout =[[sg.Text('First', size=(20,1), font='Lucida, 20', justification='left')],
         [sg.Combo(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I'], size=(20, 30), font='Lucida, 13', key='first')],
         [sg.Radio('In the row and in the correct spot', "RADIO1", font='Lucida,10' ,default=False)],
         [sg.Radio('In the row but in the wrong spot', "RADIO1", font='Lucida,10', default=True)],
         [sg.Radio('Not in the row in any spot', "RADIO1", font='Lucida,10', default=True)],
         [sg.Text('Second', size=(20, 1), font='Lucida, 20', justification='left')],
         [sg.Combo(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I'], size=(20, 30), font='Lucida, 13', key='second')],
         [sg.Radio('In the row and in the correct spot', "RADIO2", font='Lucida,10', default=False)],
         [sg.Radio('In the row but in the wrong spot', "RADIO2", font='Lucida,10', default=True)],
         [sg.Radio('Not in the row in any spot', "RADIO2", font='Lucida,10', default=True)],
         [sg.Text('Third', size=(20, 1), font='Lucida, 20',  justification='left')],
         [sg.Combo(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I'], size=(20, 30), font='Lucida, 13', key='third')],
         [sg.Radio('In the row and in the correct spot', "RADIO3", font='Lucida,10', default=False)],
         [sg.Radio('In the row but in the wrong spot', "RADIO3", font='Lucida,10', default=True)],
         [sg.Radio('Not in the row in any spot', "RADIO3", font='Lucida,10',  default=True)],
         [sg.Text('Fourth', size=(20, 1), font='Lucida, 20', justification='left')],
         [sg.Combo(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I'], size=(20, 30), font='Lucida, 13', key='fourth')],
         [sg.Radio('In the row and in the correct spot', "RADIO4", font='Lucida,10', default=False)],
         [sg.Radio('In the row but in the wrong spot', "RADIO4", font='Lucida,10', default=True)],
         [sg.Radio('Not in the row in any spot', "RADIO4", font='Lucida,10', default=True)],
         [sg.Text('Fifth', size=(20, 1), font='Lucida, 20', justification='left')],
         [sg.Combo(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I'], size=(20, 30), font='Lucida, 13', key='fifth')],
         [sg.Radio('In the row and in the correct spot', "RADIO5", font='Lucida,10', default=False)],
         [sg.Radio('In the row but in the wrong spot', "RADIO5", font='Lucida,10', default=True)],
         [sg.Radio('Not in the row in any spot', "RADIO5", font='Lucida,10', default=True)],
         [sg.T("")],
         [sg.Button('Okay', size=(10,1), font='Lucida, 20')]]

win = sg.Window('Helper', layout)
e, v = win.read()
win.close()