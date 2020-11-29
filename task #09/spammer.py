import pyautogui,time
time.sleep(5) #setting 5 seconds to get into telegram
docu=open("Hi",'r')#a text file with a lot of Hi's
for word in docu:
    pyautogui.typewrite(word)
    pyautogui.press("enter") #to press enter
    
