# new-project-title

ARE YOU LOOKING FOR A HACKATHON IDEA? Well lucky you, cause you find us.

A hackathon idea generator that looks on Devpost for past hackathon ideas and generate a new one using the Cohere API.

Scraper.getProjectData() returns a JSON with the form:
```
{
  "projectJsons": [
    {
      "title": project_title,
      "subtitle": subtitle,
      "description": description,
      "builtWith": [built_with_tags]
    },
    {
      "title": project_title,
      "subtitle": subtitle,
      "description": description,
      "builtWith": [built_with_tags]
    },
    {
      "title": project_title,
      "subtitle": subtitle,
      "description": description,
      "builtWith": [built_with_tags]
    },
  ]
}
```

To run:
```
pip install uvicorn
pip install fastapi
pip install cohere

uvicorn main:app --reload
```

Notes:
- Requires `key.txt` containing a Cohere key in the project root.
- `pip install uvicorn --user`
- `python -m uvicorn main:app --reload`
