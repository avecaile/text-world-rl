from helpers.play import play
from helpers.random_agent import RandomAgent

play(RandomAgent(), "./games/rewardsDense_goalDetailed.ulx")    # Dense rewards
play(RandomAgent(), "./games/rewardsBalanced_goalDetailed.ulx") # Balanced rewards
play(RandomAgent(), "./games/rewardsSparse_goalDetailed.ulx")   # Sparse rewards
