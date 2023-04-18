mbti = {'E':'I', 
       'I':'E',
       'S':'N',
       'N':'S',
       'T':'F',
       'F':'T',
       'P':'J',
       'J':'P'}

mine = input()
ideal = ''

for i in mine:
    ideal += mbti[i]

print(ideal)
