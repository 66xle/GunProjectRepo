from dfpyre import *

player_event('Join', [
  player_action('SendMessage', '%default has joined!', target=Target.ALL_PLAYERS),
  player_action('GiveItems', Item('apple', 10))
]).build_and_send()