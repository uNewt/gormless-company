import json

PATH_CONFIG = "./configuration.json"
PATH_DEPENDENCIES = "./dependencies.txt"
PATH_MANIFEST = "../manifest.json"

dependencyLines = []
with open(PATH_DEPENDENCIES, "r") as dependencyFile:
    for line in dependencyFile.readlines():
        dependencyLines.append(line.replace("\n", ""))

with open(PATH_CONFIG, "r") as configurationFile:
    configurationJson = json.load(configurationFile)
configurationJson["dependencies"] = dependencyLines

with open(PATH_MANIFEST, "w") as manifestFile:
    json.dump(configurationJson, manifestFile, indent=4)