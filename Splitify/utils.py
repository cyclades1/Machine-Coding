class MyError(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return(self.msg)

class User:
	user_dir = dict()
	def __init__(self, name, email, userid, phone):
		self.name = name 
		self.email = email
		self.userid = userid
		self.phone = phone
		self.balance = dict()
		self.given = dict()
		User.user_dir[userid]= self

	def get_balance(self):
		return self.balance

	def add_balance(self, user, amount):
		if user in self.given:
			if amount >=self.given[user]:
				amount -=self.given[user]
				del self.given[user]
			else:
				self.given[user]-=amount
				amount = 0
		if amount==0:
			return
		if user in self.balance:
			self.balance[user]+=amount
		else:
			self.balance[user]=amount
	def get_given(self):
		return self.given

	def add_given(self, user, amount):
		if user in self.balance:
			if amount >=self.balance[user]:
				amount -=self.balance[user]
				del self.balance[user]
			else:
				self.balance[user]-=amount
				amount = 0
		if amount==0:
			return
		if user in self.given:
			self.given[user]+=amount
		else:
			self.given[user]=amount

	def __str__(self):
		return [self.userid, self.balance]

class Splitter:
	def __init__(self, spender, price, splittype ,userlist, divide_list = []):
		self.spender = spender
		self.price = price
		self.split_type = splittype
		self.userlist = userlist
		self.divide_list = divide_list

	def splitequal(self, price, number):
		price_per_person = price/number
		extra = price - price_per_person*number
		price_list = [price_per_person]*number
		price_list[0]+=extra
		return price_list

	def splitexact(self, price, pricelist):
		return pricelist
		
	def splitpercent(self, price, percentlist):
		price_list = []
		for percent in percentlist:
			price_list.append((percent*price)/100)
		price_list[0]+= price - sum(price_list)
		return price_list

	def split(self):
		price_list = None
		user_cnt = len(self.userlist)
		if self.split_type == "EXACT":
			price_list = self.splitexact(self.price,self.divide_list)
		if self.split_type == "EQUAL":
			price_list = self.splitequal(self.price,user_cnt)
		if self.split_type == "PERCENT":
			price_list = self.splitpercent(self.price,self.divide_list)

		for i in range(user_cnt):
			user = self.userlist[i]
			if user == self.spender:
				continue
			user_price = price_list[i]
			User.user_dir[self.spender].add_given(user, user_price)
			User.user_dir[user].add_balance(self.spender, user_price)
	
