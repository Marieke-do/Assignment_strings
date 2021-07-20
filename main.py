# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line
player_score_0 = "Ruud Gullit" # Player who scored the first goal
player_score_1 = "Marco van Basten" # Player who scored the second goal

goal_0 = 32 # Minute in which first goal was scored
goal_1 = 54 # Minute in which second goal was scored

# string that tells: <scorer_name> <when_they_scored>, <scorer_name> <when_they_scored>
scorers = player_score_0 + ' ' + str(goal_0) + ', ' + player_score_1 + ' ' + str(goal_1)
print(scorers)

# string that tells:
# <scorer_name> scored in the <when_they_scored>nd minute
# <scorer_name> scored in the <when_they_scored>th minute

report = f'{player_score_0} scored in the {goal_0}nd minute\n{player_score_1} scored in the {goal_1}th minute'
print(report)

#part two

player = "Frank Rijkaard"
first_name = player[:player.find(' ')] #isolate first name of player
last_name_len = len(player[player.find(' ')+1:]) #store length of last name
name_short = player[0] + '. ' + player[player.find(' ')+1:] #isolate and store the player's name in this format: G. von Examplestein
print(first_name)
print(last_name_len)
print(name_short)

chant = (first_name + '! ') *(len(first_name)-1) + (first_name + '!') #chant first name x times, where x is len(first_name). Last character is not a space
print(chant)

good_chant = chant[-1] != " " #checks last character is not a space
print(good_chant)


