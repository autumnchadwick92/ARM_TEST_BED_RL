
#from adafruit_servokit import ServoKit
import gym
from gym import spaces
import logging
import numpy as np
from roboCam import RobotCam
from reward import reward


class RobotEnv(gym.Env):
  """Custom Environment that follows gym interface"""
  metadata = {'render.modes': ['human']}


  #Setup with H,W,Channels of Images (RGB - 3 Channels)
  def __init__(self):
    self.logger = logging.getLogger("Logger")

    self.HEIGHT = 1024
    self.WIDTH = 768
    self.N_CHANNELS = 3

    #setup intial state & camera
    self.cam = RobotCam(0)
    self.state = self.cam.takeImage()
    
    

    # Define action and observation space
    # They must be gym.spaces objects
    #discrete action space [6 servos, 3 actions 0,1,2 [noop,+1,-1], 18 total moves single action each time]

    self.action_space = spaces.Discrete(18)
    # Example for using image as input:
    self.observation_space = spaces.Box(low=0, high=255, shape=
                    (self.HEIGHT, self.WIDTH, self.N_CHANNELS), dtype=np.uint8)
    
    #contains reward info
    self.rewardclass = reward() 

    self.curr_step = 0


  def step(self, action):
    # Execute one time step within the environment
    self.curr_step += 1

    print(action)
    
    self.state = self.cam.takeImage()

    # Execute action on environment (change ventilation fan speed)
    self._execute_action(action)
        
    # Wait for environment to transition to next state
    self._transition_to_next_state()

    done = False

    reward = self._get_reward()
  
    return (self.state, reward, done, {})



  def reset(self):
    # Reset the state of the environment to an initial state

    self.state = self.cam.takeImage()

    return self.state

  def render(self, mode='human', close=False):
    # Render the environment to the screen
    pass
  
  def _execute_action(self, action):
    self.logger.info(f"Executing action")
    print(action)


  def _transition_to_next_state(self):
    self.logger.info ("Waiting for environment to respond to action...")   

  
  def _get_reward(self,state):

    #get current reward
    self.rewardclass.calc_reward() 

    #return updated reward
    return self.rewardclass.reward_val