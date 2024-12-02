ItemsInCart = 0
#2 items will be added to cart

# if ItemsInCart !=2: # raise Exception("Products Cart count not matching")
#     pass
#
# assert (0 == ItemsInCart)
#
# # try, catch
#
# try:
#     with open('filelog.txt', 'r') as reader:
#         reader.read()
#
# except:
#     print("FAILUREEEE on try block!")

try:
    with open('filelog.txt', 'r') as reader:
        reader.read()

except Exception as e:
    print(e)

finally:
    print("cleaning up resources")