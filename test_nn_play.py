from helpers.play import play
from helpers.neural_agent import NeuralAgent

agent = NeuralAgent()
play(agent, "./games/rewardsDense_goalDetailed.ulx")