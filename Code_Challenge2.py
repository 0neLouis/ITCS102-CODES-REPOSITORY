#coding challenge 2

cash = 10287

print("money to spend", cash)

thousand = (cash//1000)
cash = (cash - thousand*1000)
fivehundreds = (cash//500)
cash = (cash - fivehundreds*500)
twohundreds = (cash//200)
cash = (cash - twohundreds*200)
onehundreds = (cash//100)
cash = (cash - onehundreds*100)
fifty = (cash//50)
cash = (cash - fifty*50)
twenty = (cash//20)
cash = (cash - twenty*20)
ten = (cash//10)
cash = (cash - ten*10)
five = (cash//5)
cash = (cash - five*5)
one = (cash//1)
cash = (cash - one*1)

print("you have", thousand, " of thousand bills")

print("you have", fivehundreds, " of fivehundred bills")

print("you have", twohundreds, " of twohundreds bills")

print("you have", onehundreds, " of onehundred bills")

print("you have", fifty, " of fifty peso bills")

print("you have", twenty, " of twenty peso bills")

print("you have", ten, " of ten peso coins")

print("you have", five, " of five peso coins")

print("you have", one, " of one peso coins")





