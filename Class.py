class coutCat:
    def __init__(self,cat_name,cat_age):
        self.name = cat_name
        self.age = cat_age
        self.cat_age = cat_age

cat1 = coutCat('大菊',20)
cat2 = coutCat('cat2',30)
print(cat1.name)
print(cat1.age)



class Student :
    def __init__(self,name,ID):
        self.name = name
        self.ID = ID
        self.chengji = {"语文":0,"数学":0,"英语":0}
    def set_grade(self,course,grade):
        if course in self.chengji:
            self.chengji[course] = grade
