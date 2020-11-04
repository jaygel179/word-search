class Word(object):
    def __init__(self, text=""):
        self._text = text
        self._start_x = 0
        self._start_y = 0
        self._end_x = 0
        self._end_y = 0
        self._found = False

    @property
    def text(self):
        return self._text

    @property
    def start_x(self):
        return self._start_x

    @start_x.setter
    def start_x(self, start_x):
        self._start_x = start_x

    @property
    def start_y(self):
        return self._start_y

    @start_y.setter
    def start_y(self, start_y):
        self._start_y = start_y

    @property
    def end_x(self):
        return self._end_x

    @end_x.setter
    def end_x(self, end_x):
        self._end_x = end_x

    @property
    def end_y(self):
        return self._end_y

    @end_y.setter
    def end_y(self, end_y):
        self._end_y = end_y

    @property
    def found(self):
        return self._found

    @found.setter
    def found(self, found):
        self._found = found

    def __str__(self):
        if self._found:
            return "{text}({start_x},{start_y})({end_x},{end_y})".format(
                text=self._text.upper(),
                start_x=self._start_x,
                start_y=self._start_y,
                end_x=self._end_x,
                end_y=self._end_y,
            )
        return "{text} not found".format(text=self._text.upper())
