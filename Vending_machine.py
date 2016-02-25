class VendingMachine:
    save = {'stock':0,'crush':0,'product':"",'price':0}
    def __init__(self, *args):
        self.save['product']=args[0]
        self.save['price']=args[1]
    def vend(self):
        if self.save['stock'] == 0:
            if self.save['crush'] != 0:
                self.save['crush'] = 0
                return 'Machine is out of stock. Here is your $'+self.save['crush']+'.'
            else:
                return 'Machine is out of stock.'
        else:
            maintain = self.save['crush'] - self.save['price']
            if maintain > 0:
                self.save['stock'] -= 1
                self.save['crush'] = 0
                return 'Here is your candy and $'+str(maintain)+' change.'
            elif maintain < 0:
                return 'You must deposit $'+str(-maintain)+' more.'
            else:
                self.save['crush'] = 0
                self.save['stock'] -= 1
                return 'Here is your '+self.save['product']+'.'
    def restock(self,n):
        self.save['stock'] += n
        return 'Current '+self.save['product']+' stock: '+str(self.save['stock'])

    def deposit(self,n):
        if self.save['stock'] == 0:
            return 'Machine is out of stock. Here is your $'+str(n)+'.'
        self.save['crush'] += n
        return 'Current balance: $'+str(self.save['crush'])
