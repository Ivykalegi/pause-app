from unittest import TestCase, mock, main
from activities.activity_manager import ActivityManager


class TestActivityManager(TestCase):

    def test_get_random_activities(self):
        test_activity = {'id': 16, 'name': 'Connect', 'type': 'Wellbeing Activity', 'duration': '5 minutes', 'benefits':
                    'Relationships with people is an important part of your mental health, build up a good connection '
                    'with people to share experiences and thoughts.', 'instructions': 'Plan and organise a meet up '
                    'with a friend or family member you have not seen for a while.'}
        with mock.patch("random.choice", return_value=test_activity):
            self.assertIn(test_activity, ActivityManager().get_random_activities())


    def test_get_brain_gym_activity(self):
        test_activity = {'id': 2, 'name': 'Muscle Dance', 'type': 'Brain Gym', 'duration': '7 minutes',
                    'benefits': 'Muscle dance exercises help improve the coordination between the '
                    'right and left brain.', 'instructions': 'https://www.youtube.com/watch?v=IHwCKA6OMoU'}
        with mock.patch("random.choice", return_value=test_activity):
            self.assertEqual(test_activity, ActivityManager().get_brain_gym_activity())


    def test_get_wellbeing_activity(self):
        test_activity = {'id': 20, 'name': '5 Finger Breathing', 'type': 'Wellbeing Activity', 'duration': '5 minutes',
                         'benefits': 'Slow, medatative breathing helps your mental health by increasing oxygen to your '
                        'brain, slowing your heart rate and clearing your mind.', 'instructions': 'Hold out one hand, '
                        'use a finger to slowly trace up and down each finger, starting at your thumb. Slowly breathe '
                        'in with every trace up, breathe out with every trace down.'}
        with mock.patch("random.choice", return_value=test_activity):
            self.assertEqual(test_activity, ActivityManager().get_wellbeing_activity())

if __name__ == '__main__':
    main()