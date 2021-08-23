#!/usr/bin/env python3
#-*- coding:UTF-8 -*-

#from __future__ import print_function
import math
import sys
import time
import rospy
from rospy import timer 
from std_msgs.msg import Float64 , String





#＃All lengh unit in mm
dis_num_board = 49.0	#distance between any two number boards is 0.049m
dis_ori_plate = (63.0+70.0) #distance between origin and the plate site
link0 = 60.0
link1 = 82.0
link2 = 131.0
link3 = 206.0

up_down_dis = 20.0 #distance of arm tip from above the board to the surface
half_plate_lengh = 151.0/2.0

interval_i = 100 ##this is used for for_loop i,must be in type int
interval = 100.0 ##this is used for float division,must be in type float





class coordinate:
    
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z
##reset_point =coordinate(###)######need to set on actual robot arm
A_up  =coordinate(-dis_num_board , dis_ori_plate + half_plate_lengh + dis_num_board , up_down_dis)
A_down=coordinate(-dis_num_board , dis_ori_plate + half_plate_lengh + dis_num_board , 0.0)
B_up  =coordinate(0.0 , dis_ori_plate + half_plate_lengh + dis_num_board , up_down_dis)
B_down=coordinate(0.0 , dis_ori_plate + half_plate_lengh + dis_num_board, 0.0)
C_up  =coordinate(dis_num_board , dis_ori_plate + half_plate_lengh + dis_num_board, up_down_dis)
C_down=coordinate(dis_num_board , dis_ori_plate + half_plate_lengh + dis_num_board, 0.0)
D_up  =coordinate(-dis_num_board , dis_ori_plate + half_plate_lengh , up_down_dis)
D_down=coordinate(-dis_num_board , dis_ori_plate + half_plate_lengh , 0.0)
E_up  =coordinate(0.0 , dis_ori_plate + half_plate_lengh , up_down_dis)
E_down=coordinate(0.0 , dis_ori_plate + half_plate_lengh , 0.0)
F_up  =coordinate(dis_num_board , dis_ori_plate + half_plate_lengh , up_down_dis)
F_down=coordinate(dis_num_board , dis_ori_plate + half_plate_lengh , 0.0)
G_up  =coordinate(-dis_num_board , dis_ori_plate + half_plate_lengh - dis_num_board , up_down_dis)
G_down=coordinate(-dis_num_board , dis_ori_plate + half_plate_lengh - dis_num_board , 0.0)
H_up  =coordinate(0.0 , dis_ori_plate + half_plate_lengh - dis_num_board , up_down_dis)
H_down=coordinate(0.0 , dis_ori_plate + half_plate_lengh - dis_num_board , 0.0)
I_up  =coordinate(dis_num_board , dis_ori_plate + half_plate_lengh - dis_num_board , up_down_dis)
I_down=coordinate(dis_num_board , dis_ori_plate + half_plate_lengh - dis_num_board , 0.0)


def talker():
    pub1 = rospy.Publisher('/myrobot/joint1_position_controller/command', Float64, queue_size=10)
    pub2 = rospy.Publisher('/myrobot/joint2_position_controller/command', Float64, queue_size=10)
    pub3 = rospy.Publisher('/myrobot/joint3_position_controller/command', Float64, queue_size=10)
	
    rospy.init_node('joint_position_pub', anonymous=True)#note publisher is also a node
    rate = rospy.Rate(10) # 10hz

    while  not rospy.is_shutdown():

            Y = int(input("繼續=1，否=0:\n"))
            if Y == 1 :
                
                n=0
                j=coordinate(0,0,0)
                x_list = []
                y_list = []
                z_list = []
                while n < 2 :
                    input_posi = str(input('input position: '))
                    if input_posi == 'A_up':
                        j = A_up
                    
                    elif input_posi =='A_down':
                        j = A_down
                        
                    elif input_posi == 'B_up':
                        j = B_up
                        
                    elif input_posi =='B_down':
                        j = B_down
                        
                    elif input_posi == 'C_up':
                        j = C_up
                        
                    elif input_posi =='C_down':
                        j = C_down
                        
                    elif input_posi == 'D_up':
                        j = D_up
                        
                    elif input_posi =='D_down':
                        j = D_down
                    
                    elif input_posi == 'E_up':
                        j = E_up
                        
                    elif input_posi =='E_down':
                        j = E_down
                        
                    elif input_posi == 'F_up':
                        j = F_up
                        
                    elif input_posi =='F_down':
                        j = F_down
                        
                    elif input_posi == 'G_up':
                        j = G_up
                        
                    elif input_posi =='G_down':
                        j = G_down
                        
                    elif input_posi == 'H_up':
                        j = H_up
                    
                    elif input_posi =='H_down':
                        j = H_down
                        
                    elif input_posi == 'I_up':
                        j = I_up
                        
                    elif input_posi =='I_down':
                        j = I_down
                    else :
                        # rospy.signal_shutdown("improper input")
                        sys.exit()

                    
                    print("read in", n+1 , "x=%.4f" %j.x , "y=%.4f" %j.y , "z=%.4f" %j.z)
                    x_list+=[j.x]
                    y_list+=[j.y]
                    z_list+=[j.z]
                    #print(x_list[n])#used to check if read correctly
                    #print(y_list[n])
                    #print(z_list[n])
                    n+=1
                    ##存完兩次後xyz_list各有兩個值,讀了兩組座標

                t = 0 
                xi = x_list[0]
                xf = x_list[1]
                yi = y_list[0]
                yf = y_list[1]
                zi = z_list[0]
                zf = z_list[1]
                #type should be in float

                x_difference = (x_list[1]-x_list[0])
                y_difference = (y_list[1]-y_list[0])
                z_difference = (z_list[1]-z_list[0])
                #type should be in float

                #print(x_difference,y_difference,z_difference) 
                angle1 = 0
                angle2 = 0
                angle3 = 0
                xpt = []##x per time
                ypt=[]
                zpt=[]
                tpt = []
                angle1_pt = []##angle1 per time
                angle2_pt = []
                angle3_pt = []
                def move_on_surface(x,y): #地面上平移
                    L = math.sqrt(x**2+y**2)
                    L1 = link0+link1
                    L2 = link2
                    L3 = link3
                    L_diagonal = math.sqrt(L1**2+L**2)
                    cosR = (L2**2+L3**2-L_diagonal**2)/(2*L2*L3)
                    R = math.acos(cosR)
                    angle3 = -(math.pi - R)
                    a = math.acos(L1/L_diagonal)
                    b = math.asin(L3/L_diagonal*math.sin(R))
                    angle2 = -(math.pi - a - b)
                    angle1 = -math.asin(x/L)
                    print(angle1,angle2,angle3)
                    

                    return(angle1,angle2,angle3)

                def move_above_plate(x,y): #空中平移
                    L = math.sqrt(x**2+y**2)
                    L1 = link0+link1-up_down_dis
                    L2 = link2
                    L3 = link3
                    L_diagonal = math.sqrt(L1**2+L**2)
                    cosR = (L2**2+L3**2-L_diagonal**2)/(2*L2*L3)
                    R = math.acos(cosR)
                    angle3 = -(math.pi - R)
                    a = math.acos(L1/L_diagonal)
                    b = math.asin(L3/L_diagonal*math.sin(R))
                    angle2 = -(math.pi - a - b)
                    angle1 = -math.asin(x/L)
                    print(angle1,angle2,angle3)
                    pub1.publish(angle1)
                    pub2.publish(angle2)
                    pub3.publish(angle3)

                    return(angle1,angle2,angle3)

                def z_direction_move(x,y,z): #垂直地面上下移動
                    L = math.sqrt(x**2+y**2)
                    L1 = link0 + link1 - z###need to check
                    L2 = link2
                    L3 = link3
                    L_diagonal = math.sqrt(L1**2+L**2)
                    cosR = (L_diagonal**2-L2**2-L3**2)/(-2*L2*L3)
                    R = math.acos(cosR)
                    angle3 = -(math.pi - R)
                    a = math.acos(L1/L_diagonal)
                    b = math.asin(L3/L_diagonal*math.sin(R))
                    angle2 = -(math.pi - a - b)
                    angle1 = -math.asin(x/L)
                    print(angle1,angle2,angle3)

                    return(angle1,angle2,angle3)

                
                
                if zi == zf == 0:##moving on the surface of the plate
                    i=0
                    for i in range(interval_i)  :##
                        angle1,angle2,angle3=move_on_surface(xi,yi)
                        angle1_pt+=[angle1]##angle1_pt = angle1_pt + [angle1]
                        angle2_pt+=[angle2]
                        angle3_pt+=[angle3]

                        xpt+=[xi]
                        ypt+=[yi]
                        zpt+=[zi]
                        tpt+= [t]

                        xi+= x_difference / interval
                        yi+= y_difference / interval
                        # print(xi,yi,zi)
                        i+=1
                        time.sleep(0.1)
                        

                elif zi == zf == up_down_dis :#moving above the plate 
                    i=0
                    for i in range(interval_i)  :##
                        angle1,angle2,angle3=move_above_plate(xi,yi)
                        angle1_pt+=[angle1]##angle1_pt = angle1_pt + [angle1]
                        angle2_pt+=[angle2]
                        angle3_pt+=[angle3]

                        xpt+=[xi]
                        ypt+=[yi]
                        zpt+=[zi]
                        tpt+= [t]
                        
                        xi+= x_difference / interval #兩點之間切成100格
                        yi+= y_difference / interval
                        # print(xi,yi,zi)
                        i+=1
                        time.sleep(0.1)

                elif zi != zf :
                    i=0
                    for i in range(interval_i)  :
                        angle1,angle2,angle3=z_direction_move(xi,yi,zi)
                        angle1_pt+=[angle1]##angle1_pt = angle1_pt + [angle1]
                        angle2_pt+=[angle2]
                        angle3_pt+=[angle3]

                        xpt+=[xi]
                        ypt+=[yi]
                        zpt+=[zi]
                        tpt+= [t]
                        
                        xi+= x_difference / interval #兩點之間切成100格
                        yi+= y_difference / interval
                        zi+= z_difference / interval
                        # print(xi,yi,zi)
                        i+=1
                        time.sleep(0.1)
                else :
                    sys.exit("error")
            else:
                sys.exit("see you")

if __name__ == '__main__':
	try:
		talker()
	except rospy.ROSInterruptException:
		pass
    




 
