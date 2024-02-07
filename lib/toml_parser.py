import tomlkit


def parse_toml_file(path):
    with open(path, "r") as file:
        data = tomlkit.parse(file.read())
    print(data)
