import pylab
import math
from math import pi, sin, cos, pow, degrees

def main():
    
    aoa_list = AOA()
    calculations = Calculations(aoa_list)
    cl_list = calculations.CL()
    cd_list = calculations.CD()
    ld_list = calculations.LD()

    cl_max = max(cl_list)
    cl_max_index = cl_list.index(cl_max)
    aoa_cl_max = aoa_list[cl_max_index]
        
    #print cl_max
    #print degrees(aoa_cl_max)

    #aoa_cl_max = 57.7 degrees
    #cl_max = .7698

    pylab.plot(aoa_list, cl_list, aoa_list, cd_list, aoa_list, ld_list)
    pylab.ylabel('CL, CD, L/D')
    pylab.xlabel('angle of attack (radians)')
    pylab.title('CL, CD, L/D vs. AOA')
    pylab.show()

def AOA():
    aoa_list = []
    aoa_list.append(.10)
    counter = .10
    while True:
        increment = .001
        counter += increment
        aoa_list.append(counter)
        if counter >= pi/2:
            break
    return aoa_list

class Calculations:

    def __init__(self, aoa_list):
        self.aoa_list = aoa_list

    def CL(self):
        self.cl_list = []
        for aoa in self.aoa_list:
            cl = 2*pow(sin(aoa), 2)*cos(aoa)
            self.cl_list.append(cl)
        return self.cl_list

    def CD(self):
        self.cd_list = []
        for aoa in self.aoa_list:
            cd = 2*pow(sin(aoa), 3)
            self.cd_list.append(cd)
        return self.cd_list

    def LD(self):
        self.ld_list = []
        for i in range(len(self.cl_list)):
            try:
                cl = self.cl_list[i]
                cd = self.cd_list[i]
                ld = cl/cd
                self.ld_list.append(ld)
            except:
                self.ld_list.append(0)
        return self.ld_list

if __name__ == "__main__":
    main()
