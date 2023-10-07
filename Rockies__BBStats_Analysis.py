import csv
import matplotlib.pyplot as plt

balls = []
exit_velocity = []
player_names = []
player_instances = []
players_accepted = []
converted_exit_velocity = []

with open('RockiesData.csv', 'r') as Rockies:
    csv_reader = csv.reader(Rockies)

    header = next(csv_reader)

    for row in csv_reader:
        balls.append(row[24])
        exit_velocity.append(row[53])
        player_names.append(row[5])


    for i in range(len(balls)):
       if balls[i] == "2" and exit_velocity[i] > "0":

           player_instances.append(player_names[i])

    player_instances1 = set(player_instances)
    player_counter = {}

    for player in player_instances1:
        counter = player_instances.count(player)
        player_counter[player] = counter

    for player, counter in player_counter.items():
        if counter >= 40:
            players_accepted.append(player)


    players_and_their_exit_velocities = {}


    for i in range(len(balls)):
       if balls[i] == "2" and exit_velocity[i] > "0":
           if player_names[i] in players_accepted:
               if player_names[i] in players_and_their_exit_velocities:
                   new_ev_value = (float(exit_velocity[i]) + players_and_their_exit_velocities[player_names[i]])
                   players_and_their_exit_velocities[player_names[i]] = new_ev_value
               else:
                    players_and_their_exit_velocities[player_names[i]] = float(exit_velocity[i])

    players_and_their_average_velocities = {}

    for i in players_and_their_exit_velocities:
        for j in player_counter:
            if i == j:
                players_and_their_average_velocities[i] = players_and_their_exit_velocities[i] / player_counter[j]




    for player, velocity in players_and_their_average_velocities.items():
        if velocity == max(players_and_their_average_velocities.values()):

        
            text = f"Player with highest average exit velocity: {player} at {velocity:.2f} mph"

           
            fig, ax = plt.subplots()

            
            ax.annotate(text, xy=(0.5, 0.5), fontsize=12, ha="center")

          
            ax.axis("off")

           
            plt.show()




    # play calls are in column 10 (hit_in_play or foul are what we care about)
    # balls are in column 24
    # strikes are in column 25
    # exit velo (launch_speed) is in column 53
