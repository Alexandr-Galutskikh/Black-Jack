import random

class BlackJack:
	lst = [[elem, sym] for sym in "♥♦♣♠" for elem in '2,3,4,5,6,7,8,9,10,J,Q,K,A'.split(',')]

	def __init__(self):
		self.count = 0
		self.player_card = [self.random_card() for elem in range(2)]
		self.comp_card = [self.random_card() for elem in range(2)]
		self.sum_player = self.mathyn(self.player_card[0][0]) + self.mathyn(self.player_card[1][0])
		self.sum_comp = self.mathyn(self.comp_card[0][0]) + self.mathyn(self.comp_card[1][0])
		self.stroke_player_card = ''.join(self.player_card[0]) + ' ' + ''.join(self.player_card[1])
		self.stroke_comp_card = ''.join(self.comp_card[0]) + ' ' + ''.join(self.comp_card[1])

	def start(self):
		self.check_result()

	def random_card(self):
		card = self.lst.pop(self.lst.index(random.choice(self.lst)))
		return card

	def mathyn(self, elem):
		if elem == 'A':
			return 11
		elif elem in ['J', 'Q', 'K']:
			return 10
		else:
			return int(elem)

	def check_ace(self):
		if self.count == 0:
			if 'A' in self.stroke_player_card:
				self.count += 1
				self.sum_player -= 10
				self.check_result()

	def move(self):
		action = input('Ваш ход(Взять, остановиться):').lower()
		if action == 'взять':
			self.append_card1()
			self.check_result()
		else:
			if self.sum_comp >= 18:
				self.result()
			else:
				self.append_card2()


	def append_card1(self):
		self.player_card.append(self.random_card())
		self.sum_player += self.mathyn(self.player_card[-1][0])
		self.stroke_player_card += ' ' + ''.join(self.player_card[-1])

	def append_card2(self):
		self.comp_card.append(self.random_card())
		self.sum_comp += self.mathyn(self.comp_card[-1][0])
		self.stroke_comp_card += ' ' + ''.join(self.comp_card[-1])
		if self.sum_comp >= 18:
			self.result()
		else:
			self.append_card2()

	def check_result(self):
		if self.sum_player > 21 or self.sum_comp == 21:
			self.check_ace()
			if self.sum_player > 21:
				self.result()
		elif self.sum_player == 21:
			self.result()
		else:
			self.info()
			self.move()

	def result(self):
		if self.sum_player <= 21 and self.sum_player > self.sum_comp or self.sum_comp > 21:
			self.info()
			print('Игрок выиграл')
		elif self.sum_player == self.sum_comp:
			self.info()
			print('Ничья')
		else:
			self.info()
			print('Компьютер выиграл')

	def info(self):
		print('Ваши карты: {} \t{}\nКарты компьютера: {} \t{}'.format(
			self.stroke_player_card, self.sum_player,
			self.stroke_comp_card, self.sum_comp
		))

new_play = BlackJack()
new_play.start()
