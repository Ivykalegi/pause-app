import random
from activities.brain_gym_data import brain_gym_activities
from activities.wellbeing_data import wellbeing_activities


class ActivityManager:

    def __init__(self):
        self.brain_gym_activities = brain_gym_activities
        self.wellbeing_activities = wellbeing_activities

    def get_random_activities(self):
        random_wellbeing_activities = [self.get_wellbeing_activity() for number in range(5)]
        random_brain_gym_activities = [self.get_brain_gym_activity() for number in range(5)]
        random_activities = random_wellbeing_activities + random_brain_gym_activities
        random.shuffle(random_activities)
        return random_activities

    def get_brain_gym_activity(self):
        return random.choice(self.brain_gym_activities)

    def get_wellbeing_activity(self):
        return random.choice(self.wellbeing_activities)

if __name__ == "__main__":
    activity_manager = ActivityManager()
    print(activity_manager.get_random_activities())