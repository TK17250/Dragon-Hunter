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

image_bandit = climage.convert("img/bandit.jpeg", is_256color=True, is_truecolor=False,
                                  is_unicode=True,width=50)

image_ghost = climage.convert("img/ghost.png", is_256color=True, is_truecolor=False,
                                  is_unicode=True,width=50)

image_ant = climage.convert("img/ant.jpeg", is_256color=True, is_truecolor=False,
                                  is_unicode=True,width=50)

image_woff = climage.convert("img/woff.jpeg", is_256color=True, is_truecolor=False,
                                  is_unicode=True,width=50)

image_monster = climage.convert("img/monster.jpeg", is_256color=True, is_truecolor=False,
                                  is_unicode=True,width=50)

image_Bigmonster = climage.convert("img/Bigmonster.jpeg", is_256color=True, is_truecolor=False,
                                  is_unicode=True,width=50)

image_spider = climage.convert("img/spider.jpeg", is_256color=True, is_truecolor=False,
                                  is_unicode=True,width=50)

image_crock = climage.convert("img/crock.jpeg", is_256color=True, is_truecolor=False,
                                  is_unicode=True,width=50)

image_bird = climage.convert("img/bird.png", is_256color=True, is_truecolor=False,
                                  is_unicode=True,width=50)

image_Dragon = climage.convert("img/dragon.jpeg", is_256color=True, is_truecolor=False,
                                  is_unicode=True,width=50)

# Setting Game
ดาบไม้ = 10
ดาบหิน = 20
ดาบเหล็ก = 30
ดาบเพชร = 40
ดาบน้ำ = 50
กิ่งไม้ = 5
ใบไม้ = 1

i = 1
win_lose_Dragon = ["Win","lose"]

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
        item.clear()
        item.append(add_item)
        print("\n- ดาบไม้ = 10 \n- ดาบหิน = 20 \n- ดาบเหล็ก = 30 \n- ดาบเพชร = 40 \n- ดาบน้ำ = 50 \n- กิ่งไม้ = 5 \n- ใบไม้ = 1")
        print(f"\n* คุณได้รับ {str(item)}")
        input("\nต่อไป >>> ")

    else:
        input("\nต่อไป >>> ")

# Random box lucky
def random_lucky():
    if Y_N == "Y":
        add_lucky = random.choice(random_item_lucky)
        item.clear()
        item.append(add_lucky)
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
    print(image_ant)
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
    print(image_woff)
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
    print(image_bandit)
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
        item.clear
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
    print(image_ghost)
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
        print("\nคุณโดนผีหลอก แล้วคุณวิ่งหนีโดยทิ้งอาวุธไป\n")
        item.clear()
        input("ต่อไป >>> ")

    # content 9
    os.system('cls||clear')
    print("\nคุณตื่นมาแล้วได้มาเจอ กล่องวิเศษอันหนึ่ง คุณจะเปิดหรือไม่\n")
    print(image_open_box)
    print("เอากด Y (พิมพ์ใหญ่เท่านั้น) \nไม่เอากด N \n")
    print("คำเตือนเลือกแล้วอาวุธอันเก่าของคุณจะหาย และ ถ้าพิมพ์นอกจาก Y จะไม่ได้รับของในกล่องทันที \n")
    Y_N = input("จะเอาหรือไม่ >>> ")
    random_lucky()

    # content 10
    os.system('cls||clear')
    print("คุณเดินมาเจอ จระเข้ยักษ์ติดปีกถือปืนมี33 เศียร แต่ละเศียรมีงา 7 งาแต่ละงามีสระบัว 7 สระ แต่ละสระมีดอกบัว 7 ดอก แต่ละดอกมีกลีบ 7 กลีบ มี 7 เกสร แต่ละเกสรมีปราสาทอยู่ 7 หลัง ปราสาทแต่ละหลังมี 7 ชั้น แต่ละชั้นมี 7 ห้อง แต่ละห้องมี 7 บัลลังก์ แต่ละบัลลังก์มีเทพธิดาสถิต 7 องค์ เทพธิดาแต่ละองค์มีบริวาร องค์ละ 7 นาง เทพธิดาบริวารแต่ ละนางมีนางทาสีนางละทาสี \n")
    print(image_crock)
    print("แล้วมันก็วิ่งจะมาทำร้ายคุณ คุณจะสู้หรือไม่\n")
    print("สู้กด Y (พิมพ์ใหญ่เท่านั้น) \n\nไม่สู้กด N \n")
    print("ถ้าพิมพ์นอกจาก Y จะข้ามการต่อสู้ทันที \n")
    Y_N = input("จะสู้หรือไม่ >>> ")
    if Y_N == "Y":
        if item[0] >= ผี :
            print("\nคุณชนะ\n")
            print(image_win)
            input("ต่อไป >>> ")

        else:
            print("คุณได้ตื่นจากฝันแล้วไปโรงเรียนต่อ\n")
            exit()
    else:
        print("\nคุณโดนจระเข้จับกิน\n")
        print(image_lose)
        exit()

    # content 11
    os.system('cls||clear')
    print("\nคุณได้เข้ามาในถ้ำแล้วมาเจอ แมงมุมยักษ์ที่กำลังทำร้ายคนอยู่ คุณจะช่วยเขาหรือไม่\n")
    print(image_spider)
    print("ช่วยกด Y (พิมพ์ใหญ่เท่านั้น) \n\nไม่ช่วยกด N \n")
    print("ถ้าพิมพ์นอกจาก Y จะไม่ช่วย \n")
    Y_N = input("จะช่วยหรือไม่ >>> ")
    if Y_N == "Y":
        if item[0] >= แมงมุมยักษ์ :
            print("\nคุณช่วยเขาได้\n")
            print(image_win)
            input("ต่อไป >>> ")

        else:
            print(image_lose)
            print("คุณตายตามคนๆนั้น\n")
            exit()
    else:
        print("\nคุณเดินผ่านแล้วไม่สนใจคนที่โดนแมงมุมยักษ์ทำร้าย\n")
        input("ต่อไป >>> ")

    # content 12
    os.system('cls||clear')
    print("\nคุณได้มาเจอปีศาจไฟตัวหนึ่งที่เก็บซ่อนอะไรไว้อยู่\n")
    print("แล้วมันก็พุ่งเข้ามาทำร้ายคุณ คุณจะเลือกระหว่างสู้กลับหรือไปดูสิ่งที่มันเก็บซ้อน\n")
    print(image_monster)
    print("สู้กด Y (พิมพ์ใหญ่เท่านั้น) \n\nไม่สู้กด N \n")
    print("ถ้าพิมพ์นอกจาก Y จะไปดูของที่ปีศาจเก็บซ่อนทันทีทันที \n")
    Y_N = input("จะสู้หรือไม่ >>> ")
    if Y_N == "Y":
        if item[0] >= ปีศาจ :
            print("\nคุณชนะ\n")
            print(image_win)
            input("ต่อไป >>> ")
        else:
            print(image_lose)
            print("คุณแพ้ละ\n")
            exit()
    else:
        print("\nคุณเดินเข้าไปดูแล้วปีศาจเข้ามาฆ่าคุณจากด้านหลัง\n")
        print(image_lose)
        exit()

    # content 13
    os.system('cls||clear')
    print("\nคุณฆ่าปีศาจตัวนั้นได้แล้วมันกลายร่างกลายเป็นปีศาจยักษ์ มันจะทำลายถ้ำแห่งนี้รวมถึงคุณด้วย\n")
    print(image_Bigmonster)
    print("คุณจะสู้หรือไม่\n")
    print("สู้กด Y (พิมพ์ใหญ่เท่านั้น) \n\nไม่สู้กด N \n")
    print("ถ้าพิมพ์นอกจาก Y คุณจะวิ่งหนีออกจากถ้ำ \n")
    Y_N = input("จะสู้หรือไม่ >>> ")
    if Y_N == "Y":
        if item[0] >= ปีศาจยักษ์ :
            print("\nคุณชนะ\n")
            print(image_win)
            input("ต่อไป >>> ")
        else:
            print(image_lose)
            print("คุณแพ้ละ\n")
            exit()
    else:
        print("\nคุณวิ่งออกจากถ้ำไม่ทันแล้วคุณได้ตายที่นั้น\n")
        print(image_lose)
        exit()

    # content 14
    os.system('cls||clear')
    print("\nคุณได้เจอกล่องหายากที่ปีศาจเก็บซ่อนเอาไว้ คุณจะเอาหรือไม่ \n")
    print(image_open_box)
    print("เอากด Y (พิมพ์ใหญ่เท่านั้น) \nไม่เอากด N \n")
    print("คำเตือนเลือกแล้วอาวุธอันเก่าของคุณจะหาย และ ถ้าพิมพ์นอกจาก Y จะไม่ได้รับของในกล่องทันที \n")
    Y_N = input("จะเอาหรือไม่ >>> ")
    random_lucky()

    # content 15
    os.system('cls||clear')
    print("\nคุณได้เดินมาถึงหน้าประตูอันหนึ่งข้างในนั้นมีมังกรอาศัยอยู่ แต่ มีนกรบผู้รับใช้มังกรตัวหนึ่ง จะมาฆ่าคุณเพราะคุณได้ไปฆ่าปีศาจที่เป็นเพื่อนของเขา แล้วคุณจะสู้หรือไม่\n")
    print(image_bird)
    print("สู้กด Y (พิมพ์ใหญ่เท่านั้น) \n\nไม่สู้กด N \n")
    print("ถ้าพิมพ์นอกจาก Y คุณจะตายทันที เพราะคุณโดนนกรบผู้รับใช้มังกรฆ่าตาย \n")
    Y_N = input("จะสู้หรือไม่ >>> ")
    if Y_N == "Y":
        if item[0] >= นกรบผู้รับใช้มังกร :
            print("\nคุณชนะ\n")
            print(image_win)
            input("ต่อไป >>> ")
        else:
            print(image_lose)
            print("คุณแพ้ละ\n")
            exit()
    else:
        print("\nคุณตายเพราะโดนนกรบผู้รับใช้มังกรฆ่าตาย\n")
        print(image_lose)
        exit()

    # content 16
    os.system('cls||clear')
    print("\nก่อนคุณเข้าไปในประตูคุณได้เจอกล้อง 1 กล้อง คุณจะเอาหรือไม่ \n")
    print(image_open_box)
    print("เอากด Y (พิมพ์ใหญ่เท่านั้น) \nไม่เอากด N \n")
    print("คำเตือนเลือกแล้วอาวุธอันเก่าของคุณจะหาย และ ถ้าพิมพ์นอกจาก Y จะไม่ได้รับของในกล่องทันที \n")
    Y_N = input("จะเอาหรือไม่ >>> ")
    random_items()

    # content 17
    os.system('cls||clear')
    print("\nคุณได้เข้าไปในประตูที่มังกรอยู่แล้วมันกรตัวนั้นเป็นตัวเดียวกันกับตัวที่ฆ่าพ่อแม่คุณ")
    print(image_Dragon)
    print("\n- ดาบไม้ = 10 \n- ดาบหิน = 20 \n- ดาบเหล็ก = 30 \n- ดาบเพชร = 40 \n- ดาบน้ำ = 50 \n- กิ่งไม้ = 5 \n- ใบไม้ = 1")
    print("\nการต่อสู้โอกาสสุ่มชนะจะแล้วแต่ดาบ เช่น \n- ดาบไม้ = 10 จะสุ่มได้ 1 รอบ \nแต่ \n\nไอเท็มที่เป็นหลักหน่วยจะเป็น % โอกาศชนะเช่น \nกิ่งไม้ = 5 จะมีโอกาส 5% ที่จะชนะ\n")
    input("กด Enter เพื่อเริ่มการต่อสู้ >>> ")

    # ใบไม้
    if item[0] == ใบไม้ :
        สุ่มหน่วย = random.randint(1,100)
        if สุ่มหน่วย == 1:
            print("\nคุณฆ่ามังกรด้วย ใบไม้ คุณคือคนที่แข็งแกร่งที่สุดคุณเลยได้กลายเป็นพระราชาของอาณาจักร\n")
            print(image_win)
        else:
            print("\nคุณโดนมังกรฆ่าตาย\n")
            print(image_lose)
            exit()

    # กิ่งไม้
    elif item[0] == กิ่งไม้ :
        สุ่มหน่วย = random.randint(1,100)
        if สุ่มหน่วย == 5:
            print("\nคุณเอากิ่งไม้ไปทิ้มตาของมังกรจนมันตกใจตาย แต่ คุณได้กลับไปที่เมืองแต่ไม่มีใครเชื่อว่าคุณฆ่ามังกรด้วยกิ่งไม้ได้\n")
            print(image_win)

        else:
            print("\nคุณโดนมังกรฆ่าตาย\n")
            print(image_lose)
            exit()

    # ดาบไม้
    elif item[0] == ดาบไม้:
        while i <= 1 :
            win_lose = random.choice(win_lose_Dragon)
            if win_lose == "Win":
                print("\nคุณได้ตื่นจากการหลับไหลมานานจากการโดนรถชน แล้วเรื่องทั้งหมดมานี้คือความฝัน!!!\n")
                print(image_win)
                break

            elif win_lose == "lose":
                print("\nคุณโดนมังกรฆ่าตาย\n")
                print(image_lose)
                exit()

    # ดาบหิน
    elif item[0] == ดาบหิน:
        while i <= 2 :
            i += 1
            win_lose = random.choice(win_lose_Dragon)
            if win_lose == "Win":
                print("\nคุณฆ่ามังกรด้วยดาบหิน แล้วพระราชาให้ของรางวัลคุณคือทองคำเป็นกอง\n")
                print(image_win)
                break

            elif win_lose == "lose":
                print("\nคุณโดนมังกรฆ่าตาย\n")
                print(image_lose)
                exit()

    # ดาบเหล็ก
    elif item[0] == ดาบเหล็ก:
        while i <= 3 :
            i += 1
            win_lose = random.choice(win_lose_Dragon)
            if win_lose == "Win":
                print("\nคุณฆ่ามังกรด้วยดาบเหล็ก แล้วพระราชาให้ของรางวัลคุณคือบ้าน 1 หลัง\n")
                print(image_win)
                break

            elif win_lose == "lose":
                print("\nคุณโดนมังกรฆ่าตาย\n")
                print(image_lose)
                exit()

    # ดาบเพชร
    elif item[0] == ดาบเพชร:
        while i <= 4 :
            i += 1
            win_lose = random.choice(win_lose_Dragon)
            if win_lose == "Win":
                print("\nคุณฆ่ามังกรด้วยดาบเพชร แล้วคุณได้กลายเป็นอัศวินที่ฆ่ามังกรได้คนแรกของอาณาจักรแล้วได้แต่งงานกับลูกสาวของพระราชาแล้วอยู่ด้วยกันอย่างมีความสุข (ฉากจบที่แท้จริง)\n")
                print(image_win)
                break

            elif win_lose == "lose":
                print("\nคุณโดนมังกรฆ่าตาย\n")
                print(image_lose)
                exit()

    # ดาบน้ำ
    elif item[0] == ดาบน้ำ:
        while i <= 5 :
            i += 1
            win_lose = random.choice(win_lose_Dragon)
            if win_lose == "Win":
                print("\nคุณได้เล่นจนจบเกมแล้วแต่คุณได้โดนยึดมือถือเนื่องจากคุณเล่นเกมในเวลาเรียน\n")
                print(image_win)
                break

            elif win_lose == "lose":
                print("\nคุณโดนมังกรฆ่าตาย\n")
                print(image_lose)
                exit()

elif input_GUI == "2":
    os.system('cls||clear')
    print("ผู้จัดทำ")
    print("1.TK17250 \n2.0hmmbga")

else:
    print("Error")
