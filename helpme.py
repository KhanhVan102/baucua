import random
import os

cubes = [
	'Bầu','Cua','Tôm','Cá','Hươu','Gà'
	]

cubesNew = [
	'Bầu','Cua','Tôm','Cá','Hươu','Gà'
	]

random.shuffle(cubesNew)
dealer = []
player = []

dealer.append(cubesNew[0])
dealer.append(cubesNew[1])
dealer.append(cubesNew[2])

def converChoice(index):
	return cubes[index]

def openBowl():
	listResult = []
	print('Trên dĩa có: [{}]'.format(']['.join(dealer)))
	for item in player:
		for face in dealer:
			if(item==face):
				listResult.append(face)
	if len(listResult)>0 :
		print('Bạn đã thắng cược: {}'.format('-'.join(listResult)))
	else:
		print('Bạn quá non!')


def selectFace():
	print('1.Bầu')
	print('2.Cua')
	print('3.Tôm')
	print('4.Cá')
	print('5.Hươu')
	print('6.Gà')
	print('7.Bỏ qua')
	choice = input('Bạn muốn đặt cược? :')
	if(int(choice)>=7):
		openBowl()
		return True
	else:
		player.append(converChoice(int(choice)-1))
		return False

while True:
	os.system('cls' if os.name == 'nt' else 'clear')
	if len(player)>0:
		print('Bạn đã đặt cược: [{}]'.format(']['.join(player)))
		answer = input('Bạn muốn đặt cược tiếp không?(y/n): ')
		if answer == 'y':
			if selectFace():
				break
		else:
			openBowl()
			break
	else:
		if selectFace():
			break
