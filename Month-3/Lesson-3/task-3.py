#masala: Write a python program that takes a text file as input and returns the number of words of the given text file
#Note: Some words can be separated by a comma with no space  => Matnli faylni kirish sifatida qabul qiluvchipython dasturini yozing va berilgan
# matn faylining soz sonini qaytaring. Eslatma: ba'zi sozlarni bo'sh joysiz vergul bilan ajratish mumkin


with open('t7.txt', 'r') as f:
    matn = f.read()
    sozlar =matn.split()
    print(len(sozlar))