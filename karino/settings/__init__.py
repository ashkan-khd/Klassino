from os import getenv

MODE = getenv('MODE')

if MODE == "production":
    from karino.settings.production import *
elif MODE == "staging":
    from karino.settings.staging import *
elif MODE == "testing":
    from karino.settings.production import *
else:
    from karino.settings.development import *
