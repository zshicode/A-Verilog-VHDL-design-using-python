from myhdl import *

def dff(q, d, clk):

    @always(clk.posedge)
    def logic():
        #describe the logic function of D flip-flop
        q.next = d

    return logic
    
    

#test block

from random import randrange

def test_dff():

    q, d, clk = [Signal(bool(0)) for i in range(3)]

    dff_inst = dff(q, d, clk)

    @always(delay(10))
    def clkgen():
        clk.next = not clk
        #a clk signal whose term is 20ns, V(0)=0

    @always(clk.negedge)
    def stimulus():
        d.next = randrange(2)

    return dff_inst, clkgen, stimulus


def simulate(timesteps):
    tb = traceSignals(test_dff)
    sim = Simulation(tb)
    sim.run(timesteps)

simulate(2000)

'''
finish the test block, and we'll see a *.vcd waveform file，which can be viewed by quartus or modelsim,
2000 means that simulation time lasts for 2000ns
'''

def convert():
    q, d, clk = [Signal(bool(0)) for i in range(3)]
    toVerilog(dff, q, d, clk)
    toVHDL(dff, q, d, clk)

convert()
#generate Verilog/VHDL files
