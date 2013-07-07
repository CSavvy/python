from Myro import *
init() #port might be different
beep(1, 600) #start signal

C3 = 261.63;
E3 = 329.63;
F3 = 349.23;
C4 = 523.25;
D4 = 587.33;
E4 = 659.26;
F4 = 698.46;
G4 = 783.99;
A4 = 880;
B4 = 987.77;
C5 = 1046.5;
D5 = 1174.66;
E5 = 1318.51;
F5 = 1396.91;
G5 = 1567.98;

for i in range(2):
 beep(0.16,F4,F3);
 beep(0.16,A4,C4);
 beep(0.32,B4,C4);   

 
beep(0.16,F4,F3);
beep(0.16,A4,C4);
beep(0.16,B4,C4);
beep(0.16,E5,C4);
beep(0.32,D5,F3);

beep(0.16,B4,C4);
beep(0.16,C5,C4);
beep(0.16,B4,E3);
beep(0.16,G4,C4);
beep(0.64,E4,C4);
wait(0.16);

beep(0.16,D4,C3);
beep(0.16,E4,E3);
beep(0.16,G4,C4);
beep(0.64,E4,C4);
wait(0.32);

for i in range(2):
 beep(0.16,F4,F3);
 beep(0.16,A4,C4);
 beep(0.32,B4,C4);   

 
beep(0.16,F4,F3);
beep(0.16,A4,C4);
beep(0.16,B4,C4);
beep(0.16,E5,C4);
beep(0.32,D5,F3);

beep(0.16,B4,C4);
beep(0.16,C5,C4);
beep(0.16,E5,E3);
beep(0.16,B4,C4);
beep(0.64,G4,C4);
wait(0.16);

beep(0.16,B4,C3);
beep(0.16,G4,E3);
beep(0.16,D4,C4);
beep(0.64,E4,C4);
wait(0.32);

beep(0.16,D4);
beep(0.16,E4);
beep(0.32,F4);
beep(0.16,G4);
beep(0.16,A4);
beep(0.32,B4);
beep(0.16,C5);
beep(0.16,B4);
beep(0.64,E4);
wait(0.32);
 
beep(0.16,D4,F4);
beep(0.16,E4,G4);    
beep(0.32,F4,A4);
beep(0.16,G4,B4);
beep(0.16,A4,C5);
beep(0.32,B4,D5);
beep(0.16,C5,E5);
beep(0.16,D5,F5);
beep(0.64,E5,G5);
wait(0.32);

beep(0.16,D4);   
beep(0.16,E4);
beep(0.32,F4);
beep(0.16,G4);
beep(0.16,A4);
beep(0.32,B4);
beep(0.16,C5);
beep(0.16,B4);
beep(0.64,E4);
wait(0.32);

beep(0.16,D4,F4);
beep(0.16,C4,E4);
beep(0.16,F4,A4);
beep(0.16,E4,G4);
beep(0.16,G4,B4);
beep(0.16,F4,A4);
beep(0.16,A4,C5);
beep(0.16,G4,B4);
beep(0.16,B4,D5);
beep(0.16,A4,C5);
beep(0.16,C5,E5);
beep(0.16,B4,D5);
beep(0.16,D5,F5);
beep(0.16,C5,E5);
beep(0.08,B4,E5);
beep(0.08,C5,F5);
wait(0.08);
beep(0.08,A4,D5);
beep(1.28,B4,E5);
wait(1.28);
