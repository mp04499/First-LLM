import json

with open('movesets.json') as f:
    data = json.load(f)

dataset = []

default_input = "What type of move matches this description: "
for x in data:
    input_text = default_input + x["effect"]
    dataset.append(
        {
            "input_text": input_text,
            "output_text": x["category"]
        }
    )

with open('movesets-train.json', 'w') as fp:
    json.dump(dataset, fp)
    