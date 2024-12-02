#file = open('text.txt')
#Read all the contents of file
#read n number of characters by passing parameter
#print(file.read(5))

#read one singe line at a time readLine()
#print(file.readline())
#print(file.readline())

#Print Line by line using readline method
# line = file.readline()
# while line != "":
#     print(line)
#     line = file.readline()

# list = file.readlines()
# for i in list:
#     print(i)

#file.close()

#this does not need close.
#read the file and store all the lines in list
#reverse the list
#write the list back to the file
with open('text.txt', 'r') as reader:
    content = reader.readlines()
    with open('text.txt', 'w') as writer:
        for line in reversed(content):
            writer.write(line)



