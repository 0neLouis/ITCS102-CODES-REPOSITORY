# Code_Challenge2

cash = 10287

print("Money to deposit -->", cash)

#money to deposit

thousand=cash//1000
money = (cash - thousand*1000)
fivehundred=cash//500
money = (cash - fivehundred*500)
twohundred=cash//200
money = (cash - twohundred*200)
onehundred=cash//100
money = (cash - onehundred*100)


print("You have 1k of", thousand)
print("You have fivehundred of", fivehundred)
print("You have twohundred of", twohundred)
print("You have onehundred of", onehundred)
