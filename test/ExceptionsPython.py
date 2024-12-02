ItemsInCart = 0
#2 items will be added to cart

if ItemsInCart != 2:
    pass
    # raise Exception("Products Cart count not matching")

assert(ItemsInCart == 0)

# try, catch
try:
    with open('filelog.txt', 'r') as reader:
        reader.read()

except Exception as e:
    print(e)