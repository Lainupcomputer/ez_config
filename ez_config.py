import json


class ez_config:

    file_path = ""
    separator = "#"
    debug = False

    def send_debug(self, message):
        if self.debug:
            print(message)

    def initialise(self, file_path, separator=None, debug=False):
        self.file_path = file_path
        self.debug = debug
        if separator is not None:
            self.separator = separator

        there = True
        while there:
            if self.file_path != "":
                try:
                    with open(self.file_path, "r"):
                        self.send_debug("[*] Data found...")
                        break

                except FileNotFoundError:
                    with open(self.file_path, "w") as f:
                        f.write("{\n\n}")
                        self.send_debug("[*] Data created...")
            else:
                print("Insert: file_path!")

    def save(self, file):  # Save data to settings
        with open(self.file_path, "w") as f:
            json.dump(file, f, indent=2)

    def read_file(self):  # Read all settings to process
        with open(self.file_path, "r") as f:
            file = json.load(f)
        return file

    def get(self, cfg, data):  # get data from settings
        try:
            file = self.read_file()
            value = file[str(cfg)][data]
            self.send_debug(f"got {value} from {cfg}>{data}")
            return value

        except KeyError:
            self.send_debug(f"{cfg}>{data} Not Found")

    def edit(self, cfg, data, value):  # edit in settings
        try:
            file = self.read_file()
            file[str(cfg)][data] = value
            self.save(file)
            self.send_debug(f"edited {value} from {cfg}>{data}")
        except KeyError:
            self.send_debug(f"{value} for {cfg}>{data} Not Found")

    def add(self, cfg, data):  # Add Data to settings
        file = self.read_file()
        file[str(cfg)] = {}
        for entry in data.split(self.separator):
            file[str(cfg)][str(entry)] = ""
        self.save(file)
        self.send_debug(f"added {cfg}>{data}")

