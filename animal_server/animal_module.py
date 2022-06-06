from marshmallow import Schema, fields
from flask_restful import Resource
from flask import make_response, request
from check_json import check_json
from pathlib import Path
from detecto import core, utils

class _OptionsSchema(Schema):
    """Class specifies module options"""
    name = fields.String(required=False)
    animal = fields.String(required=True)
    animalConfidence = fields.Integer(required=False)


class _Schema(Schema):
    """Class specifies API parameters"""
    paths = fields.List(fields.String())
    options = fields.Nested(_OptionsSchema)


class AnimalModule(Resource):
    animals = [
    'tiger',
    'elephant',
    'panda'
    ]


    def __init__(self) -> None:
        super().__init__()
        module_path = Path()
        self.model_path = module_path / "model_weights.pth"

    def detect_animals(self, animal, animalConfidence, paths):
        filtered_paths = []
        for file in paths:
            evaluated_animals = self.detect_animal(file)
            maxVal = max(evaluated_animals.values())
            if max(evaluated_animals, key=evaluated_animals.get) == animal and  maxVal >= animalConfidence:
                filtered_paths.append(file)

        return filtered_paths

    def detect_animal(self, file_path: str):
        print(self.model_path)
        model = core.Model.load(self.model_path, self.animals)
        image = utils.read_image(file_path)

        labels, _, scores = model.predict(image)

        animal_scores = {label: [score for i, score in enumerate(scores)
                                if labels[i] == label] for label in set(labels)}

        return {label: round(float(max(animal_scores[label])) * 100) for label in animal_scores}
 
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
        animal = json_data.get("options").get("animal")
        animalConfidence = json_data.get("options").get("animalConfidence")

        if animalConfidence:
            filter_paths = AnimalModule().detect_animals(animal, animalConfidence, paths)
        else:
            filter_paths = AnimalModule().detect_animals(animal, 0, paths)
 
        return make_response({"pictures": filter_paths, }, 200)