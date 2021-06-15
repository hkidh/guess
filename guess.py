import random
y = 0

i = int(input('請輸入開始數字'))
j = int(input('請輸入結束數字'))
while i >= j:
	print('結束不可小於開始,請重新輸入數字')
	i = int(input('請輸入開始數字'))
	j = int(input('請輸入結束數字'))
	if i < j:
		break
r = random.randint(i,j)
while True:
	x = input('請輸入數字')
	y = y + 1
	x = int(x)
	if x == r:
		print('你猜對了')
		print('總共猜了', y, '次了')
		break
	elif x > r: 
		print('請猜小點')
	elif x < r:
		print('請猜大一點')


