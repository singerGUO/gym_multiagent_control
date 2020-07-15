from gym.envs.registration import register

register(
    id='foo-v0',
    entry_point='gym_multiagent_control.envs:MountainCarEnv',
)

register(
    id='foo-v1',
    entry_point='gym_multiagent_control.envs:CartPoleEnv',
)
