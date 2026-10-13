from function import get_date, stock, input_sales_category





mainFoodlist = ['จานเดียว', 'ผัดและทอด', 'ต้มและแกง']
sFoodlist = ["กะเพราหมูสับ/ไก่ไข่ดาว", "ผัดซีอิ๊วหมู/ไก่", "ข้าวผัดหมู/ไก่", "ข้าวหน้าไก่/หมูทอดกระเทียม", "ผัดพริกแกงหมู/ไก่"]
fFoodlist = ["ไข่เจียวหมูสับ", "ผัดผักบุ้งไฟแดง", "ปลาทอดน้ำปลา/ทอดสามรส", "กุ้งผัดพริกเกลือ/ผัดผงกะหรี่", "ผัดคะน้าหมูกรอบ"]
wFoodlist = ["ต้มยำกุ้ง/ทะเล", "ต้มจืดเต้าหู้หมูสับ", "แกงเขียวหวานไก่"]


day, month, year = get_date()
print(f"---- Food Stock (ประจำวันที่ {day}/{month}/{year}) ----")

# ------------------------------------------------------------------------------------ปรับให้ด้วย
leave = False
while not leave:
    while True:
        sfoodstock = stock(sFoodlist, mainFoodlist[0])
        go = input("ไปต่อNext(n) : ")
        if go == "n":
            ffoodstock = stock(fFoodlist, mainFoodlist[1])
            go = input("ไปต่อNext(n) กลับBack(b) : ")
            if go == "n":
                while True:
                    wfoodstock = stock(wFoodlist, mainFoodlist[2])
                    go = input("ไปต่อNext(n) กลับBack(b) : ")
                    if go == "n":
                        leave = True
                        break
                    elif go == "b":
                        break
                if leave:   
                    break


# -------------------------------------------------------------------------------------------ปรับให้ด้วย

    print(f"\n---- Sold Food ----")
    soldsfoodlist = input_sales_category(sFoodlist, sfoodstock, mainFoodlist[0])

    go = input("ไปต่อหมวดผัดและทอด? (y/n) : ").strip().lower()
    if go == "y":
        soldffoodlist = input_sales_category(fFoodlist, ffoodstock, mainFoodlist[1])
        go2 = input("ไปต่อหมวดต้มและแกง? (y/n) : ").strip().lower()
        if go2 == "y":
            soldwfoodlist = input_sales_category(wFoodlist, wfoodstock, mainFoodlist[2])
        elif go2 == "n":
            soldwfoodlist = [0] * len(wFoodlist)
    elif go == "n":
        soldffoodlist = [0] * len(fFoodlist)
        soldwfoodlist = [0] * len(wFoodlist)

    # 4. แสดงผลสรุปการขาย
    print("\n================ สรุปการขายประจำวัน ================")

    print(f"\n<--- {mainFoodlist[0]} --->")
    for idx, val in enumerate(soldsfoodlist):
        print(f"- {sFoodlist[idx]} : ขายได้ {val} จาน | เหลือ {sfoodstock[idx]} จาน")

    if soldffoodlist:
        print(f"\n<--- {mainFoodlist[1]} --->")
        for idx, val in enumerate(soldffoodlist):
            print(f"- {fFoodlist[idx]} : ขายได้ {val} จาน | เหลือ {ffoodstock[idx]} จาน")

    if soldwfoodlist:
        print(f"\n<--- {mainFoodlist[2]} --->")
        for idx, val in enumerate(soldwfoodlist):
            print(f"- {wFoodlist[idx]} : ขายได้ {val} จาน | เหลือ {wfoodstock[idx]} จาน")













