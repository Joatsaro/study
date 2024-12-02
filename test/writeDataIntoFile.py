#read the file and store all the lines in list
#reverse the list
#write the list back to the file
with open('text.txt', 'r') as reader:
    content = reader.readlines() #[abd, bvdsf, cat, dog, elephant]
    reversed(content) #[elephant, dog, cat, bvdsf, abc]
    with open('test.txt', 'w') as writer:
        for line in reversed(content):
            writer.write(line)
