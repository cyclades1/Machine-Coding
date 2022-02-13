from utils import User, Splitter


class MyError(Exception):

    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return(self.msg)



getnums = lambda : map(int, input().split())
getnum = lambda : int(input())
types = ["EXACT","PERCENT","EQUAL"]

def main():
	for i in range(1,10):
		userid = "u"+str(i)
		newuser = User(userid, userid, userid, userid)

	t = getnum()
	for _ in range(t):
		choice = input().split()
		if choice[0] == "SHOW":
			if len(choice)==2:
				fl = True
				userid = choice[1]
				pricemap = User.user_dir[userid].get_balance()
				for spender in pricemap:
					fl = False
					print(userid, "owes to ", spender, pricemap[spender])
				pricemap = User.user_dir[userid].get_given()
				for person in pricemap:
					fl = False
					print(person, "owes to ", userid, pricemap[person])
				if fl :
					print("No balance")
				continue
			else:
				fl = True
				for user in User.user_dir.keys():
					pricemap = User.user_dir[user].get_balance()
					for spender in pricemap:
						fl = False
						print(user, "owes to ", spender, pricemap[spender])
				if fl:
					print("No balance")
			continue
		user, price  = input().split()
		try:
			price = float(price)
		except Exception as e:
			print(e)
			break
		try:
			user_list = list(input().split())
			for u in user_list:
				if not u in User.user_dir:
					raise(MyError("User does not exist: "+str(user)))
		except Exception as e:
			print(e)
			break
		split_type = input()
		
		if not split_type in types:
			print("invalid split type: ", split_type)
			break

		divide_list = []
		if split_type!="EQUAL":
			divide_list = list(getnums())
			if len(user_list)!=len(divide_list):
				print("User list and division list count is not equal ({},{})".format(len(user_list),len(divide_list)))
				break
			if split_type=="EXACT" and sum(divide_list)!=price:
				print("Sum of division list is not equal to total price")
				break
			if split_type=="PERCENT" and sum(divide_list)!=100:
				print("Sum of division list is not equal 100")
				break

		splitter = Splitter(user, price, split_type, user_list, divide_list)
		splitter.split()


if __name__ =="__main__":
	main()