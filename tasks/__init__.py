from invoke import Collection

from . import env, docker

ns = Collection()
ns.add_collection(env)
ns.add_collection(docker)
