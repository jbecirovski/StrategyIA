__author__ = 'jbecirovski'

import math

class BlackBoard:
    # TODO Make BlackBoard documentation
    def __init__(self, field, team, opponent_team):
        self.field = field
        self.team = team
        self.opponent_team = opponent_team

        t_player_key = ('pose', 'position', 'orientation', 'kick', 'skill', 'tactic', 'next_pose', 'target',
                        'goal', 'pst_save', 'speed')
        d_team = {}
        d_op_team = {}
        d_ball = {'position': self.field.ball.position}
        d_game = dict(zip(('play', 'state', 'sequence'), ('pHalt', None, None)))

        for player in self.team.players:
            t_player_data = (player.pose, player.pose.position,
                             player.pose.orientation, 0, None, None, None, None, None, [Position() for x in range(5)], (0, 0))
            d_team[str(player.id)] = dict(zip(t_player_key, t_player_data))
        d_team['is_yellow'] = self.team.is_team_yellow
        d_team['count'] = len(self.team.players)

        for player in self.opponent_team.players:
            t_player_data = (player.pose, player.pose.position,
                             player.pose.orientation, 0, None, None)
            d_op_team[str(player.id)] = dict(zip(t_player_key, t_player_data))
        d_op_team['is_yellow'] = self.opponent_team.is_team_yellow
        d_op_team['count'] = len(self.opponent_team.players)

        self.bb = dict(zip(('ball', 'friend', 'enemy', 'game'), (d_ball, d_team, d_op_team, d_game)))

    def __getitem__(self, item):
        return self.bb[item]

    def update(self):
        self.bb['ball']['position'] = self.field.ball.position

        for i in range(6):
            self.bb['friend'][str(i)]['pst_save'].append(self.team.players[i].pose.position)
            if len(self.bb['friend'][str(i)]['pst_save']) > 10:
                del self.bb['friend'][str(i)]['pst_save'][0]
            self.bb['friend'][str(i)]['speed'] = getSpeed(self.bb['friend'][str(i)]['pst_save'])
            self.bb['friend'][str(i)]['pose'] = self.team.players[i].pose
            self.bb['friend'][str(i)]['position'] = self.team.players[i].pose.position
            self.bb['friend'][str(i)]['orientation'] = self.team.players[i].pose.orientation

            self.bb['enemy'][str(i)]['pose'] = self.opponent_team.players[i].pose
            self.bb['enemy'][str(i)]['position'] = self.opponent_team.players[i].pose.position
            self.bb['enemy'][str(i)]['orientation'] = self.opponent_team.players[i].pose.orientation

class Position:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

def getSpeed(liste):
    distance = 0
    angle = 0
    xref, yref = liste[0].x, liste[0].y
    for pst in liste[1:]:
        xcur, ycur = pst.x, pst.y
        angle += math.atan2(ycur-yref, xcur-xref)
        distance += ((xref-xcur)**2 + (yref-ycur)**2)**0.5
        xref, yref = xcur, ycur
    return distance/(len(liste)-1), angle/(len(liste)-1)
        
        
        
        
        
        
        
        
        
