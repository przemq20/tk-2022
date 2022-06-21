from flask import make_response
import os

MODULE_PATH = os.path.dirname(__file__)


def check_json(json_data):
    """Check if JSON is valid"""
    error = None
    if not json_data:
        error = "No JSON in body"

    if not json_data.get("paths"):
        error = "No paths specified"

    if not json_data.get("options"):
        error = "No options specified"

    if not json_data.get("options").get("color"):
        error = "No color specified"

    return error
