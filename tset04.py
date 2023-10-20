#----------- List คือข้อมูลหลายข้อมูล คนละชนิด ซ้ำกันได้ และมีลำดับ อีกทั้งแก้ไขได้ด้วย----------
        #  0    1    2    3    4         5
my_listl = [10, 20, True, 10, 'SAU', [20, 'Iot']]
        #   6   5    4    3    2          1     ติด-
                                    #  2     1  ติด-
#การเข้าถึงข้อมูลใน List เพื่อเอาข้อมูลมาใช้ หรือแก้ไขคำข้อมูลให้มันใหม่
#เข้าถึงทีละข้อมูล
print(my_listl[4]) # SAU
print(my_listl[-2]) # SAU
print(my_listl[5]) # [20, 'Iot]
print(my_listl[-1]) # [20, 'Iot']
print(my_listl[5][1]) # Iot
print(my_listl[-1][-1]) # Iot

# เข้าถึงทีละหลายข้อมูล เราเรียกการ Slicing ผลลัพธ์จะเป็น List
print(my_listl[1:4])  # 20, True, 10
print(my_listl[3:])  # 10, 'SAU', [20, 'Iot']
print(my_listl[:3]) # 10, 20, True

#เข้าถึงทุกข้อมูล
for info in my_listl :
    print(info, end=', ')

print()

print(my_listl)
my_listl[4] = 'Thailand'
print(my_listl)

# List Metod
my_listl2 = [10, 20, True, 10, 'SAU', [20, 'Iot']]
my_listl2.append('wow')
print(my_listl2)
my_listl2.append(['111,222,333'])
print(my_listl2)
my_listl2.extend([444,555])
print(my_listl2)
my_listl2.remove(10) #เอาออกตัวเดียวตัวเเรกที่เจอ
my_listl2.remove('SAU')
my_listl2.remove(['111,222,333'])
print(my_listl2)
my_listl2.pop()
my_listl2.pop()
my_listl2.pop()
print(my_listl2)
my_listl2.pop(2) #2 คือ index
print(my_listl2)

# List functing -> len(), min(), max()
my_listl3 = [10, 20, 10, 30, True]
print(len[my_listl3])
print(min[my_listl3])
print(max[my_listl3])
