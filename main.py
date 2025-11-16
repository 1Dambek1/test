from pydantic_settings import BaseSettings, SettingsConfigDict

class Env(BaseSettings):
 KEY:int
 model_config= SettingsConfigDict(env_file=".env")


env = Env()
print(env.KEY)


