import time
import FreeSimpleGUI as sg
label=sg.Text("Type in a To-Do")
input_box=sg.InputText()
add_button=sg.Button("ADD")
window=sg.Window('my to do app',layout=[[label],[input_box,add_button]])
window.read()
window.close()