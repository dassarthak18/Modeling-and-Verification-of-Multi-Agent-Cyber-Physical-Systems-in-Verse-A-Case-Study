from verse.plotter.plotter2D import *
from acc_agent import ACCAgent
from verse.map.example_map.simple_map2 import SimpleMap2
from verse import Scenario, ScenarioConfig
from enum import Enum, auto
import copy

class TacticalMode(Enum):
    NORMAL = auto()
    ACCEL = auto()
    DECEL = auto()

class State:
    x: float
    y: float
    vx: float
    ax: float
    ''' track mode need not be written explicitly
    as there is only a single track mode '''
    mode:TacticalMode

    def __init__(self, x, y, vx, ax, mode: TacticalMode):
        pass

def decisionLogic(ego:State, others:List[State]):
    output = copy.deepcopy(ego)
    ''' defining the behaviour in each mode '''
    if ego.mode == TacticalMode.NORMAL:
        output.ax = 0
    if ego.mode == TacticalMode.ACCEL:
        output.ax = 1
    if ego.mode == TacticalMode.DECEL:
        output.ax = -1
    ''' defining the control strategy '''
    if any(other.x-ego.x>5 for other in others):
        output.mode = TacticalMode.ACCEL
    if any(other.x-ego.x<3.5 for other in others):
        output.mode = TacticalMode.DECEL
    ''' defining the safety violation '''
    assert not any(other.x < ego.x
        for other in others), "Collision"
    return output


if __name__ == "__main__":
    ACC = Scenario(ScenarioConfig(parallel=False))
    ego = ACCAgent("ego",file_name='./acc.py')
    lead = ACCAgent("lead",file_name='./acc_agent.py')
    ACC.add_agent(ego)
    ACC.add_agent(lead)
    ''' the map is set here; sensor is not explicitly
    set, hence the default sensor is invoked '''
    track = SimpleMap2()
    ACC.set_map(track)
    ''' the initial conditions are set here '''
    ACC.set_init([[[5, 0, 28, 0], [5, 0, 28, 0]],
    [[15, 0, 28, 0], [15, 0, 28, 0]]],
    [(TacticalMode.NORMAL,), (TacticalMode.NORMAL,)],)
    ''' the verification function is called here '''
    traces = ACC.verify(100, 0.1)
    fig = go.Figure()
    fig = simulation_tree(traces, None, fig, 0, 1, [0, 1], "lines", "trace")
    fig.show()
