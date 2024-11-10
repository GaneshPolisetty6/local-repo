# finding whether a number is armstrong or not
num = 153
length = len(str(num))
res = 0
for i in str(num):
    res += int(i)**length
print(res)
if res == num:
    print('armstrong number')