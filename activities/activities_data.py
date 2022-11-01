all_activities = [
    {'id': 1, 'name': 'Cross crawl', 'type': 'Brain Gym', 'duration': '180 seconds',
    'benefits': 'Cross crawl exercise helps improve the coordination between the '
    'right and left brain.', 'instructions': 'https://www.youtube.com/watch?v=fYJs9NZJj2g'},
    {'id': 2, 'name': 'Muscle dance', 'type': 'Brain Gym', 'duration': '480 seconds',
    'benefits': 'Muscle dance exercises help improve the coordination between the '
    'right and left brain.', 'instructions': 'https://www.youtube.com/watch?v=IHwCKA6OMoU'},
    {'id': 3, 'name': 'Muscle dance (easy)', 'type': 'Brain Gym', 'duration': '3_minutes',
    'benefits': 'Muscle dance exercises help improve the coordination between the '
    'right and left brain.', 'instructions': 'https://www.youtube.com/watch?v=YzJKug_IMZ0'},
    {'id': 4, 'name': 'Neck circles', 'type': 'Brain Gym', 'duration': '3minutes',
    'benefits': 'Neck circles are good for neck muscles and head movement coordination. '
    'This activity also improves balance if you do it while standing. '
    'Keep your eyes closed when you do this exercise.',
    'instructions': 'https://www.youtube.com/watch?v=gBwGyIp5vdM'},
    {'id': 5, 'name': 'Lazy 8', 'type': 'Brain Gym', 'duration': '3minutes',
    'benefits': 'Lazy 8 improves eye muscle movement, visual tracking, peripheral vision, '
    'attention span, and coordination. This activity enhances your abilities to '
    'understand languages, study comprehension, and eliminate reversals and transpositions.',
    'instructions': 'https://youtu.be/glOzFitlT2c'},
    {'id': 6, 'name': 'Thinking cap', 'type': 'Brain Gym', 'duration': '3minutes',
    'benefits': 'Thinking cap improves learning speed and mood, increases attention span, '
    'and boosts memory in kids and adults.', 'instructions': 'https://www.youtube.com/watch?v=wa-3IRwl1jc'},
    {'id': 7, 'name': 'Belly breathing (long)', 'type': 'Brain Gym', 'duration': '9minutes',
    'benefits': 'Belly breathing helps increase oxygen supply in the body, which, in turn, '
    'helps you relax and improves your reading and speaking abilities.',
    'instructions': 'https://www.youtube.com/watch?v=7zZC32WGAHs'},
    {'id': 8, 'name': 'Belly breathing (short)', 'type': 'Brain Gym', 'duration': '2minutes',
    'benefits': 'Belly breathing helps increase oxygen supply in the body, which, in turn, '
    'helps you relax and improves your reading and speaking abilities.',
    'instructions': 'https://www.youtube.com/watch?v=qTN_MtV5TFw'},
    {'id': 9, 'name': 'Positive points', 'type': 'Brain Gym', 'duration': '3minutes',
    'benefits': 'Positive points helps draw positive emotions and reduces the negative ones. '
    'It releases stress, relieves memory blocks, and boosts your mood. '
    'The positive points brain gym also enhances long-term memory and improves learning, '
    'reading, academic skills, and stage and sports performances.',
     'instructions': 'https://www.youtube.com/watch?v=enXPdTB3kYI'},
    {'id': 10, 'name': 'Brain button', 'type': 'Brain Gym', 'duration': '3minutes',
    'benefits': 'Brain button or switching on helps improve the flow of electromagnetic energy. It relaxes the eyes, '
    'shoulder, and neck and promotes body balance.', 'instructions': 'https://www.youtube.com/watch?v=XJ0NhV-u2b0'},
    {'id': 11, 'name': 'Read an inspirational quote', 'type': 'Wellbeing Activity', 'duration': '5 minutes', 'benefits': 'Feel '
    'inspired and motivated by reading words of advice.', 'instructions': 'Do not let yesterday take up too much of today' 
    '- Will Rogers'}, 
    {'id': 12, 'name': 'Learn a new number fact', 'type': 'Wellbeing Activity', 'duration': '5 minutes', 'benefits': 'Expand your '
    'mind with knowledge, feel good learning a new fact about the wonderful world of numbers!', 'instructions': '75 is the age ' 
    'in years that the Saguaro Cactus, found in southwestern US, must be to grow branches.'},
     {'id': 13, 'name': 'Stretch', 'type': 'Wellbeing Activity', 'duration': '5 minutes', 'benefits': 'Move your body to help reset ' 
     'your mind, movement is the ideal way to take a study break.', 'instructions': 'Get up out of your seat, stretch your arms up ' 
     'high and stretch your legs by walking into another room; do some star jumps or stretches, then walk back to your seat.'},
     {'id': 14, 'name': 'Refresh', 'type': 'Wellbeing Activity', 'duration': '5 minutes', 'benefits': 'Movement of your body helps to refresh '
     'your mind. Stimulate the blood flow around your body with a big stretch and also increase blood flow to your brain.', 
     'instructions': 'Get up out of your seat, stretch your arms up high and bend down to touch your toes. Then shake out your hands and arms.'},
     {'id': 15, 'name': 'Hydrate', 'type': 'Wellbeing Activity', 'duration': '5 minutes', 'benefits': 'Water is crucial for a healthy '
     'brain and body. Stimulate your mind by keeping your body well hydrated.', 'instructions': 'Get up out of your seat, get a large glass ' 
     'of water and take a big drink. Keep hydrated!'},
     {'id': 16, 'name': 'Connect', 'type': 'Wellbeing Activity', 'duration': '5 minutes', 'benefits': 'Relationships with people is an '
     'important part of your mental health, build up a good connection with people to share experiences and thoughts.', 'instructions': 'Plan ' 
     'and organise a meet up with a friend or family member you have not seen for a while.'},
     {'id': 17, 'name': 'Aspire', 'type': 'Wellbeing Activity', 'duration': '5 minutes', 'benefits': 'Learning a new skill is a good boost to your '
     'mental health, building self-esteem and new connections.', 'instructions': 'Think of a new skill to learn or a new activity to try. ' 
     'Find a local place to start your new hobby and meet new friends.'},
     {'id': 18, 'name': 'Kindness', 'type': 'Wellbeing Activity', 'duration': '5 minutes', 'benefits': 'Giving to others and acts of kindness are ' 
     'good for your mental health as you achieve a sense of reward, positive feelings and can help you connect with other people.', 'instructions': 
     'Think of a random act of kindness you can give. Maybe a gift to charity, help someone in need or even just smile to the next person you see'},
     {'id': 19, 'name': 'Mindfulness', 'type': 'Wellbeing Activity', 'duration': '5 minutes', 'benefits': 'Mindfulness and being aware of the world ' 
     'around you helps your mental health as you become more able to live in and appreciate the present moment.', 'instructions': 'Find a window and ' 
     'take a look outside. Notice something new or beautiful and be grateful for living in the present moment.'},
     {'id': 20, 'name': '5 Finger Breathing', 'type': 'Wellbeing Activity', 'duration': '5 minutes', 'benefits': 'Slow, medatative breathing helps your '
     'mental health by increasing oxygen to your brain, slowing your heart rate and clearing your mind.', 'instructions': 'Hold out one hand, use a' 
     'finger to slowly trace up and down each finger, starting at your thumb. Slowly breathe in with every trace up, breathe out with every trace down.'}
     ]