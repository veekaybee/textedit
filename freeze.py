import pip
with open("requirements.txt", "w") as f:
    for dist in pip.get_installed_distributions():
        req = dist.as_requirement()
        f.write(str(req) + "\n")