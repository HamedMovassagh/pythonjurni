

stor=[("your mom",1.5),("your dad",50),("black peapole",99)]


chang_transfer=lambda data:(data[0],data[1]*0.95)


to_euro=map(chang_transfer,stor)


for i in to_euro:
    print(i)
