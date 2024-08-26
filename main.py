class BlockWorld:
  def __init__(self,initial_state,goal_state):
    self.state = initial_state
    self.goal_state = goal_state
    self.actions = []
  def move_to_table(self, block):
    if self.state[block] != 'table':
      self.state[block] = 'table'
      self.actions.append(f"Move {block} to the table.")
  def stack(self, block1, block2):
    if self.state[block1] != block2:
      self.state[block1] = block2
      self.actions.append(f"Stack {block1} on {block2}.")
  def execute_actions(self):
    for block, target in self.goal_state.items():
      if target == 'table':
        self.move_to_table(block)
      else:
        self.stack(block, target)
  def get_final_state(self):
    return self.state
  def get_action_sequence(self):
    return self.actions

initial_state = {
      'A' : 'B',
      'B' : 'C',
      'C' : 'table'
}

goal_state = {
      'A' : 'table',
      'B': 'A',
      'C' : 'B'
}

world = BlockWorld(initial_state, goal_state)

world.execute_actions()

final_state = world.get_final_state()
action_sequence = world.get_action_sequence()
print("Final State:", final_state)
print("Action Sequence:")
for action in action_sequence:
  print(action)

