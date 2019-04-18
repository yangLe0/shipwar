class SweetPotato:

    def __init__(self):
        self.cookedString="生的"
        self.cookedLevel = 0
        self.condiments = []

    def __str__(self):
        return "地瓜状态：%s(%d),添加的佐料有：%s"%(self.cookedString,self.cookedLevel,self.condiments)

    def cook(self,cooked_time):
        self.cookedLevel += cooked_time

        if self.cookedLevel >= 0 and self.cookedLevel<3:
            self.cookedString = "生的"
        elif self.cookedLevel >= 3 and self.cookedLevel<5:
            self.cookedString = "半生不熟"
        elif self.cookedLevel >= 5 and self.cookedLevel<8:
            self.cookedString = "熟了"
        elif self.cookedLevel>8:
            self.cookedString = "烤糊了"

    def addCondiment(self,item):
        self.condiments.append(item)

di_gua = SweetPotato()
print(di_gua)

di_gua.addCondiment("番茄酱")
di_gua.cook(1)
print(di_gua)
di_gua.addCondiment("大蒜")
di_gua.cook(1)
print(di_gua)
di_gua.addCondiment("沙拉酱")
di_gua.cook(1)
print(di_gua)
di_gua.addCondiment("孜然")
di_gua.cook(1)
print(di_gua)
di_gua.cook(1)
print(di_gua)
di_gua.cook(1)
print(di_gua)
di_gua.cook(1)
print(di_gua)
di_gua.cook(1)
print(di_gua)
di_gua.cook(1)
print(di_gua)