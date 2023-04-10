import PySimpleGUI as psg
import json


def main_app():
    psg.set_options(font=('Arial Bold', 16))
    psg.theme('Black')
    layout = [
        [psg.Text('Base Account', size=(15, 1)), psg.Input(expand_x=True)],
        [psg.Text('Fol./Unfol.[0/1]', size=(15, 1)), psg.Input(expand_x=True)],
        [psg.OK(), psg.Cancel()]
    ]
    window = psg.Window('Github Bot', layout)
    event, values = window.read()
    window.close()
    return event, values


def perm_val_set():
    def variable_app():
        psg.set_options(font=('Arial Bold', 16))
        psg.theme('Black')
        layout = [
            [psg.Text('Set login credentials')],
            [psg.Text('Username', size=(15, 1)), psg.Input(expand_x=True)],
            [psg.Text('Password', size=(15, 1)), psg.Input(expand_x=True)],
            [psg.OK(), psg.Cancel()]
        ]
        window = psg.Window('perma var set', layout)
        event, values = window.read()
        window.close()
        return event, values

    values = variable_app()

    json_value = {
        "username": values[1][0],
        "password": values[1][1],
    }
    save_file = open("data", "w")
    json.dump(json_value, save_file, indent=6)
    save_file.close()



