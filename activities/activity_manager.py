import random
from activities.activities_data import all_activities



class ActivityManager:


    def get_random_activities(self):
        random_activities = self.get_activities()
        return [random_activities.get(x) for x in ['name', 'benefits', 'instructions']]

    def get_activities(self):
        return random.choice(all_activities)

if __name__ == "__main__":
    activity_manager = ActivityManager()
    print(activity_manager.get_random_activities())