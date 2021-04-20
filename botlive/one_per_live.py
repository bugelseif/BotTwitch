from datetime import datetime, timedelta
from shelve import open as shelve_open


class OnePerLive:
    def __init__(self, filename):
        self.filename = filename
        self.file = shelve_open(filename, writeback=True)
        self._check_struct()

    def _get_date(self):
        date = datetime.now()
        if date.hour < 6:
            date -= timedelta(days=1)
        return date.today().strftime('%Y-%m-%d')

    def _check_struct(self):
        if 'date' not in self.file:
            self.file['date'] = self._get_date()
        if 'usernames' not in self.file:
            self.file['usernames'] = set()
        self.file.sync()

    def is_in(self, username):
        if self._get_date() != self.file['date']:
            return False

        return username in self.file['usernames']

    def add(self, username):
        date = self._get_date()
        if date == self.file['date']:
            if username in self.file['usernames']:
                return False
            self.file['usernames'].add(username)
        else:
            self.file['date'] = date
            self.file['usernames'] = {username}
        self.file.sync()
        return True
