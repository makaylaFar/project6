# Makayla Farley
# february 8th, 2024

from direct.showbase.ShowBase import ShowBase
import defensePaths as defensePaths
import spaceJamClasses as spaceJamClasses
from collideObjectBase import PlacedObject
from panda3d.core import CollisionTraverser, CollisionHandlerPusher
import player as playerClass


class spaceJam(ShowBase):

    # for the camera setup
    def SetCamera(self):
        # prevents mouse from being able to move camera
        #self.disableMouse()
        # reparents the model to the ship/player
        self.camera.reparentTo(self.ship.modelNode)
        # makes it so it's position is moving so it can collide into things
        self.camera.setFluidPos(0, 0, 1)
        
        self.disableMouse()

    # Initialize ShowBase to be used later
    def __init__(self):
        ShowBase.__init__(self)
        self.traverser = CollisionTraverser()
        base.cTrav = self.traverser
        #self.cTrav.traverse(self.render)
        self.pusher = CollisionHandlerPusher()
        #self.cTrav.showCollisions(self.render)
        self.traverser.traverse(self.render)
        self.sceneSetup()
        

    # Draws the cloudDefense
    def DrawCloudDefense(self, centralObject, droneName):
        # calls the position calculated in defensePaths.Cloud
        unitVec = defensePaths.Cloud()
        # normalizes the vec
        unitVec.normalize()
        # makes the position so it accounts for the planet and some space between it and the drones
        position = unitVec * 500 + centralObject.modelNode.getPos()
        spaceJamClasses.Drone(self.loader, "./assets/DroneDefender/DroneDefender.obj", self.render, droneName, "./assets/DroneDefender/octotoad1_auv.png", position, 10)
        

    def DrawBaseballSeams(self, centralObject, droneName, step, numSeams, radius = 1): 
        unitVec = defensePaths.BaseballSeams(step, numSeams, B = 0.4)
        unitVec.normalize()
        position = unitVec * radius * 350 + centralObject.modelNode.getPos()
        spaceJamClasses.Drone(self.loader, "./assets/DroneDefender/DroneDefender.x", self.render, droneName, "./assets/DroneDefender/octotoad1_auv.png", position, 5)
   
    def DrawCircleXY(self, centralObject, droneName):
        unitVec = defensePaths.CircleXY()
        unitVec.normalize()
        position = unitVec * 600 + centralObject.modelNode.getPos()
        spaceJamClasses.Drone(self.loader, "./assets/DroneDefender/DroneDefender.obj", self.render, droneName, "./assets/DroneDefender/octotoad1_auv.png", position,5)

    def DrawCircleYZ(self, centralObject, droneName):
        unitVec = defensePaths.CircleYZ()
        unitVec.normalize()
        position = unitVec * 300 + centralObject.modelNode.getPos()
        spaceJamClasses.Drone(self.loader, "./assets/DroneDefender/DroneDefender.obj", self.render, droneName, "./assets/DroneDefender/octotoad1_auv.png", position,5)
    
    def DrawCircleXZ(self, centralObject, droneName):
        unitVec = defensePaths.CircleXZ()
        unitVec.normalize()
        position = unitVec * 600 + centralObject.modelNode.getPos()
        spaceJamClasses.Drone(self.loader, "./assets/DroneDefender/DroneDefender.obj", self.render, droneName, "./assets/DroneDefender/octotoad1_auv.png", position,5)
    
        
    def sceneSetup(self):
        self.universe = spaceJamClasses.universe(self.loader, "./assets/universe/Universe.x", self.render,'universe',"./assets/universe/universe.jpeg", (0, 0, 0), 10000)
        self.planet1 = spaceJamClasses.Planet(self.loader, "./assets/planets/protoPlanet.x", self.render,'planet1',"./assets/planets/weirdPlanet.png", (-6000, -3000, -800), 250)
        self.planet2 = spaceJamClasses.Planet(self.loader, "./assets/planets/protoPlanet.x", self.render,'planet2',"./assets/planets/moon.jpg", (0, 6000, 0), 300)
        self.planet3 = spaceJamClasses.Planet(self.loader, "./assets/planets/protoPlanet.x", self.render,'planet3',"./assets/planets/rocky.jpg", (-6000, -5000, 200), 500)
        self.planet4 = spaceJamClasses.Planet(self.loader, "./assets/planets/protoPlanet.x", self.render,'planet4',"./assets/planets/sandy.jpg", (300, 6000, 500), 200)
        self.planet5 = spaceJamClasses.Planet(self.loader, "./assets/planets/protoPlanet.x", self.render,'planet5',"./assets/planets/mars.jpg", (700, 2000, 100), 500)
        self.planet6 = spaceJamClasses.Planet(self.loader, "./assets/planets/protoPlanet.x", self.render,'planet6',"./assets/planets/sun.jpg", (0, -900, -1400), 700)
        self.ship = playerClass.spaceShip(self.loader, "./assets/spaceShip/Dumbledore.egg", self.render,'ship', "./assets/spaceShip/spacejet_C.png", (0, 0, 0), 11, self.taskMgr, self.render, self.accept, self.traverser)
        self.spaceStation = spaceJamClasses.spaceStation(self.loader, "./assets/spaceStation/spaceStation.egg", self.render,'ship', "./assets/spaceStation/SpaceStation1_Dif2.png", (-3100, 200, 2000), 10)

        
        
        self.SetCamera()    
        fullCycle = 60

        for j in range(fullCycle):
            spaceJamClasses.Drone.droneCount += 1
            nickName = "Drone" + str(spaceJamClasses.Drone.droneCount)
            self.DrawCloudDefense(self.planet1, nickName)
            self.DrawBaseballSeams(self.planet2, nickName, j, fullCycle)
            self.DrawCircleXZ(self.planet5, nickName)
            self.DrawCircleXY(self.planet3, nickName)
            self.DrawCircleYZ(self.planet4, nickName)
            

app = spaceJam()  
app.run()