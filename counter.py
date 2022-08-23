from tkinter import Canvas
from area import Area
import constants


class Counter:
    def __init__(self, canvas: Canvas, uncollectedDirtNumber: int, area: Area):
        self.score = 0
        self.canvas = canvas
        self.canvas.create_text(70, 50, text="Score: " + str(self.score), tags="counter")
        self.uncollectedDirtNumber = uncollectedDirtNumber
        self.totalDirtAddedNumber = uncollectedDirtNumber
        self.priorityArea = area
        self.priorityAreaExistedMoves = 0
        self.existanceOfPriorityAreas = 0
    
    def dirtAdded(self, dirtNumber: int):
        self.uncollectedDirtNumber += dirtNumber
        self.totalDirtAddedNumber += dirtNumber

    def setPriorityArea(self, area: Area):
        self.removePriorityArea()
        self.priorityArea = area
        self.priorityArea.draw(self.canvas, color=constants.priorityZoneColor)
        self.priorityAreaExistedMoves = 0

    def removePriorityArea(self):
        if self.priorityArea == None:
            return 
        self.canvas.delete(self.priorityArea.name)
        self.priorityArea = None
        self.score += (constants.priorityAreaCleanedPoints - self.priorityAreaExistedMoves)

    def itemCollected(self):
        self.uncollectedDirtNumber -= 1
        self.score += constants.scoreForDirtCollected
        self.canvas.itemconfigure("counter", text="Score: " + str(self.score))

    def movePassed(self):
        if self.priorityArea != None:
            self.priorityAreaExistedMoves += 1
            self.existanceOfPriorityAreas += 1
        
        self.score -= (self.uncollectedDirtNumber * constants.scoreLossPerMove)
        self.canvas.itemconfigure("counter", text=f"Score: %.2f" %self.score)