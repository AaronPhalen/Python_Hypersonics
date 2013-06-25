import math
from math import pi, pow, radians, degrees, sin, atan, sqrt

def main():
    
    gamma = 1.4

    mach_number = float(raw_input("Enter Mach number: "))
    prandtl_meyer_angle = PrandtlMeyerAngle(gamma, mach_number)
    prandtl_meyer_angle_degrees =  degrees(prandtl_meyer_angle)

    prandtl_meyer_angle = radians(float(raw_input("Enter Prandtl-Meyer Angle Degrees: ")))
    mach_list = MachList()
    PrandtlMeyerMach(prandtl_meyer_angle, gamma, mach_list)    
    

def PrandtlMeyerAngle(gamma, mach):
    prandtl_meyer = sqrt((gamma+1)/(gamma-1))*atan(sqrt(((gamma-1)/(gamma+1))*(pow(mach,2) -1)))-atan(sqrt(pow(mach,2)-1))
    return prandtl_meyer

def PrandtlMeyerMach(prandtl_meyer_angle, gamma, mach_list):
    for mach in mach_list:
        try:
            prandtl_meyer = sqrt((gamma+1)/(gamma-1))*atan(sqrt(((gamma-1)/(gamma+1))*(pow(mach,2) -1)))-atan(sqrt(pow(mach,2)-1))
            print "Prandtly Meyer Angle: ", prandtl_meyer_angle
            print "Prandtl Meyer: ", prandtl_meyer
        except:
            pass
        
def MachList():
    mach_list = []
    mach_list.append(0)
    while True:
        index = len(mach_list) - 1
        value = mach_list[index] + .001
        mach_list.append(value)
        if value > 15:
            break
    return mach_list
    
if __name__ == "__main__":
    main()
