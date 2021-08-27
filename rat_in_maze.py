from tkinter import *
from time import *
from tkinter import messagebox
import random

but_dict={}
root = 0

def Rand_Maze():
    global but_dict
    global root

    allowed = list(range(17,30)) + list(range(32,45)) + list(range(47,60)) + list(range(62,75)) + list(range(77,90))+list(range(92,105))+list(range(107,120)) + list(range(122,135)) + list(range(137,150)) + list(range(152,165)) + list(range(167,180)) + list(range(182,195)) + list(range(197,210))
    #allowed = list(range(12,20))+list(range(22,30))+list(range(32,40))+list(range(42,50))+list(range(52,60))+list(range(62,70))+list(range(72,80))+list(range(82,90))
    poss = [0,1]

    for i in allowed:

        sel = random.choice(poss)

        if(sel==1):
            but_dict[i]["text"]="1"
            but_dict[i]["bg"]="black"
        else:
            but_dict[i]["text"]=chr(32)
            but_dict[i]["bg"]="SystemButtonFace"
    return

def Destroy():
    global root
    root.destroy()
    Create_Maze()
    return

def Solve_Maze():
    global but_dict
    global root
    global solve
    '''
    for i in range(1,101):
        if but_dict[i]["text"]==1 or but_dict[i]["text"]=="1":
      but_dict[i]["bg"]="black" '''

    posi=[1,15,-1,-15]
    decisions=[]
    path=[]
    Flag=True
    but_dict[16]["text"]=chr(1422)
    if but_dict[17]["text"]=="1":
        messagebox.showinfo("Result", "No Solution to the Maze")
        solve["state"]=DISABLED
        return
    head=17

    while(Flag):


        num=0
        for spot in posi:
            if but_dict[head+spot]["text"]==chr(32):
                num+=1

        path.append(head)
        if num>=2:
            decisions.append([head,num])

        for x in posi:
            if but_dict[head+x]["text"]==chr(32) :

                but_dict[head]["text"]=chr(1422)
                head+=x
                but_dict[head]["text"]=chr(1820)
                break

        else:
            if decisions==[]:
                messagebox.showinfo("Result", "No Solution to the Maze")
                solve["state"]=DISABLED
                return
            else:
                if decisions[-1][1]==0:
                    decisions.pop()
                for wrong in reversed(path):
                    if decisions==[]:
                        messagebox.showinfo("Result", "No Solution to the Maze")
                        solve["state"]=DISABLED
                        return
                    elif wrong==decisions[-1][0]:
                        break
                    but_dict[wrong]["text"]=chr(935)
                    but_dict[wrong]["bg"]="red"
                    path.pop()
                    root.update()
                    sleep(0.1)

                decisions[-1][1]-=1
                head=decisions[-1][0]


        sleep(0.25)
        root.update()

        if(head==210):

            but_dict[16]["bg"]="green"
            but_dict[210]["bg"]="green"
            for i in path:
                but_dict[i]["bg"]="green"
            messagebox.showinfo("Result","Solution path has been discovered")
            solve["state"]=DISABLED

            break


def Check(ID):
    global but_dict
    global root
    if(ID in range(16) or ID in range(16,226,15) or ID in range(210,226) or ID in range(30,226,15)):
        return
    if(but_dict[ID]["text"]=="1" or but_dict[ID]["text"]==1):
        but_dict[ID]["text"]=chr(32)
        but_dict[ID]["bg"]="SystemButtonFace"

    else:
        but_dict[ID]["text"]="1"
        but_dict[ID]["bg"]="black"
    return

def Create_Maze():
    global but_dict
    global root

    root = Tk()
    root.title("Vizualiser of Backtracking")
    #Frame for the grid of 15x15 maze
    grid_frame = Frame(root)
    grid_frame.pack()

    start_lab = Label(grid_frame,text="Start --> ")
    start_lab.grid(row = 2,column=1)

    but_dict[1] = Button(grid_frame,height = 1,command =lambda: Check(1), width = 3,text=1,bg="black")
    but_dict[2] = Button(grid_frame,height = 1,command =lambda: Check(2), width = 3,text=1,bg="black")
    but_dict[3] = Button(grid_frame,height = 1,command =lambda: Check(3), width = 3,text=1,bg="black")
    but_dict[4] = Button(grid_frame,height = 1,command =lambda: Check(4), width = 3,text=1,bg="black")
    but_dict[5] = Button(grid_frame,height = 1,command =lambda: Check(5), width = 3,text=1,bg="black")
    but_dict[6] = Button(grid_frame,height = 1,command =lambda: Check(6), width = 3,text=1,bg="black")
    but_dict[7] = Button(grid_frame,height = 1,command =lambda: Check(7), width = 3,text=1,bg="black")
    but_dict[8] = Button(grid_frame,height = 1,command =lambda: Check(8), width = 3,text=1,bg="black")
    but_dict[9] = Button(grid_frame,height = 1,command =lambda: Check(9), width = 3,text=1,bg="black")
    but_dict[10] = Button(grid_frame,height = 1,command =lambda: Check(10), width = 3,text=1,bg="black")
    but_dict[11] = Button(grid_frame,height = 1,command =lambda: Check(11), width = 3,text=1,bg="black")
    but_dict[12] = Button(grid_frame,height = 1,command =lambda: Check(12), width = 3,text=1,bg="black")
    but_dict[13] = Button(grid_frame,height = 1,command =lambda: Check(13), width = 3,text=1,bg="black")
    but_dict[14] = Button(grid_frame,height = 1,command =lambda: Check(14), width = 3,text=1,bg="black")
    but_dict[15] = Button(grid_frame,height = 1,command =lambda: Check(15), width = 3,text=1,bg="black")
    but_dict[16] = Button(grid_frame,height = 1,command =lambda: Check(16), width = 3,text=chr(32))
    but_dict[17]= Button(grid_frame,height = 1,command =lambda: Check(17), width = 3,text=chr(32))
    but_dict[18]= Button(grid_frame,height = 1,command =lambda: Check(18), width = 3,text=chr(32))
    but_dict[19]= Button(grid_frame,height = 1,command =lambda: Check(19), width = 3,text=chr(32))
    but_dict[20]= Button(grid_frame,height = 1,command =lambda: Check(20), width = 3,text=chr(32))
    but_dict[21]= Button(grid_frame,height = 1,command =lambda: Check(21), width = 3,text=chr(32))
    but_dict[22]= Button(grid_frame,height = 1,command =lambda: Check(22), width = 3,text=chr(32))
    but_dict[23]= Button(grid_frame,height = 1,command =lambda: Check(23), width = 3,text=chr(32))
    but_dict[24]= Button(grid_frame,height = 1,command =lambda: Check(24), width = 3,text=chr(32))
    but_dict[25]= Button(grid_frame,height = 1,command =lambda: Check(25), width = 3,text=chr(32))
    but_dict[26]= Button(grid_frame,height = 1,command =lambda: Check(26), width = 3,text=chr(32))
    but_dict[27]= Button(grid_frame,height = 1,command =lambda: Check(27), width = 3,text=chr(32))
    but_dict[28]= Button(grid_frame,height = 1,command =lambda: Check(28), width = 3,text=chr(32))
    but_dict[29]= Button(grid_frame,height = 1,command =lambda: Check(29), width = 3,text=chr(32))
    but_dict[30] = Button(grid_frame,height = 1,command =lambda: Check(30), width = 3,text=1,bg="black")
    but_dict[31] = Button(grid_frame,height = 1,command =lambda: Check(31), width = 3,text=1,bg="black")
    but_dict[32]= Button(grid_frame,height = 1,command =lambda: Check(32), width = 3,text=chr(32))
    but_dict[33]= Button(grid_frame,height = 1,command =lambda: Check(33), width = 3,text=chr(32))
    but_dict[34]= Button(grid_frame,height = 1,command =lambda: Check(34), width = 3,text=chr(32))
    but_dict[35]= Button(grid_frame,height = 1,command =lambda: Check(35), width = 3,text=chr(32))
    but_dict[36]= Button(grid_frame,height = 1,command =lambda: Check(36), width = 3,text=chr(32))
    but_dict[37]= Button(grid_frame,height = 1,command =lambda: Check(37), width = 3,text=chr(32))
    but_dict[38]= Button(grid_frame,height = 1,command =lambda: Check(38), width = 3,text=chr(32))
    but_dict[39]= Button(grid_frame,height = 1,command =lambda: Check(39), width = 3,text=chr(32))
    but_dict[40]= Button(grid_frame,height = 1,command =lambda: Check(40), width = 3,text=chr(32))
    but_dict[41]= Button(grid_frame,height = 1,command =lambda: Check(41), width = 3,text=chr(32))
    but_dict[42]= Button(grid_frame,height = 1,command =lambda: Check(42), width = 3,text=chr(32))
    but_dict[43]= Button(grid_frame,height = 1,command =lambda: Check(43), width = 3,text=chr(32))
    but_dict[44]= Button(grid_frame,height = 1,command =lambda: Check(44), width = 3,text=chr(32))
    but_dict[45] = Button(grid_frame,height = 1,command =lambda: Check(45), width = 3,text=1,bg="black")
    but_dict[46] = Button(grid_frame,height = 1,command =lambda: Check(46), width = 3,text=1,bg="black")
    but_dict[47]= Button(grid_frame,height = 1,command =lambda: Check(47), width = 3,text=chr(32))
    but_dict[48]= Button(grid_frame,height = 1,command =lambda: Check(48), width = 3,text=chr(32))
    but_dict[49]= Button(grid_frame,height = 1,command =lambda: Check(49), width = 3,text=chr(32))
    but_dict[50]= Button(grid_frame,height = 1,command =lambda: Check(50), width = 3,text=chr(32))
    but_dict[51]= Button(grid_frame,height = 1,command =lambda: Check(51), width = 3,text=chr(32))
    but_dict[52]= Button(grid_frame,height = 1,command =lambda: Check(52), width = 3,text=chr(32))
    but_dict[53]= Button(grid_frame,height = 1,command =lambda: Check(53), width = 3,text=chr(32))
    but_dict[54]= Button(grid_frame,height = 1,command =lambda: Check(54), width = 3,text=chr(32))
    but_dict[55]= Button(grid_frame,height = 1,command =lambda: Check(55), width = 3,text=chr(32))
    but_dict[56]= Button(grid_frame,height = 1,command =lambda: Check(56), width = 3,text=chr(32))
    but_dict[57]= Button(grid_frame,height = 1,command =lambda: Check(57), width = 3,text=chr(32))
    but_dict[58]= Button(grid_frame,height = 1,command =lambda: Check(58), width = 3,text=chr(32))
    but_dict[59]= Button(grid_frame,height = 1,command =lambda: Check(59), width = 3,text=chr(32))
    but_dict[60] = Button(grid_frame,height = 1,command =lambda: Check(60), width = 3,text=1,bg="black")
    but_dict[61] = Button(grid_frame,height = 1,command =lambda: Check(61), width = 3,text=1,bg="black")
    but_dict[62]= Button(grid_frame,height = 1,command =lambda: Check(62), width = 3,text=chr(32))
    but_dict[63]= Button(grid_frame,height = 1,command =lambda: Check(63), width = 3,text=chr(32))
    but_dict[64]= Button(grid_frame,height = 1,command =lambda: Check(64), width = 3,text=chr(32))
    but_dict[65]= Button(grid_frame,height = 1,command =lambda: Check(65), width = 3,text=chr(32))
    but_dict[66]= Button(grid_frame,height = 1,command =lambda: Check(66), width = 3,text=chr(32))
    but_dict[67]= Button(grid_frame,height = 1,command =lambda: Check(67), width = 3,text=chr(32))
    but_dict[68]= Button(grid_frame,height = 1,command =lambda: Check(68), width = 3,text=chr(32))
    but_dict[69]= Button(grid_frame,height = 1,command =lambda: Check(69), width = 3,text=chr(32))
    but_dict[70]= Button(grid_frame,height = 1,command =lambda: Check(70), width = 3,text=chr(32))
    but_dict[71]= Button(grid_frame,height = 1,command =lambda: Check(71), width = 3,text=chr(32))
    but_dict[72]= Button(grid_frame,height = 1,command =lambda: Check(72), width = 3,text=chr(32))
    but_dict[73]= Button(grid_frame,height = 1,command =lambda: Check(73), width = 3,text=chr(32))
    but_dict[74]= Button(grid_frame,height = 1,command =lambda: Check(74), width = 3,text=chr(32))
    but_dict[75] = Button(grid_frame,height = 1,command =lambda: Check(75), width = 3,text=1,bg="black")
    but_dict[76] = Button(grid_frame,height = 1,command =lambda: Check(76), width = 3,text=1,bg="black")
    but_dict[77]= Button(grid_frame,height = 1,command =lambda: Check(77), width = 3,text=chr(32))
    but_dict[78]= Button(grid_frame,height = 1,command =lambda: Check(78), width = 3,text=chr(32))
    but_dict[79]= Button(grid_frame,height = 1,command =lambda: Check(79), width = 3,text=chr(32))
    but_dict[80]= Button(grid_frame,height = 1,command =lambda: Check(80), width = 3,text=chr(32))
    but_dict[81]= Button(grid_frame,height = 1,command =lambda: Check(81), width = 3,text=chr(32))
    but_dict[82]= Button(grid_frame,height = 1,command =lambda: Check(82), width = 3,text=chr(32))
    but_dict[83]= Button(grid_frame,height = 1,command =lambda: Check(83), width = 3,text=chr(32))
    but_dict[84]= Button(grid_frame,height = 1,command =lambda: Check(84), width = 3,text=chr(32))
    but_dict[85]= Button(grid_frame,height = 1,command =lambda: Check(85), width = 3,text=chr(32))
    but_dict[86]= Button(grid_frame,height = 1,command =lambda: Check(86), width = 3,text=chr(32))
    but_dict[87]= Button(grid_frame,height = 1,command =lambda: Check(87), width = 3,text=chr(32))
    but_dict[88]= Button(grid_frame,height = 1,command =lambda: Check(88), width = 3,text=chr(32))
    but_dict[89]= Button(grid_frame,height = 1,command =lambda: Check(89), width = 3,text=chr(32))
    but_dict[90] = Button(grid_frame,height = 1,command =lambda: Check(90), width = 3,text=1,bg="black")
    but_dict[91] = Button(grid_frame,height = 1,command =lambda: Check(91), width = 3,text=1,bg="black")
    but_dict[92]= Button(grid_frame,height = 1,command =lambda: Check(92), width = 3,text=chr(32))
    but_dict[93]= Button(grid_frame,height = 1,command =lambda: Check(93), width = 3,text=chr(32))
    but_dict[94]= Button(grid_frame,height = 1,command =lambda: Check(94), width = 3,text=chr(32))
    but_dict[95]= Button(grid_frame,height = 1,command =lambda: Check(95), width = 3,text=chr(32))
    but_dict[96]= Button(grid_frame,height = 1,command =lambda: Check(96), width = 3,text=chr(32))
    but_dict[97]= Button(grid_frame,height = 1,command =lambda: Check(97), width = 3,text=chr(32))
    but_dict[98]= Button(grid_frame,height = 1,command =lambda: Check(98), width = 3,text=chr(32))
    but_dict[99]= Button(grid_frame,height = 1,command =lambda: Check(99), width = 3,text=chr(32))
    but_dict[100]= Button(grid_frame,height = 1,command =lambda: Check(100), width = 3,text=chr(32))
    but_dict[101]= Button(grid_frame,height = 1,command =lambda: Check(101), width = 3,text=chr(32))
    but_dict[102]= Button(grid_frame,height = 1,command =lambda: Check(102), width = 3,text=chr(32))
    but_dict[103]= Button(grid_frame,height = 1,command =lambda: Check(103), width = 3,text=chr(32))
    but_dict[104]= Button(grid_frame,height = 1,command =lambda: Check(104), width = 3,text=chr(32))
    but_dict[105] = Button(grid_frame,height = 1,command =lambda: Check(105), width = 3,text=1,bg="black")
    but_dict[106] = Button(grid_frame,height = 1,command =lambda: Check(106), width = 3,text=1,bg="black")
    but_dict[107]= Button(grid_frame,height = 1,command =lambda: Check(107), width = 3,text=chr(32))
    but_dict[108]= Button(grid_frame,height = 1,command =lambda: Check(108), width = 3,text=chr(32))
    but_dict[109]= Button(grid_frame,height = 1,command =lambda: Check(109), width = 3,text=chr(32))
    but_dict[110]= Button(grid_frame,height = 1,command =lambda: Check(110), width = 3,text=chr(32))
    but_dict[111]= Button(grid_frame,height = 1,command =lambda: Check(111), width = 3,text=chr(32))
    but_dict[112]= Button(grid_frame,height = 1,command =lambda: Check(112), width = 3,text=chr(32))
    but_dict[113]= Button(grid_frame,height = 1,command =lambda: Check(113), width = 3,text=chr(32))
    but_dict[114]= Button(grid_frame,height = 1,command =lambda: Check(114), width = 3,text=chr(32))
    but_dict[115]= Button(grid_frame,height = 1,command =lambda: Check(115), width = 3,text=chr(32))
    but_dict[116]= Button(grid_frame,height = 1,command =lambda: Check(116), width = 3,text=chr(32))
    but_dict[117]= Button(grid_frame,height = 1,command =lambda: Check(117), width = 3,text=chr(32))
    but_dict[118]= Button(grid_frame,height = 1,command =lambda: Check(118), width = 3,text=chr(32))
    but_dict[119]= Button(grid_frame,height = 1,command =lambda: Check(119), width = 3,text=chr(32))
    but_dict[120] = Button(grid_frame,height = 1,command =lambda: Check(120), width = 3,text=1,bg="black")
    but_dict[121] = Button(grid_frame,height = 1,command =lambda: Check(121), width = 3,text=1,bg="black")
    but_dict[122]= Button(grid_frame,height = 1,command =lambda: Check(122), width = 3,text=chr(32))
    but_dict[123]= Button(grid_frame,height = 1,command =lambda: Check(123), width = 3,text=chr(32))
    but_dict[124]= Button(grid_frame,height = 1,command =lambda: Check(124), width = 3,text=chr(32))
    but_dict[125]= Button(grid_frame,height = 1,command =lambda: Check(125), width = 3,text=chr(32))
    but_dict[126]= Button(grid_frame,height = 1,command =lambda: Check(126), width = 3,text=chr(32))
    but_dict[127]= Button(grid_frame,height = 1,command =lambda: Check(127), width = 3,text=chr(32))
    but_dict[128]= Button(grid_frame,height = 1,command =lambda: Check(128), width = 3,text=chr(32))
    but_dict[129]= Button(grid_frame,height = 1,command =lambda: Check(129), width = 3,text=chr(32))
    but_dict[130]= Button(grid_frame,height = 1,command =lambda: Check(130), width = 3,text=chr(32))
    but_dict[131]= Button(grid_frame,height = 1,command =lambda: Check(131), width = 3,text=chr(32))
    but_dict[132]= Button(grid_frame,height = 1,command =lambda: Check(132), width = 3,text=chr(32))
    but_dict[133]= Button(grid_frame,height = 1,command =lambda: Check(133), width = 3,text=chr(32))
    but_dict[134]= Button(grid_frame,height = 1,command =lambda: Check(134), width = 3,text=chr(32))
    but_dict[135] = Button(grid_frame,height = 1,command =lambda: Check(135), width = 3,text=1,bg="black")
    but_dict[136] = Button(grid_frame,height = 1,command =lambda: Check(136), width = 3,text=1,bg="black")
    but_dict[137]= Button(grid_frame,height = 1,command =lambda: Check(137), width = 3,text=chr(32))
    but_dict[138]= Button(grid_frame,height = 1,command =lambda: Check(138), width = 3,text=chr(32))
    but_dict[139]= Button(grid_frame,height = 1,command =lambda: Check(139), width = 3,text=chr(32))
    but_dict[140]= Button(grid_frame,height = 1,command =lambda: Check(140), width = 3,text=chr(32))
    but_dict[141]= Button(grid_frame,height = 1,command =lambda: Check(141), width = 3,text=chr(32))
    but_dict[142]= Button(grid_frame,height = 1,command =lambda: Check(142), width = 3,text=chr(32))
    but_dict[143]= Button(grid_frame,height = 1,command =lambda: Check(143), width = 3,text=chr(32))
    but_dict[144]= Button(grid_frame,height = 1,command =lambda: Check(144), width = 3,text=chr(32))
    but_dict[145]= Button(grid_frame,height = 1,command =lambda: Check(145), width = 3,text=chr(32))
    but_dict[146]= Button(grid_frame,height = 1,command =lambda: Check(146), width = 3,text=chr(32))
    but_dict[147]= Button(grid_frame,height = 1,command =lambda: Check(147), width = 3,text=chr(32))
    but_dict[148]= Button(grid_frame,height = 1,command =lambda: Check(148), width = 3,text=chr(32))
    but_dict[149]= Button(grid_frame,height = 1,command =lambda: Check(149), width = 3,text=chr(32))
    but_dict[150] = Button(grid_frame,height = 1,command =lambda: Check(150), width = 3,text=1,bg="black")
    but_dict[151] = Button(grid_frame,height = 1,command =lambda: Check(151), width = 3,text=1,bg="black")
    but_dict[152]= Button(grid_frame,height = 1,command =lambda: Check(152), width = 3,text=chr(32))
    but_dict[153]= Button(grid_frame,height = 1,command =lambda: Check(153), width = 3,text=chr(32))
    but_dict[154]= Button(grid_frame,height = 1,command =lambda: Check(154), width = 3,text=chr(32))
    but_dict[155]= Button(grid_frame,height = 1,command =lambda: Check(155), width = 3,text=chr(32))
    but_dict[156]= Button(grid_frame,height = 1,command =lambda: Check(156), width = 3,text=chr(32))
    but_dict[157]= Button(grid_frame,height = 1,command =lambda: Check(157), width = 3,text=chr(32))
    but_dict[158]= Button(grid_frame,height = 1,command =lambda: Check(158), width = 3,text=chr(32))
    but_dict[159]= Button(grid_frame,height = 1,command =lambda: Check(159), width = 3,text=chr(32))
    but_dict[160]= Button(grid_frame,height = 1,command =lambda: Check(160), width = 3,text=chr(32))
    but_dict[161]= Button(grid_frame,height = 1,command =lambda: Check(161), width = 3,text=chr(32))
    but_dict[162]= Button(grid_frame,height = 1,command =lambda: Check(162), width = 3,text=chr(32))
    but_dict[163]= Button(grid_frame,height = 1,command =lambda: Check(163), width = 3,text=chr(32))
    but_dict[164]= Button(grid_frame,height = 1,command =lambda: Check(164), width = 3,text=chr(32))
    but_dict[165] = Button(grid_frame,height = 1,command =lambda: Check(165), width = 3,text=1,bg="black")
    but_dict[166] = Button(grid_frame,height = 1,command =lambda: Check(166), width = 3,text=1,bg="black")
    but_dict[167]= Button(grid_frame,height = 1,command =lambda: Check(167), width = 3,text=chr(32))
    but_dict[168]= Button(grid_frame,height = 1,command =lambda: Check(168), width = 3,text=chr(32))
    but_dict[169]= Button(grid_frame,height = 1,command =lambda: Check(169), width = 3,text=chr(32))
    but_dict[170]= Button(grid_frame,height = 1,command =lambda: Check(170), width = 3,text=chr(32))
    but_dict[171]= Button(grid_frame,height = 1,command =lambda: Check(171), width = 3,text=chr(32))
    but_dict[172]= Button(grid_frame,height = 1,command =lambda: Check(172), width = 3,text=chr(32))
    but_dict[173]= Button(grid_frame,height = 1,command =lambda: Check(173), width = 3,text=chr(32))
    but_dict[174]= Button(grid_frame,height = 1,command =lambda: Check(174), width = 3,text=chr(32))
    but_dict[175]= Button(grid_frame,height = 1,command =lambda: Check(175), width = 3,text=chr(32))
    but_dict[176]= Button(grid_frame,height = 1,command =lambda: Check(176), width = 3,text=chr(32))
    but_dict[177]= Button(grid_frame,height = 1,command =lambda: Check(177), width = 3,text=chr(32))
    but_dict[178]= Button(grid_frame,height = 1,command =lambda: Check(178), width = 3,text=chr(32))
    but_dict[179]= Button(grid_frame,height = 1,command =lambda: Check(179), width = 3,text=chr(32))
    but_dict[180] = Button(grid_frame,height = 1,command =lambda: Check(180), width = 3,text=1,bg="black")
    but_dict[181] = Button(grid_frame,height = 1,command =lambda: Check(181), width = 3,text=1,bg="black")
    but_dict[182]= Button(grid_frame,height = 1,command =lambda: Check(182), width = 3,text=chr(32))
    but_dict[183]= Button(grid_frame,height = 1,command =lambda: Check(183), width = 3,text=chr(32))
    but_dict[184]= Button(grid_frame,height = 1,command =lambda: Check(184), width = 3,text=chr(32))
    but_dict[185]= Button(grid_frame,height = 1,command =lambda: Check(185), width = 3,text=chr(32))
    but_dict[186]= Button(grid_frame,height = 1,command =lambda: Check(186), width = 3,text=chr(32))
    but_dict[187]= Button(grid_frame,height = 1,command =lambda: Check(187), width = 3,text=chr(32))
    but_dict[188]= Button(grid_frame,height = 1,command =lambda: Check(188), width = 3,text=chr(32))
    but_dict[189]= Button(grid_frame,height = 1,command =lambda: Check(189), width = 3,text=chr(32))
    but_dict[190]= Button(grid_frame,height = 1,command =lambda: Check(190), width = 3,text=chr(32))
    but_dict[191]= Button(grid_frame,height = 1,command =lambda: Check(191), width = 3,text=chr(32))
    but_dict[192]= Button(grid_frame,height = 1,command =lambda: Check(192), width = 3,text=chr(32))
    but_dict[193]= Button(grid_frame,height = 1,command =lambda: Check(193), width = 3,text=chr(32))
    but_dict[194]= Button(grid_frame,height = 1,command =lambda: Check(194), width = 3,text=chr(32))
    but_dict[195] = Button(grid_frame,height = 1,command =lambda: Check(195), width = 3,text=1,bg="black")
    but_dict[196] = Button(grid_frame,height = 1,command =lambda: Check(196), width = 3,text=1,bg="black")
    but_dict[197]= Button(grid_frame,height = 1,command =lambda: Check(197), width = 3,text=chr(32))
    but_dict[198]= Button(grid_frame,height = 1,command =lambda: Check(198), width = 3,text=chr(32))
    but_dict[199]= Button(grid_frame,height = 1,command =lambda: Check(199), width = 3,text=chr(32))
    but_dict[200]= Button(grid_frame,height = 1,command =lambda: Check(200), width = 3,text=chr(32))
    but_dict[201]= Button(grid_frame,height = 1,command =lambda: Check(201), width = 3,text=chr(32))
    but_dict[202]= Button(grid_frame,height = 1,command =lambda: Check(202), width = 3,text=chr(32))
    but_dict[203]= Button(grid_frame,height = 1,command =lambda: Check(203), width = 3,text=chr(32))
    but_dict[204]= Button(grid_frame,height = 1,command =lambda: Check(204), width = 3,text=chr(32))
    but_dict[205]= Button(grid_frame,height = 1,command =lambda: Check(205), width = 3,text=chr(32))
    but_dict[206]= Button(grid_frame,height = 1,command =lambda: Check(206), width = 3,text=chr(32))
    but_dict[207]= Button(grid_frame,height = 1,command =lambda: Check(207), width = 3,text=chr(32))
    but_dict[208]= Button(grid_frame,height = 1,command =lambda: Check(208), width = 3,text=chr(32))
    but_dict[209]= Button(grid_frame,height = 1,command =lambda: Check(209), width = 3,text=chr(32))
    but_dict[210]= Button(grid_frame,height = 1,command =lambda: Check(210), width = 3,text=chr(32))
    but_dict[211]= Button(grid_frame,height = 1,command =lambda: Check(211), width = 3,text=1,bg="black")
    but_dict[212]= Button(grid_frame,height = 1,command =lambda: Check(212), width = 3,text=1,bg="black")
    but_dict[213]= Button(grid_frame,height = 1,command =lambda: Check(213), width = 3,text=1,bg="black")
    but_dict[214]= Button(grid_frame,height = 1,command =lambda: Check(214), width = 3,text=1,bg="black")
    but_dict[215]= Button(grid_frame,height = 1,command =lambda: Check(215), width = 3,text=1,bg="black")
    but_dict[216]= Button(grid_frame,height = 1,command =lambda: Check(216), width = 3,text=1,bg="black")
    but_dict[217]= Button(grid_frame,height = 1,command =lambda: Check(217), width = 3,text=1,bg="black")
    but_dict[218]= Button(grid_frame,height = 1,command =lambda: Check(218), width = 3,text=1,bg="black")
    but_dict[219]= Button(grid_frame,height = 1,command =lambda: Check(219), width = 3,text=1,bg="black")
    but_dict[220]= Button(grid_frame,height = 1,command =lambda: Check(220), width = 3,text=1,bg="black")
    but_dict[221]= Button(grid_frame,height = 1,command =lambda: Check(221), width = 3,text=1,bg="black")
    but_dict[222]= Button(grid_frame,height = 1,command =lambda: Check(222), width = 3,text=1,bg="black")
    but_dict[223]= Button(grid_frame,height = 1,command =lambda: Check(223), width = 3,text=1,bg="black")
    but_dict[224]= Button(grid_frame,height = 1,command =lambda: Check(224), width = 3,text=1,bg="black")
    but_dict[225]= Button(grid_frame,height = 1,command =lambda: Check(225), width = 3,text=1,bg="black")
    but_dict[1].grid(row =1,column = 2 )
    but_dict[2].grid(row =1,column = 3 )
    but_dict[3].grid(row =1,column = 4 )
    but_dict[4].grid(row =1,column = 5 )
    but_dict[5].grid(row =1,column = 6 )
    but_dict[6].grid(row =1,column = 7 )
    but_dict[7].grid(row =1,column = 8 )
    but_dict[8].grid(row =1,column = 9 )
    but_dict[9].grid(row =1,column = 10 )
    but_dict[10].grid(row =1,column = 11 )
    but_dict[11].grid(row =1,column = 12 )
    but_dict[12].grid(row =1,column = 13 )
    but_dict[13].grid(row =1,column = 14 )
    but_dict[14].grid(row =1,column = 15 )
    but_dict[15].grid(row =1,column = 16 )
    but_dict[16].grid(row =2,column = 2 )
    but_dict[17].grid(row =2,column = 3 )
    but_dict[18].grid(row =2,column = 4 )
    but_dict[19].grid(row =2,column = 5 )
    but_dict[20].grid(row =2,column = 6 )
    but_dict[21].grid(row =2,column = 7 )
    but_dict[22].grid(row =2,column = 8 )
    but_dict[23].grid(row =2,column = 9 )
    but_dict[24].grid(row =2,column = 10 )
    but_dict[25].grid(row =2,column = 11 )
    but_dict[26].grid(row =2,column = 12 )
    but_dict[27].grid(row =2,column = 13 )
    but_dict[28].grid(row =2,column = 14 )
    but_dict[29].grid(row =2,column = 15 )
    but_dict[30].grid(row =2,column = 16 )
    but_dict[31].grid(row =3,column = 2 )
    but_dict[32].grid(row =3,column = 3 )
    but_dict[33].grid(row =3,column = 4 )
    but_dict[34].grid(row =3,column = 5 )
    but_dict[35].grid(row =3,column = 6 )
    but_dict[36].grid(row =3,column = 7 )
    but_dict[37].grid(row =3,column = 8 )
    but_dict[38].grid(row =3,column = 9 )
    but_dict[39].grid(row =3,column = 10 )
    but_dict[40].grid(row =3,column = 11 )
    but_dict[41].grid(row =3,column = 12 )
    but_dict[42].grid(row =3,column = 13 )
    but_dict[43].grid(row =3,column = 14 )
    but_dict[44].grid(row =3,column = 15 )
    but_dict[45].grid(row =3,column = 16 )
    but_dict[46].grid(row =4,column = 2 )
    but_dict[47].grid(row =4,column = 3 )
    but_dict[48].grid(row =4,column = 4 )
    but_dict[49].grid(row =4,column = 5 )
    but_dict[50].grid(row =4,column = 6 )
    but_dict[51].grid(row =4,column = 7 )
    but_dict[52].grid(row =4,column = 8 )
    but_dict[53].grid(row =4,column = 9 )
    but_dict[54].grid(row =4,column = 10 )
    but_dict[55].grid(row =4,column = 11 )
    but_dict[56].grid(row =4,column = 12 )
    but_dict[57].grid(row =4,column = 13 )
    but_dict[58].grid(row =4,column = 14 )
    but_dict[59].grid(row =4,column = 15 )
    but_dict[60].grid(row =4,column = 16 )
    but_dict[61].grid(row =5,column = 2 )
    but_dict[62].grid(row =5,column = 3 )
    but_dict[63].grid(row =5,column = 4 )
    but_dict[64].grid(row =5,column = 5 )
    but_dict[65].grid(row =5,column = 6 )
    but_dict[66].grid(row =5,column = 7 )
    but_dict[67].grid(row =5,column = 8 )
    but_dict[68].grid(row =5,column = 9 )
    but_dict[69].grid(row =5,column = 10 )
    but_dict[70].grid(row =5,column = 11 )
    but_dict[71].grid(row =5,column = 12 )
    but_dict[72].grid(row =5,column = 13 )
    but_dict[73].grid(row =5,column = 14 )
    but_dict[74].grid(row =5,column = 15 )
    but_dict[75].grid(row =5,column = 16 )
    but_dict[76].grid(row =6,column = 2 )
    but_dict[77].grid(row =6,column = 3 )
    but_dict[78].grid(row =6,column = 4 )
    but_dict[79].grid(row =6,column = 5 )
    but_dict[80].grid(row =6,column = 6 )
    but_dict[81].grid(row =6,column = 7 )
    but_dict[82].grid(row =6,column = 8 )
    but_dict[83].grid(row =6,column = 9 )
    but_dict[84].grid(row =6,column = 10 )
    but_dict[85].grid(row =6,column = 11 )
    but_dict[86].grid(row =6,column = 12 )
    but_dict[87].grid(row =6,column = 13 )
    but_dict[88].grid(row =6,column = 14 )
    but_dict[89].grid(row =6,column = 15 )
    but_dict[90].grid(row =6,column = 16 )
    but_dict[91].grid(row =7,column = 2 )
    but_dict[92].grid(row =7,column = 3 )
    but_dict[93].grid(row =7,column = 4 )
    but_dict[94].grid(row =7,column = 5 )
    but_dict[95].grid(row =7,column = 6 )
    but_dict[96].grid(row =7,column = 7 )
    but_dict[97].grid(row =7,column = 8 )
    but_dict[98].grid(row =7,column = 9 )
    but_dict[99].grid(row =7,column = 10 )
    but_dict[100].grid(row =7,column = 11 )
    but_dict[101].grid(row =7,column = 12 )
    but_dict[102].grid(row =7,column = 13 )
    but_dict[103].grid(row =7,column = 14 )
    but_dict[104].grid(row =7,column = 15 )
    but_dict[105].grid(row =7,column = 16 )
    but_dict[106].grid(row =8,column = 2 )
    but_dict[107].grid(row =8,column = 3 )
    but_dict[108].grid(row =8,column = 4 )
    but_dict[109].grid(row =8,column = 5 )
    but_dict[110].grid(row =8,column = 6 )
    but_dict[111].grid(row =8,column = 7 )
    but_dict[112].grid(row =8,column = 8 )
    but_dict[113].grid(row =8,column = 9 )
    but_dict[114].grid(row =8,column = 10 )
    but_dict[115].grid(row =8,column = 11 )
    but_dict[116].grid(row =8,column = 12 )
    but_dict[117].grid(row =8,column = 13 )
    but_dict[118].grid(row =8,column = 14 )
    but_dict[119].grid(row =8,column = 15 )
    but_dict[120].grid(row =8,column = 16 )
    but_dict[121].grid(row =9,column = 2 )
    but_dict[122].grid(row =9,column = 3 )
    but_dict[123].grid(row =9,column = 4 )
    but_dict[124].grid(row =9,column = 5 )
    but_dict[125].grid(row =9,column = 6 )
    but_dict[126].grid(row =9,column = 7 )
    but_dict[127].grid(row =9,column = 8 )
    but_dict[128].grid(row =9,column = 9 )
    but_dict[129].grid(row =9,column = 10 )
    but_dict[130].grid(row =9,column = 11 )
    but_dict[131].grid(row =9,column = 12 )
    but_dict[132].grid(row =9,column = 13 )
    but_dict[133].grid(row =9,column = 14 )
    but_dict[134].grid(row =9,column = 15 )
    but_dict[135].grid(row =9,column = 16 )
    but_dict[136].grid(row =10,column = 2 )
    but_dict[137].grid(row =10,column = 3 )
    but_dict[138].grid(row =10,column = 4 )
    but_dict[139].grid(row =10,column = 5 )
    but_dict[140].grid(row =10,column = 6 )
    but_dict[141].grid(row =10,column = 7 )
    but_dict[142].grid(row =10,column = 8 )
    but_dict[143].grid(row =10,column = 9 )
    but_dict[144].grid(row =10,column = 10 )
    but_dict[145].grid(row =10,column = 11 )
    but_dict[146].grid(row =10,column = 12 )
    but_dict[147].grid(row =10,column = 13 )
    but_dict[148].grid(row =10,column = 14 )
    but_dict[149].grid(row =10,column = 15 )
    but_dict[150].grid(row =10,column = 16 )
    but_dict[151].grid(row =11,column = 2 )
    but_dict[152].grid(row =11,column = 3 )
    but_dict[153].grid(row =11,column = 4 )
    but_dict[154].grid(row =11,column = 5 )
    but_dict[155].grid(row =11,column = 6 )
    but_dict[156].grid(row =11,column = 7 )
    but_dict[157].grid(row =11,column = 8 )
    but_dict[158].grid(row =11,column = 9 )
    but_dict[159].grid(row =11,column = 10 )
    but_dict[160].grid(row =11,column = 11 )
    but_dict[161].grid(row =11,column = 12 )
    but_dict[162].grid(row =11,column = 13 )
    but_dict[163].grid(row =11,column = 14 )
    but_dict[164].grid(row =11,column = 15 )
    but_dict[165].grid(row =11,column = 16 )
    but_dict[166].grid(row =12,column = 2 )
    but_dict[167].grid(row =12,column = 3 )
    but_dict[168].grid(row =12,column = 4 )
    but_dict[169].grid(row =12,column = 5 )
    but_dict[170].grid(row =12,column = 6 )
    but_dict[171].grid(row =12,column = 7 )
    but_dict[172].grid(row =12,column = 8 )
    but_dict[173].grid(row =12,column = 9 )
    but_dict[174].grid(row =12,column = 10 )
    but_dict[175].grid(row =12,column = 11 )
    but_dict[176].grid(row =12,column = 12 )
    but_dict[177].grid(row =12,column = 13 )
    but_dict[178].grid(row =12,column = 14 )
    but_dict[179].grid(row =12,column = 15 )
    but_dict[180].grid(row =12,column = 16 )
    but_dict[181].grid(row =13,column = 2 )
    but_dict[182].grid(row =13,column = 3 )
    but_dict[183].grid(row =13,column = 4 )
    but_dict[184].grid(row =13,column = 5 )
    but_dict[185].grid(row =13,column = 6 )
    but_dict[186].grid(row =13,column = 7 )
    but_dict[187].grid(row =13,column = 8 )
    but_dict[188].grid(row =13,column = 9 )
    but_dict[189].grid(row =13,column = 10 )
    but_dict[190].grid(row =13,column = 11 )
    but_dict[191].grid(row =13,column = 12 )
    but_dict[192].grid(row =13,column = 13 )
    but_dict[193].grid(row =13,column = 14 )
    but_dict[194].grid(row =13,column = 15 )
    but_dict[195].grid(row =13,column = 16 )
    but_dict[196].grid(row =14,column = 2 )
    but_dict[197].grid(row =14,column = 3 )
    but_dict[198].grid(row =14,column = 4 )
    but_dict[199].grid(row =14,column = 5 )
    but_dict[200].grid(row =14,column = 6 )
    but_dict[201].grid(row =14,column = 7 )
    but_dict[202].grid(row =14,column = 8 )
    but_dict[203].grid(row =14,column = 9 )
    but_dict[204].grid(row =14,column = 10 )
    but_dict[205].grid(row =14,column = 11 )
    but_dict[206].grid(row =14,column = 12 )
    but_dict[207].grid(row =14,column = 13 )
    but_dict[208].grid(row =14,column = 14 )
    but_dict[209].grid(row =14,column = 15 )
    but_dict[210].grid(row =14,column = 16 )
    but_dict[211].grid(row =15,column = 2 )
    but_dict[212].grid(row =15,column = 3 )
    but_dict[213].grid(row =15,column = 4 )
    but_dict[214].grid(row =15,column = 5 )
    but_dict[215].grid(row =15,column = 6 )
    but_dict[216].grid(row =15,column = 7 )
    but_dict[217].grid(row =15,column = 8 )
    but_dict[218].grid(row =15,column = 9 )
    but_dict[219].grid(row =15,column = 10 )
    but_dict[220].grid(row =15,column = 11 )
    but_dict[221].grid(row =15,column = 12 )
    but_dict[222].grid(row =15,column = 13 )
    but_dict[223].grid(row =15,column = 14 )
    but_dict[224].grid(row =15,column = 15 )
    but_dict[225].grid(row =15,column = 16 )

    end_lab = Label(grid_frame,text="--> End")
    end_lab.grid(row = 14,column=17)

    #Frame for the buttons
    buttons_frame = Frame(root)
    buttons_frame.pack()

    #Space Frames for the line between the grid and the buttons and the Main buttons
    space_frame1 = Frame(buttons_frame)
    space_frame2 = Frame(buttons_frame)
    space_frame1.pack(side = "top")
    space_frame2.pack(side = "bottom")


    spacer = Label(space_frame1,width=50,bg="red",text="-----------------------------")
    spacer.pack()

    randomize = Button(space_frame2,text="Create New Maze",command=Destroy)
    randomize.grid(row=1,column=1)

    global solve
    solve = Button(space_frame2,text="Solve The Maze",command = Solve_Maze)
    solve.grid(row=1,column=2)


    Rand_Maze()
    root.mainloop()
    return

Create_Maze()

