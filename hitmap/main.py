from roboflow import Roboflow
import json

rf = Roboflow(api_key="px1uTQC3WV6c9JsQUO4L")
project = rf.workspace().project("person-wozrc")
model = project.version(1).model
predictions=model.predict("OIP.jpg", confidence=40, overlap=30).json()
print(predictions)