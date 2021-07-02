products = [] #大清單
while True:
    name = input('請輸入商品名稱：')
    if name == 'q':
        break
    price = input('請輸入商品價格：')
    #大清單中的小清單
    p = [] #也可以用p = [name, price]就不用append的兩行
    p.append(name)
    p.append(price)
    products.append(p)
print(products)

#第一個[0]是大清單的第一筆，第二個[0]是小清單的第一筆
#products[0][0]

#顯示products大清單內小清單p的各項
for p in products:
    print(p[0], '的價格為', p[1])

#寫入檔案
with open('products.csv', 'w') as f:
    for p in products:
        f.write(p[0] + ',' + p[1] + '\n')