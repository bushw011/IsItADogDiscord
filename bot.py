import discord
import os
from dotenv import load_dotenv
load_dotenv()
from isitdog import isItDog

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(context):
    image_url = context.attachments[0].url
    # detect last 3 or 4 characters of image url to see if it is jpg or jpeg
    # I wasn't initially sure how to detect if a message is an image. I borrow some code from this cool project I found: https://github.com/rossanodan/rossanodroid-py
    image_format_jpg = image_url[-3:]
    image_format_jpeg = image_url[-4:]
    if image_format_jpg.lower() == 'jpg' or image_format_jpeg.lower() == 'jpeg':
        #call api
        try:
            isitdog = isItDog()
            result = isitdog.dog_detector(image_url)
            await context.channel.send("this is a dog :)" if result else "this is not a dog :(")
        except:
            raise discord.DiscordException

client.run(os.getenv('TOKEN'))