class MissManners():
    
    def __init__(self, *args):
        self.asked_obj = args[0]
        self.do_list = dir(args[0])
    def ask(self,*args):
        
        if (args[0][0:6]) != 'please':
            return 'You must learn to say please first.'
        else:
            if args[0][7:] not in self.do_list:
                  return 'Thanks for asking, but I know not how to '+args[0][7:]
            else:
                self.methed = getattr(self.asked_obj,args[0][7:])
         
             
                if len(args) == 1:
                    return self.methed()
                else:
                    if args[0][7:] == 'ask':
                        return self.methed(*args[1:])
                    else:
                        return self.methed(args[1])