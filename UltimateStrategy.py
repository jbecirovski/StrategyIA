from PythonFramework.Strategy.Strategy import Strategy
from PythonFramework.Command import Command
from UltimateStrat.Executor.CoachExecutor import CoachExecutor
from UltimateStrat.Executor.PlayExecutor import PlayExecutor
from UltimateStrat.Executor.TacticExecutor import TacticExecutor
from UltimateStrat.Executor.SkillExecutor import SkillExecutor
import UltimateStrat.Router as Router
import sys, time

__author__ = 'jbecirovski'

class UltimateStrategy(Strategy):
    def __init__(self, field, referee, team, opponent_team, is_team_yellow=False):
        Strategy.__init__(self, field, referee, team, opponent_team)

        # Create InfoManager
        self.team.is_team_yellow = is_team_yellow
        Router.initialize(field, team, opponent_team)

        # Create Executors
        self.ex_coach = CoachExecutor(Router)
        self.ex_play = PlayExecutor(Router)
        self.ex_tactic = TacticExecutor(Router)
        self.ex_skill = SkillExecutor(Router)


    def on_start(self):

        Router.update()
        # Main Strategy sequence
        self.ex_coach.exec()
        self.ex_play.exec()
        self.ex_tactic.exec()
        self.ex_skill.exec()

        # send command
        for i in range(6):
            self._send_command(Command.MoveToAndRotate(self.team.players[i], self.team, Router.getPlayerNextPose(i)))

    def on_halt(self):
        self.on_start()

    def on_stop(self):
        self.on_start()