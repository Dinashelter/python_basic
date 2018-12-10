# In this file, we will try to draw a rectangle in the middle of the screen
# In the rectangle there will be a sentence...emmm what should I put...
# we draw the result manually here
#  *----------------------------*
#  |                            |
#  |        I'm an idiot        |
#  |                            |
#  *----------------------------*

screenWidth = 80

sentence = input("Please write a sentence here: ")

sentenceLength = len(sentence)
marginInBox = 6
marginOutOfBox = round((screenWidth - sentenceLength - (6+1)*2) / 2)

line1 = marginOutOfBox * " " + "*" + (marginInBox * 2 + sentenceLength) * "-" + "*"
line2 = marginOutOfBox * " " + "|" + (marginInBox * 2 + sentenceLength) * " " + "|"
line3 = marginOutOfBox * " " + "|" + marginInBox * " " + sentence + marginInBox * " " + "|"
line4 = line2
line5 = line1

print(line1)
print(line2)
print(line3)
print(line4)
print(line5)
