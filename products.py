import os #operating system 

def read_file(filename):
    products = []
    with open(filename,"r", encoding = "utf-8") as f:
            for line in f:
                if "商品,價格" in line:
                    continue #繼續下一個迴圈，不會執行下面的程式
                name, price= line.strip().split(",")
		#name = s[0] 這兩行 變成上面一行
		#price = s[1]
		#strip.() = 去掉\n。split分割，（）裡面寫用什麼切割
                products.append([name, price])
            return products

#讓使用者輸入 
def user_input(products):
    while True:
        name = input("請輸入商品名稱")
        if name == "q":
            break
        price = input("請輸入商品價格")
        p = []
	#p.append(name)
	#p.append(price)
	#p = [name, price]#上兩行的組合
        products.append([name, price])
    print(products)
    return products

#印出所有購買紀錄
def print_products(products):
    for p in products:
        print(p[0], "的價格是", p[1])

#寫入檔案
def write_file(filename, products):
    with open(filename, "w",encoding = "utf-8") as f:
        f.write("商品, 價格\n")
        for p in products:
            f.write(p[0] + "," + p[1] + "\n")

def main():
    filename = "products1.csv"
    if os.path.isfile(filename): #檢查檔案在不在
        products = read_file(filename)
        print("Yeah!找到檔案了")
    else:
        print("找不到檔案")

    products = user_input(products)
    print_products(products)
    write_file("products1.csv", products)

main()
