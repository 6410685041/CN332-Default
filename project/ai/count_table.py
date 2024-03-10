import cv2
import numpy as np

class LoopCount:
    def __init__(self,row_count,draw_org,loop):
        self.table = [[0 for i in range(3)] for j in range(row_count)]
        self.draw_org = draw_org
        self.loop = loop
    def add_straight(self,vechicle_type):
        self.table[vechicle_type][0]+=1
    def add_left(self,vechicle_type):
        self.table[vechicle_type][1]+=1
    def add_right(self,vechicle_type):
        self.table[vechicle_type][2]+=1
    def draw(self,countTable):
        countTable.data = self.table
        countTable.location = self.draw_org
        countTable.title = self.loop["name"]
        countTable.draw()

        
class CountTable:
    def __init__(self, img, data, row_headers=None, col_headers=None, border=True, border_color=(0,0,0), location = (0,0), text_color=(0,0,0),title=""):
        self.img = img
        self.data = data
        self.row_headers = row_headers
        self.col_headers = col_headers
        self.border = border
        self.border_color = border_color
        self.location = location
        self.text_color = text_color
        self.title = title

    def draw(self):
        # Get image height and width
        x_offset,y_offset = int(self.location["x"]),int(self.location["y"])

        if self.title != "":
            cv2.putText(self.img,self.title,(x_offset,y_offset),cv2.FONT_HERSHEY_SIMPLEX,0.5,self.border_color,2)
        # Draw table borders
        if self.border:
            cv2.rectangle(self.img, (x_offset, y_offset+10), (x_offset + 110*3, y_offset + 32*len(self.row_headers)), self.border_color, 2)

        # Draw row headers
        if self.row_headers:
            for i, row_header in enumerate(self.row_headers):
                cv2.putText(self.img, str(row_header), (x_offset + 10, y_offset + 30 + i*30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, self.text_color, 2)

        # Draw column headers
        if self.col_headers:
            for j, col_header in enumerate(self.col_headers):
                cv2.putText(self.img, str(col_header), (x_offset + 50 + j*100, y_offset ), cv2.FONT_HERSHEY_SIMPLEX, 0.5, self.text_color, 2)

        # Draw 2D list on the image
        for i, row in enumerate(self.data):
            for j, val in enumerate(row):
                cv2.putText(self.img, str(val), (x_offset + 200 + j*50, y_offset + 30 + i*30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, self.text_color, 2)



