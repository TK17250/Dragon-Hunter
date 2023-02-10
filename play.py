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

starter_pack = [ดาบไม้, ใบไม้, กิ่งไม้]
item = []
random_item = [ดาบน้ํา, ดาบหิน, ดาบเพชร, ดาบเหล็ก, กิ่งไม้, ใบไม้]

# Starter Pack
def random_start():
    add_start = random.choice(starter_pack)
    item.append(add_start)
    print("\nคุณได้ไปหาคนตีดาบ แต่เขาไม่มีดาบเหล็กให้เขาเลยให้")
    print(f"\n* {str(item)} มาแทน\n")

# Random items
def random_items():
    if Y_N == "Y":
        add_item = random.choice(random_item)
        item.remove(item[0])
        item.append(add_item)
        print("\n- ดาบไม้ = 10 \n- ดาบหิน = 20 \n- ดาบเหล็ก = 30 \n- ดาบเพชร = 40 \n- ดาบน้ำ = 50 \n- กิ่งไม้ = 5 \n- ใบไม้ = 1")
        print(f"\n* คุณได้รับ {str(item)}")
        input("\nต่อไป >>> ")

    else:
        input("\nต่อไป >>> ")


# GUI
print("\nDragon Hunter\n")
print("1.เริ่มเกม \n2.ผู้จัดทำ")

try:
    input_GUI = input("ใส่เลข >>> ")

except:
    print("Error")

# start game
if input_GUI == "1":
    # content 1
    os.system('cls||clear')
    print("\nคุณเป็นอัศวินที่โดนมักรที่ทำลายบ้านเมืองและฆ่าพ่อแม่ของเขาจนเขาเคลียดแค้น และพระราชาจะให้รางวัลคนที่ปราบมังกรได้\n")
    print(image_startgame)
    print("- ดาบไม้ = 10 \n- ดาบหิน = 20 \n- ดาบเหล็ก = 30 \n- ดาบเพชร = 40 \n- ดาบน้ำ = 50 \n- กิ่งไม้ = 5 \n- ใบไม้ = 1")
    random_start()
    input("ต่อไป >>> ")

    # content 2
    os.system('cls||clear')
    print("\nคุณได้ไปกล้อง 1 กล้อง คุณจะเอาหรือไม่ \n")
    print("เอากด Y \nไม่เอากด N \n(พิมพ์ใหญ่เท่านั้น)\n")
    print("คำเตือนเลือกแล้วอาวุธอันเก่าของคุณจะหาย และ ถ้าพิมพ์นอกจาก Y จะไม่ได้รับของในกล่องทันที \n")
    Y_N = input("จะเอาหรือไม่ >>> ")
    random_items()


elif input_GUI == "2":
    os.system('cls||clear')
    print("ผู้จัดทำ")
    print("1.TK17250 \n2.sdkljfdlskjfdlskjfdsklfjdslfjds")

else:
    print("Error")
