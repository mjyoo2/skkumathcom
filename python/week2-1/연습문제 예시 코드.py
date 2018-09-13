class elevator:
    floor=1
    personlist=[]
    
    def move(self,upfl):
        self.floor+=upfl
        print(self.floor,"층에 도착하였습니다.")
        for person in self.personlist:
            person.temp_floor+=upfl  
        
    def inperson(self,person):
        if self.floor==person.temp_floor:
            self.personlist.append(person)
        else:
            print("엘레베이터가 다른 층에 있습니다.")
        
    def outperson(self,person):
        self.personlist.remove(person)

class Person:
    name=""
    age=0
    temp_floor=1
    
    
LDJ=Person()
LDJ.name="이동준"

ele=elevator()
ele.inperson(LDJ)
ele.move(3)
ele.outperson(LDJ)
print(LDJ.temp_floor)

ele.move(-1)
ele.inperson(LDJ)