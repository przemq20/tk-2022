from flask import make_response

LABELS = []

weather_types_file = open("./predict_weather_in_image/retrained_labels.txt", "r")

for line in weather_types_file:
	LABELS.append(line.rstrip())

def check_json(json_data):
	"""Check if JSON is valid"""
	error = None
	if not json_data:
		error = "No JSON in body"

	if not json_data.get("paths"):
		error = "No paths specified"

	if not json_data.get("options"):
		error = "No options specified"

	if not json_data.get("options").get("weatherType"):
		error = "No weather type specified"
		
	weather_type = json_data.get("options").get("weatherType")
	if weather_type not in LABELS:
		error = f"Invalid weather type: {weather_type}"

	return error