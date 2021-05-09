class User:

    def __init__(self, id, pin):

        self._id = id
        self._pin = pin

    def get_id(self):

        return self._id

    def get_pin(self):

        return self._pin

