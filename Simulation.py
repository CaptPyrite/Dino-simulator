import random

class dino():
  def __init__(self):
    self.height = random.randint(5,100)
    self.width = random.randint(20,100)
    self.food_required = self.height*self.width
    
  def get_data(self):
    return(self.height,self.width,self.food_required)
  
class env():
  def __init__(self):
    self.dinos = [dino().get_data() for x in range(50)] #batch size
    self.trees_height = 32
    self.amount_of_leaf = 160
    
  def get_dino_data(self):
    return(self.dinos)
    
  def kill_dino(self):
    del self.dinos
    del self.trees_height
    del amount_of_leaf

  def run(self):
    number_that_passed = 0
    N_avg_food = []
    N_avg_height = []
    for e,i in enumerate(self.dinos):
      if i[0]>=self.trees_height:
        if i[2] <= self.amount_of_leaf*6:
          N_avg_height.append(i[0])
          N_avg_food.append(i[2])
          number_that_passed += 1
        
        else:
           self.kill_dino()
    
    try:
      return(sum(N_avg_height)/len(N_avg_height),sum(N_avg_food)/len(N_avg_food)) 
      
      
    except:
      pass
    
for i in range(10):
  x = env().run()
  if x == None:
    pass
  else:
    print(x)
