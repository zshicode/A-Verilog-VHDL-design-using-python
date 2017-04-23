from myhdl import *

def adder(s,g,c,a,b):
    
    @always_comb
    def logic():
        g.next = (a and c) or (a and b) or (b and c)
        s.next = a + b + c
        
    return logic
    
s,a,b = [Signal(intbv(0)[8:]) for i in range(3)]
g,c = [Signal(intbv(0)) for i in range(2)]
toVerilog(adder,s,g,c,a,b)
