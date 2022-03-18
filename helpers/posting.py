
class Posting():
    def __init__(self, login):
        self.login = login

        def post(self, description):
            return self.login.env['rest.post'].create({
                'description': description,
            })