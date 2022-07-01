import numpy as np

students = ['name1', 'name2', 'name3', 'name4', 'name5', 'name6']

teams_fixed = [['name1'], ['name3']]
teams_fixed_backup = list(teams_fixed)

# shuffle students with a specific random seed
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

for t in teams:
    print(t)
        
