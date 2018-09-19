from pathlib import Path


class BusCounter:

    count: int

    def write_to_file(self, file_path, text):
        try:
            f = open(file_path, 'w')
            f.write(text)
        except Exception as e:
            print(e)
        finally:
            f.close()

    def generate_txt(self, path, count):
        file_path = path + "\\bus_counter.txt"
        self.write_to_file(self, file_path, "Traffic Violations: " + str(count))

    def traffic_violation_detected(self, count):
        dir_path = str(Path.cwd())
        count += 1
        self.generate_txt(self, dir_path, count)
        return count
