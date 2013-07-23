from Myro import *
init("sim") #port might be different

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
t = 0.10

for i in range(2):
 beep(2*t,F4,F3);
 beep(2*t,A4,C4);
 beep(4*t,B4,C4);

 
beep(2*t,F4,F3);
beep(2*t,A4,C4);
beep(2*t,B4,C4);
beep(2*t,E5,C4);
beep(4*t,D5,F3);

beep(2*t,B4,C4);
beep(2*t,C5,C4);
beep(2*t,B4,E3);
beep(2*t,G4,C4);
beep(8*t,E4,C4);
wait(2*t);

beep(2*t,D4,C3);
beep(2*t,E4,E3);
beep(2*t,G4,C4);
beep(8*t,E4,C4);
wait(4*t);

for i in range(2):
 beep(2*t,F4,F3);
 beep(2*t,A4,C4);
 beep(4*t,B4,C4);   

 
beep(2*t,F4,F3);
beep(2*t,A4,C4);
beep(2*t,B4,C4);
beep(2*t,E5,C4);
beep(4*t,D5,F3);

beep(2*t,B4,C4);
beep(2*t,C5,C4);
beep(2*t,E5,E3);
beep(2*t,B4,C4);
beep(8*t,G4,C4);
wait(2*t);

beep(2*t,B4,C3);
beep(2*t,G4,E3);
beep(2*t,D4,C4);
beep(8*t,E4,C4);
wait(4*t);

beep(2*t,D4);
beep(2*t,E4);
beep(4*t,F4);
beep(2*t,G4);
beep(2*t,A4);
beep(4*t,B4);
beep(2*t,C5);
beep(2*t,B4);
beep(8*t,E4);
wait(4*t);
 
beep(2*t,D4,F4);
beep(2*t,E4,G4);    
beep(4*t,F4,A4);
beep(2*t,G4,B4);
beep(2*t,A4,C5);
beep(4*t,B4,D5);
beep(2*t,C5,E5);
beep(2*t,D5,F5);
beep(8*t,E5,G5);
wait(4*t);

beep(2*t,D4);   
beep(2*t,E4);
beep(4*t,F4);
beep(2*t,G4);
beep(2*t,A4);
beep(4*t,B4);
beep(2*t,C5);
beep(2*t,B4);
beep(8*t,E4);
wait(4*t);

beep(2*t,D4,F4);
beep(2*t,C4,E4);
beep(2*t,F4,A4);
beep(2*t,E4,G4);
beep(2*t,G4,B4);
beep(2*t,F4,A4);
beep(2*t,A4,C5);
beep(2*t,G4,B4);
beep(2*t,B4,D5);
beep(2*t,A4,C5);
beep(2*t,C5,E5);
beep(2*t,B4,D5);
beep(2*t,D5,F5);
beep(2*t,C5,E5);
beep(t,B4,E5);
beep(t,C5,F5);
wait(t);
beep(t,A4,D5);
beep(16*t,B4,E5);
wait(16*t);
