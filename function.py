def get_int_input(prompt):
    """ฟังก์ชั่นสำหรับรับค่าตัวเลขจำนวนเต็ม พร้อมดักจับข้อผิดพลาดด้วย try-except"""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("❌ กรุณากรอกตัวเลขจำนวนเต็มที่ถูกต้องเท่านั้นครับ")

def get_str_N(prompt):
    "ฟังก์ชันสำหรับรับค่าและบังคับให้ใส่ N,n เท่านั้น"
    while True:
        val = input(prompt).strip().lower()
        if val == 'n':
            return val
        print("N,n เท่านั้นครับ")


def get_date():
    # ฟังก์ชั่นสำหรับรับค่าวันที่ (1-31), เดือน (1-12) และปี (4 หลัก, 2026, 2569)
    print("date (วันที่ :)")
    while True:
        try:
            month = int(input("เดือน (ตัวเลข 1-12) : "))
            if not (1 <= month <= 12):
                raise ValueError("เดือนต้องอยู่ระหว่าง 1 ถึง 12 เท่านั้นครับ")
            elif month == 2 :
                day = int(input("วันที่ (1-28) :"))
                if not (1 <= day <= 28):
                    raise ValueError("วันที่ต้องอยู่ระหว่าง 1 ถึง 28 เท่านั้นครับ ")
            elif month == 4 or month == 6 or month == 9 or month == 11:
                day = int(input("วันที่ (1-30): "))
                if not (1 <= day <= 30):
                    raise ValueError("วันที่ต้องอยู่ระหว่าง 1 ถึง 30 เท่านั้นครับ")
            else :
                day = int(input("วันที่ (1-31) : "))
                if not (1 <= day <= 31):
                    raise ValueError("วันที่ต้องอยู่ระหว่าง 1 ถึง 31 เท่านั้นครับ")
            
            year_str = input("ปี (พ.ศ. 4 หลัก อยู่ในปี พ.ศ.2569 เท่านั้นครับ ) : ")
            if len(year_str) != 4 or not year_str.isdigit():
                raise ValueError("ปีต้องเป็นตัวเลข 4 หลักเท่านั้นครับ")

            year = int(year_str)
            if not year == 2569 :
                raise ValueError("ปีต้องอยู่ใน ปี พ.ศ.2569 เท่านั้นครับ")
            
            return day, str(month), year
            
        except ValueError as e:
            print(f"❌ กรุณากรอกตัวเลขจำนวนเต็มที่ถูกต้องเท่านั้นครับ {e}")


def stock(food_list, category_name):
    print(f"\n[เพิ่มสต็อกหมวด: {category_name}]")
    stock = []
    for item in food_list:
        while True:
            try:
                pstock = int(input(f"{item} : "))
                stock.append(pstock)
                break
            except ValueError:
                print("❌ กรุณากรอกตัวเลขจำนวนเต็มที่ถูกต้องเท่านั้นครับ")
    return stock



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