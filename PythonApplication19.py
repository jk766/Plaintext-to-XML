sample = "<prime><note><xxx><to>Tove</to><from>Jani</from></xxx><heading>Reminder</heading><body>Don't forget me this weekend!</body></note></prime>"
#txt = sample #str(input())

class XMLConvert:
    def __init__(self, data):
        self.d = data

    def separate(self):
        txt = self.d
        txtlst = txt.split("<")
        txtlst.remove("")
        
        txtlst = list(map(lambda x: '<' + x, txtlst))
        
        txtlst = list(map(lambda x : x.split(">"), txtlst))
        
        txtlst = list(map(lambda x : [x[0], "no"] if x[1] == "" else x, txtlst))
        
        all = []
        
        for item in txtlst:
            if (item[1] == "no"): 
                all.append(item[0])
            else: 
                all.append(item[0])
                all.append(item[1])
        
        all = list(map(lambda x : x + ">" if "<" in x else x, all))
        return all

    def find_pair(self, lst, ind, dest, ws):   
        item = lst[ind]
        sub = item.split("<")
        sub = str(sub[1])
        if (item not in dest):
            tabs = ""
            for wsA in range(0, ws):
                tabs = tabs + "\t"
            dest.append(tabs)
            dest.append(item)
            dest.append("\n")
        for i in range(ind + 1, len(lst)):
            if (sub in lst[i]):
                tabs = ""
                if (lst[i] not in dest):
                    for wsB in range(0, ws):
                        tabs = tabs + "\t"
                    dest.append(tabs)
                    dest.append(lst[i])
                    dest.append("\n")
                return
            elif ("<" not in lst[i]):
                if(lst[i] not in dest):
                    tabs = ""
                    for wsC in range(0, ws):
                        tabs = tabs + "\t"
                    dest.append(tabs + "   ")
                    dest.append(lst[i])
                    dest.append("\n")
            elif ("</" in lst[i] and sub not in lst[i]):
                continue
            else:
                self.find_pair(lst, i, dest, ws + 1)

    def XMLConv(self):
        xstr = self.separate()
        indent = 0
        destination=[]
        self.find_pair(xstr,0,destination,indent)
        formatted = ""
        destination.pop()
        for i in destination:
            formatted = formatted + i
        return(formatted)
    def PrintConverted(self):
        print(self.d)
        print("\n")
        print(self.XMLConv())
        print("\n")


ST = XMLConvert(sample)
ST.PrintConverted()




3


