import math
c=3*100000000
#dielectric constant
er=2.33

#Resonant frquency
F=3.5*1000000000

#substrate thickness
h=0.787/100

W=c/(2*F*(math.sqrt((er+1)/2)))
print("W= ",W*100," cm")

x=math.sqrt(1+(12*(h/W)))
er1=(er+1)/2
er2=(er-1)/2
ereff=er1+(er2/x)

dL=0.412*h*((((W/h)+0.264)*(ereff+0.3))/((ereff-0.258)*((W/h)+0.8)))
Leff=c/(2*F*math.sqrt(ereff))
L=Leff-((2*(dL)))

print("L= ",L*100," cm")
