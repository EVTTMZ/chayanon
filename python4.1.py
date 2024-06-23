
numbers = range(1, 21)

# สร้างลิสต์เพื่อเก็บจำนวนคี่และจำนวนคู่
even_numbers = []
odd_numbers = []

# วนลูปผ่านตัวเลขทุกตัวในช่วง 1 ถึง 20
for number in numbers:
    if number % 2 == 0:
        even_numbers.append(number)  # ถ้าตัวเลขหารด้วย 2 ลงตัว ถือเป็นจำนวนคู่
    else:
        odd_numbers.append(number)  # ถ้าไม่ลงตัว ถือเป็นจำนวนคี่

# แสดงผลลัพธ์
print("จำนวนคู่:", even_numbers)
print("จำนวนคี่:", odd_numbers)