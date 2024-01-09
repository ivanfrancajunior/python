# Variables and contants - best pratices intro


# 1 - Prioritize writing capital letters

CONSTANT = 'use uppercase '

# Avoid complexity in the code : create variable s to simplify your code


RADAR_1_LIMIT_SPEED = 60 # Velocidade máxiam captada pelo radar
LOCAL_1 = 100 # kilometro em q o radar esta fixado 
RADAR_RANGE = 1 # alcance do radar

car_speed = 61  # velocidade atual do carro
car_local = 100 # local em que o carro está na estrada

position_minimum_range = -1 

position_maximum_range = 1 

if (car_local - LOCAL_1 < position_minimum_range) or (LOCAL_1 - car_local  > position_maximum_range ) and car_speed > RADAR_1_LIMIT_SPEED :
    
    print('Pega nada, segue a meta')
else:
    print('Você será multado')
