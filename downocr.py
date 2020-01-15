import pytesseract as tess
from datamuse import datamuse
import json
from PIL import Image

api = datamuse.Datamuse()

im = Image.open("down1.jpg")
text = tess.image_to_string(im)

i = 0
last = i
for x in text:
    if x == 'o':
        x = ' '
    if x == ')':
        last = i
    i = i + 1

newtext = text[:last].split(')')
newtext2 = []
temp = []
dic = ()
for x in newtext:
    temp.clear()
    # print(x)
    x = x.replace('\n', '')
    asd = x.split(' ', 1)
    # print(asd)
    temp.append(asd[0])
    temp.append(asd[1].split('('))
    print(temp)
    newtext2.append(temp[:])

print(newtext2)
print(len(newtext2))
print(newtext2[0][1][0])

best_word = api.words(ml=newtext2[0][1][0])
print(type(best_word))
print(best_word)
print(len(best_word[0]['word']))
print(newtext2[1][1][1][0])

#print('-------------------------------------------------')

finalans = [None] * len(newtext2)

for x in range(len(newtext2)):
    #print('-------------------------------------------------')
    best_word = api.words(ml=newtext2[x][1][0], max=100)
    #print(best_word)
    #print('-------------------------------------------------')
    for y in range(50):
        #print(len(best_word[y]['word']))
        #print('-------------------------------------------------')
        #print(newtext2[x][1][1][0])
        #print('-------------------------------------------------')
        if(len(best_word[y]['word'])==int(newtext2[x][1][1][0])):
            finalans[x] = best_word[y]['word']
            break


print(finalans)
