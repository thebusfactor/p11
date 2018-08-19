from pathlib import Path


def write_to_file(file_path, text):
    try:
        f = open(file_path, 'w')
        f.write(text)
    except Exception as e:
        print(e)
    finally:
        f.close()


def generate_txt(path, count):
    file_path = path + "\\bus_counter.txt"
    write_to_file(file_path, "Traffic Violations: " + str(count))


def traffic_violation_detected(count):
    dir_path = str(Path.cwd())
    generate_txt(dir_path, count)

