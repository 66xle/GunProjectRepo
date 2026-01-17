from pyreutils.wrapper import *

# ─── Local Vars ─────────────────────────────────────────────
num_CurrentClip = local('num-CurrentClip')
dict_CurrentClip = local('dict-CurrentClip')
num_ID = local('num-ID')

with Function('ReduceClip') as f:

    # Reduce current clip by 1
    SetVariable.Decrement(num_CurrentClip)

    # Update the current clip in the dictionary using weapon ID
    SetVariable.SetDictValue(dict_CurrentClip, '%var(num-ID)', num_CurrentClip)

f.build_and_send()
