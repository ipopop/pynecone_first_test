import pynecone as pc

class MyapppcConfig(pc.Config):
    pass

config = MyapppcConfig(
    app_name="my_app_pc",
    db_url="sqlite:///pynecone.db",
    env=pc.Env.DEV,
)
