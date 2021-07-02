import os #operating system

products = [] #大清單

if os.path.isfile('products.csv'): #檢查檔案
    print('有檔案')
    #讀取舊檔案
    with open('products.csv', 'r', encoding='utf-8') as f:
        for line in f:
            if '商品,價格' in line:
                continue
            name, price = line.strip().split(',') #忽略/n並用逗號切割
            products.append([name, price])
    print(products)
else:
    print('沒檔案')

while True:
    name = input('請輸入商品名稱：')
    if name == 'q':
        break
    price = input('請輸入商品價格：')
    price = int(price)
    #大清單中的小清單
    products.append([name, price])
print(products)


#第一個[0]是大清單的第一筆，第二個[0]是小清單的第一筆
#products[0][0]

#顯示products大清單內小清單p的各項
for p in products:
    print(p[0], '的價格為', p[1])

#寫入檔案
with open('products.csv', 'w', encoding='utf-8') as f:
    f.write('商品,價格\n')
    for p in products:
        f.write(p[0] + ',' + str(p[1]) + '\n')