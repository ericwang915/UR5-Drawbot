class Interpreter():
    def __init__(self,filename):
        self.filename = filename
        self.fw = open('label.txt', 'w')
        self.fw.truncate()
    def XYposition(self,lines):
        lines += " "
        #given a movement command line, return the X Y position
        if lines.count('X') == 1:
            xchar_loc=lines.index('X');
            i=xchar_loc+1;
            while (47<ord(lines[i])<58)|(lines[i]=='.')|(lines[i]=='-'):
                    i+=1;
            x=float(lines[xchar_loc+1:i]);
            ychar_loc=lines.index('Y');
            i=ychar_loc+1;
            while (47<ord(lines[i])<58)|(lines[i]=='.')|(lines[i]=='-'):
                    i+=1;
            y=float(lines[ychar_loc+1:i]);
            print('X:'+str(x)+'Y:'+str(y))
            self.fw.write('X:'+str(x)+'Y:'+str(y)+'\n')
        return x,y;
    def gcode_executer(self,lines):
        if lines==[]:
            1; #blank lines
        elif lines[0:3]=='G90':
            print( 'absolute mode and Z push to 1mm');
            self.fw.write('absolute mode and Z push to 1mm\n')
        elif lines[0:3]=='G20':# working in inch;
            adj_unit = 25.4
            print('Working in inch')
            self.fw.write('Working in inch\n')
        elif lines[0:3]=='G21':# working in mm;
            adj_unit = 1
            print( 'Working in mm');
            self.fw.write('Working in mm\n')
        elif lines[0:3]=='G1 ' and lines.count('Z') == 0:# working in mm;
            [x,y]=self.XYposition(lines);
        elif lines[0:3]=='G4 ':# working in mm;
            print('Pause 150ms');
            self.fw.write('Pause 150ms\n')
        elif lines[5:8]=='S30':# working in mm;
            print('Pen Down')
            self.fw.write('Pen Down\n')
        elif lines[5:8]=='S50':# working in mm;
            print('Pen UP');
            self.fw.write('Pen Up\n')

        return 0
    def print_start(self):
        try:#read and execute G code
            for lines in open(self.filename,'r'):
                self.gcode_executer(lines)
            self.fw.close()
        except KeyboardInterrupt:
            pass
    def kill(self):
        del self

# if __name__ == '__main__':
#     filename='robot.gcode'
#     Interpreter_Obj =Interpreter(filename)
#     Interpreter_Obj.print_start()

