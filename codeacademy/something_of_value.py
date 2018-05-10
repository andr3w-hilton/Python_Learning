// A DAY AT THE SUPERMARKET
// Something of Value
// For paperwork and accounting purposes, let's record the total value of your inventory. It's nice to know what we're worth!

prices = {
  "banana": 4,
  "apple": 2,
  "orange": 1.5,
  "pear": 3
}

stock = {
  "banana": 6, 
  "apple": 0, 
  "orange": 32, 
  "pear": 15
}

for key in prices:
  print key
  print "Price = %s" % prices[key]
  print "Stock = %s" % prices[key]
  
total = 0
for number in prices:
	total += prices[number]*stock[number]
  
print total
