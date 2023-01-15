#Program to calculate the shorter angle between the hour and minute hand in an analog clock after getting hh:mm from the user.
#Defining a function to perform the algorithms.
def calculate_angle(time): 
    hh, mm = time.split(':') 
  
    hh, mm = int(hh), int(mm) 
  
    # validate the input 
    if (hh < 0 or mm < 0 or hh > 12 or mm > 60): 
        print('Wrong input') 
  
    if (hh == 12): 
        hh = 0
    if (mm == 60): 
        mm = 0
  
    # Calculate the angles moved by  
    # hour and minute hands with  
    # reference to 12:00 
    hour_angle = 0.5 * (hh * 60 + mm) 
    minute_angle = 6 * mm 
  
    # Find the difference between two angles 
    angle = abs(hour_angle - minute_angle) 
  
    # Return the smaller angle of two  
    # possible angles 
    angle = min(360 - angle, angle) 
    
    return angle 
  
# Main body
print('Enter time in format hour:min when the hh and mm appear seperately')
hh = int(input('Enter hour hh : '))
mm = int(input('Enter minute mm : '))
time= (f'{hh}:{mm}')
print(f'The angle between {time} is',calculate_angle(time))