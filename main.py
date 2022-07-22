class User:
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0
#         in the case that there's an attribute that always has a default value,
#         you can just name it and NOT SET IT EQUAL to a parameter (ie notice there's no 'followers' param)

    def follow(self, user):
        self.following += 1
        user.followers += 1


user_1 = User("001", "dsump")
# we are initializing a user_1 object from User class with 001 and dsump as attributes
user_2 = User("002", "esump")

user_1.follow(user_2)
print(user_1.following, user_2.followers)