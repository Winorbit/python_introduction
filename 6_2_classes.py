class User:
	__strong_secret = "value"
	_not_so_strong_secret = "value"
	meeh = "value"

# print(User.__strong_secret)
# print(User._not_so_strong_secret)
# print(User.meeh)


# print(User().__strong_secret)
print(User()._not_so_strong_secret)
print(User().meeh)


# print(User.__dict__)
# print(User().__dict__)

class User:
	def __init__(self, username:str=""):
		self.username = username
		self.lat = 0.0
		self.lon = 0.0
		# self.position_message = f"Your current position is lattitude:{self.lat}, longitude:{self.lon}"

	def update_coords(self, lon:float=0.0, lat:float=0.0):
		self.lon = lon
		self.lat = lat

	@classmethod
	def position_message(self):
		return f"Your current position is lattitude:{self.lat}, longitude:{self.lon}"
	


kiril = User(username="Kiril")
kiril.update_coords(lon=56.71, lat=94.12)
print(kiril.position_message)

