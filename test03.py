#  Primtive Data Type
# Number , Boolean , String

# Non Primtive Data Type / Collection / Data Structur ข้อมูลชนิดไม่พื้นฐาน
#List , Tuple , Set , Dictionary

#Data Type จะเอามาใช้กับเขียนโปรแกรมในเรื่องของ  ตัวแปร พารามิเตอร์ ฟังก์ชัน เมธอด

#----------- List คือข้อมูลหลายข้อมูล คนละชนิด ซ้ำกันได้ และมีลำดับ อีกทั้งแก้ไขได้ด้วย----------
        #  0    1    2    3    4         5
my_listl = [10, 20, True, 10, 'SAU', [20, 'Iot']]
        #   6   5    4    3    2          1     ติด-

#----------- Tuple คือข้อมูลหลายข้อมูล คนละชนิด ซ้ำกันได้ และมีลำดับ แต่แก้ไขไม่ได้ เพิ่ม ลบไม่ได้----------
        #   0    1    2    3    4         5
my_tuplel = [10, 20, True, 10, 'SAU', [20, 'Iot']]
        #   6   5    4    3    2          1     ติด-

#----------- Set คือข้อมูลหลายข้อมูล คนละชนิด ซ้ำกันไม่ได้ {หากซ้ำถือว่าเป็นตัวเดียวกัน} และมีลำดับ และแก้ไขไม่ได้ แต่เพิ่ม ลบได้----------
my_setl = {10, 20, True, 10, 'SAU', (20, 'Iot')}

#----------- Dictionary คือข้อมูลหลายข้อมูล ที่เป็น key value แก้ไขได้ด้วย ไม่มีลำดับ ซ้ำได้----------
#key เป็น String/Integer ส่วน value เป็นอะไรก็ได้
my_dictionaryl = {'name':'mod','age':32, 555:999, 'flag':True, 'wow':[10, 20, 30]}