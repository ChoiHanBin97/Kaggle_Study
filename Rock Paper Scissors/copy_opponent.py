
import random
from kaggle_environments.envs.rps.utils import get_score

def copy_opponent(observation, configuration):

    # 상대방이 직전에 냈던 것을 냄
    if observation.step > 0:
        return observation.lastOpponentAction
    
    # 처음에 랜덤으로 냄
    else:
        return random.randrange(0, configuration.signs)
