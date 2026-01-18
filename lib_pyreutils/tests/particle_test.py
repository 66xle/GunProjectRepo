from pyreutils.wrapper import *

f = Function("test", (
    Particle.Vibration(),
    Particle.Trail(),
    Particle.FadeDust()
    ))

f.build_and_send()