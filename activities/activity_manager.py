import random
from pprint import pprint
from activities.brain_gym_data import brain_activities
from activities.wellbeing_data import wellb_activities



class ActivityManager:

    def get_random_activities(self):
        wellbeing_activities = [self.get_wellbeing_activity() for number in range (4)]
        brain_gym_activities = [self.get_brain_gym_activity() for number in range(4)]
        random_activities = wellbeing_activities + brain_gym_activities
        random.shuffle(random_activities)
        number = random.randint(0,8)
        return [random_activities[number].get(x) for x in ['name', 'benefits', 'instructions']]

    def get_brain_gym_activity(self):
        return random.choice(brain_activities)

    def get_wellbeing_activity(self):
        return random.choice(wellb_activities)

if __name__ == "__main__":
    activity_manager = ActivityManager()
    print(activity_manager.get_random_activities())