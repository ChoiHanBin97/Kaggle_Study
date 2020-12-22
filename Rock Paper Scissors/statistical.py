
import random
from kaggle_environments.envs.rps.utils import get_score

action_histogram = {}

def statistical(observation, configuration):
    global action_histogram
    
    # 처음에는 action_histogram = {}으로 덮어 씌우기
    if observation.step == 0:
        action_histogram = {}
        return
    
    # action에 상대방이 직전에 낸 값을 대입
    action = observation.lastOpponentAction
    
    # action_histogram에 해당 값이 없으면 해당 key만들고 value에 +1
    if action not in action_histogram:
        action_histogram[action] = 0
    action_histogram[action] += 1
    
    # mode_action_count가 제일 많은 것의 mode_action + 1을 출력(mode_action이 이기는 수)
    mode_action = None
    mode_action_count = None
    for k, v in action_histogram.items():
        if mode_action_count is None or v > mode_action_count:
            mode_action = k
            mode_action_count = v
            continue
    
    return (mode_action + 1) % configuration.signs
