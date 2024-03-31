from src.Factory import Factory

config_path = "config_drawing/myhouse.json"

f = Factory(config_path)
d = f.getDrawing()


# d.draw("my_house.png")
# d.draw("my_house.jpg")
d.draw("test.png")