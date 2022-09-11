import pathlib

class InputRepository:
    def __init__(self, storage_base_path=None) -> None:
        if storage_base_path and pathlib.Path(storage_base_path).is_dir():
            self.storage_base_path: pathlib.Path = pathlib.Path(storage_base_path)
        else:
            self.storage_base_path = pathlib.Path.cwd() / "inputs"
        if not self.storage_base_path.exists():
            # TODO: handle unhappy paths
            pathlib.Path.mkdir(self.storage_base_path)
    
    def get_input(self, year, day):
        if (target_path := self.get_target_path(year, day)).exists():
            return target_path.open()
        else:
            return None

    def set_input(self, year, day, content):
        # make the parent directory if it doesn't exist
        (target_path := self.get_target_path(year, day)).parent.mkdir(parents=True, exist_ok=True)
        with target_path.open(mode='w') as outfile:
            outfile.write(content)


    def get_target_path(self, year, day) -> pathlib.Path:
        return pathlib.Path(self.storage_base_path) / str(year) / str(day) / "input.txt"

            