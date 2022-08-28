import sys
input= sys.stdin.readline

roomCount=1
roomNum=1
N=int(input())

while N>roomNum:
  roomNum+=6*roomCount
  roomCount+=1

print(roomCount)