# -*- coding: utf-8 -*-

import os
os.system('chcp 949')

import numpy as np


students = ['오현택', '전승원','조성현', '신혜지', '이기욱', '백동렬', '문성민','이혜미', '양정윤', '김동한', '조민식', '허규','박혜은', '고관성','최동근']

teams_fixed = [['김동한', '조민식'], ['전승원', '양정윤', '조성현']]

teams_fixed_backup = list(teams_fixed)

# shuffle students with a specific random seed
np.random.seed(27) # note that: this seed number has been generated randomly from 0~99
shuffle_idx = np.random.permutation(len(students))
print(shuffle_idx)

# number of students/team
n = 3

# team_assignment
id = 0
to_break = False

teams = []

while True:
    team = []
    members = 0
    if len(teams_fixed)>0:
        team = teams_fixed.pop()
        members = len(team)

    while members<n:
        shuffle_id = shuffle_idx[id]
        name = students[shuffle_id]
        # check if this name already included in other teams
        exist = False
        for t in teams_fixed_backup:
            if name in t:
                exist = True
                break
        
        if not exist:
            team.append(name)
            members += 1
        id = id+1
        if id >= len(shuffle_idx):
            to_break = True
            break

    teams.append(team)
    if to_break:
        break

captains=[]
captains.append('') # Team-1
captains.append('') # Team-2
captains.append('') # Team-3
captains.append('백동렬') # Team-4
captains.append('') # Team-5

for t in range(len(teams)):
    print('Team #{}: {}'.format(t+1, teams[t]))
