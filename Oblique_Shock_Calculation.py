import math
from math import tan, cos, sin, pi, pow, atan, sqrt, degrees, radians
import mpmath
from mpmath import cot


def main():

    while True:
        turn_angle = radians(float(raw_input("Enter Turn Angle (degrees): ")))
        mach_1 = float(raw_input("Enter Mach_1: "))
        gamma = 1.4

        beta = BetaCalculation(turn_angle, mach_1, gamma)
        beta_degrees = degrees(beta)

        oblique_shock_calculations = ObliqueShockCalculations(beta, gamma, mach_1, turn_angle)
        pressure_ratio = oblique_shock_calculations.PressureRatio()
        density_ratio = oblique_shock_calculations.DensityRatio()
        temperature_ratio = oblique_shock_calculations.TemperatureRatio()
        mach_2 = oblique_shock_calculations.Mach2()
        total_temperature_ratio = oblique_shock_calculations.TotalTemperatureRatio()
        total_pressure_ratio = oblique_shock_calculations.TotalPressureRatio()
        velocity_ratio = oblique_shock_calculations.VelocityRatio()

        print "Pressure Ratio: ", pressure_ratio
        print "Density Ratio: ", density_ratio
        print "Temperature Ratio: ", temperature_ratio
        print "Mach2: ", mach_2
        print "Total Temperature Ratio: ", total_temperature_ratio
        print "Total Pressure Ratio: ", total_pressure_ratio
        print "Velocity Ratio: ", velocity_ratio
        print "\n"
    

#Create a class to organize modules for oblique shock calculations
class ObliqueShockCalculations:

    def __init__(self, beta, gamma, mach_1, turn_angle):
        self.beta = beta
        self.gamma = gamma
        self.mach_1 = mach_1
        self.turn_angle = turn_angle

    #Calculate Pressure ratio
    def PressureRatio(self):
        self.pressure_ratio = 1 + (2*self.gamma/(self.gamma + 1))*(pow(self.mach_1, 2)*pow(sin(self.beta), 2) - 1)
        return self.pressure_ratio

    #Calculate Density Ratio
    def DensityRatio(self):
        self.density_ratio = (((self.gamma + 1)*pow(self.mach_1, 2)*pow(sin(self.beta), 2))/((self.gamma -1)*pow(self.mach_1, 2)*pow(sin(self.beta), 2) + 2))
        return self.density_ratio

    #Calculate Temperature Ratio
    def TemperatureRatio(self):
        self.temperature_ratio = self.pressure_ratio*pow(self.density_ratio, -1)
        return self.temperature_ratio

    #Calculate Mach2
    def Mach2(self):
        self.mach_2 = (1/sin(self.beta-self.turn_angle))*sqrt((1+((self.gamma-1)/2)*pow(self.mach_1,2)*pow(sin(self.beta),2))/(self.gamma*pow(self.mach_1,2)*pow(sin(self.beta),2)-((self.gamma-1)/2)))
        return self.mach_2

    def TotalTemperatureRatio(self):
        self.total_temperature_ratio = ((2*self.gamma*pow(self.mach_1, 2)*pow(sin(self.beta), 2) - (self.gamma - 1))*((self.gamma - 1)*pow(self.mach_1, 2)*pow(sin(self.beta), 2) + 2))/(pow(self.gamma + 1, 2)*pow(self.mach_1, 2)*pow(sin(self.beta), 2))
        return self.total_temperature_ratio

    def TotalPressureRatio(self):
        self.total_pressure_ratio = pow(((self.gamma + 1)*pow(self.mach_1, 2)*pow(sin(self.beta), 2))/((self.gamma - 1)*pow(self.mach_1, 2)*pow(sin(self.beta), 2) + 2), (self.gamma / (self.gamma - 1)))*pow((self.gamma + 1) / (2*self.gamma*pow(self.mach_1, 2)*pow(sin(self.beta), 2) - (self.gamma - 1)), (1 / (self.gamma - 1)))
        return self.total_pressure_ratio

    def VelocityRatio(self):
        self.velocity_ratio = (self.mach_2/self.mach_1)*sqrt(self.temperature_ratio)
        return self.velocity_ratio

#Solve for Beta by setting ThetaEquation == BMEquation and backing out gamma
def BetaCalculation(turn_angle, mach_1, gamma):
    domain_list = DomainList()
    tangent_theta = ThetaEquation(turn_angle)
    for angle in domain_list:
        bm_equation = BMEquation(gamma, mach_1, angle)
        try:
            if round(float(bm_equation), 4) == round(float(tangent_theta), 4):    
                beta = angle
                break
        except:
            beta = ''
            pass
    return beta
    
#Create a Theta Equation (Left-side of BM-Theta)
def ThetaEquation(turn_angle):
    tangent_theta = tan(turn_angle)
    return tangent_theta

#Create Beta Mach Equation (Right-side of BM-Theta)
def BMEquation(gamma, mach_1, beta):
    bm_equation = ''
    if beta > 0:
        bm_equation = 2*cot(beta)*((pow(mach_1, 2)*pow(sin(beta), 2) - 1)/(pow(mach_1, 2)*(gamma + cos(2*beta)) + 2))
    return bm_equation

#Create a list of angles from 0 to 1.6 radians
def DomainList():
    domain_list = []
    domain_list.append(0)
    while True:
        index = len(domain_list) - 1
        value = domain_list[index] + .0001
        domain_list.append(value)
        if value > 1.6:
            break
    return domain_list


if __name__ == "__main__":
    main()
    



    
