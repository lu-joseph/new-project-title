import cohere
import json
import re
from scraper import getProjectData
import threading

# what we're trying to do
TASK_DESCRIPTION = "This program will generate a project title and project subtitle for a hackathon project."

STOP_SEQUENCE = "--"

DATA_FILE = "data.json"

# retrieves a generated idea from our store
def get_idea():
  with open(DATA_FILE) as f:
    data = json.load(f)
  
  fail_count = 0
  while len(data) == 0:
    print("no ideas ready")
    fail_count += 1
    if (fail_count >= 3):
      return {
        "message": "All out of new ideas :("
      }

    generate()

    with open(DATA_FILE) as f:
      data = json.load(f)
  
  idea = data.pop(0)

  with open(DATA_FILE, "w") as f:
    f.write(json.dumps(data))

  if (len(data) <= 5):
    print("restocking ideas")
    thread = threading.Thread(target=generate)
    thread.start()

  return idea

# generates new ideas
def generate():
  print("generating new ideas...")
  with open('key.txt', 'r') as file:
    KEY = file.read().replace('\n', '')

  co = cohere.Client(KEY)

  data = getProjectData(5, "https://devpost.com/software/search?query=is%3Afeatured")

  prompt = TASK_DESCRIPTION + "\n" + "".join(map(lambda project: (
    STOP_SEQUENCE + "\n" +
    "Project title: " + project["title"] + "\n" +
    "Project subtitle: " + project["subtitle"] + "\n"
    # "Project description: " + project["description"] + "\n"
  ), data)) + STOP_SEQUENCE + "\n"

  print("prompt:", prompt)

  response = co.generate(
    prompt= prompt,
    max_tokens=300
  )

  # not 100% sure about the output from the api, may try to produce more than one post
  # so we take the first one
  ideas = response.generations[0].text.strip().split("\n--\n")

  ideas_processed = []
  for idea in ideas:
    print("idea", idea)
    re_results = re.search("Project title: (.*)\nProject subtitle: (.*)", idea.strip())
    if not re_results:
      break
    ideas_processed.append({
      "title": re_results.group(1),
      "subtitle": re_results.group(2),
    })

  
  with open(DATA_FILE, "r") as f:
    data = json.load(f)
    data = data + ideas_processed
  with open(DATA_FILE, "w") as f:
    f.write(json.dumps(data))
