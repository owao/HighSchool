#작년 파일

from jajuchaUtil import *

################################ set cascade ################################
trafficlight_cascade = cv2.CascadeClassifier('trafficlight_cascade.xml')
#############################################################################

def findTrafficLight(image):
    # ROI 설정
    height, width = image.shape[:2]
    ROI_image = image[:120, :]
    light = False # Red light
    
    # 학습 모델을 사용하여 신호등 위치 추정
    ROI_gray = cv2.cvtColor(ROI_image, cv2.COLOR_BGR2GRAY)
    # trafficlight = trafficlight_cascade.detectMultiScale(ROI_gray, 1.3, 5)
    trafficlight = trafficlight_cascade.detectMultiScale(ROI_gray, 1.1, 4)
    cv2.imshow('roi', ROI_gray)

    for (x,y,w,h) in trafficlight:
        # 신호등이 30cm 이상 밖에 있다고 판단하고 그대로 함수 종료
        if w < 35:
            break

        # 신호등이 30cm 이내 거리에 있다고 판단
        ROI = ROI_gray[y:y+h, x:x+w]        
        ROI_X = ROI.shape[1]
        ROI_Y = ROI.shape[0]

        light_position = -1
        
        # 신호등 위치에서 밝기를 기준으로 왼쪽과 오른쪽 중 어느곳에 불이 들어와 있는지 판단
        for i in range(ROI_X):
            for j in range(ROI_Y):
                if ROI[i, j] > 150: # 밝기 비교
                    light_position = j
        
        # 오른쪽에 불이 들어와 있다면 green을 리턴 (기본값 False)
        if light_position > ROI_X/2 + 4:
            light = True
        
        return (x, y, w, h, light)
    
    # 발견된 신호등이 없으면 그냥 False 리턴
    # False is red / True is green
    return False

def autoDrive_algorithm(original_img, canny_img, points, lines, LiDAR, prevComm, status, light):
    height, width = canny_img.shape[:2]
    center = int(width/2) - 2
    debug = True
    # debug = False
    command = prevComm

    result = findTrafficLight(original_img)
    
    if result != False:
        x = result[0]
        y = result[1]
        w = result[2]
        h = result[3]
        light = result[4]
        cv2.rectangle(original_img,(x,y),(x+w,y+h),(0,0,255),2)

    H1LD = points['H1LD']
    H1RD = points['H1RD']
    H2LD = points['H2LD']
    H2RD = points['H2RD']
    H3LD = points['H3LD']
    H3RD = points['H3RD']
    H1Y = int(height/3)*1
    H2Y = int(height/3)*2
    H3Y = int(height/3)*3

    V1D = points['V1D']
    V2D = points['V2D']
    V3D = points['V3D']
    V4D = points['V4D']
    V5D = points['V5D']
    V6D = points['V6D']
    V7D = points['V7D']
    V1X = int(width/8)*1        # 1 block distance by y axis
    V2X = int(width/8)*2        # 2 blocks distance by y axis
    V3X = int(width/8)*3        # 3 blocks distance by y axis
    V4X = int(width/8)*4        # 4 blocks distance by y axis
    V5X = int(width/8)*5        # 5 blocks distance by y axis
    V6X = int(width/8)*6        # 6 blocks distance by y axis
    V7X = int(width/8)*7        # 7 blocks distance by y axis

    XD1 = int(width/8)*1        # 1 block distance by x axis
    XD2 = int(width/8)*2        # 2 blocks distance by x axis
    XD3 = int(width/8)*3        # 3 blocks distance by x axis
    
    leftLane, rightLane, endLane = getLane(lines)
    left = right = end = False
    if len(leftLane) != 0:
        left = True
    if len(rightLane) != 0:
        right = True
    if len(endLane) != 0:
        end = True

    light = True
    # lane detection algorithm
    if not light: # when red light
        # False is red / True is green
        print('Traffic Light: RED')
        command = 'S0150E'
    elif status is ONSTRAIGHT:
        if 1 < LiDAR and LiDAR < 300:
            print('Obstacle Detected at %dmm' % LiDAR)
            command = 'S0150E'
        
        if left and right:  # 1, 2
            if debug: 
                print('case 1,2 / ONSTRAIGHT')
                # print(leftLane, rightLane)
                # print('left lean: %f' % getLean(leftLane))
                # print('right lean: %f' % getLean(rightLane))
            if getLean(rightLane) < 0.53:
                if debug: 
                    print('right lean exception')
                command = 'S1150E'

            # left_center, right_center = getCenterPoint(leftLane, rightLane)
            if H2LD != 160 and H2RD != 160:
                if debug: print('center point calculated by H2 points %d, %d' % (H2LD, H2RD))
                centerPoint_X = (320 - H2LD + H2RD)/2
            elif H3LD != 160 and H3RD != 160:
                if debug: print('center point calculated by H3 points %d, %d' % (H3LD, H3RD))
                centerPoint_X = (320 - H3LD + H3RD) - 67
            else:
                return prevComm, status, light
            # centerPoint_X = (left_center+right_center)/2
            # if debug: 
            #     print(centerPoint_X)
                # print(H1LD, H1RD, H2LD, H2RD, H3LD, H3RD)
                # print(V1D, V2D, V3D, V4D, V5D, V6D, V7D)

            # if H1LD < 30 and H1RD < 30:
            #     command = 'S1133E'
            if H1RD is -1 or H2RD is -1:
                print('Status changed Straight to ONRIGHT')
                status = ONRIGHT
            elif centerPoint_X > center: # v pos left
                if centerPoint_X > 200:
                    command = 'S1170E'
                else:
                    command = 'S1160E'
            elif centerPoint_X < center-10: # v pos left
                command = 'S1140E'
            else:
                command = 'S1150E'

        elif right and not left and end: # case 3
            if debug: 
                print('case 3')
                print('Status changed straight to leftcorner')
                command = prevComm
                status = ONLEFT
        elif not right and left and end and H3LD > 90: #case 4
            if debug:
                print('case 4')
                print('Status changed straight to right corner')
                command = 'S1170E'
                status = ONRIGHT
    elif status is ONLEFT:
        if right and not left and end: # case 3
            if debug: 
                print('case 3 / ONLEFT')
                # print('right lean: %f' % getLean(rightLane))
                # print('%d %d %d %d %d %d %d' % (V1D, V2D, V3D, V4D, V5D, V6D, V7D))
            if V4D < 75:
                command = 'S1120E'
        elif right and left:
            if debug:
                print('case 1,2 / ONLEFT')
            # if V4D > 80:
            #     command = 'S1160E'
            #     status = ONSTRAIGHT
            if (H2LD > 60 and H2RD > 60) or (H3LD > 65 and H2RD > 65) :
                if debug:
                    print('Status changed leftcorner to straight')
                command = 'S1150E'
                status = ONSTRAIGHT
        elif end:
            print('only end line detected')
            command = 'S1120E'
        else:
            print('out of range')
            command = prevComm
            
    elif status == ONRIGHT:
        print('ONRIGHT')
        if 10 < LiDAR and LiDAR < 300:
            print('Obstacle Detected at %dmm' % LiDAR)
            command = 'S0160E'
            status = ONSTRAIGHT
        elif V4D < 55:
            command = 'S1180E'
            status = ONSCORNER
        else:
            command = 'S1150E'
    elif status == ONSCORNER:
        print('ONSCORNER')
        command = 'S1185E'
        if right and left:
            if debug:
                print('case 1,2 / ONRIGHT')
            if H3LD > 60 and H3RD > 60:
                if debug:            
                    print('Status changed rightcorner to straight')
                command = 'S1150E'
                status = ONSTRAIGHT

    if H2LD !=160 and H2RD !=160:
    	if debug: print('center point calculated by H2 points %d, %d' % (H2LD, H2RD))
    	centerPoint_X=(320-H2LD+H2RD)/2
    	if centerPoint_X> center+5: 
    		if centerPoint_X> center+20:
    			command='S1170E'
    		else:
    			command='S1160E'

    return command, status, light

