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
random_item = [ดาบน้ํา,ดาบหิน,ดาบเพชร,ดาบเหล็ก,กิ่งไม้,ใบไม้]

def random_items():
    if Y_N == "Y" or "y":
        add_item = random.choice(random_item)
        item.remove(item[0])
        item.append(add_item)
        print (f"คุณได้รับ {str(item)}")

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

    # content 2
    os.system('cls||clear')
    print ("\n คุณได้ไปกล้อง 1 กล้อง คุณจะเอาหรือไม่ \n")
    print ("เอากด Y \nไม่เอากด N \n")
    print ("คำเตือนเลือกแล้วอาวุธอันเก่าของคุณจะหาย \n")
    Y_N = input("จะเอาหรือไม่")
    random_items()


elif input_GUI == "2" :
    os.system('cls||clear')
    print("ผู้จัดทำ")
    print("1.TK17250 \n2.sdkljfdlskjfdlskjfdsklfjdslfjds")

else:
    print("Error")