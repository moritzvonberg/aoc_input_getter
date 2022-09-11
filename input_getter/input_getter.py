from urllib import response
import zoneinfo
import requests
import pathlib
import datetime
import input_repo

class InputGetter:
    
    def __init__(self, session_key=None) -> None:
        self.session_key = {"session": session_key}
        if not session_key and pathlib.Path("session.txt").exists():
            with open("session.txt") as infile:
                self.session_key["session"] = infile.readline().strip().split("=")[1]
        self.input_repo = input_repo.InputRepository()
                
    def get_problem_input(self, day=None, year=None, write_input_to_local_dir=False):
        # TODO implement writing copy of input to local dir
        time_now = datetime.datetime.now(time_zone:=zoneinfo.ZoneInfo('US/Eastern'))
        if year is None:
            year = time_now.year if time_now.month == 12 else time_now.year - 1
        if day is None:
            if time_now.month == 12 and 1 < time_now.day <= 15:
                day = time_now.day
            else:
                day = 25
        problem_input = self.input_repo.get_input(year, day)
        if not problem_input:
            response = self.request_input(year, day)
            if not 200 <= response.status_code < 300:
                raise OSError(f"Coudln't connect to {response.url}, status code: {response.status_code}")
            elif response.status_code == 200:
                self.input_repo.set_input(year, day, problem_input)
                problem_input = self.input_repo.get_input(year, day)
        
        return problem_input
        
    def request_input(self, year, day) -> requests.models.Response:
        url = f'https://www.adventofcode.com/{year}/day/{day}/input'
        return requests.get(url, cookies=self.session_key)

