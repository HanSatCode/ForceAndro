import pyautogui as pag
import time
import subprocess
import os.path

from tkinter import messagebox as msg
from tkinter import Tk

# 데이터베이스 읽기

databasePath = os.path.abspath("Database.txt")

readList = open(databasePath, 'r')
useList = readList.readlines()
readList.close()

count = 0
countList = len(useList)

# \n 처리 삭제

for count in range (0, countList) :
    useList[count] = useList[count].replace("\n", "")


# 빈 데이터베이스 판별

if useList == [] :
    root= Tk()
    root.withdraw()
    msg.showerror('작업 실패','데이터베이스에 아무것도 적혀있지 않습니다.\n제거하실 패키지 이름을 Database.txt 에 입력해주세요.')
    exit()

root= Tk()
root.withdraw()
msg.showwarning('작업 경고', '데이터베이스의 양에 따라 시간이 오래 소요될 수 있습니다.\n작업 중에는 절대 조작하지 마세요.')


# 작업영역

subprocess.Popen("powershell.exe")

time.sleep(2)
pag.typewrite("cd platform-tools")

pag.press('enter')
            
time.sleep(2)
pag.typewrite(".\\adb devices")
pag.press('enter')
            
time.sleep(2)
pag.typewrite(".\\adb shell")
pag.press('enter')
            
time.sleep(2)
for count in range(0, countList) :
    pag.typewrite("pm uninstall -k --user 0 " + useList[count])
    pag.press('enter')

    time.sleep(4)

pag.typewrite("exit")
pag.press('enter')

pag.typewrite("exit")
pag.press('enter')

msg.showinfo('작업 완료', '작업이 완료되었습니다. 디바이스를 다시 시작하여 상태를 확인해주세요.')
exit()
