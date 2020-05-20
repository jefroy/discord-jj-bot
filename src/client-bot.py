from models.CustomClient import CustomClient

cc = CustomClient()
cc.run(cc.get_token())  # runs the client using the token
