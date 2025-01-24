import datetime

def update_readme():
    tz = datetime.timezone(datetime.timedelta(hours=8))
    current_time = datetime.datetime.now(tz=tz).strftime("%Y-%m-%d %H:%M:%S")
    readme_path = "./README.md"

    with open(readme_path, "r") as readme_file:
        lines = readme_file.readlines()

    lines[14] = current_time + "\n"

    with open(readme_path, "w") as readme_file:
        readme_file.writelines(lines)

if __name__ == "__main__":
    update_readme()
