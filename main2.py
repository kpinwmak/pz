from function import get_date, stock, input_sales_category, get_str_N , get_str_nb




mainFoodlist = ['จานเดียว', 'ผัดและทอด', 'ต้มและแกง']
sFoodlist = ["กะเพราหมูสับ/ไก่ไข่ดาว(50฿)", "ผัดซีอิ๊วหมู/ไก่(50฿)", "ข้าวผัดหมู/ไก่(50฿)", "ข้าวหน้าไก่/หมูทอดกระเทียม(50฿)", "ผัดพริกแกงหมู/ไก่(50฿)"]
fFoodlist = ["ไข่เจียวหมูสับ(40฿)", "ผัดผักบุ้งไฟแดง(45฿)", "ปลาทอดน้ำปลา/ทอดสามรส(119฿)", "กุ้งผัดพริกเกลือ/ผัดผงกะหรี่(80฿)", "ผัดคะน้าหมูกรอบ(65฿)"]
wFoodlist = ["ต้มยำกุ้ง/ทะเล(110฿)", "ต้มจืดเต้าหู้หมูสับ(60฿)", "แกงเขียวหวานไก่(55฿)"]
pricesFoodlist=[50]
pricefFoodlist=[40,45,119,80,65]
pricewFoodlist=[110,60,55]


day, month, year = get_date()
print(f"---- Food Stock (ประจำวันที่ {day}/{month}/{year}) ----")

while True:
    print("\n|------------------------------เพิ่มสต็อก------------------------------|")

    sfoodstock = stock(sFoodlist, mainFoodlist[0])
    go = get_str_N("ไปต่อ Next (n) : ")

    ffoodstock = stock(fFoodlist, mainFoodlist[1])
    go = get_str_N("ไปต่อ Next (n) : ")

    wfoodstock = stock(wFoodlist, mainFoodlist[2])
    print("|------------------------------เพิ่มสต็อกสำเร็จ------------------------------|\n")

    print(f"\n|------------------------------ใน Stock ของคุณมีดังนี้------------------------------|")
    print(f"\n<--- {mainFoodlist[0]} --->")
    for idx in range(len(sfoodstock)):
        print(f"- {sFoodlist[idx]} : เหลือ {sfoodstock[idx]} จาน")
    if ffoodstock:
        print(f"\n<--- {mainFoodlist[1]} --->")
        for idx in range(len(ffoodstock)):
            print(f"- {fFoodlist[idx]} : เหลือ {ffoodstock[idx]} จาน")
    if wfoodstock:
        print(f"\n<--- {mainFoodlist[2]} --->")
        for idx in range(len(wfoodstock)):
            print(f"- {wFoodlist[idx]} : เหลือ {wfoodstock[idx]} จาน")
    print(f"\n|------------------------------ใน Stock ของคุณมีดังนี้------------------------------|\n")
    go = get_str_nb("ไปต่อ Next (n) ย้อนกลับ Back (b) : ")
    if go == "n":
        break






print(f"\n|------------------------------บันทึกการขาย------------------------------|")
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
print(f"\n|------------------------------บันทึกการขาย------------------------------|\n")
# 4. แสดงผลสรุปการขาย
print(f"\n================ สรุปการขายประจำวัน ================\n       |---------ประจำวันที่ {day}/{month}/{year}---------|")
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


categories = [
    (mainFoodlist[0], sFoodlist, soldsfoodlist, pricesFoodlist * len(sFoodlist)),
    (mainFoodlist[1], fFoodlist, soldffoodlist, pricefFoodlist),
    (mainFoodlist[2], wFoodlist, soldwfoodlist, pricewFoodlist),
]
 
total_all = 0
for cat_name, foods, solds, prices in categories:
    cat_total = 0
    for i in range(len(foods)):
        money = solds[i] * prices[i]
        cat_total += money
    total_all += cat_total
 
print(f"\n==================================================")
print(f"ยอดขายรวมทั้งวัน : {total_all:,} บาท")
print(f"==================================================")








