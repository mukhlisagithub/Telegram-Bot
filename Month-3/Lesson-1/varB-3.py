#3-masala: Nozima matematik hisob-kitoblar qilishda qiynaladi. unga imtihon payti quyidagicha masala tushdi. Bir list
# elementlari, yani sonlar probel bilan ajratib beriladi. Siz listdagi 2 ta ixtiyoriy elementni olib, agar ularning farqi 3 ga
# teng bolsa, shu son;arni list qilib olib, natijaviy listga qoshing. har bir sondan 1 martadan foydalanish kerak boladi.
#namuna: 0 1 2 5 9 90 4 8 93 6 => output=[[2,5],[6,9],[90,93],[1,4]] shu tarzda bolishi kerak!
#!Izoh: [5,8] chiqmasligi kerak, chunki [5,2]da 5 ishlatilgan. Agar [5,8] olinsa, unda [2,5] chqmasligi kerak!!!

nums = list(map(int, input().split()))
res = []
i = 0
while i<len(nums):
    v = nums[i]+3
    if v in nums:
        res.append([nums[i],v])
        nums.remove(nums[i])
        nums.remove(v)
    else:
        i += 1
print(res)

