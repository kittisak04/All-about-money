#http://app.memo8.com/web/car-calculator/#CalTab2#
price = float(input('carprice ')) #carprice
down_baht = float(input('down ')) #down
pernum = float(input('year ')) #time
interrest = float(input('dok ')) #dok

down_per = (down_baht/price)*100 #down money baht
price_remain = price - down_baht
total_inter = interrest * (pernum/12)
price_total = (price_remain * total_inter)/100 #total price
pay_mouth = (price_total+price_remain)/pernum

print down_per
print price_remain
print pay_mouth
