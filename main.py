import PySimpleGUI as sg, random
import numpy as np
from typing import List, Any, Union, Tuple, Dict

# All the stuff inside your window.
layout = [  [sg.Text("Sudoku")],
            [sg.Text("Select difficulty")],
            [sg.Button('Easy',button_color = ('white', 'navy'))],
            [sg.Button('Medium',button_color = ('white', 'navy'))],
            [sg.Button('Hard',button_color = ('white', 'navy'))],
            [sg.Button('Start Game',button_color = ('white', 'navy'))],
            [sg.Text("Learn how to play Sudoku! Improve your logic skills!")],
            [sg.Button('Close',button_color = ('white', 'navy'))] ]

# Create the Window
window = sg.Window('Sudoku', layout, finalize = True)

window.bind('<FocusOut>', '+FOCUS OUT+')

window['Start Game'].bind('<Enter>', '_MOUSE OVER')
window['Start Game'].bind('<Leave>', '_MOUSE AWAY')

difficulty = 0
game_start = 0
move_list = []
restart_removebg = b'iVBORw0KGgoAAAANSUhEUgAAABwAAAAaCAYAAACkVDyJAAAAAXNSR0IArs4c6QAAAtJJREFUSEvtlW9IE3EYx5+73WEbrvCNMBGCwDcS9GJoyuYLE9+cKfZGLloKx1pJgb0a1WKOog3fBCIcNCe3ihjlIC5zb/wLRS+kJehQQerNckvwhS/WkDu3J08UdFN/Z8Feda8Onu/z+zzf53nufhSU+KFKzAPdQLvdfqmhocFlsVjaEPE8wzAb8/PzLycmJgZTqdRPAEA9xROBNpvNHovFPplMJmAYBpaXl2F7exsqKiqgurp6931xcRH8fv/daDQqkqCFwDMAsLWXxIqiuOFyuc6ur6+DIAg30um0vLCw8Hv/UKvVeo7juEder9etFePxeJ76/X7vSdBDQIfDgZIkAcuyH5PJ5FXNgSAInyVJaiJV3t/f/8zn8z2UJOmdIAj8cfpDQJ7nMRKJgNPphFAoBM3NzTOzs7NXSLD9uNvtvhcIBAZbW1vrpqenvx2VdwjIcRyOjY0BTdNae7S5EGdceGgikfhSW1t7maZpAxHY0dGBsizv6lpaWsBsNt9aXV19tbS0pOh1qelyuZxqMBhYIpDn+bZQKPTBaDTSmktEhKGhocG+vr77pwFOTk46jEbjRZvN9qAw79Qt0wtGxDRFUZaSAfP5fIymaa5kwB2Ht3ccvigl8AdFURf0AGkAyOud1XE6VVVVlmWLNrVoabLZLE5NTUF7e/s/LdTc3Fy8vr7eSnQ4PDyM3d3dUFZWxmif1N84RcStzs7O67IsvycCa2pqcGVlBYLB4J3e3t6ioZMKSCaTwcrKSudewUWjObJtPT09ODIysjkwMNDk8XgSJMjBuKIoucbGxrp4PE7+lx5MjEQi17q6uh6Pjo4+53n+jR5oJpNR3G73TVEU3+q6LY4SIeLu/Tc+Pv46Go36wuHwr0IdIoYzmQxvNpu1+/TER/cmrq2tPamqqmrKZrPfTSbTJgAEVFWdURTla3l5uUAC7cd1A/UeSNL9B5I6dOr4H+hlDSqg+ropAAAAAElFTkSuQmCC'
undo_removebg = b'iVBORw0KGgoAAAANSUhEUgAAABsAAAAYCAYAAAALQIb7AAAAAXNSR0IArs4c6QAAAppJREFUSEvtlMFLIlEcx7+jMwmuy7p76GbSpasgelCRZUU9CVsU1eLBFQ+BHgai0X+g2l3BFQ+7zF6XEio26NjaXpYowUPhzYsHpdJst4wlpZmceAMtsqhT0sYe9sHwmPfe7/f5fX/v/X4UHnBQD8jCvwejaTopiuILiqJ+MQzz8fLyMt1PRhSVMQwjZbNZmEwmqFQqbGxsYGxsTNGuUzA9jbRabTiTyXyw2+2ybTqdht/v7wtE7HsZPt7Z2Tm32WxotVrgeR6RSKRvUC+YZnt7u+lwOGRFtVoNLMuCpmn5f2BgQJ6vrq7ktc3NTZTLZcVAOh2gcrncD4vF8pQooihK/iRJkmcyBEEAwzC/r2Vvbw9erxcnJyfPAJx2ezwdo5mdnY0tLi6+1Wg0sp0oijg7O4NOp0Oj0YBWq5Ufyw2QBFWpVGC1WnF4eNhVYdeNmZmZOZ7n34miqCKOJicnsbu7+0mn09UEQfg5Pj7+nqhxuVwwGAxyQEdHRxgZGUGz2ezot2eeOY6bi8fjbwCoj4+PLzwez8t8Pv+tPU1DQ0PNXC6nGRwclJdHR0dJeTwCcPFnOhUvNRwOv06lUjxN0xpJkgSv1/tqa2vrS7ujpaUlaXp6Gmq1GlNTU1hdXb27shuHwWDwudvttoqiaKxWq81oNMq1w+Lx+HeO45wklQS2vr7eP0ypNcVisczCwoKbKCMKV1ZW/g5Mr9fr9/f3T41Go1x3gUAAy8vL9w/z+Xz++fn5zyaTSUVABwcHcDqdKJVK9wtLJpNJlmVZSZIoUnOk1oaHh7uClHpjz6taW1v7OjEx4W61WlS9XgfpoYVC4QmA8zt1EKUHQfZDoVDAbDZHAFgTiQSKxaJiGSkeuA34tmf+w26bqZ7nrgH20fYZ6RaFZwAAAABJRU5ErkJggg=='

# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()

    if difficulty == 0:
        if event == 'Start Game_MOUSE OVER':
            window_startpop = sg.Window('Start Game', [[sg.Text("Select difficulty before beginning a game")]], finalize = True)
        if event == 'Start Game_MOUSE AWAY':
            window_startpop.close()
    # if user closes window or clicks cancel
    if event == sg.WIN_CLOSED or event == 'Close':
        break
    elif event == 'Easy':
        window['Easy'].update(button_color = ('black','yellow'))
        window['Medium'].update(button_color = ('white', 'navy'))
        window['Hard'].update(button_color = ('white', 'navy'))
        puzzle = [[0,0,0,0,1,0,2,4,8],[0,0,1,0,0,0,7,0,3],[0,0,0,6,7,0,5,0,1],[0,0,0,0,0,0,3,7,0],[3,0,0,4,0,6,0,0,5],[0,1,4,0,0,0,0,0,0],[9,0,5,0,6,1,0,0,0],[1,0,3,0,0,0,4,0,0],[2,7,6,0,3,0,0,0,0]]
        puzzle_update = puzzle
        difficulty = 1
    elif event == 'Medium':
        window['Easy'].update(button_color = ('white', 'navy'))
        window['Medium'].update(button_color = ('black','yellow'))
        window['Hard'].update(button_color = ('white', 'navy'))
        puzzle = [[8,0,0,3,0,5,2,0,0],[0,0,0,0,4,0,9,0,0],[0,9,0,0,0,0,0,3,0],[0,0,4,2,0,0,0,9,0],[0,0,2,6,0,4,7,0,0],[0,5,0,0,0,3,6,0,0],[0,2,0,0,0,0,0,8,0],[0,0,5,0,6,0,0,0,0],[0,0,3,5,0,9,0,0,1]]
        puzzle_update = puzzle
        difficulty = 1
    elif event == 'Hard':
        window['Easy'].update(button_color = ('white', 'navy'))
        window['Medium'].update(button_color = ('white', 'navy'))
        window['Hard'].update(button_color = ('black','yellow'))
        puzzle = [[5,0,0,0,0,4,0,0,0],[0,0,3,0,8,0,7,9,0],[0,7,9,0,0,5,0,4,0],[6,0,0,0,0,0,0,0,0],[0,4,8,0,0,0,5,2,0],[0,0,0,0,0,0,0,0,1],[0,8,0,2,0,0,1,3,0],[0,3,7,0,4,0,8,0,0],[0,0,0,8,0,0,0,0,2]]
        puzzle_update = puzzle
        difficulty = 1
    elif event == 'Start Game' and difficulty == 1:
        game_start = 1
        window.close()

        #Frame and puzzle filling code adapted from here: https://github.com/PySimpleGUI/PySimpleGUI/blob/master/DemoPrograms/Demo_Sudoku.py
        window = sg.Window('Sudoku',
                    [[sg.Frame('', [[sg.I(random.randint(1,9), justification='c', size=(3,1),enable_events=True, key=(fr*3+r,fc*3+c)) for c in range(3)] for r in range(3)]) for fc in range(3)] for fr in range(3)] +
                    [[sg.B('How to play'), sg.B('', image_data=undo_removebg, key = 'Undo'), sg.B('', image_data=restart_removebg, key = 'Restart'), sg.B('Close')],], finalize=True)

        for r, row in enumerate(puzzle_update):
            for c, col in enumerate(row):
                window[r, c].update(puzzle_update[r][c] if puzzle_update[r][c] != 0 else '', background_color=sg.theme_input_background_color())

        window.bind('<FocusOut>', '+FOCUS OUT+')

        window['Undo'].bind('<Enter>', '_MOUSE OVER')
        window['Undo'].bind('<Leave>', '_MOUSE AWAY')

        window['Restart'].bind('<Enter>', '_MOUSE OVER')
        window['Restart'].bind('<Leave>', '_MOUSE AWAY')

    if event == 'Undo_MOUSE OVER':
        window_undopop = sg.Window('Undo', [[sg.Text("Reverts last number placement. Cannot be undone.")]], finalize = True)
    if event == 'Undo_MOUSE AWAY' or event == "Undo":
        window_undopop.close()

    if event == 'Restart_MOUSE OVER':
        window_undopop = sg.Window('Undo', [[sg.Text("Restart game.")]], finalize = True)
    if event == 'Restart_MOUSE AWAY' or event == "Undo":
        window_undopop.close()

    if event == 'Undo':
        last_move = move_list[0]
        move_list.pop(0)
        puzzle_update[last_move[0]][last_move[1]] = 0
        window[last_move[0],last_move[1]].update(puzzle_update[last_move[0]][last_move[1]] if puzzle_update[last_move[0]][last_move[1]] != 0 else '', background_color=sg.theme_input_background_color())

    if event == 'How to play':
        window_howtoplay = sg.Window('How to play', [[sg.Text("Select a spot in the grid, then select a number to enter into \nthe grid, or type a number using the keyboard. \nThe goal is to fill in the entire grid with numbers 1-9 such \nthat each row, column, and 3x3 square contains each \nnumber 1 through 9 one time.")]] + 
                                                        [[sg.B('Close', key = 'How to play Close')]], finalize = True, modal = True)
        event, values = window_howtoplay.read()
    
    if event == 'How to play Close':
        window_howtoplay.close()

    if event == 'Restart':
        window_restart = sg.Window('Restart', [[sg.Text("Are you sure you wish to restart? All progress will be lost.")]] +
                    [[sg.B('Yes'), sg.B('No')]], finalize = True, modal = True)
        event, values = window_restart.read()
        
    if event == 'Yes':
        window_restart.close()
        puzzle_update = puzzle
        for r, row in enumerate(puzzle_update):
            for c, col in enumerate(row):
                window[r, c].update(puzzle_update[r][c] if puzzle_update[r][c] != 0 else '', background_color=sg.theme_input_background_color())
    
    if event == 'No':
        window_restart.close()

    if game_start == 1:
        for r, row in enumerate(puzzle_update):
                for c, col in enumerate(row):
                    if puzzle_update[r][c] == 0 and window[r,c].get() != '':
                        if [r,c] not in move_list:
                            move_list.insert(0,[r,c])       
    

window.close()