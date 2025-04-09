yfrom gpiozero import LED,Button
from time import sleep
from random import uniform


led=LED(4)
right_button=Button(15)
left_button=Button(14)

left_name=input('left player name is')
right_name=input('right player name is')
left_score=0
right_score=0



def pressed(button):
  global left_score,right_score
  end_time=time.time
  elapsed_time=end_time-start_time
  if button.pin.number==14 :
      left_score+=1
      print(left_name + 'won the game,the score is'+left_score+',time is'+elapsed_time)
  else:
      right_score+=1
      print(right_name + 'won the game,the score is'+right_score+',time is'+elapsed_time)


while True:
   led.on()
   time.sleep(uniform(5,10))
   led.off()
   start_time=time.time()
   right_button.when_pressed=pressed
   left_button.when_pressed=pressed
   time.sleep(0.1)

