import os
from typing import List
import yaml

languages = {}
languages_present = {}


def get_command(value: str) -> List:
    return commands["command"][value]


def get_string(lang: str):
    return languages[lang]


for filename in os.listdir(r"./Strings/languages/"):
    if "en" not in languages:
        languages["en"] = yaml.safe_load(
            open(r"./Strings/languages/en.yml", encoding="utf8")
        )
        languages_present["en"] = languages["en"]["name"]
    if filename.endswith(".yml"):
        language_name = filename[:-4]
        if language_name == "en":
            continue
        languages[language_name] = yaml.safe_load(
            open(r"./Strings/languages/" + filename, encoding="utf8")
        )
        for item in languages["en"]:
            if item not in languages[language_name]:
                languages[language_name][item] = languages["en"][item]
        try:
            languages_present[language_name] = languages[language_name]["name"]
        except Exception as e:
            print(f"There is some issue with the language file '{filename}': {e}")
            exit()
