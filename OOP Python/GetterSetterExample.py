class Student:
    def __init__(self, ho, dem, ten, dob):
        self.ho = ho
        self.dem = dem
        self.ten = ten
        self.dob = dob

    @property
    def fullname(self):
        if(self.ho == None or self.dem == None or self.ten == None):
            return None
        return '{} {} {}'.format(self.ho, self.dem, self.ten)
    
    @fullname.setter
    def fullname(self, s):
        list = s.split(' ')
        list2 = [st.strip() for st in list]
        ho, dem, ten = list2
        self.ho = ho
        self.dem = dem
        self.ten = ten
    
    @fullname.deleter
    def fullname(self):
        self.ho = None
        self.dem = None
        self.ten = None
        print("Deleted!")
    
tphan = Student("Phan", "Duy", "Thang", "27/09/2002")
tphan.fullname = "Nguyen Van A"
print(tphan.ho)

del tphan.fullname
print(tphan.fullname)
