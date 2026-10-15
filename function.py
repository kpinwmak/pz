def get_int_input(prompt):
    """ฟังก์ชั่นสำหรับรับค่าตัวเลขจำนวนเต็ม พร้อมดักจับข้อผิดพลาดด้วย try-except"""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("❌ กรุณากรอกตัวเลขจำนวนเต็มที่ถูกต้องเท่านั้นครับ")

def get_str_N(prompt):
    """ฟังก์ชันสำหรับรับค่าและบังคับให้ใส่ N,n เท่านั้น"""
    while True:
        val = input(prompt).strip().lower()
        if val == 'n':
            return val
        print("N,n เท่านั้นครับ")



def get_date():
    """ฟังก์ชั่นสำหรับรับค่าวันที่ (1-31), เดือน (1-12) และปี (4 หลัก, 2568-2569)"""
    print("date")
    while True:
        try:
            # 1. ตรวจสอบวัน (1-31)
            day = int(input("วันที่ (1-31) : "))
            if not (1 <= day <= 31):
                raise ValueError("วันที่ต้องอยู่ระหว่าง 1 ถึง 31 เท่านั้นครับ")
            
            # 2. ตรวจสอบเดือน (1-12)
            month = int(input("เดือน (ตัวเลข 1-12) : "))
            if not (1 <= month <= 12):
                raise ValueError("เดือนต้องอยู่ระหว่าง 1 ถึง 12 เท่านั้นครับ")
            
            # 3. ตรวจสอบปี (ต้องเป็นตัวเลข 4 หลัก และอยู่ระหว่าง 2568 - 2569)
            year_str = input("ปี (พ.ศ. 4 หลัก เช่น 2568-2569) : ")
            if len(year_str) != 4 or not year_str.isdigit():
                raise ValueError("ปีต้องเป็นตัวเลข 4 หลักเท่านั้นครับ")
            
            year = int(year_str)
            if not (2568 <= year <= 2569):
                raise ValueError("ปีต้องอยู่ระหว่าง 2568 ถึง 2569 เท่านั้นครับ")
            
            return day, str(month), year
            
        except ValueError as e:
            print(f"❌ {e}")


def stock(food_list, category_name):
    print(f"\n[เพิ่มสต็อกหมวด: {category_name}]")
    while True:
        try:
            stock=[]
            for i in food_list:
                pstock = int(input(f"{i} : "))
                stock.append(pstock)
            return(stock)
        except ValueError:
            print("❌ กรุณากรอกตัวเลขจำนวนเต็มที่ถูกต้องเท่านั้นครับ")



# def show1(food_list, mainfood):
#     print(f"ตอนนี้ในStockของ{mainfood[0]}คุณมี")
#     for item in enumerate(food_list,1):
#         print(f"{food_list[item]}")











# def stockback(foodlist):
#     for i in enumerate(foodlist):
#         print(f"ของในStockตอนนี้ {foodlist[i]} :")




# def ask():
#     while True:
#         go = input("ไปต่อNext(n) กลับBack(b) : ").strip().lower()
#         if go == "n" or go == "b":
#             return go
#         print("❌ พิมพ์ n หรือ b เท่านั้นครับ")


# def askb():
    



def input_sales_category(food_list, stock_list, category_name):
    """ฟังก์ชั่นสำหรับบันทึกการขายและหักลบสต็อก"""
    print(f"\n[Sold Food] หมวด: {category_name}")
    sold_list = []
    for idx, item in enumerate(food_list):
        while True:
            soldsfood = get_int_input(f"{item} in stock {stock_list[idx]} sold : ")
            # ป้องกันกรณีขายมากกว่าสต็อกที่มี
            if soldsfood > stock_list[idx]:
                print(f"⚠️ แจ้งเตือน: ของในสต็อกมีแค่ {stock_list[idx]} จาน แต่ขายไป {soldsfood} จาน (กรุณากรอกใหม่)")
            else:
                break
        stock_list[idx] -= soldsfood
        sold_list.append(soldsfood)
    return sold_list