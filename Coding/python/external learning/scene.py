import cs1graphics as cs
canvas=cs.Canvas(1000,500) #캔버스 사이즈 지정
class Scene():    
    class Background():
        def setTitle(name): #캔버스 이름 설정 함수
            canvas.setTitle(name)
            
        class sea():
            canvas.setBackgroundColor("lightblue")
            def seaColor(r,g,b): #배경 색이 바뀔 rgb값 지정
                Color=(r,g,b) #tuple형 변수로 지정
                canvas.setBackgroundColor(Color)
                #seaColor로 색지정을 해주지 않으면 배경은 하늘색
                
        class rock(): #실행시키면 바로 돌을 그림
            rock1=cs.Ellipse(100)
            rock1.setHeight(200)
            rock1.setWidth(400)
            rock1.setBorderColor("gray")
            rock1.setFillColor("gray")
            canvas.add(rock1)
            rock1.moveTo(50,500) #왼쪽 구석 돌
            rock1.setDepth(10)

            rock2=cs.Ellipse(100)
            rock2.setHeight(100)
            rock2.setWidth(200)
            rock2.setBorderColor("gray")
            rock2.setFillColor("gray")
            canvas.add(rock2)
            rock2.moveTo(700,500) #오른쪽 돌
            rock2.setDepth(10)

        class ground(): #실행시키면 바로 땅을 그림
            ground=cs.Rectangle(1000,80)
            ground.setBorderColor((250,179,58))
            ground.setFillColor((250,179,58))
            canvas.add(ground)
            ground.moveTo(500,460)
            
        class seaweed(): #실행시키면 바로 해초를 그림
            seaweed1=cs.Ellipse(100)
            seaweed1.setHeight(300)
            seaweed1.setWidth(50)
            seaweed1.setBorderColor("darkgreen")
            seaweed1.setFillColor("darkgreen")
            canvas.add(seaweed1) #첫번째해초
            seaweed1.moveTo(100,400)
            seaweed1.setDepth(15)

            seaweed2=cs.Ellipse(100)
            seaweed2.setHeight(200)
            seaweed2.setWidth(30)
            seaweed2.setBorderColor("darkgreen")
            seaweed2.setFillColor("darkgreen")
            canvas.add(seaweed2) #두번째해초
            seaweed2.moveTo(150,400)
            seaweed2.setDepth(15)

        class bubble(): #실행시키면 배경에 공기방울을 그림
            bubble1=cs.Circle(20)
            bubble1.setBorderColor("white")
            bubble1.setFillColor("white")
            canvas.add(bubble1) # 왼쪽 큰 공기방울
            bubble1.moveTo(200,50)

            bubble2=cs.Circle(15)
            bubble2.setBorderColor("white")
            bubble2.setFillColor("white")
            canvas.add(bubble2) # 왼쪽 중간 공기방울
            bubble2.moveTo(200,100)

            bubble3=cs.Circle(10)
            bubble3.setBorderColor("white")
            bubble3.setFillColor("white")
            canvas.add(bubble3) # 왼쪽 작은 공기방울
            bubble3.moveTo(200,140)

            bubble4=cs.Circle(20)
            bubble4.setBorderColor("white")
            bubble4.setFillColor("white")
            canvas.add(bubble4) # 오른쪽 큰 공기방울
            bubble4.moveTo(850,200)

            bubble5=cs.Circle(15)
            bubble5.setBorderColor("white")
            bubble5.setFillColor("white")
            canvas.add(bubble5) # 오른쪽 중간 공기방울
            bubble5.moveTo(850,250)

            bubble6=cs.Circle(10)
            bubble6.setBorderColor("white")
            bubble6.setFillColor("white")
            canvas.add(bubble6) # 오른쪽 작은 공기방울
            bubble6.moveTo(850,290)
            
     
    class fish():
        class body():
            body=cs.Ellipse(100)
            body.setHeight(100)
            body.setWidth(150)
            body.setFillColor("white") #물고기 기본 색은 흰색
            canvas.add(body)
            body.moveTo(500,250)
            body.setDepth(5)
            def setColor(r,g,b): #물고기 몸통 색이 바뀔 rgb값 지정
                color=(r,g,b)
                body.setFillColor(color)
                    
        class eye():
            eye=cs.Circle(10)
            eye.setFillColor("black")
            canvas.add(eye)
            eye.moveTo(470,250) #몸통의 x좌표에서 30만큼 뺀 게 x좌표
            eye.setDepth(1)
                
        class fin():
            fin=cs.Polygon(cs.Point(0,50), cs.Point(50,0), cs.Point(50,100))
            fin.setFillColor("white")
            canvas.add(fin)
            fin.moveTo(575,250) #몸통의 x좌표에서 25만큼 더한 게 x좌표
            fin.setDepth(5)
            def setColor(r,g,b): #몸통과 같은 rgb 입력
                color=(r,g,b)
                fin.setFillColor(color)
