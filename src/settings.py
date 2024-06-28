""" Archivo con las configuraciones del proyecto """

import os

from dataclasses import dataclass

from dotenv import load_dotenv

from flask_cors import CORS
from flask import Flask

load_dotenv()

def is_true(val: str = "") -> bool:
    """
    If the value is not empty and the first character is either "t" or "1", then return True

    :param val: str = ""
    :return: bool
    """
    if not val:
        return False

    val_comp = val.lower()
    if val_comp[0] != "t" and val_comp[0] != "1":
        return False

    return True

@dataclass
class Config():
    """
        The Config class is a Python object that holds all
        the configuration variables for the application
    """
    DEVELOPMENT: bool = is_true(os.getenv("DEVELOPMENT"))
    DEBUG: bool = is_true(os.getenv("DEBUG"))
    TESTING: bool = is_true(os.getenv("TESTING"))
    ENV: str = os.getenv("ENV", "").lower()


configuration = Config()

application = Flask(__name__)
CORS(application)
application.config.from_object(configuration)
