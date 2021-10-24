# ver 1.0


DAYS = [
            {"num" : 0, "title" : "понедельник", "active" : False, "color" : "#FFE739", "order" : [0,1,2,3,4,5,6], "temp" : 0, "type" : "-"},
            {"num" : 1, "title" : "понедельник", "active" : False, "color" : "#FFE739", "order" : [1,2,3,4,5,6,0], "temp" : 0, "type" : "-"},
            {"num" : 2, "title" : "понедельник", "active" : False, "color" : "#FFE739", "order" : [2,3,4,5,6,0,1], "temp" : 0, "type" : "-"},
            {"num" : 3, "title" : "понедельник", "active" : False, "color" : "#FFE739", "order" : [3,4,5,6,0,1,2], "temp" : 0, "type" : "-"},
            {"num" : 4, "title" : "понедельник", "active" : False, "color" : "#FFE739", "order" : [4,5,6,0,1,2,3], "temp" : 0, "type" : "-"},
            {"num" : 5, "title" : "понедельник", "active" : False, "color" : "#FFE739", "order" : [5,6,0,1,2,3,4], "temp" : 0, "type" : "-"},
            {"num" : 6, "title" : "понедельник", "active" : False, "color" : "#FFE739", "order" : [6,0,1,2,3,4,5], "temp" : 0, "type" : "-"}
]


def today():
    res = {
        "city" : "Город",
        "temp" : 10
    }
    return res
