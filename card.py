#card class


class Card:
    def __init__(self, name, science, ecology, culture, commerce, industry):
        self.list = [name, science, ecology, culture, commerce, industry]
        
    def getList(self):
        return self.list
    
    def getName(self):
        return self.list[0]
    
    def getScienceValue(self):
        return self.list[1]
    
    def getEcologyValue(self):
        return self.list[2]
    
    def getCultureValue(self):
        return self.list[3]
    
    def getCommerceValue(self):
        return self.list[4]
    
    def getIndustryValue(self):
        return self.list[5]
    
    def __repr__(self):
        return(self.list[0] + "\nScience Value: " + str(self.list[1]) +
               "\nEcology Value: " + str(self.list[2]) +
               "\nCulture Value: " + str(self.list[3]) +
               "\nCommerce Value: " + str(self.list[4]) +
               "\nIndustry Value: " + str(self.list[5]) + "\n")
    
    
    

