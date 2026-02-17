import yaml

from typing import Literal
from pydantic import BaseModel, Field, IPvAnyAddress

class ServerConfig(BaseModel):
    host: IPvAnyAddress
    port: int = Field(..., ge=1, le=65535)

class LogConfig(BaseModel):
    level: Literal["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]

class DatabaseConfig(BaseModel):
    server: str # Not IPvAnyAddress
    port: int
    username: str
    password: str
    dbname: str

class AppConfig(BaseModel):
    server: ServerConfig
    log: LogConfig
    database: DatabaseConfig

    @classmethod
    def load_config(cls, filepath: str):
        with open(filepath) as f:
            config_dict = yaml.safe_load(f)
            return cls(**config_dict) # Here pydantic automatically validate the config
