time = list(map(int,input("Enter time: ").split()))
distance = list(map(int, input("Enter distance: ").split()))
if(len(time)!=len(distance)):
    print("Time and distances number is not equal!!!!")
time_deltas = []
distance_deltas = []
for i in range(len(time)):
    if(i<len(time)-1):
     time_deltas.append(time[i+1] -time[i])
     distance_deltas.append(distance[i+1]-distance[i])
velocities = []
print(time_deltas)
print(distance_deltas)
for i in range(len(time_deltas)):
   velocity = distance_deltas[i]/time_deltas[i]
   velocities.append(velocity)
print(velocities)
for i in range(len(time_deltas)):
   print('Prędkość na odcinku ', time[i],"s","-",time[i+1],"s",": ",velocities[i]," m/s",sep="")
print("Średnia prędkość: ",sum(velocities)/len(velocities)," m/s")