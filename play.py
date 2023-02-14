import climage
import os
import random

# add image
image_startgame = climage.convert("img/start-game.jpg", is_256color=True, is_truecolor=False,
                                  is_unicode=True,width=50)

image_open_box = climage.convert("img/openbox.png", is_256color=True, is_truecolor=False,
                                  is_unicode=True,width=50)

image_win = climage.convert("img/Win.jpeg", is_256color=True, is_truecolor=False,
                                  is_unicode=True,width=50)

image_lose = climage.convert("img/lose.jpeg", is_256color=True, is_truecolor=False,
                                  is_unicode=True,width=50)

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
random_item_lucky = [ดาบน้ํา,ดาบเพชร,ดาบเหล็ก]

# Monster
มด = 1
หมาป่า = 5
ปีศาจ = 10
แมงมุมยักษ์ = 10
โจร = 10
ผี = 20
ปีศาจยักษ์ = 30
นกรบผู้รับใช้มังกร = 50
จระเข้ = 7
มังกร = 100

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
    print("\nคุณได้ไปเจอกล้อง 1 กล้อง คุณจะเอาหรือไม่ \n")
    print(image_open_box)
    print("เอากด Y (พิมพ์ใหญ่เท่านั้น) \nไม่เอากด N \n")
    print("คำเตือนเลือกแล้วอาวุธอันเก่าของคุณจะหาย และ ถ้าพิมพ์นอกจาก Y จะไม่ได้รับของในกล่องทันที \n")
    Y_N = input("จะเอาหรือไม่ >>> ")
    random_items()

    # content 3
    os.system('cls||clear')
    print("\nคุณได้ไปไปเจอรังมด คุณจะต่อสู้กับพวกมันหรือไม่ \n")
    print("สู้กด Y (พิมพ์ใหญ่เท่านั้น) \n\nไม่สู้กด N \n")
    print("ถ้าพิมพ์นอกจาก Y จะข้ามการต่อสู้ทันที \n")
    Y_N = input("จะสู้หรือไม่ >>> ")
    if Y_N == "Y":
        if item[0] >= มด :
            print("\nคุณชนะ\n")
            print(image_win)
            input("ต่อไป >>> ")

        else:
            print(image_lose)
            print("คุณแพ้ละ\n")
            exit()
    else:
        input("\nต่อไป >>> ")

    # content 4
    os.system('cls||clear')
    print("\nคุณกำลังจะนอนแล้วมีหมาป่าเข้ามาทำร้ายคุณ คุณจะสู้หรือไม่ \n")
    print("สู้กด Y (พิมพ์ใหญ่เท่านั้น) \n\nไม่สู้กด N \n")
    print("ถ้าพิมพ์นอกจาก Y จะข้ามการต่อสู้ทันที \n")
    Y_N = input("จะสู้หรือไม่ >>> ")
    if Y_N == "Y":
        if item[0] >= หมาป่า :
            print("\nคุณชนะ\n")
            print(image_win)
            input("ต่อไป >>> ")

        else:
            print(image_lose)
            print("คุณแพ้ละ\n")
            exit()
    else:
        print(f"\n{image_lose}")
        print("คุณโดนหมาป่าฆ่า\n")
        exit()

    # content 5
    os.system('cls||clear')
    print("\nคุณตื่นมาแล้วคุณได้ไปเจอกล้อง 1 กล้อง คุณจะเอาหรือไม่ \n")
    print(image_open_box)
    print("เอากด Y (พิมพ์ใหญ่เท่านั้น) \nไม่เอากด N \n")
    print("คำเตือนเลือกแล้วอาวุธอันเก่าของคุณจะหาย และ ถ้าพิมพ์นอกจาก Y จะไม่ได้รับของในกล่องทันที \n")
    Y_N = input("จะเอาหรือไม่ >>> ")
    random_items()

    # content 6
    os.system('cls||clear')
    print("\nคุณโดนโจรปล้น คุณจะสู้หรือไม่\n")
    print("สู้กด Y (พิมพ์ใหญ่เท่านั้น) \n\nไม่สู้กด N \n")
    print("ถ้าพิมพ์นอกจาก Y จะข้ามการต่อสู้ทันที \n")
    Y_N = input("จะสู้หรือไม่ >>> ")
    if Y_N == "Y":
        if item[0] >= โจร :
            print("\nคุณชนะ\n")
            print(image_win)
            input("ต่อไป >>> ")

        else:
            print(f"\n{image_lose}")
            print("คุณโดนโจรฆ่าตาย\n")
            exit()
    else:
        print("\nคุณโดนโจรปล้น")
        item.remove(item[0])
        input("\nต่อไป >>> ")

    # content 7
    os.system('cls||clear')
    print("\nคุณได้เข้าไปในป่ามรณะที่มีสัตว์อันตราย แล้ว คุณได้ไปเจอกล้อง 1 กล้อง คุณจะเอาหรือไม่ \n")
    print(image_open_box)
    print("เอากด Y (พิมพ์ใหญ่เท่านั้น) \nไม่เอากด N \n")
    print("คำเตือนเลือกแล้วอาวุธอันเก่าของคุณจะหาย และ ถ้าพิมพ์นอกจาก Y จะไม่ได้รับของในกล่องทันที \n")
    Y_N = input("จะเอาหรือไม่ >>> ")
    random_items()

    # content 8
    os.system('cls||clear')
    print("\nตอนนี้ในป่าเป็นตอนกลางคืน แล้วคุณได้ไปเจอผีในป่าที่กำลังจะมาหลอกคุณ คุณจะสู้หรือไม่\n")
    print("สู้กด Y (พิมพ์ใหญ่เท่านั้น) \n\nไม่สู้กด N \n")
    print("ถ้าพิมพ์นอกจาก Y จะข้ามการต่อสู้ทันที \n")
    Y_N = input("จะสู้หรือไม่ >>> ")
    if Y_N == "Y":
        if item[0] >= ผี :
            print("\nคุณชนะ\n")
            print(image_win)
            input("ต่อไป >>> ")

        else:
            print(image_lose)
            print("คุณแพ้ละ\n")
            exit()
    else:
        if list(item) not in list(item):
            print("\nคุณวิ่งหนีผี\n")

        elif item in list(item):
            item.remove(item[0])
            print("\nคุณโดนผีหลอก แล้วคุณวิ่งหนีแล้วเผลอทิ้งอาวุณไป\n")

        input("ต่อไป >>> ")

elif input_GUI == "2":
    os.system('cls||clear')
    print("ผู้จัดทำ")
    print("1.TK17250 \n2.sdkljfdlskjfdlskjfdsklfjdslfjds")

else:
    print("Error")
