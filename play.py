import climage
import os
import random

# add image
image_startgame = climage.convert("img/start-game.jpg", is_256color=True, is_truecolor=False, 
    is_unicode=True)

# Setting Game
ดาบไม้ = 10
ดาบหิน = 20
ดาบเหล็ก = 30
ดาบเพชร = 40
ดาบน้ำ = 50
กิ่งไม้ = 5
ใบไม้ = 1

item = [ดาบไม้]

# GUI
print("\nDragon Hunter\n")
print("1.เริ่มเกม \n2.ผู้จัดทำ")

try :
    input_GUI = input("ใส่เลข >>> ")

except :
    print("Error")

# start game
if input_GUI == "1" :
    # content 1
    os.system('cls||clear')
    print ("\nคุณเป็นอัศวินที่โดนมักรที่ทำลายบ้านเมืองและฆ่าพ่อแม่ของเขาจนเขาเคลียดแค้น และพระราชาจะให้รางวัลคนที่ปราบมังกรได้\n")
    print (image_startgame)
    print ("คุณได้ไปหาคนตีดาบ แต่เขาไม่มีดาบเหล็กให้เขาเลยให้\n * ดาบไม้ \nมาแทน\n")
    input ("ต่อไป >>> ")

elif input_GUI == "2" :
    os.system('cls||clear')
    print("ผู้จัดทำ")
    print("1.TK17250 \n2.sdkljfdlskjfdlskjfdsklfjdslfjds")

else:
    print("Error")