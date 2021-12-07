
#from adafruit_servokit import ServoKit
import gym
from gym import spaces
import logging
import numpy as np
from reward import reward
from action import action

class RobotEnv(gym.Env):
  """Custom Environment that follows gym interface"""
  metadata = {'render.modes': ['human']}


  #Setup with H,W,Channels of Images (RGB - 3 Channels)
  def __init__(self):
    self.logger = logging.getLogger("Logger")

    self.HEIGHT = 32
    self.WIDTH = 32
    self.N_CHANNELS = 3
 
    

    # Define action and observation space
    # They must be gym.spaces objects
    #discrete action space [6 servos, 3 actions 0,1,2 [noop,+1,-1], 18 total moves single action each time]
    self.numServos = 2
    self.action_space = spaces.Discrete(2*self.numServos)
    # Example for using image as input:
    self.observation_space = spaces.Box(low=0, high=255, shape=
                    (self.HEIGHT, self.WIDTH, self.N_CHANNELS), dtype=np.uint8)
    


    #setup action class
    self.actionclass = action()
    
    #contains reward info
    self.rewardclass = reward() 

    #setup intial state & camera
    self.state = self.rewardclass.get_state()
    


    self.curr_step = 0


  def step(self, action):
    # Execute one time step within the environment
    self.curr_step += 1

    print(action)
    
    self.state = self.rewardclass.get_state()

    # Execute action on environment (change ventilation fan speed)
    self._execute_action(action)
        
    done = False

    reward = self._get_reward()
  
    return (self.state, reward, done, {})



  def reset(self):
    # Reset the state of the environment to an initial state
    self.actionclass.reset_robot()
    self.state = self.rewardclass.get_state()
    return self.state

  def render(self, mode='human', close=False):
    # Render the environment to the screen
    pass
  
  def _execute_action(self, action):
    self.logger.info(f"Executing action")
    print(action)
    self.actionclass.move_robot_arm(action)


  
  def _get_reward(self):
    #get current reward
    return float(self.rewardclass.reward_cal()) 
