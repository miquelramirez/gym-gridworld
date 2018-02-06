from gym.envs.registration import register
from gym.scoreboard.registration import add_task, add_group
from .package_info import USERNAME

# Environment registration

for d in [ 4, 8, 16, 32, 64 ] :
    register(
        id='{}/gridworld-{}x{}'.format(USERNAME,d,d),
        entry_point='{}_gym_gridworld:GridWorldEnv'.format(USERNAME),
        max_episode_steps=1000,
        reward_threshold=9000.0,
        kwargs={
            'average_over': 3,
            'passing_grade': -20,
            'min_tries_for_avg': 3
        },
    )

# Scoreboard registration
# ==========================
add_group(
    id= 'gridworld',
    name= 'GridWorld',
    description= 'Sutton & Barto classic Gridworld environment.'
)

for d in [ 4, 8, 16, 32, 64 ] :
    add_task(
        id='{}/GridWorld-{}x{}'.format(USERNAME,d,d),
        group='gridworld',
        summary='Sutton and Barto Grid world, {}x{}.'.format(d),
        description="""
        """)
