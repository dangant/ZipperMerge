from vpython import *
#from JNCarClass import *
import time
from timeit import default_timer
scene.caption = default_timer()
import random

class Car:
    def __init__(self, size=1,position = vector(0,0,0),velocity=vector(0,0,0), acceleration=vector(0,0,0),Carcolor=vector(1,1,1),Reacting = 0, Interacting = 0, Time =0, Merge =0):
        self.size = size
        self.position = position
        self.velocity = velocity
        self.acceleration = acceleration
        self.color = Carcolor
        self.sphere = sphere(pos = position, radius=size, color = Carcolor)
        self.Interacting = Interacting
        self.Reacting = Reacting
        self.ReactionStartTime = Time
        self.Merge = Merge
        
 

    def set_size(self, size):
        self.size = size
        self.sphere.radius = size

    def update_velocity(self, delta_v):
        self.velocity += delta_v

    def update_acceleration(self, delta_a):
        self.acceleration += delta_a

    def update_position(self):
        #self.velocity += self.acceleration
        self.sphere.pos += self.velocity
        
    def update_InteractionFlag(self,Interacting):
        self.Interacting = Interacting
        
    def update_Reacting(self,Reacting):
        self.Reacting = Reacting
    
    def update_ReactionStartTime(self,Time):
        self.ReactionStartTime = Time
        
    def update_IsMerging(self,status):
        self.Merge = status
        
    def get_InteractionFlag(self):
        return self.Interacting
        
    def get_Reacting(self):
        return self.Reacting
    
    def get_ReactionStartTime(self):
        return self.ReactionStartTime
    
    def get_position(self):
        return self.sphere.pos
    
    def get_positionX(self):
        return self.sphere.pos.x

    def get_positionY(self):
        return self.sphere.pos.y
    
    def get_positionZ(self):
        return self.sphere.pos.z

    def get_velocity(self):
        return self.velocity

    def get_velocityX(self):
        return self.velocity.x
    
  
    def get_velocityY(self):
        return self.velocity.y
    
    def get_velocityZ(self):
        return self.velocity.z
    
    def get_color(self):
        return self.sphere.color
    
    def get_IsMerge(self):
        return self.Merge


"""Right button drag or Ctrl-drag to rotate "camera" to view scene.
To zoom, drag with middle button or Alt/Option depressed, or use scroll wheel.
    On a two-button mouse, middle is left + right.
Shift-drag to pan left/right and up/down.
Touch screen: pinch/extend to zoom, swipe or two-finger rotate."""

RoadAdjustment =40
RoadXsize = 170  # => 2000 ft so 1unit here = 2 ft
RoadYsize = 0.01
RoadZsize = 5

RoadposX = RoadXsize/2
RoadposY = RoadYsize/2
RoadposZ = RoadZsize/2 + RoadAdjustment

MergeXSize = 200-RoadXsize
MergeYSize = RoadYsize  
MergeZSize = RoadZsize /2 

MergeXpos = RoadXsize + (MergeXSize / 2) 
MergeYpos = RoadposY 
MergeZpos = RoadZsize*3 /4 + RoadAdjustment

LaneX = RoadXsize/2
LaneY = 2
LaneZ = 3

CarSize =1


#35mi/hr = 51ft/sec
#Road colors (for y =0 then merge 0.22; for y=.01 then merge .42)
MergeColor = 0.42
v1 = vertex(pos=vector(RoadXsize,RoadposY,RoadAdjustment),color=color.gray(MergeColor))
v2 = vertex(pos=vector(RoadXsize + MergeXSize,RoadposY,RoadZsize/2 + RoadAdjustment),color=color.gray(MergeColor))
v3 = vertex(pos=vector(RoadXsize,RoadposY, RoadZsize/2+ RoadAdjustment),color=color.gray(MergeColor))
Rise = MergeXSize
Run = RoadZsize/2


ProMergeRoad= box (pos=vector(RoadposX, RoadposY, RoadposZ), size=vector(RoadXsize, RoadYsize, RoadZsize),  color = color.gray(0.7))
MoreRoad   = box (pos=vector(MergeXpos, MergeYpos, MergeZpos), size=vector(MergeXSize, MergeYSize,MergeZSize),color=color.gray(0.7))#,  texture=textures.flower)
MergeLane = triangle(vs=[v1,v2,v3])

#YellowLine=box (pos=vector(-10, .1, 0), size=vector(2, .001, .50),  color = color.yellow)
i=0
while i < RoadXsize/2:
    if 1 + i*3 < MergeXpos + MergeXSize/2:
        YellowLine=box (pos=vector(1 + i*3, .1+RoadposY, RoadposZ), size=vector(1.25, .001, .25),  color = color.yellow)
        #print("yes we hit it")
    i = i +1

j=10
TrafficCone = cone(pos=vector(RoadXsize/2 + RoadposX ,RoadposY, RoadAdjustment), radius=.5, axis=vector(0,2,0),color=color.orange)
while j < MergeXSize + 1 :
    TrafficConeTwo = cone(pos=vector(RoadXsize/2 + j +RoadposX ,RoadposY, RoadAdjustment + j/(Rise/Run) ), radius=.5, axis=vector(0,2,0),color=color.orange)
    j = j + 10



RoadXsize = 170  # => 2000 ft so 1unit here = 2 ft
RoadYsize = 0.01
RoadZsize = 5

RoadposX = RoadXsize/2
RoadposY = RoadYsize/2
RoadposZ = RoadZsize/2

MergeXSize = 200-RoadXsize
MergeYSize = RoadYsize  
MergeZSize = RoadZsize /2

MergeXpos = RoadXsize + (MergeXSize / 2) 
MergeYpos = RoadposY 
MergeZpos = RoadZsize*3 /4

LaneX = RoadXsize/2
LaneY = 2
LaneZ = 3

CarSize =1


#35mi/hr = 51ft/sec
#Road colors (for y =0 then merge 0.22; for y=.01 then merge .42)
MergeColor = 0.42
v1 = vertex(pos=vector(RoadXsize,RoadposY,0),color=color.gray(MergeColor))
v2 = vertex(pos=vector(RoadXsize + MergeXSize,RoadposY,RoadZsize/2),color=color.gray(MergeColor))
v3 = vertex(pos=vector(RoadXsize,RoadposY, RoadZsize/2),color=color.gray(MergeColor))
Rise = MergeXSize
Run = RoadZsize/2


Road= box (pos=vector(RoadposX, RoadposY, RoadposZ), size=vector(RoadXsize, RoadYsize, RoadZsize),  color = color.gray(0.7))
MoreRoad   = box (pos=vector(MergeXpos, MergeYpos, MergeZpos), size=vector(MergeXSize, MergeYSize,MergeZSize),color=color.gray(0.7))#,  texture=textures.flower)
MergeLane = triangle(vs=[v1,v2,v3])

#YellowLine=box (pos=vector(-10, .1, 0), size=vector(2, .001, .50),  color = color.yellow)
i=0
while i < RoadXsize/2:
    if 1 + i*3 < MergeXpos + MergeXSize/2:
        YellowLine=box (pos=vector(1 + i*3, .1+RoadposY, RoadposZ), size=vector(1.25, .001, .25),  color = color.yellow)
    i = i +1

j=10
TrafficCone = cone(pos=vector(RoadXsize/2 +RoadposX ,RoadposY,-1 * RoadYsize / 2 ), radius=.5, axis=vector(0,2,0),color=color.orange)
while j < MergeXSize + 1 :
    TrafficConeTwo = cone(pos=vector(RoadXsize/2 + j +RoadposX ,RoadposY,-1 * RoadYsize / 2 + j/(Rise/Run)), radius=.5, axis=vector(0,2,0),color=color.orange)
    j = j + 10
 
    
 
    
 
    
 

def accelerate(MaxAcc,MaxVel,Lamda,Car):
    CurAcc = MaxAcc - MaxAcc*(Car.get_velocityX()/MaxVel)**Lamda
    Car.update_velocity(vector(CurAcc,0,0))
    Car.update_position()

def decelerate(DeCel,MinDist,Car,CarAhead):
    CurAcc = -1*((Car.get_velocityX()*(Car.get_velocityX()-CarAhead.get_velocityX()))**2/(4*DeCel*MinDist*MinDist))
    Car.update_velocity(vector(CurAcc,0,0))
    Car.update_position()

def UpdateReaction(Car,time):
    Car.update_ReactionStartTime(time)
    Car.update_Reacting(1)

#def reacted(Car,time):

def move(i, CarAhead, Car,CarBehind, time):
    rate(400)
    ## Free Road
    if (CarAhead.get_positionX()- Car.get_positionX()) > ReactionDistance or CarAhead.get_velocityX() > Car.get_velocityX():
        if Car.get_InteractionFlag() > 0:
            Car.update_ReactionStartTime(time)
            Car.update_InteractionFlag(0)
            Car.update_Reacting(1)
           # print("Interacting to freeroad")
           # print("car reacting "+str(Car.get_Reacting()))
        elif Car.get_Reacting() > 0:
            if time - Car.get_ReactionStartTime() > random.randint(1, 3):
                Car.update_Reacting(0)  
                accelerate(MaxAcc,MaxVel,Lamda,Car)
              #  print("reaction time")
        else:
            if  Car.get_velocityX() < MaxVel:
                accelerate(MaxAcc,MaxVel,Lamda,Car) 
            else:
                Car.update_position()
        Car.update_InteractionFlag(0)
    
    ## Interaction
    else:
        Car.update_InteractionFlag(1)
        if (CarAhead.get_positionX()-Car.get_positionX())> MinDist:
             decelerate(DeCel,MinDist,Car,CarAhead)
        else:
            #Stop car
          #  print("before stop "+str(Car.get_velocity()))
            Car.update_velocity(-1 * Car.get_velocity())
          #  print("After stop "+str(Car.get_velocity()))
          
          

# 0.377 Miles = 1990 ft (start to one lane)
# merge into lane 200 ft
# average length of a car = 14 ft 

Factor = 10
MinDist = 5
MaxVel = 0.035  * Factor #35 mph
MaxAcc = 0.0005 * Factor # 60 miles / hour in 5 seconds
CurAccZ = 0.00009 *Factor
DeCel = 0.0001 * Factor
ReactionDistance =15
NumOfCars = 21

Decel = 4  #15 ft / second
TravelBrake =2
DesDistance = 2
Lamda = 3
ReactionTime = 2
Velocity = .1
MergeLanePosition =  RoadZsize*1/4
StartMergeZone = RoadXsize - 10
MergeNow = MergeXpos + 10
TrafficLight = 0
MergeDistbuffer = 3
ReactedFlag = 0
TrafficLightStop = RoadXsize + MergeXSize          

AntiMerge =[]
ProMerge = []
z=0
for z in range(NumOfCars):
    AntiMerge.append(Car(size=1,position=vector(RoadposX+RoadXsize/2 + MergeXSize - z*10 +random.randint(1, 3), CarSize + RoadposY, RoadZsize*3/4 + RoadAdjustment),velocity=vector(0,0,0),acceleration=vector(0,0,0),Carcolor =vector(random.randint(0, 1),random.randint(0, 1),random.randint(0, 1)),Reacting = 0, Interacting = 0, Time = 0, Merge = 0))
 
    if z % 2 == 0:
        ProMerge.append(Car(size=1,position=vector(RoadposX+RoadXsize/2 + MergeXSize -z*10 +random.randint(1, 3), CarSize + RoadposY, RoadZsize*3/4),velocity=vector(0,0,0),acceleration=vector(0,0,0),Carcolor =vector(random.randint(0, 1),random.randint(0, 1),random.randint(0, 1)),Reacting = 0, Interacting = 0, Time = 0, Merge = 0))
    else:
        ProMerge.append(Car(size=1,position=vector(RoadposX+RoadXsize/2 + MergeXSize -z*10 +random.randint(1, 3), CarSize + RoadposY, RoadZsize*1/4),velocity=vector(0,0,0),acceleration=vector(0,0,0),Carcolor =vector(random.randint(0, 1),random.randint(0, 1),random.randint(0, 1)),Reacting = 0, Interacting = 0, Time = 0, Merge = 1))



TrafficLightArrow = pyramid(pos = vector(RoadposX+ RoadXsize/2 ,RoadposY,RoadZsize/2 + RoadAdjustment/2), size = vector(10,10,10),axis = vector(0,1,0),color=vector(1,0,0))
blankspace = " "
message = "                                      ¯\_(ツ)_/¯  Please Standby As We Prepare the Simulation ¯\_(ツ)_/¯    "
RecordTimer =time.time()
counter = 0
switch= 0
while time.time() - RecordTimer < 20:
    if counter % 10000 == 0:
        switch = 1 - switch
    if switch == 1:
        scene.caption =blankspace*5 + message
    else: 
        scene.caption =blankspace + message
    counter += 1    
    print("wow")
countdowntime =time.time()
while time.time() - RecordTimer < 25:
    if time.time() - countdowntime < 1:
        scene.caption = "                          The Simulation will begin in 5 seconds..."
    elif time.time() - countdowntime < 2:
        scene.caption = "                          The Simulation will begin in 4 seconds..."
    elif time.time() - countdowntime < 3:
        scene.caption = "                          The Simulation will begin in 3 seconds..."
    elif time.time() - countdowntime < 4:
        scene.caption = "                          The Simulation will begin in 2 seconds..."
    elif time.time() - countdowntime < 5:
        scene.caption = "                          The Simulation will begin in 1 seconds..."
        
    print("fivesecondwarning")
AntiMergeTimer=0
ProMergeTimer=0
startTime = time.time()
camerazoomone = 0
camerazoomtwo= 0
while i < 1000000000000:
    AntiMerge = sorted(AntiMerge, key=lambda x: x.get_positionX(),reverse=True)
    ProMerge = sorted(ProMerge, key=lambda x: x.get_positionX(),reverse=True)
    j = NumOfCars - 1
    print("Traffic light "+ str(TrafficLight))
    if (time.time()-startTime) < 20:
        TrafficLight = 0
    else:
        TrafficLight = 1 
        TrafficLightArrow = pyramid(pos = vector(RoadposX+ RoadXsize/2 ,RoadposY,RoadZsize/2 + RoadAdjustment/2), size = vector(10,10,10),axis = vector(0,1,0),color=vector(0,1,0))
    j = 0
    while j <= NumOfCars - 1:
                #print("Car "+str(j)+ " merge? "+str(ProMerge[j].get_IsMerge()))
        if TrafficLight == 1 and j == 0 and TrafficLightStop - ProMerge[j].get_positionX() < MinDist:
          #  print("Passed traffic light j == " + str(j))
           # print("reacting "+str(ProMerge[j].get_Reacting())+" VelX "+str(ProMerge[j].get_velocityX()))
            if ProMerge[j].get_Reacting() < 1 and ProMerge[j].get_velocityX() < 0.00001 and ReactedFlag < 1:
               # print("Reacting j == " + str(j))
                UpdateReaction(ProMerge[j],time.time())
                ReactedFlag = 1
            else:
                if time.time() - ProMerge[j].get_ReactionStartTime() > random.uniform(1.0, 3.0):
                    #print("Reacted j == " + str(j))
                    ProMerge[j].update_Reacting(0)
                    if ProMerge[j].get_velocityX() < MaxVel:
                        accelerate(MaxAcc,MaxVel,Lamda,ProMerge[j])
                    else:
                        ProMerge[j].update_position()
        elif TrafficLight != 1 and j == 0 and  TrafficLightStop - ProMerge[j].get_positionX() < ReactionDistance:
           # print("wow traffic light stop")
            if TrafficLightStop - ProMerge[j].get_positionX() < MinDist:
                ProMerge[j].update_velocity(-1 * ProMerge[j].get_velocity())
                ProMerge[j].update_position()
            else:
                CurAcc = -1*((ProMerge[j].get_velocityX()*(ProMerge[j].get_velocityX()))**2/(4*DeCel*MinDist*MinDist))
                ProMerge[j].update_velocity(vector(CurAcc,0,0))
                ProMerge[j].update_position()
            ReactedFlag = 0
        elif j == 0 and TrafficLightStop - ProMerge[j].get_positionX() > ReactionDistance:
            
            if ProMerge[j].get_velocityX() < MaxVel:
                accelerate(MaxAcc,MaxVel,Lamda,ProMerge[j])
               # print("first car accerlating Vel = "+str(ProMerge[j].get_velocityX()))
            else:
                ProMerge[j].update_position()
        
        ##Moving before the merge zone
        elif j <= NumOfCars - 1 and ProMerge[j].get_positionX() < StartMergeZone:
            k = j - 1
            CarIdentified = 0
            
            if ProMerge[j].get_IsMerge() == 1:
                #print("Car "+str(j))
                while k >= 0 and CarIdentified != 1:
                    #print("Car "+str(j)+ "Pass")
                    if ProMerge[k].get_IsMerge() == 1 or k == 0:
                        CarIdentified = 1
                        move(i,ProMerge[k] ,ProMerge[j],"",time.time())
                    else:
                        k = k - 1     
            else:
                while k >= 0 and CarIdentified != 1:
                   # print("k two "+str(k))
                    if ProMerge[k].get_IsMerge() != 1 or k == 0:
                        CarIdentified = 1
                        move(i,ProMerge[k] ,ProMerge[j],"",time.time())
                    else:
                        k = k- 1         
        ##Try to merge
        elif ProMerge[j].get_IsMerge() == 1 and j < NumOfCars - 1 and ProMerge[j].get_positionX() > StartMergeZone:
           # print("Car "+str(j)+ " is trying to merge")
            #if j ==1:
              #  print("Vel ")
            if ProMerge[j-1].get_positionX() - ProMerge[j].get_positionX() > MinDist and ProMerge[j].get_positionX() - ProMerge[j+1].get_positionX() > MinDist:
                move(i,ProMerge[j-1] ,ProMerge[j],ProMerge[j+1],time.time())
                ##merge
                #print("hit this elif")
                if ProMerge[j].get_positionZ() <= RoadZsize*3/4:
                    #print("Car is merging")
                    ProMerge[j].update_velocity(vector(0,0,CurAccZ))
                    ProMerge[j].update_position()
                elif ProMerge[j].get_positionZ() > RoadZsize*3/4:
                    ProMerge[j].update_IsMerging(0)
                    ProMerge[j].update_velocity(vector(0,0,-1*ProMerge[j].get_velocityZ()))
                    
            elif ProMerge[j-1].get_positionX() - ProMerge[j].get_positionX() <= MinDist and ProMerge[j].get_positionX() - ProMerge[j+1].get_positionX() > MinDist:
                ##decelerate
               # print("decelerating")
                CurAcc = -1*((ProMerge[j].get_velocityX()*(ProMerge[j].get_velocityX()-ProMerge[j-1].get_velocityX()))**2/(4*DeCel*MinDist*MinDist))
                ProMerge[j].update_velocity(vector(CurAcc,0,0))
                ProMerge[j].update_position()
            elif ProMerge[j-1].get_positionX() - ProMerge[j].get_positionX() > MinDist and ProMerge[j].get_positionX() - ProMerge[j+1].get_positionX() <= MinDist:
                ##accelerate
                 CurAcc = MaxAcc - MaxAcc*(ProMerge[j].get_velocityX()/MaxVel)**Lamda
                 ProMerge[j].update_velocity(vector(CurAcc,0,0))
                 ProMerge[j].update_position()
            else:
                ##stop
                ProMerge[j].update_velocity(-1 * ProMerge[j].get_velocity())
        ##Let cars merge
        elif ProMerge[j].get_IsMerge() != 1 and j < NumOfCars - 1 and ProMerge[j].get_positionX() > StartMergeZone:
            if ProMerge[j-1].get_IsMerge() == 1 and ProMerge[j-1].get_positionX() - ProMerge[j].get_positionX() > MinDist:
                move(i,ProMerge[j-1] ,ProMerge[j],"",time.time())
            elif ProMerge[j-1].get_IsMerge() == 1 and ProMerge[j-1].get_positionX() - ProMerge[j].get_positionX() <= MinDist:
                ##decelerate
                CurAcc = -1*((ProMerge[j].get_velocityX()*(ProMerge[j].get_velocityX()-ProMerge[j-1].get_velocityX()))**2/(4*DeCel*MinDist*MinDist))
                ProMerge[j].update_velocity(vector(CurAcc,0,0))
                ProMerge[j].update_position()
            else:
               move(i,ProMerge[j-1] ,ProMerge[j],"",time.time()) 
        else:
           move(i,ProMerge[j-1] ,ProMerge[j],"",time.time())
           #print("wow the end")
                #print("Car "+str(j)+ " merge? "+str(AntiMerge[j].get_IsMerge()))
        if TrafficLight == 1 and j == 0 and TrafficLightStop - AntiMerge[j].get_positionX() < MinDist:
           # print("Passed traffic light j == " + str(j))
           # print("reacting "+str(AntiMerge[j].get_Reacting())+" VelX "+str(AntiMerge[j].get_velocityX()))
            if AntiMerge[j].get_Reacting() < 1 and AntiMerge[j].get_velocityX() < 0.00001 and ReactedFlag < 1:
            #    print("Reacting j == " + str(j))
                UpdateReaction(AntiMerge[j],time.time())
                ReactedFlag = 1
            else:
                if time.time() - AntiMerge[j].get_ReactionStartTime() > random.uniform(1.0, 3.0):
                   # print("Reacted j == " + str(j))
                    AntiMerge[j].update_Reacting(0)
                    if AntiMerge[j].get_velocityX() < MaxVel:
                        accelerate(MaxAcc,MaxVel,Lamda,AntiMerge[j])
                    else:
                        AntiMerge[j].update_position()
        elif TrafficLight != 1 and j == 0 and  TrafficLightStop - AntiMerge[j].get_positionX() < ReactionDistance:
           # print("wow traffic light stop")
            if TrafficLightStop - AntiMerge[j].get_positionX() < MinDist:
                AntiMerge[j].update_velocity(-1 * AntiMerge[j].get_velocity())
                AntiMerge[j].update_position()
            else:
                CurAcc = -1*((AntiMerge[j].get_velocityX()*(AntiMerge[j].get_velocityX()))**2/(4*DeCel*MinDist*MinDist))
                AntiMerge[j].update_velocity(vector(CurAcc,0,0))
                AntiMerge[j].update_position()
            ReactedFlag = 0
        elif j == 0 and TrafficLightStop - AntiMerge[j].get_positionX() > ReactionDistance:
            
            if AntiMerge[j].get_velocityX() < MaxVel:
                accelerate(MaxAcc,MaxVel,Lamda,AntiMerge[j])
                #print("first car accerlating Vel = "+str(AntiMerge[j].get_velocityX()))
            else:
                AntiMerge[j].update_position()
        
        ##Moving before the merge zone
        elif j <= NumOfCars - 1 and AntiMerge[j].get_positionX() < StartMergeZone:
            k = j - 1
            CarIdentified = 0
            
            if AntiMerge[j].get_IsMerge() == 1:
                #print("Car "+str(j))
                while k >= 0 and CarIdentified != 1:
                    #print("Car "+str(j)+ "Pass")
                    if AntiMerge[k].get_IsMerge() == 1 or k == 0:
                        CarIdentified = 1
                        move(i,AntiMerge[k] ,AntiMerge[j],"",time.time())
                    else:
                        k = k - 1     
            else:
                while k >= 0 and CarIdentified != 1:
                   # print("k two "+str(k))
                    if AntiMerge[k].get_IsMerge() != 1 or k == 0:
                        CarIdentified = 1
                        move(i,AntiMerge[k] ,AntiMerge[j],"",time.time())
                    else:
                        k = k- 1         
        ##Try to merge
        elif AntiMerge[j].get_IsMerge() == 1 and j < NumOfCars - 1 and AntiMerge[j].get_positionX() > StartMergeZone:
           # print("Car "+str(j)+ " is trying to merge")
           # if j ==1:
                #print("Vel ")
            if AntiMerge[j-1].get_positionX() - AntiMerge[j].get_positionX() > MinDist and AntiMerge[j].get_positionX() - AntiMerge[j+1].get_positionX() > MinDist:
                move(i,AntiMerge[j-1] ,AntiMerge[j],AntiMerge[j+1],time.time())
                ##merge
                #print("hit this elif")
                if AntiMerge[j].get_positionZ() <= (RoadZsize*3/4 +RoadAdjustment):
                    #print("Car is merging")
                    AntiMerge[j].update_velocity(vector(0,0,CurAccZ))
                    AntiMerge[j].update_position()
                elif AntiMerge[j].get_positionZ() > (RoadZsize*3/4 +RoadAdjustment):
                    AntiMerge[j].update_IsMerging(0)
                    AntiMerge[j].update_velocity(vector(0,0,-1*AntiMerge[j].get_velocityZ()))
                    
            elif AntiMerge[j-1].get_positionX() - AntiMerge[j].get_positionX() <= MinDist and AntiMerge[j].get_positionX() - AntiMerge[j+1].get_positionX() > MinDist:
                ##decelerate
               # print("decelerating")
                CurAcc = -1*((AntiMerge[j].get_velocityX()*(AntiMerge[j].get_velocityX()-AntiMerge[j-1].get_velocityX()))**2/(4*DeCel*MinDist*MinDist))
                AntiMerge[j].update_velocity(vector(CurAcc,0,0))
                AntiMerge[j].update_position()
            elif AntiMerge[j-1].get_positionX() - AntiMerge[j].get_positionX() > MinDist and AntiMerge[j].get_positionX() - AntiMerge[j+1].get_positionX() <= MinDist:
                ##accelerate
                 CurAcc = MaxAcc - MaxAcc*(AntiMerge[j].get_velocityX()/MaxVel)**Lamda
                 AntiMerge[j].update_velocity(vector(CurAcc,0,0))
                 AntiMerge[j].update_position()
            else:
                ##stop
                AntiMerge[j].update_velocity(-1 * AntiMerge[j].get_velocity())
        ##Let cars merge
        elif AntiMerge[j].get_IsMerge() != 1 and j < NumOfCars - 1 and AntiMerge[j].get_positionX() > StartMergeZone:
            if AntiMerge[j-1].get_IsMerge() == 1 and AntiMerge[j-1].get_positionX() - AntiMerge[j].get_positionX() > MinDist:
                move(i,AntiMerge[j-1] ,AntiMerge[j],"",time.time())
            elif AntiMerge[j-1].get_IsMerge() == 1 and AntiMerge[j-1].get_positionX() - AntiMerge[j].get_positionX() <= MinDist:
                ##decelerate
                CurAcc = -1*((AntiMerge[j].get_velocityX()*(AntiMerge[j].get_velocityX()-AntiMerge[j-1].get_velocityX()))**2/(4*DeCel*MinDist*MinDist))
                AntiMerge[j].update_velocity(vector(CurAcc,0,0))
                AntiMerge[j].update_position()
            else:
               move(i,AntiMerge[j-1] ,AntiMerge[j],"",time.time()) 
        else:
           move(i,AntiMerge[j-1] ,AntiMerge[j],"",time.time())
           #print("wow the end")    
        j += 1
    
    
    if AntiMerge[NumOfCars - 1].get_positionX() < TrafficLightStop:
        AntiMergeTimer = round(time.time()-startTime,1)
    if ProMerge[NumOfCars - 1].get_positionX() < TrafficLightStop:
        ProMergeTimer = round(time.time()-startTime,1)
 
    scene.caption = "                                            Anti-Merge Time " +str(AntiMergeTimer) + "       Pro-Merge Time " +str(ProMergeTimer)
    #scene.caption = "Seconds " +str(round(time.time()-startTime,3)) + " velocity " + str(round(CarArr[NumOfCars-1].get_velocityX()*1000,3)) + "mph Distance " + str(round(CarArr[NumOfCars-1].get_positionX()*10,3)) +"ft"
    i = i + 1
    
    CurrentTime=round(time.time()-startTime,1)
    


    if CurrentTime > 8 and CurrentTime < 13:
        scene.camera.pos = ProMerge[NumOfCars-1].get_position() + vector(5,20,30)
        scene.camera.axis = vector(5,-20,-31)
    if CurrentTime> 13 and CurrentTime < 18:
        scene.camera.pos = AntiMerge[NumOfCars-1].get_position() + vector(5,20,30)
        scene.camera.axis = vector(5,-20,-31)
        camerazoomtwo = camerazoomtwo - 1
    if CurrentTime> 18 and CurrentTime < 21:
        scene.camera.pos = AntiMerge[0].get_position() + vector(-5,20,30)
        scene.camera.axis = vector(5,-20,-31)
    if CurrentTime> 45 and CurrentTime < 50:
        scene.camera.pos = AntiMerge[NumOfCars-1].get_position() + vector(5,20,30)
        scene.camera.axis = vector(5,-20,-31)
        
    if CurrentTime > 90 and CurrentTime <95:
        scene.camera.pos = ProMerge[NumOfCars-1].get_position() + vector(5,20,30)
        scene.camera.axis = vector(5,-20,-31)
    if CurrentTime> 95 and CurrentTime < 100:
        scene.camera.pos = AntiMerge[NumOfCars-1].get_position() + vector(5,20,30)
        scene.camera.axis = vector(5,-20,-31)
    if CurrentTime > 100 and CurrentTime <105:
        scene.camera.pos = ProMerge[NumOfCars-1].get_position() + vector(5,20,30)
        scene.camera.axis = vector(5,-20,-31)
    if CurrentTime> 105 and CurrentTime < 110:
        scene.camera.pos = AntiMerge[NumOfCars-1].get_position() + vector(5,20,30)
        scene.camera.axis = vector(5,-20,-31)
    if CurrentTime > 110 and CurrentTime <112:
        scene.camera.pos = ProMerge[NumOfCars-1].get_position() + vector(5,20,30)
        scene.camera.axis = vector(5,-20,-31)
    if CurrentTime> 114 and CurrentTime < 117:
        scene.camera.pos = AntiMerge[NumOfCars-1].get_position() + vector(5,20,30)
        scene.camera.axis = vector(5,-20,-31)
    if CurrentTime > 117 and CurrentTime < 119:
        scene.camera.pos = ProMerge[NumOfCars-1].get_position() + vector(5,20,30)
        scene.camera.axis = vector(5,-20,-31)
        
    if CurrentTime> 119:
        scene.camera.pos =vector(RoadposX+RoadXsize/2 + MergeXSize,CarSize + RoadposY, RoadZsize*3/4 + RoadAdjustment)+ vector(-5,20,30)
        scene.camera.axis = vector(5,-20,-31)
        
    #time.sleep(.05)