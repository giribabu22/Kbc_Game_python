from random import randrange
from colorama import Fore, Back, Style
import pyttsx3 

engine = pyttsx3.init()
engine.setProperty("rate", 120)

print(''' TV Show Kaun Banega Crorepati(KBC)
                      wel come to KBC Game show ''')                

questions =[':The International Literacy Day is observed on ?',
            ': The language of Lakshadweep. a Union Territory of India, is ?',
            ':In which group of places the Kumbha Mela is held every twelve years?',
            ':Bahubali festival is related to',
            ':Which day is observed as the World Standards  Day?',
            ':Which of the following was the theme of the World Red Cross and Red Crescent Day?',
            ':September 27 is celebrated every year as ?',':Who is the author of Manas Ka-Hans ?',
            ':The death anniversary of which of the following leaders is observed as Martyrs Day ?',
            ':Who is the author of the epic Meghdoot"?']

options = [['1.Sep 8 ', '2.Nov 28  ' ,'3.May 2 ' ,'4.Sep 22 ' ,' '],
           ['1. Tamil' ,'2.Hindi' ,'3.Malayalam' ,'4.Telugu ' ,' '],
           ['1.Ujjain.Purl.Prayag.Haridwar' ,'2.Prayag.Haridwar,Ujjain,Nasik     ' ,'3.Rameshwaram. Purl, Badrinath. Dwarika   ' ,'4.Chittakoot,Ujjain,Prayag,Haridwar',' ',' '],
           ['1.Islam ' ,'2.Hinduism     ' ,'3.Buddhism    ' ,'4.Jainism ' ,' '],
           ['1,June 26 ' ,'2,Oct 14    ' ,'3,Nov 15    ' ,'4,Dec 2  ' ,' '],
           ['1,Dignity for all-focus on women ' ,'2,Dignity for all-focus on Children' ,'3,Focus on health for all ' ,'4,Nourishment for all-focus on children ' ,' '],
           ["1,Teachers' Day ","2,National Integration Day  ","3,World Tourism Day    ","4,International Literacy Day  "," "],
           [" 1,Khushwant Singh "," 2,Prem Chand    "," 3,Jayashankar Prasad    "," 4,Amrit Lal Nagar   "," "],
           ["1,Smt. Indira Gandhi  ","2,PI. Jawaharlal Nehru  ","3,Mahatma Oandhi  ","4,Lal Bahadur Shastri   "," "],
           ["1,Vishakadatta    ","2,Valmiki    ","3,Banabhatta    ","4,Kalidas   ","  "] ] 

helpline_options = [['1.Sep 8 ','2.Nov 28 ', ],['1.Telugu  ','2.Malayalam'],
                    ['1.Ujjain.Purl.Prayag. Haridwar','2.Prayag.Haridwar,Ujjain,Nasik'],
                    ['1.Jainism ','2,Hinduism'],['1,June 26','2,Oct 14'],
                    ['1,Dignity for all-focus on Children ','2.Dignity for all - focus on women'],
                    ["1,Teachers' Day  ","2,World Tourism Day"],
                    ["1,Amrit Lal Nagar   ","2,Khushwant Singh"],["1,Smt. Indira Gandhi  ","2,Mahatma Oandhi"],
                    ["1,Banabhatta ","2,Kalidas"] ] 

helpline,amount=[') 50:50',') phone call',') skip',') audience poll'],['0','100','200','300','400','500','600','700','800','900']
answers,hepline=[1,3,2,4,2,2,3,4,3,4],[1,2,2,1,2,1,2,1,2,2]
h,qust,h_len,add_add,a,help,option,qust,hpl_num,ame=1,1,10,8,0,0,0,1,0,0
normal_lis=[]

while a < h_len:
    for numbers_normal in range(len(questions)):
        if len(normal_lis) < add_add and amount[-1] != 800:
            rgn=randrange(0,8)
            while h > 0:
                a1 = randrange(1,101)
                a2 = randrange(1,101)
                a3 = randrange(1,101)
                a4 = randrange(1,101)
                if a1 + a2 + a3 + a4 == 100:break
                else:h += 1
            if rgn not in normal_lis:
                normal_lis.append(rgn)
                aud_poll=randrange(1,4)
                que=questions[rgn]
                print(Fore.LIGHTRED_EX,qust,que,'\n','\033[0m')
                engine.say(que)
                engine.runAndWait()
                for op in options[rgn]:
                    print(Fore.GREEN+'\t',op,Style.RESET_ALL)
                    #engine.say(op)
                    #engine.runAndWait()
                if len(helpline)!=0:
                    print('\033[100m',"press '5' to take lifeline\n"'you have left',len(helpline),'lifeline play carefully','\033[0m')
                    engine.say("press '5' to take lifeline  ok  play carefully")
                    engine.runAndWait()
                ans =int(input('\nenter the Answer :'))
                if ans == answers[rgn]:
                    ame+=1
                    qust+=1 
                    engine.say('your answer is correct  you wine amount     next question')
                    engine.runAndWait() 
                    print('\033[33m', 'your answer is correct you wine ',amount[ame],'\n','\033[0m')
                elif   ans==5:
                    engine.say('YOU SELECTed the  lifeline')
                    for hp in helpline:
                        hpl_num+=1
                        print('\033[33m',hpl_num,hp,'\033[0m')
                        engine.say(hp)
                        engine.runAndWait()
                    hpl_num=0
                    h=int(input('\nwhat is your helpline :'))
                    h=h-1
                    pr=helpline[h]
                    if pr == ') 50:50':
                        helpline.remove(') 50:50')
                        print(Fore.LIGHTRED_EX,qust,que,Style.RESET_ALL)
                        for hepop in helpline_options[rgn]:print(Fore.BLUE+'\t',hepop,Style.RESET_ALL)
                        hel_op=int(input('\n enter the answer :'))
                        if hepline[rgn]==hel_op:
                            ame+=1 
                            qust+=1 
                            engine.say('your answer is correct ✓ you wine amount     next question')
                            engine.runAndWait() 
                            print('\033[33m','your answer is correct ✓ you wine ',amount[ame],'\033[0m',)
                        else:
                            engine.say('hoo your answer is wrong try again  ')
                            engine.runAndWait() 
                            print(Fore.RED+'wrong you lose !!\n ',Fore.LIGHTYELLOW_EX+' you wine this amount ',amount[ame],'',Style.RESET_ALL)
                            ch_y=input('if you want to play again y/n :')
                            if ch_y=='y':h,qust,h_len,add_add,a,help,option,qust,hpl_num,ame,helpline,normal_lis=1,1,10,8,0,0,0,1,0,0,[') 50:50',') phone call',') skip',') audience poll'],[]
                            else:
                                a=100
                                break     
                    elif pr==') phone call':
                        helpline.remove(') phone call')
                        hp=int(input('phone call 1) girlfrend  2)mom :'))
                        if hp == 1:
                            print('your girlfrend is saying ',hepline[option])
                            print('\033[70m',qust,que,'\n','\033[0m')
                            for momop in options[rgn]:print('\t',momop)
                            hel_op=int(input('enter the answer :'))
                            if hel_op == answers[rgn]:
                                ame+=1
                                qust+=1
                                engine.say('your answer is correct ✓ you wine amount      next question')
                                engine.runAndWait()  
                                print(Fore.LIGHTYELLOW_EX+'your answer is correct ✓ you wine ',amount[ame])
                            else:
                                engine.say('hoo your answer is wrong try again  ')
                                engine.runAndWait() 
                                print(Fore.RED+'wrong you lose !!\n ',Fore.LIGHTYELLOW_EX+' you wine this amount ',amount[ame],'$$',Style.RESET_ALL)
                                ch_y=input('if you want to play again y/n :')
                                if ch_y=='y':h,qust,h_len,add_add,a,help,option,qust,hpl_num,ame,helpline,normal_lis=1,1,10,8,0,0,0,1,0,0,[') 50:50',') phone call',') skip',') audience poll'],[]
                                else:
                                    a=100
                                    break  
                        elif hp ==2:
                            print('your mom is saying',answers[rgn])
                            print(qust,que,'\n')
                            for momop in options[rgn]:print('\t',momop)
                            hel_op=int(input('enter the answer :'))
                            if hel_op == answers[rgn]:
                                ame+=1
                                qust+=1
                                engine.say('your answer is correct ✓ you wine amount     next question')
                                engine.runAndWait()  
                                print(Fore.LIGHTYELLOW_EX+'your answer is correct ✓ you wine ',amount[ame],Style.RESET_ALL)
                            else:
                                engine.say('hoo your answer is wrong try again  ')
                                engine.runAndWait() 
                                print(Fore.RED+'wrong you lose !!\n ',Fore.LIGHTYELLOW_EX+' you wine this amount ',amount[ame],'$$',Style.RESET_ALL)
                                ch_y=input('if you want to play again y/n :')
                                if ch_y=='y':h,qust,h_len,add_add,a,help,option,qust,hpl_num,ame,helpline,normal_lis=1,1,10,8,0,0,0,1,0,0,[') 50:50',') phone call',') skip',') audience poll'],[]
                                else:
                                    a=100
                                    break  
                    elif pr==') skip':
                        add_add+=1
                        helpline.remove(") skip")
                        print('chainging the question ')
                        rgn+=1
                        resp=questions[len(questions)-1]
                        print(que[rgn],questions[0])
                        if questions[rgn] == questions[0]:
                            print(qust,questions[0])
                            for op in options[0]:print('\t',op)
                            pol=int(input('\n enter the answer :'))
                            if answers[0]== pol:
                                ame+=1
                                engine.say('your answer is correct ✓ you wine amount     next question')
                                engine.runAndWait() 
                                print(Fore.LIGHTYELLOW_EX+'your answer is correct ✓ you wine ',amount[ame],Style.RESET_ALL)
                                normal_lis.append(0)
                                qust+=1 
                            else:
                                engine.say('hoo your answer is wrong try again  ')
                                engine.runAndWait() 
                                print(Fore.RED+'wrong you lose !!\n ',Fore.LIGHTYELLOW_EX+' you wine this amount ',amount[ame],'$$','',Style.RESET_ALL)
                                ch_y=input('if you want to play again y/n :')
                                if ch_y=='y':h,qust,h_len,add_add,a,help,option,qust,hpl_num,ame,helpline,normal_lis=1,1,10,8,0,0,0,1,0,0,[') 50:50',') phone call',') skip',') audience poll'],[]
                                else:
                                    a=100
                                    break 
                        if questions[rgn]!=questions[0]:
                            print('\n',qust,questions[9],'\n')
                            for op in options[9]:print('\t',op)
                            pol=int(input('\n enter the answer :'))
                            if answers[9]== pol:
                                ame+=1
                                engine.say('your answer is correct ✓ you wine amount     next question')
                                engine.runAndWait() 
                                print(Fore.LIGHTYELLOW_EX+'your answer is correct ✓ you wine ',amount[ame],Style.RESET_ALL)
                                normal_lis.append(0)
                                qust+=1 
                            else:
                                engine.say('hoo your answer is wrong try again  ')
                                engine.runAndWait()
                                print(Fore.RED+'wrong you lose !!\n ',Fore.LIGHTYELLOW_EX+' you wine this amount ',amount[ame],'$$','',Style.RESET_ALL)
                                ch_y=input('if you want to play again y/n :')
                                if ch_y=='y':h,qust,h_len,add_add,a,help,option,qust,hpl_num,ame,helpline,normal_lis=1,1,10,8,0,0,0,1,0,0,[') 50:50',') phone call',') skip',') audience poll'],[]
                                else:
                                    a=100
                                    break 
                    elif pr==') audience poll':
                            helpline.remove(') audience poll') 
                            print(Fore.MAGENTA+'audience answer A is',a1,'%','\naudience answer B is',a2,'%','\nAudience answer C is',a3,'%','\nAudience answer D is',a4,'%',Style.RESET_ALL)             
                            print(Fore.CYAN+'\n',qust,que,'\n')
                            for op in options[rgn]:print(Fore.CYAN+'\t',op,Style.RESET_ALL)
                            pol=int(input('\n enter the answer :'))
                            if answers[rgn]== pol:
                                ame+=1
                                qust+=1
                                engine.say('your answer is correct ✓ you wine amount     next question')
                                engine.runAndWait() 
                                print(Fore.LIGHTYELLOW_EX+'your answer is correct ✓ you wine amount',amount[ame],Style.RESET_ALL)
                            else: 
                                engine.say('hoo your answer is wrong try again  ')
                                engine.runAndWait()
                                print(Fore.RED+'wrong you lose !!\n ',Fore.LIGHTYELLOW_EX+' you wine this amount ',amount[ame],'$$',Style.RESET_ALL)                               
                                ch_y=input('if you want to play again y/n :')
                                if ch_y=='y':h,qust,h_len,add_add,a,help,option,qust,hpl_num,ame,helpline,normal_lis=1,1,10,8,0,0,0,1,0,0,[') 50:50',') phone call',') skip',') audience poll'],[]
                                else:
                                   a=100
                                   break       
                else:
                    engine.say('hoo your answer is wrong try again ')
                    engine.runAndWait()
                    print(Fore.RED+'wrong you lose !!\n ',Fore.LIGHTYELLOW_EX+' you wine this amount ',amount[ame],'$$',Style.RESET_ALL)
                    ch_y=input('if you want to play again y/n :')                
                    if ch_y=='y':h,qust,h_len,add_add,a,help,option,qust,hpl_num,ame,helpline,normal_lis=1,1,10,8,0,0,0,1,0,0,[') 50:50',') phone call',') skip',') audience poll'],[]
                    else:
                        a=100
                        break
        else:
            print(Fore.LIGHTYELLOW_EX+'game end $$$$$')
            print('you winned the total amount',amount[ame],'$ cng you made it ',Style.RESET_ALL)
            a+=100
            break
    option+=1 
    a+=1