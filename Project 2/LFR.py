from controller import Robot
robot = Robot()
timestep = int(robot.getBasicTimeStep())

time_step = 64
max_speed = 8

end_error=I=D=P=error=0
kp=1.5
ki=0
kd=0.3

#motor

left_motor1 = robot.getDevice('wheel1')
right_motor1 = robot.getDevice('wheel2')
left_motor2 = robot.getDevice('wheel3')
right_motor2 = robot.getDevice('wheel4')
left_motor1.setPosition(float('inf'))
right_motor1.setPosition(float('inf'))
left_motor2.setPosition(float('inf'))
right_motor2.setPosition(float('inf'))
left_motor1.setVelocity(0.0)
right_motor1.setVelocity(0.0)
left_motor2.setVelocity(0.0)
right_motor2.setVelocity(0.0)


#IR sensor
right_ir = robot.getDevice('ds_right')
right_ir.enable(time_step)
mid_ir = robot.getDevice('ds_mid')
mid_ir.enable(time_step)
left_ir = robot.getDevice('ds_left')
left_ir.enable(time_step)


#simulation 
#main loop:
target=400
while robot.step(time_step) != -1:
    right_ir_val = right_ir.getValue()
    mid_ir_val = mid_ir.getValue()
    left_ir_val = left_ir.getValue()
    print("left: {} mid: {} right: {}".format(left_ir_val, mid_ir_val, right_ir_val))
    
    
    #Process sensor data
    if left_ir_val<target and right_ir_val<target and mid_ir_val>=target:
         error=0
    elif left_ir_val<target and right_ir_val>=target and mid_ir_val>=target:
         error=-1
    elif left_ir_val>=target and right_ir_val<target and mid_ir_val>=target:
         error=1
    elif left_ir_val>=target and right_ir_val<target and mid_ir_val<target:
         error=2
    elif left_ir_val<target and right_ir_val>=target and mid_ir_val<target:
            error=-2
   
        
        
    P=error
    I=error+I
    D=error-end_error
    balance=int((kp*P)+(ki*I)+(kd*D))
    end_error=error
    
    left_speed = max_speed-balance
    right_speed = max_speed+balance
    
    
    if left_speed> max_speed:
        left_motor1.setVelocity(left_speed)
        right_motor1.setVelocity(0)
        left_motor2.setVelocity(left_speed)
        right_motor2.setVelocity(0)
        
    if right_speed> max_speed:
        left_motor1.setVelocity(0)
        right_motor1.setVelocity(right_speed)
        left_motor2.setVelocity(0)
        right_motor2.setVelocity(right_speed)
        
    if left_speed< 0:
        left_motor1.setVelocity(0)
        right_motor1.setVelocity(rightspeed)
        left_motor2.setVelocity(0)
        right_motor2.setVelocity(rightspeed)
        
    if right_speed< 0:
        left_motor1.setVelocity(left_speed)
        right_motor1.setVelocity(0)
        left_motor2.setVelocity(left_speed)
        right_motor2.setVelocity(0)
        
    if right_speed== max_speed:
        left_motor1.setVelocity(left_speed)
        right_motor1.setVelocity(right_speed)
        left_motor2.setVelocity(left_speed)
        right_motor2.setVelocity(right_speed)
                                            
    pass