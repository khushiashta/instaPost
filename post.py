from instabot import Bot
bot = Bot()

#login
bot.login(username = ("username"),password = ("password"))

#upload photo
bot.upload_photo("yoda.jpeg", caption="biscuit eating baby")

#following
bot.follow("elonrmuskk")

#send a message
bot.send_message("Hello", ['user1','user2'])

#get follower info
my_followers = bot.get_user_followers("dhavalsays")
for follower in my_followers:
    print(follower)

bot.unfollow_everyone()
