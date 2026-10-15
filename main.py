from function import get_date, stock, input_sales_category, get_str_N





mainFoodlist = ['จานเดียว', 'ผัดและทอด', 'ต้มและแกง']
sFoodlist = ["กะเพราหมูสับ/ไก่ไข่ดาว", "ผัดซีอิ๊วหมู/ไก่", "ข้าวผัดหมู/ไก่", "ข้าวหน้าไก่/หมูทอดกระเทียม", "ผัดพริกแกงหมู/ไก่"]
fFoodlist = ["ไข่เจียวหมูสับ", "ผัดผักบุ้งไฟแดง", "ปลาทอดน้ำปลา/ทอดสามรส", "กุ้งผัดพริกเกลือ/ผัดผงกะหรี่", "ผัดคะน้าหมูกรอบ"]
wFoodlist = ["ต้มยำกุ้ง/ทะเล", "ต้มจืดเต้าหู้หมูสับ", "แกงเขียวหวานไก่"]


# day, month, year = get_date()
# print(f"---- Food Stock (ประจำวันที่ {day}/{month}/{year}) ----")

# ------------------------------------------------------------------------------------ปรับให้ด้วย
try:
    sfoodstock = stock(sFoodlist, mainFoodlist[0])
    go = get_str_N("ไปต่อ Next (n) : ")
    
    ffoodstock = stock(fFoodlist, mainFoodlist[1])
    go = get_str_N("ไปต่อ Next (n) : ")
    
    wfoodstock = stock(wFoodlist, mainFoodlist[2])
    go = get_str_N("ไปต่อ Next (n) : ")
except Exception as e:
    print(f"เกิดข้อผิดพลาด: {e}")



print(f"\n|----ในStock ของคุณมีดังนี้----|")
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


# -------------------------------------------------------------------------------------------ปรับให้ด้วย


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












