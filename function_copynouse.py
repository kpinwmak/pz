def get_int_input(prompt):
    """ฟังก์ชั่นสำหรับรับค่าตัวเลขจำนวนเต็ม พร้อมดักจับข้อผิดพลาดด้วย try-except"""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("❌ กรุณากรอกตัวเลขจำนวนเต็มที่ถูกต้องเท่านั้นครับ")


def get_int_28(prompt):
    while True:
        try:
            val = int(input(prompt))
            if not (1 <= val <= 28):
                raise ValueError("วันที่ต้องอยู่ระหว่าง 1 ถึง 28 เท่านั้นครับ ")
            return val
        except ValueError as e:
            print(e)

def get_int_30(prompt):
    while True:
        try:
            val = int(input(prompt))
            if not (1 <= val <= 30):
                raise Exception("วันที่ต้องอยู่ระหว่าง 1 ถึง 30 เท่านั้นครับ ")
            return val
        except Exception as e :
            print(e)

def get_int_31(prompt):
    while True:
        try:
            val = int(input(prompt))
            if not (1 <= val <= 31):
                raise Exception("วันที่ต้องอยู่ระหว่าง 1 ถึง 31 เท่านั้นครับ ")
            return val
        except ValueError as e:
            print(f"❌ กรุณากรอกให้ถูกต้อง | {e} |")


def get_year(p):
    while True:
            try:
                val = input(p)
                if len(val) != 4 or not val.isdigit():
                    raise ValueError("ปีต้องเป็นตัวเลข 4 หลักเท่านั้นครับ")
                year = int(val)
                if not year >= 2569 :
                    raise ValueError("ปีต้องอยู่ใน ปี พ.ศ.2569 หรือสูงเท่านั้นครับ")
                return year
            except Exception as e:
                print(e)


def get_str_N(p):
    while True:
        try:
            val = input(p).strip().lower()
            if val != 'n':
                raise Exception("N, n เท่านั้นครับ")
            return val
        except Exception as e:
            print(e)


def get_str_nb(p):
    while True:
            try:
                val = input(p).strip().lower()
                if val != 'n' and val != 'b':
                    raise Exception("(N, n or B,b) เท่านั้นครับ")
                return val
            except Exception as e:
                print(e)







def get_date():
    # ฟังก์ชั่นสำหรับรับค่าวันที่ (1-31), เดือน (1-12) และปี (4 หลัก, 2026, 2569)
    print("|------------------DATE------------------|")
    while True:
        try:
            month = get_int_input("เดือน (ตัวเลข 1-12) : ")
            if not (1 <= month <= 12):
                raise ValueError("เดือนต้องอยู่ระหว่าง 1 ถึง 12 เท่านั้นครับ")
            elif month == 2 :
                day = get_int_28("วันที่ (1-28) :")
            elif month == 4 or month == 6 or month == 9 or month == 11:
                day = get_int_30("วันที่ (1-30): ")
            else :
                day = get_int_31("วันที่ (1-31) : ")

            year = get_year("ปี (พ.ศ. 4 หลัก อยู่ในปี พ.ศ.2569 หรือสูงกว่าครับ ) : ")
            
            return day, str(month), year
            
        except ValueError as e:
            print(f"❌ กรุณากรอกให้ถูกต้อง | {e} |")


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
    # """ฟังก์ชั่นสำหรับบันทึกการขายและหักลบสต็อก"""
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