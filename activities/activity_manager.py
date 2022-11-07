import random
from activities.brain_gym_data import brain_gym_activities
from activities.wellbeing_data import wellbeing_activities


class ActivityManager:
    '''
    A class to represent management of the activities data.
    
    Attributes
    ----------
    brain_gym_activities : list[dict[str]]: Brain Gym activity list.
    wellbeing_activities : list[dict[str]]: wellbeing activity list.

    Methods
    -------
    get_brain_gym_activity()
    returns randomly chosen Brain Gym activity.

    get_wellbeing_activity()
    returns randomly chosen wellbeing activity.

    get_random_activities()
    returns randomly selected activities in range of 20 from Brain Gym data and wellbeing data files combined.
    '''

    def __init__(self):
        self.brain_gym_activities = brain_gym_activities
        self.wellbeing_activities = wellbeing_activities
    '''
    All the attributes for the activity manager object.

        Parameters
        ----------
        brain_gym_activities : list[dict[str]]: Brain Gym activity list.
        wellbeing_activities : list[dict[str]: wellbeing activity list.
    '''

    def get_brain_gym_activity(self):
        '''
        Returns the randomly chosen Brain Gym activity.

                Parameters
                ----------
                brain_gym_activities : list[dict[str]]: Brain Gym activity list.
                wellbeing_activities : list[dict[str]] : wellbeing activity list.

                Returns:
                --------
                random.choice: (seq): randomly chosen Brain Gym activity from data file.  
        '''
        return random.choice(self.brain_gym_activities)

    def get_wellbeing_activity(self):
        '''
        Returns the randomly chosen wellbeing activity.

                Parameters
                ----------
                brain_gym_activities : list[dict[str]]: Brain Gym activity list.
                wellbeing_activities : list[dict[str]] : wellbeing activity list.

                Returns:
                --------
                random.choice: (seq): randomly chosen wellbeing activity from data file. 
        '''
        return random.choice(self.wellbeing_activities)
    
    def get_random_activities(self):
        '''
        Returns randomly selected activities from Brain Gym data and wellbeing data files combined.
                
                Parameters
                ----------
                brain_gym_activities : list[dict[str]]: Brain Gym activity list.
                wellbeing_activities : list[dict[str]] : wellbeing activity list.

                Returns:
                --------
                random_wellbeing_activities: list[dict[str]]: get 20 wellbeing activities from data file. 
                random_brain_gym_activities: list[dict[str]]: get 20 Brain Gym activities from data file.
                random_activities: list[dict[str]]: random Brain Gym activities added to wellbeing activities list.
                random.shuffle: (x): randomly chosen activities from Brain Gym data and wellbeing data files combined. 
        '''
        random_wellbeing_activities = [self.get_wellbeing_activity() for number in range(20)]
        random_brain_gym_activities = [self.get_brain_gym_activity() for number in range(20)]
        random_activities = random_wellbeing_activities + random_brain_gym_activities
        random.shuffle(random_activities)
        return random_activities
