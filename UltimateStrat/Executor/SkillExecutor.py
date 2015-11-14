from UltimateStrat.Executor.Executor import Executor
from RULEngine.Util.Pose import Pose, Position
import math

__author__ = 'jbecirovski'

CONST_TIME = 3

class SkillExecutor(Executor):
    """
    SkillExecutor is a sequence of request that select next pose for each players
    1 - what's player skill ?
    2 - what's player target ?
    3 - what's player goal ?
    4 - get skill object
    5 - generate next pose
    6 - set next pose
    """
    def __init__(self, info_manager):
        Executor.__init__(self, info_manager)

    def exec(self):
        # Execution for each players
        for id_player in range(self.info_manager.getCountPlayer()):
            # 1 - what's player skill ?
            current_skill = self.info_manager.getPlayerSkill(id_player)

            # 2 - what's player target ?
            current_target = self.info_manager.getPlayerTarget(id_player)

            # 3 - what's player goal ?
            current_goal = self.info_manager.getPlayerGoal(id_player)

            # 4 - get skill object
            skill = self.skill_book[current_skill]
            
            current_pose = self.info_manager.getPlayerPose(id_player)
            # 5 - generate next pose
            next_pose = skill().act(self._genFuturPose(id_player, current_pose), current_target, current_goal)

            # 6 - set next pose
            #print(current_skill, id_player, self.info_manager.getPlayerPose(id_player))
            #print("NextPose: ", next_pose)
            self.info_manager.setPlayerNextPose(id_player, next_pose)
            #print("GetNextP: ", self.info_manager.getPlayerNextPose(id_player))
            
    def _genFuturPose(self, p_id, p_pose):
        speed, agl = self.info_manager.getSpeed(p_id)
        print(speed * CONST_TIME, agl)
        n_pst_x = speed * math.cos(agl) * CONST_TIME + p_pose.position.x
        n_pst_y = speed * math.sin(agl) * CONST_TIME + p_pose.position.y
        return Pose(Position(n_pst_x, n_pst_y), p_pose.orientation)