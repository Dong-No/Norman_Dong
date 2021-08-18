import math
import sys
##import matplotlib.pyplot as plt
##from mpl_toolkits.mploangle3d.axes3d import Axes3D




#＃All lengh unit in mm
dis_num_board = 0.049*1000.0	#distance between any two number boards is 0.049m
dis_ori_plate = (0.063+0.07)*1000.0 #distance between origin and the plate site
link0 = 0.06*1000.0
link1 = 0.082*1000.0
link2 = 0.131*1000.0
link3 = 0.206*1000.0
num_block_cent_dis = 0.045*1000.0
up_down_dis = 0.02*1000.0 #distance of arm tip from above the board to the surface
half_plate_lengh = 0.151/2.0*1000.0
interval = 100##兩座標之間的間隔數


class coordinate:
    
        def __init__(self,x,y,z):
            self.x=x
            self.y=y
            self.z=z
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

while  True :
    Y = int(input("繼續=1，否=0:\n"))
    if Y == 1 :

        n=0
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
                sys.exit("improper input")

            
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
            L=math.sqrt(x**2+y**2)
            L1=link0+link1
            L2=link2
            L3=link3
            L0=math.sqrt(L1**2+L**2)
            R=(L0**2-L2**2-L3**2)/(-2*L2*L3)
            r=math.acos(R)
            a=math.asin((L2/L0)*math.sin(r))
            b=math.asin((L3/L0)*math.sin(r))
            a1=math.atan(L1/L)
            b1=math.atan(L/L1)
            angle1=90-math.degrees(math.atan(x/y))
            angle2=180-math.degrees(b+b1)
            angle3=90+math.degrees(a+a1)
            return(angle1,angle2,angle3)
        def move_above_plate(x,y): #空中平移
            L=math.sqrt(x**2+y**2)
            L1=link0+link1-up_down_dis
            L2=link2
            L3=link3
            L0=math.sqrt(L1**2+L**2)
            R=(L0**2-L2**2-L3**2)/(-2*L2*L3)
            r=math.acos(R)
            a=math.asin((L2/L0)*math.sin(r))
            b=math.asin((L3/L0)*math.sin(r))
            a1=math.atan(L1/L)
            b1=math.atan(L/L1)
            angle1=90-math.degrees(math.atan(x/y))
            angle2=180-math.degrees(b+b1)
            angle3=90+math.degrees(a+a1)
            return(angle1,angle2,angle3)
        def z_direction_move(x,y,z): #垂直地面上下移動
            L=math.sqrt(x**2+y**2)
            L1=z###need to check
            L2=link2
            L3=link3
            L0=math.sqrt(L1**2+L**2)
            R=(L0**2-L2**2-L3**2)/(-2*L2*L3)
            r=math.acos(R)
            a=math.asin((L2/L0)*math.sin(r))
            b=math.asin((L3/L0)*math.sin(r))
            a1=math.atan(L1/L)
            b1=math.atan(L/L1)
            angle1=90-math.degrees(math.atan(x/y))
            angle2=180-math.degrees(b+b1)
            angle3=90+math.degrees(a+a1)
            return(angle1,angle2,angle3)

        
        
        if zi == zf == 0:##moving on the surface of the plate
            i=0
            for i in range(interval)  :##
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
                print(xi,yi)
                i+=1

        elif zi == zf == up_down_dis :#moving above the plate 
            i=0
            for i in range(interval)  :##
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
                print(xi,yi)
                i+=1
        elif zi != zf :
            i=0
            for i in range(interval)  :
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
                print(xi,yi,zi)
                i+=1
        else :
            sys.exit("error")
    else:
        sys.exit("see you")



'''
        print(angle1_pt)
        print(angle2_pt)
        print(angle3_pt)
        print(tpt)
        plt.subplot(2, 2,1) 
        plt.plot(tpt,angle1_pt,'--ok') #畫線
        plt.title("T1", fontsize=8) #圖表標題
        plt.subplot(2, 2, 2) 
        plt.plot(tpt,angle2_pt,'--oc') #畫線
        plt.title("T2", fontsize=8) #圖表標題
        plt.subplot(2, 2, 3) 
        plt.plot(tpt,angle3_pt,'--og') #畫線
        plt.title("T3", fontsize=8) #圖表標題
        plt.subplot(2, 2, 4) 
        ##plt.plot(xpt,ypt,zpt,'-or') #畫線
        ##plt.xticks([-45,0,45]) #設定x軸刻度
        ##plt.yticks([257.5,208.5,159.5]) #設定y軸刻度
        ##plt.zticks([0,10,20]) #設定y軸刻度
        fig=plt.figure()
        ax=Axes3D(fig)
        ax.scatter(xpt,ypt,zpt,c='black')
        plt.title("X-Y-Z", fontsize=8) #圖表標題
    else:
        plt.show() #顯示繪製的圖形
'''
 
