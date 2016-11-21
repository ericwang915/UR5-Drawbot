import urx
import interpreter
import logging
from time import sleep

def XYposition(lines):
    lines += " "
    # given a movement command line, return the X Y position
    if lines.count('X') == 1:
        xchar_loc = lines.index('X');
        ychar_loc = lines.index('Y');
        #print lines[xchar_loc+2:ychar_loc]
        #print lines[ychar_loc+2:-1]
        x = float(lines[xchar_loc+2:ychar_loc]);
        y = float(lines[ychar_loc+2:-1]);
    return x, y;

def robot_draw(action_filename,Intial_Pose):
    for lines in open(action_filename, 'r'):
        if lines == []:
            1;  # blank lines
        elif lines[0:2] == 'X:':
            print('Move in X and Y')
            [x,y]=XYposition(lines)
            x=x/1000*1
            y=y/1000*1
            pose[0]= Intial_Pose[0]+y
            pose[1]= Intial_Pose[1]-x
            rob.movel(pose, acc=a, vel=v)
            sleep(0.15)
        elif lines[0:8] == 'Pen Down':  # working in inch;
            print('Pen Down')
            pose = rob.getl()
            pose[2]= Intial_Pose[2]-0.0015
            rob.movel(pose, acc=a, vel=v)
            sleep(0.15)
        elif lines[0:6] == 'Pen Up':  # working in mm;
            print('Pen Up');
            pose = rob.getl()
            pose[2]=Intial_Pose[2]+0.01
            rob.movel(pose, acc=a, vel=v)
            sleep(0.15)
        elif lines[0:3] == 'Pau':  # working in mm;
            sleep(0.25)
            print('Pause 150ms');
if __name__ == "__main__":
    gcode_filename = 'drawing.gcode'
    Interpreter_Obj = interpreter.Interpreter(gcode_filename)
    Interpreter_Obj.print_start()
    logging.basicConfig(level=logging.WARN)
    rob = urx.Robot("192.168.0.100")
    #rob = urx.Robot("localhost")
    rob.set_tcp((0,0,0,0,0,0))
    rob.set_payload(0.5, (0,0,0))
    Intial_Pose = rob.getl()
    try:
        l = 0.05
        v = 0.05
        a = 0.3
        robot_draw('label.txt',Intial_Pose)
        Intial_Pose[2]=Intial_Pose[2]+0.0030
        rob.movel(Intial_Pose, acc=a, vel=v)
        # pose = rob.getl()
        # print("robot tcp is at: ", pose)
        # print("absolute move in base coordinate ")
        # pose[2] += l
        # rob.movel(pose, acc=a, vel=v)
        #print("relative move in base coordinate ")
        #rob.translate((0, 0, 0), acc=a, vel=v)
        #print("relative move back and forth in tool coordinate")
        #rob.translate_tool((0, 0, -l), acc=a, vel=v)
        #rob.translate_tool((0, 0, l), acc=a, vel=v)
    finally:
        rob.close()

#rob.movel(pose, acc=a, vel=v)  absolute movement
#rob.translate((0, 0, -l), acc=a, vel=v) relative move in base coordinate
#rob.translate_tool((0, 0, -l), acc=a, vel=v) relative move back and forth in tool coordinate