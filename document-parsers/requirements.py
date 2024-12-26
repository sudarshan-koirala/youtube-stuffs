import toml

# Path to your pyproject.toml file
pyproject_path = "pyproject.toml"

# Load the pyproject.toml file
with open(pyproject_path, "r") as file:
    pyproject_data = toml.load(file)

# Extract the dependencies section
dependencies = pyproject_data.get("project", {}).get("dependencies", [])

# Write the dependencies to a requirements.txt file
with open("requirements.txt", "w") as req_file:
    req_file.writelines([dep + "\n" for dep in dependencies])

print("Dependencies extracted and saved to requirements.txt:")
print("\n".join(dependencies))