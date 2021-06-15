import random
y = 0
r = random.randint(1,100)
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


