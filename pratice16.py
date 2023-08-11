# from random import *

# list=[10,20,30,2,3,5,6,78,8]

# print([ number for number in list if number%2==0])


artist_list =[["KK",["song1","song2","song3"],"6pm"],["Sonu",["song4","song5","song6"],"7pm"],["Badasha",["song7","song8","song9"],"8pm"]]


#display the  artist name and performance time

for i in artist_list:
    print(i[0],i[2])

#display the songs played in the concept 
for i in artist_list:
    [print(song) for song in i[1]]

#remove the song 5 from the sonu

artist_list[1][1].remove("song5")
print(artist_list[1])

artist_list2=[["arjith",["songA","songb","songc"],"8PM"],["jubin",["songd","songe","songf"],"9PM"]]
#combing the addition artist to the music festival
artist_list.extend(artist_list2)
print("Updated artist list ",artist_list)
#KK is not performing 
for i in range(0,len(artist_list)-1):
    print(artist_list[i][0])
    if artist_list[i][0]=="KK":
        artist_list.pop(i)
# sorting based on the time 
print("After removing KK ",artist_list)
def sortSecond(val):
    return val[2].upper()
artist_list.sort(key=sortSecond)
print(artist_list)


