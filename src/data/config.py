from environs import Env

env = Env()
env.read_env()

PG_NAME = env.str('PG_NAME')
PG_PAS = env.str('PG_PAS')
PG_DB = env.str('PG_DB')
ip = env.str('ip')

POSTGRES_URI = f'postgresql://{PG_NAME}:{PG_PAS}@{ip}/{PG_DB}'
