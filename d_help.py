# coding=UTF-8
class s_Help:
    @classmethod
    def check_str(cls,c_str):
        cr_str=c_str.replace("'","\'")
        print(c_str)
        return cr_str 
        
    def Total(p1,p2):
        p3 = p1-p2
        return p3
    
    def Conver(self):
        for ch in ['$',',']:
            self=self.replace(ch,'')
        return self
    
    def Conver_ya(self):
        ya_complete = self.replace(" ","+")
        return ya_complete
