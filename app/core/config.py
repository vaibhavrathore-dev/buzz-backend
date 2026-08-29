from pydantic_settings import BaseSettings,SettingsConfigDict

class Settings(BaseSettings):
        jwt_private_key : str = "app/keys/jwt_private.pem"
        jwt_public_key : str = "app/keys/jwt_public.pem"
        DATABASE_URL : str
        smtp_host: str
        smtp_port: int
        smtp_username: str
        smtp_password: str
        model_config = SettingsConfigDict(
            env_file = ".env",
            env_file_encoding = "utf-8"
        )

settings = Settings()
