from pathlib import Path


class BusCounter:

    count: int

    def write_to_file(self, file_path, text):
        """
           Writes the traffic violation counter to the file located at the given path.

           Parameters
           ----------
           file_path : string
               Location of the file to be written to.
           text: string
               Text that needs to be written into the file.
        """
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
