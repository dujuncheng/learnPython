filename = 'pi_digits.txt'

# with open(filename) as filecontent:
#     print(filecontent.read())


lines = []
text = ''
with open(filename) as filecontent:
    lines = filecontent.readlines()


for line in lines:
    text = text + str(line)

print (text)