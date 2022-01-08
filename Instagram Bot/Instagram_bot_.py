from instabot import Bot
bot = Bot()
bot.login(username="irahulbairagi", password="201728627")

######  upload a picture #######
bot.upload_photo("dogememe.jpg", caption="i love cheems")

######  follow someone #######
bot.follow("python.hub")
bot.unfollow("python.hub")


######  send a message #######
bot.send_message("Hello from Rahul", ['user1','user2'])

######  get follower info #######
my_followers = bot.get_user_followers("irahulbairagi")
for follower in my_followers:
    print(follower)
    print(bot.get_user_info(follower))
    
######  get following info #######
my_following = bot.get_user_following("irahulbairagi")
for following in my_following:
    print(follower)
    print(bot.get_user_info(following))    

bot.unfollow_everyone()