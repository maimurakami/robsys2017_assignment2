# robsys2017_assignment2
1526110 村上舞  
ROSでカウント&LED点滅  
カウントは講義でのroslaunchまで行い  
LEDの点滅はpigpioで制御し  
PWM制御を用いて緩やかに点滅する  
## Demo
[RaspberryPiでカウント&LED点滅](https://youtu.be/elg05B4Hasg)
## Requirements
+ RaspberryPi3 (Ubuntu) 
+ LED  
+ 抵抗器(10Ω)  
## Circuit
![](https://github.com/maimurakami/robsys2017_assignment2/blob/master/IMG_01.jpg)
## Usage
+ roslaunchを実行  
`roslaunch mypkg mypkg.launch`
+ カウントを行う  
`rostopic echo /twice`
+ LEDの点滅  
`rosrun mypkg led.py`
## Reference/Quotation
[ロボットシステム学 講義資料](https://github.com/ryuichiueda/robosys2017/blob/master/12.md)
