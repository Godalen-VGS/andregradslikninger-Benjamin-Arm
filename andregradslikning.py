# Finner løsninger til alle andregradslikninger på formen ax^2+bx+c=0
import math

def losninger(a, b, c):
  diskriminant = b**2-4*a*c
  if diskriminant < 0:
    return "Likningen har ingen løsning"
  
  losning1 = round((-b + math.sqrt(diskriminant))/(2*a), 2)
  losning2 = round((-b - math.sqrt(diskriminant))/(2*a), 2)

  print(diskriminant)

  løsning1 print(diskrimant)


  if diskriminant  == 0:
    return losning1 #Et flyttall avrundet til to desimaler
  else:
    return (losning1, losning2)
  

  
  # Din kode her
  return #Returneringsverdi
