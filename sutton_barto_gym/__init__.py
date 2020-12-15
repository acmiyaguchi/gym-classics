from gym.envs import register


register(
    id='5Walk-v0',
    entry_point='sutton_barto_gym.envs.linear_walks:Walk5'
)

register(
    id='19Walk-v0',
    entry_point='sutton_barto_gym.envs.linear_walks:Walk19'
)

register(
    id='ClassicGridworld-v0',
    entry_point='sutton_barto_gym.envs.classic_gridworld:ClassicGridworld'
)

register(
    id='CliffWalk-v0',
    entry_point='sutton_barto_gym.envs.cliff_walk:CliffWalk'
)

register(
    id='DynaMaze-v0',
    entry_point='sutton_barto_gym.envs.dyna_maze:DynaMaze'
)

register(
    id='FourRooms-v0',
    entry_point='sutton_barto_gym.envs.four_rooms:FourRooms'
)

register(
    id='Racetrack1-v0',
    entry_point='sutton_barto_gym.envs.racetracks:Racetrack1'
)

register(
    id='Racetrack2-v0',
    entry_point='sutton_barto_gym.envs.racetracks:Racetrack2'
)

register(
    id='SparseGridworld-v0',
    entry_point='sutton_barto_gym.envs.sparse_gridworld:SparseGridworld'
)

register(
    id='WindyGridworld-v0',
    entry_point='sutton_barto_gym.envs.windy_gridworld:WindyGridworld'
)

register(
    id='WindyGridworldKings-v0',
    entry_point='sutton_barto_gym.envs.windy_gridworld:WindyGridworldKings'
)

register(
    id='WindyGridworldKingsNoOp-v0',
    entry_point='sutton_barto_gym.envs.windy_gridworld:WindyGridworldKingsNoOp'
)

register(
    id='WindyGridworldKingsStochastic-v0',
    entry_point='sutton_barto_gym.envs.windy_gridworld:WindyGridworldKingsStochastic'
)
