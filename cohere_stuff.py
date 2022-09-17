import cohere
import json

with open('key.txt', 'r') as file:
  KEY = file.read().replace('\n', '')

co = cohere.Client(KEY)

# what we're trying to do
TASK_DESCRIPTION = "This program will generate a project title, project subtitle and project description for a hackathon project."

STOP_SEQUENCE = "--"

with open('data.json') as json_file:
    data = json.load(json_file)

prompt = TASK_DESCRIPTION + "\n" + "".join(map(lambda project: (
  STOP_SEQUENCE + "\n" +
  "Project title: " + project["title"] + "\n" +
  "Project subtitle: " + project["subtitle"] + "\n" +
  "Project description: " + project["description"] + "\n"
), data)) + STOP_SEQUENCE + "\n"

print("prompt:", prompt)

response = co.generate(
  prompt= prompt,
  max_tokens=300
)

output = response.split("\n--\n")[0]

# split stuff into json to give a clean copy to frontend

print('{}'.format(response.generations[0].text))
