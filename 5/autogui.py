import pyautogui
import time 
time.sleep(2)
print(pyautogui.position())
reader=pyautogui.alert(text="Hello world",title="Test Gui",button="Click!")
print(reader)
reader2=pyautogui.confirm(text="Hello world",title="Test Gui",buttons=("Click!","Cancel"))
print(reader2)
reader3=pyautogui.prompt(text="Hello world",title="Test Gui")
print(reader3)
reader4=pyautogui.password(text="Hello world",title="Test Gui")
print(reader4)