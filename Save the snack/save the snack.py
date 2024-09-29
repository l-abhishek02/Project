import pygame
from pygame import mixer
import random
import math
import json
# import reset
from reset import reset

pygame.init()
info=pygame.display.Info()
width,height=info.current_w,info.current_h
sc=pygame.display.set_mode((0,0),pygame.FULLSCREEN,32)
pygame.display.set_caption("Save The Snack")
charl=0
charr=0
print(width,height)
strt_snd=mixer.Sound("audio/funny-and-comical-melody-glide-synth-bass-and-trumpet-21398.mp3")
strt_snd.play(-1)
##SCREEN IMG
bg1=pygame.image.load("ww2.jpg")
menu=pygame.image.load("Screens/s1.jpg")
sltchr_s=pygame.image.load("Screens/s2.jpg")
nm_s=pygame.image.load("Screens/s3.jpg")
game_over_img=pygame.image.load("Screens/s4.jpg")
high_s=pygame.image.load("Screens/s5.jpg")
tm=pygame.image.load("Screens/s51.png")
credit_s=pygame.image.load("Screens/c1.jpg")
menun=pygame.transform.scale(bg1,(width,height))
sc.blit(menun,(0,0))

##BUTTON IMG
strt_img=pygame.image.load("btn/strt1.png")
cred_img=pygame.image.load("btn/cred.png")
highs_img=pygame.image.load("btn/hi_sb.png")
exit_img=pygame.image.load("btn/ex.png")
easy_img=pygame.image.load("btn/easy.png")
med_img=pygame.image.load("btn/med.png")
hard_img=pygame.image.load("btn/hard.png")
mm_img=pygame.image.load("btn/mm.png")
rstrt_img=pygame.image.load("btn/rstrt.png")

##PLAYER BUTTON IMG
p1_img=pygame.image.load("btn/p1.png")
p2_img=pygame.image.load("btn/p2.png")
p3_img=pygame.image.load("btn/p3.png")
p4_img=pygame.image.load("btn/p4.png")

text_font=pygame.font.SysFont("Constantia",34)
text_font1=pygame.font.SysFont("Constantia",70)
text_font2=pygame.font.SysFont("Constantia",26)

##RENDERING FONT
def draw_scr(text,font,text_col,x,y):
    scr=font.render(text,True,text_col)
    sc.blit(scr,(x,y))
        
##BUTTON CLASS
class buttons():
    def __init__(self,x,y,image):
        self.image=image
        self.rect=self.image.get_rect()
        self.rect.topleft=(x,y)
        self.clicked=False

    def draw(self):
        pos=pygame.mouse.get_pos()
        action=False
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0]==1 and self.clicked==False:
                self.clicked=True
                print('Clicked')
                action=True
        if pygame.mouse.get_pressed()[0]==0:
            self.clicked=False    
        sc.blit(self.image,(self.rect.x,self.rect.y))
        return action

##MENU
def men():
    
    start_button=buttons(227+(width/2)-350,315+(height/2)-350,strt_img)
    credits_button=buttons(227+(width/2)-350,423+(height/2)-350,cred_img)
    highs_button=buttons(505+(width/2)-350,645+(height/2)-350,highs_img)
    exit_button=buttons(227+(width/2)-350,533+(height/2)-350,exit_img)  
    run=True
    while run:

        sc.blit(menu,((width/2)-350,(height/2)-350))
        if start_button.draw():
            sltchar()
            break
        if credits_button.draw():
            creditlop()
            break
        if highs_button.draw():
            high_scrn()
            break
        if exit_button.draw():
            break
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run=False
        pygame.display.flip()

##CREDIT SCREEN
def creditlop():
    
    lop=True
    while lop:
        sc.blit(credit_s,(((width/2)-350,(height/2)-350)))
        for event in pygame.event.get():
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_BACKSPACE:
                    lop=False
                    men()
        pygame.display.update()

##HIGH SCORE SCREEN
def high_scrn():
    lop=True
    cnt2=0
    rstrt_button=buttons(640+(width/2)-350,640+(height/2)-350,rstrt_img)
    while lop:
        spc=100
        sc.blit(high_s,(((width/2)-350,(height/2)-350)))
        draw_scr("Sr.no",text_font,(0,0,0),136+(width/2)-350,168+(height/2)-350)
        draw_scr("Name",text_font,(0,0,0),290+(width/2)-350,168+(height/2)-350)
        draw_scr("Score",text_font,(0,0,0),482+(width/2)-350,168+(height/2)-350)
        if rstrt_button.draw():
            reset.resetfunct()
        with open("data.json",'r')as rd:
            hs=json.load(rd)
        for i in hs:
            draw_scr(str(i['no']),text_font,(0,0,0),160+(width/2)-350,168+(height/2)-350+spc)
            draw_scr(str(i['name']),text_font,(0,0,0),290+(width/2)-350,168+(height/2)-350+spc)
            draw_scr(str(i['score']),text_font,(0,0,0),506+(width/2)-350,168+(height/2)-350+spc)
            spc+=100
        
        for event in pygame.event.get():
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_BACKSPACE:
                    lop=False
                    men()
                    break
        pygame.display.update()

##CHARACTER SELECTION SCREEN
def sltchar():
    lop1=True
    p1_button=buttons(20+(width/2)-350,232+(height/2)-350,p1_img)
    p2_button=buttons(536+(width/2)-350,232+(height/2)-350,p2_img)
    p3_button=buttons(25+(width/2)-350,440+(height/2)-350,p3_img)
    p4_button=buttons(536+(width/2)-350,440+(height/2)-350,p4_img)

    while lop1:
        sc.blit(sltchr_s,(((width/2)-350,(height/2)-350)))
        if p1_button.draw():
            charl=pygame.image.load("charc/c2l.png")
            charr=pygame.image.load("charc/c1r.png")
            bg=pygame.image.load("Themes/bg1.jpg")
            mixer.music.load("audio/sh.mp3")
            fd=pygame.image.load("Snack/cc.png")
            lst=[charl,charr,bg,fd]
            ent_name(lst)
            break

        if p2_button.draw():
            charl=pygame.image.load("charc/c8l.png")
            charr=pygame.image.load("charc/c7r.png")
            bg=pygame.image.load("Themes/bg2.jpg")
            mixer.music.load("audio/dora.mp3")
            fd=pygame.image.load("Snack/dc.png")
            lst=[charl,charr,bg,fd]
            ent_name(lst)
            break

        if p3_button.draw():
            charl=pygame.image.load("charc/c6l.png")
            charr=pygame.image.load("charc/c5r.png")
            bg=pygame.image.load("Themes/bg3.jpg")
            mixer.music.load("audio/nh.mp3")
            fd=pygame.image.load("Snack/rc.png")
            lst=[charl,charr,bg,fd]
            ent_name(lst)
            break

        if p4_button.draw():
            charl=pygame.image.load("charc/c4l.png")
            charr=pygame.image.load("charc/c3r.png")
            mixer.music.load("audio/tj.mp3")
            bg=pygame.image.load("Themes/bg4.jpg")
            fd=pygame.image.load("Snack/cheese.png")
            lst=[charl,charr,bg,fd]
            ent_name(lst)
            break

        for event in pygame.event.get():
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_BACKSPACE:
                    lop1=False
                    men()
        pygame.display.update()

##LEVEL SELECTION SCREEN
def ent_name(lst):

##ACCEPTING NAME
    
    user_ip = ''
    font = pygame.font.SysFont(None,48)
    text_box = pygame.Rect(116+(width/2)-350,204+(height/2)-350,420,50)
    color = pygame.Color('purple')
    en=True

##LEVEL SELECTOR
    
    easy_button=buttons(57+(width/2)-350,502+(height/2)-350,easy_img)
    med_button=buttons(274+(width/2)-350,502+(height/2)-350,med_img)
    hard_button=buttons(493+(width/2)-350,502+(height/2)-350,hard_img)
    cnt=0
    active=True
    while en:
        
        sc.blit(nm_s,(((width/2)-350,(height/2)-350)))
        if cnt==8:
            active=False
        for event in pygame.event.get():
            if len(user_ip)==0:
                draw_scr("Enter name & then select level",text_font2,(0,0,0),130+(width/2)-350,214+(height/2)-350)
                draw_scr("Maximum 8 characters.",text_font2,(0,0,0),130+(width/2)-350,280+(height/2)-350)

            if event.type == pygame.QUIT:
                break
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE and len(user_ip)==0:
                    en=False
                    sltchar()
                    break
                if event.key == pygame.K_BACKSPACE:
                    active=True
                if active:
                    if event.key == pygame.K_BACKSPACE:
                        user_ip = user_ip[:-1]
                        cnt-=1
                    if event.key == pygame.K_a or event.key == pygame.K_b or event.key==pygame.K_c or event.key==pygame.K_d or event.key==pygame.K_e or event.key==pygame.K_f or event.key==pygame.K_g or event.key==pygame.K_h or event.key==pygame.K_i or event.key==pygame.K_j or event.key==pygame.K_k or event.key==pygame.K_l or event.key==pygame.K_m or event.key==pygame.K_n or event.key==pygame.K_o or event.key==pygame.K_p or event.key==pygame.K_q or event.key==pygame.K_r or event.key==pygame.K_s or event.key==pygame.K_t or event.key==pygame.K_u or event.key==pygame.K_v or event.key==pygame.K_w or event.key==pygame.K_x or event.key==pygame.K_y or event.key==pygame.K_z:
                        user_ip += event.unicode
                        cnt+=1

            if len(user_ip)>0:    
                if easy_button.draw():
                    en=False
                    fdc=0.2
                    mgame(lst,user_ip,fdc)
                    break

                if med_button.draw():
                    en=False
                    fdc=0.5
                    mgame(lst,user_ip,fdc)
                    break

                if hard_button.draw():
                    en=False
                    fdc=1
                    mgame(lst,user_ip,fdc)
                    break

            pygame.draw.rect(sc,color, text_box,4)
            surf = font.render(user_ip,True,'dark green')
            sc.blit(surf, (text_box.x +5 , text_box.y +5))
            pygame.display.update()

##MAIN GAME LOOP SCREEN
def mgame(lst,user_ip,fdc):
    charl=lst[0]
    charr=lst[1]
    bg=lst[2]
    fd=lst[3]
    mrun=True
    score=0
    strt_snd.stop()
    mixer.music.play(-1)

    playerimg=charl
    playc=0
    playx=350+(width/2)-350
    playy=600+(height/2)-350

    fdimg=fd
    fdx=random.randint(50+(width/2)-350,600+(width/2)-350)
    fdy=50+(height/2)-350
    temp_fdc=fdc
    
    cntdwn=5
    lastcnt=pygame.time.get_ticks()

##READING HIGHSCORE

    with open("data.json",'r')as rd:
        hs=json.load(rd)
        for i in hs:
            if i['no']==1:
                h=i['score']
                print(h)

##GAME LOOP
                
    while mrun:
        sc.blit(bg,(((width/2)-350,(height/2)-350)))
        sc.blit(fdimg,(fdx,fdy))
        if playx>=0+(width/2)-350 and playx<=640+(width/2)-350:
            sc.blit(playerimg,(playx,playy))

##STARTING COUNTDOWN

        if cntdwn>0:
            sc.blit(tm,(228+(width/2)-350,300+(height/2)-350))
            draw_scr("GAME BEGINS",text_font,(255,255,255),252+(width/2)-350,330+(height/2)-350)
            draw_scr("IN",text_font,(255,255,255),348+(width/2)-350,380+(height/2)-350)
            draw_scr(str(cntdwn),text_font,(255,255,255),358+(width/2)-350,430+(height/2)-350)
            cntime=pygame.time.get_ticks()
            if cntime-lastcnt>1000:
                cntdwn-=1
                lastcnt=cntime

        if cntdwn==0:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    mrun=False

##MOVEMENT
            
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_LEFT:
                        playc-=1.5
                        playerimg=charl
                    if event.key==pygame.K_RIGHT:
                        playc+=1.5
                        playerimg=charr
                    if event.key==pygame.K_ESCAPE:
                        mrun=False
                if event.type==pygame.KEYUP:
                    if event.key == pygame.K_LEFT or event.key==pygame.K_RIGHT:
                        playc=0
                if playx<=0+(width/2)-350:
                    playx=0+(width/2)-350
                    sc.blit(menun,(0,0))
                if playx>=640+(width/2)-350:
                    playx=640+(width/2)-350
                    sc.blit(menun,(0,0))
                playx+=playc

            fdy+=fdc
            playx+=playc

##SCORE COUNTER
            
            cth=catch(playx,playy,fdx,fdy)
            if cth:
                score+=1
                fdx=random.randint(50+(width/2)-350,600+(width/2)-350)
                fdy=50
                cth_snd=mixer.Sound("audio/cth.mp3")
                cth_snd.play()

                ##LEVEL UP
                if score%2==0:
                    fdc+=0.08
                    print(fdc)
                if score>0 and score%15==0:
                    sc.blit(tm,(228+(width/2)-350,300+(height/2)-350))
                    draw_scr("LEVEL",text_font,(255,255,255),310+(width/2)-350,320+(height/2)-350)
                    draw_scr("UP!!",text_font,(255,255,255),335+(width/2)-350,370+(height/2)-350)
                    draw_scr("MOVE FASTER!",text_font,(255,255,255),252+(width/2)-350,430+(height/2)-350)
                    pygame.display.update()
                    pygame.time.delay(3000)
            elif fdy>620:
                print("Loss")
                mrun=False
                game_over(score,user_ip,lst,fdc,temp_fdc)
                break
            draw_scr("Score:"+str(score),text_font,(0,0,0),5+(width/2)-350,5+(height/2)-350)
            draw_scr("Hi-score:"+str(h),text_font,(0,0,0),525+(width/2)-350,5+(height/2)-350)
        pygame.display.update()

##CATCHING CALCULATION
def catch(playx,playy,fdx,fdy):
    dist=math.sqrt((math.pow(fdx-playx,2))+ (math.pow(fdy-playy,2)))
    if dist<38:
        return True
    else:
        return False

##GAME OVER SCREEN
def game_over(score,user_ip,lst,fdc,temp_fdc):
    mm_button=buttons(260+(width/2)-350,610+(height/2)-350,mm_img)
    mixer.music.stop()
    go_snd=mixer.Sound("audio/Game Over.mp3")
    go_snd.play()
    cnt1=0
    nv=[]
    rstrt_button=buttons(330+(width/2)-350,515+(height/2)-350,rstrt_img)
##MODIFYING HIGH SCORE

    with open("data.json",'r')as rd:
        hs=json.load(rd)
        for each in hs:
            if score>each['score'] and cnt1==0:
                new={}
                new['no']=each['no']
                new['name']=user_ip
                new['score']=score
                nv.append(new)
                cnt1+=1
            else:
                new={}
                new['no']=each['no']
                new['name']=each['name']
                new['score']=each['score']
                nv.append(new)
    with open('data.json','w') as f:
        f.write(json.dumps(nv))

##GAME OVER LOOP
    gm=True
    while gm:
        sc.blit(game_over_img,(((width/2)-350,(height/2)-350)))
        draw_scr(str(score),text_font1,(0,0,0),330+(width/2)-350,300+(height/2)-350)
        if mm_button.draw():
            gm=False
            men()
            break
        if rstrt_button.draw():
            gm=False
            fdc=temp_fdc
            mgame(lst,user_ip,fdc)
            break
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gm=False
                strt_snd.play(-1) 
        pygame.display.update()
men()

