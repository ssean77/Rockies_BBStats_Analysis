import csv
import matplotlib.pyplot as plt

# Initialize empty list for the 3 columns we want

player_names = []
outcomes = []
runner_on_second_base = []
runner_on_third_base = []
outs_when_at_bat = []
players_meeting_criteria = []
accepted_outcomes = ["single", "double", "triple", "home_run", "strikeout", "field_error", "field_out", "force_out",
                     "grounded_into_double_play", "fielders_choice_out", "sac_fly", "sac_bunt", "double_play"]
positive_outcomes = ["single", "double", "triple", "home_run"]
negative_outcomes = ["strikeout", "field_error", "field_out", "force_out",
                     "grounded_into_double_play", "fielders_choice_out", "sac_fly", "sac_bunt", "double_play"]
player_instances = []
# This opens the CSV file in the directory and sets it as a readable file called Rockies
# reading

with open('RockiesData.csv', 'r') as Rockies:
    csv_reader = csv.reader(Rockies)

    #skipping the header row
    header = next(csv_reader)

    #Iterating through the rows in the CSV file
    # entering values into the lists
    for row in csv_reader:
        player_names.append(row[5])
        outcomes.append(row[8])
        runner_on_second_base.append(row[32])
        runner_on_third_base.append(row[31])
        outs_when_at_bat.append(row[34])


# Find each player's BA with runner's in scoring position

# Relevant Columns:
# 5 - player name
# 8 - events (what happend during the AB)
# 31 - runners on 3rd
# 32 - runners on 2nd
# ^ these two columns show a player's numerical id. Can say > "0"
# 34 - outs_when_up (either 0, 1, or 2)

# Batting average is found by taking the number of hits and dividing it by the number of ABs
# Increases BA: single, double, triple, home_run
# Doesn't Effect BA: walk, hit_by_pitch, caught_stealing_2b
# Decreases BA: strikeout, field_error, field_out, force_out, grounded_into_double_play, fielders_choice_out
#                sac_fly, sac_bunt, double_play



number_of_hits = 0
number_of_no_hits = 0

hit_counter = {}

for i in range(len(outs_when_at_bat)):
    if (runner_on_second_base[i] > "0" or runner_on_third_base[i] > "0") and (outcomes[i] in accepted_outcomes):
        player_instances.append(player_names[i])
        if player_names[i] not in hit_counter:
            if outcomes[i] in positive_outcomes:
                hit_counter[player_names[i]] = 1
            if outcomes[i] in negative_outcomes:
                hit_counter[player_names[i]] = 0
        if player_names[i] in hit_counter:
            if outcomes[i] in positive_outcomes:
                hit_counter[player_names[i]] += 1
            if outcomes[i] in negative_outcomes:
                hit_counter[player_names[i]] += 0

player_instances1 = set(player_instances)
AB_counter = {}

for player in player_instances1:
    counter = player_instances.count(player)
    AB_counter[player] = counter

# AB_counter gives us the number of times the player qualifies, which
# effectively gives us the number of ABs

# hit_counter gives us the number of hits

accepted_AB_counter = []

for player, counter in AB_counter.items():
    if counter >= 20:
        accepted_AB_counter.append(player)

for player in accepted_AB_counter:
    if player in hit_counter:
        hits = hit_counter[player]
        batting_average = hits / AB_counter[player]
        hit_counter[player] = batting_average

entries_to_remove = []

for player1, batting_average1 in hit_counter.items():
    if batting_average1 == 0 or batting_average1 >= 1:
        entries_to_remove.append(player1)

for key in entries_to_remove:
    hit_counter.pop(key, None)

# We have got a dictionary of the players and their batting averages in hit_counter


# The following is the visualization of the data we've gathered

x_axis = hit_counter.keys()
y_axis = hit_counter.values()

plt.bar(x_axis, y_axis, edgecolor='black')

for x_axis, y_axis in zip(x_axis, y_axis):
    plt.text(x_axis, y_axis, str(round(y_axis, 3)), ha='center', va='bottom')


plt.xlabel('Batters')
plt.ylabel('Batting Average')
plt.title('Batting Average with Runners in Scoring Position')

plt.show()