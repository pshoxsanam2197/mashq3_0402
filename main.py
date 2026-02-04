# 1.8-masala
data = [10, 20, 30, 40, 50]
if 30 in data:
    print("30 ro'yxatda bor")
else:
    print("30 ro'yxatda yo'q")
i = data.index(30)
print("30 indeksi:", i)
data[i] = 35
print(data)
data.append(60)
print(data)
print(data)

# 1.9-masala
nums = [1, 2, 3, 4, 5, 6, 7, 8]
new_roy = []
for i in range(len(nums)):
    if nums [i] % 2 == 0:
        new_roy.append(nums[i])
print(new_roy)
summa = sum(new_roy)
print(summa)
new_roy.sort()
print(new_roy)
new_roy.append(10)
print(new_roy)
print(new_roy)
