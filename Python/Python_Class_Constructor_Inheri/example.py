class Company:
    def __init__(self,name,proj):
        self.name=name
        self.proj=proj

    def show(self):
        print("The code of company is = ",self.ccode)    

class Emp(Company):        
    def __init__(self,ename,sal,cname,proj):
        Company.__init__(self,cname,proj)
        self.ename=ename
        self.sal=sal

    def show_sal(self):
        print("salary of ",self.ename," is ",self.sal)    


c=Company("Bodhi Technology","OTT")

e=Emp("Amey",18000,c.name,c.proj)


e.show_sal()