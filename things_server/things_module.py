from marshmallow import Schema, fields
from flask_restful import Resource
from flask import make_response, request
from ptii import ThingsDetector
from check_json import check_json


class _OptionsSchema(Schema):
    """Class specifies module options"""
    name = fields.String(required=False)
    imagePath = fields.String(required=True)    

class _Schema(Schema):
    """Class specifies API parameters"""
    paths = fields.List(fields.String())
    options = fields.Nested(_OptionsSchema)


class ThingsModule(Resource):
    """Class responsible for handling the image module"""

    @staticmethod
    def get_images(image_path, paths):
        detector = ThingsDetector()
        traits = detector.detecto(image_path)
        trait_set = set(traits)

        def detected(path):
            return bool(detector.detecto(path) & trait_set)

        filtered = filter(lambda p: detected(p), paths)

        return list(filtered)

    @staticmethod
    def post():
        schema = _Schema()

        # validate request
        errors = schema.validate(request.get_json())
        if errors:
            print("ERROR: ", errors)
            return make_response(errors, 400)

        json_data: dict = request.get_json(force=True)
        response_err = check_json(json_data)
        if response_err:
            print("Response error: ", response_err)
            return make_response(response_err, 400)

        # load data
        paths = json_data.get("paths")
        image_path = json_data.get("options").get("imagePath")
        filter_paths = ThingsModule.get_images(image_path, paths)

        return make_response({"pictures": filter_paths, }, 200)
