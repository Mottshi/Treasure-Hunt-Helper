import algorithm
import random
import PySimpleGUI as sg

sg.theme('Black')


layout = [
    [sg.Text('Number of resources', font='Courier` 20'),
     sg.InputText(key='-INPUT-', font='Courier` 20'),
     sg.Button('Confirm', key='-CONFIRM-', font='Courier` 20')
     ],
    [sg.Text()],
    [sg.Text('0 - Correct!, 1 - Needed for another pirate, 2 - Not needed anywhere, 3 - Update the combination', font='Courier` 20')],
    [sg.Text()],
    [sg.Text('Response', font='Courier` 20'),
     sg.InputText(key='-INPUT1-', font='Courier` 20'),
     sg.Button('Confirm', key='-CONFIRM1-', font='Courier` 20')
     ],
    [sg.Text('Output', key='-OUTPUT-', font='Courier` 20')],
    [sg.CloseButton('Close', font='Courier` 20')]
]

window = sg.Window('Treasure Hunt Helper', layout)
while True:
    event, values = window.read()


    if event == '-CONFIRM-':
        match int(values['-INPUT-']):
            case 2:
                elements = ['A', 'B']
                combination = ['A', 'B', 'A', 'B', 'A']
            case 3:
                elements = ['A', 'B', 'C']
                combination = ['A', 'B', 'C', 'A', 'B']
            case 4:
                elements = ['A', 'B', 'C', 'D']
                combination = ['A', 'B', 'C', 'D', 'A']
            case 5:
                elements = ['A', 'B', 'C', 'D', 'E']
                combination = ['A', 'B', 'C', 'D', 'E']
            case 6:
                elements = ['A', 'B', 'C', 'D', 'E', 'F']
                combination = ['A', 'B', 'C', 'D', 'E']
            case 7:
                elements = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
                combination = ['A', 'B', 'C', 'D', 'E']
            case 8:
                elements = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
                combination = ['A', 'B', 'C', 'D', 'E']
            case 9:
                elements = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
                combination = ['A', 'B', 'C', 'D', 'E']
        allpossiblecomb = algorithm.CreateNewComb(elements)
        window['-OUTPUT-'].update(combination)

    if event == sg.WIN_CLOSED:
        break


    if event == '-CONFIRM1-':
        response = list(values['-INPUT1-'])
        window['-INPUT1-']('')
        if response == ['3']:
            combination = random.choice(allpossiblecomb)
        for i in range(len(response)):
            if response[i] == '0':
                allpossiblecomb = algorithm.SortingForZero(allpossiblecomb, combination, i)
        for i in range(len(response)):
            if response[i] == '1':
                allpossiblecomb = algorithm.SortingForOne(allpossiblecomb, combination, i)
        for i in range(len(response)):
            if response[i] == '2':
                allpossiblecomb = algorithm.SortingForTwo(allpossiblecomb, combination, i)
        combination = random.choice(allpossiblecomb)
        window['-OUTPUT-'].update(combination)
        if response == ['0','0', '0', '0', '0']:
            window['-OUTPUT-'].update('')

window.close()