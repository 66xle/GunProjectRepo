from pyreutils.wrapper import *

# ─── Local Vars ─────────────────────────────────────────────
num_CurrentClip = local('num-CurrentClip')
dict_CurrentClip = local('dict-CurrentClip')
num_ID = local('num-ID')

with Function('ReduceClip') as f:

    # Reduce current clip by 1
    num_CurrentClip -= 1

    # Update the current clip in the dictionary using weapon ID
    dict_CurrentClip.v = SetV.SetDictValue('%var(num-ID)', num_CurrentClip)

f.build_and_send()
