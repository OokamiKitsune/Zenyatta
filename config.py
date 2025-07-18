import os
from dotenv import load_dotenv
load_dotenv()


class Config:
    """
    Configuration class to hold application settings.
    This can be extended to include more settings as needed.
    """

    ## LLM Configuration
    LLM_MODEL = os.getenv('OLLAMA_MODEL')
    EMBEDDING_MODEL = os.getenv('EMBEDDING_MODEL', 'deepseek-r1')

    ## App Settings
    APP_NAME = os.getenv('APP_NAME', 'AI Assistant')
    APP_DESCRIPTION = os.getenv('APP_DESCRIPTION', 'My custom AI Assistant')

    ## Database Settings
    DATABASE_PATH = os.getenv('DATABASE_PATH', './util/chroma_db')



