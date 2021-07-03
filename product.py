import os #operating system

def read_file(filename):
    products = [] #大清單
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            if '商品,價格' in line:
                continue
            name, price = line.strip().split(',') #忽略/n並用逗號切割
            products.append([name, price])
    return products

def user_input(products):
    while True:
        name = input('請輸入商品名稱：')
        if name == 'q':
            break
        price = input('請輸入商品價格：')
        price = int(price)
        #大清單中的小清單
        products.append([name, price])
    print(products)
    return products

#第一個[0]是大清單的第一筆，第二個[0]是小清單的第一筆
#products[0][0]

#顯示products大清單內小清單p的各項
def print_products(products):
    for p in products:
        print(p[0], '的價格為', p[1])

#寫入檔案
def write_file(filename, products):
    with open(filename, 'w', encoding='utf-8') as f:
        f.write('商品,價格\n')
        for p in products:
            f.write(p[0] + ',' + str(p[1]) + '\n')

def main():
    filename = 'products.csv'
    if os.path.isfile(filename): #檢查檔案
        print('有檔案')
        products = read_file(filename)
    else:
        print('沒檔案')

    products = user_input(products)
    print_products(products)
    write_file('products.csv', products)

main()