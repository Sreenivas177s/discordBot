import discord
import asyncio

global friends,target_name,audio_source
friends = ["Phantom_Blaze"]
target_name = "sample"# Here you put the IDs of the people you consider as friends
audio_source = "audio1.mp3"

client = discord.Client()


@client.event
async def on_ready():
    print("\njoined succesfully")
    guild = client.get_guild(673112955381874715)
@client.event
async def on_voice_state_update(member, before, after):
    channel = after.channel # Voice channel
    bot_connection = member.guild.voice_client


    # Bot connection

    if channel and member.name in friends:
        if bot_connection:
            # Move to new channel if bot was connected to a previous one
            vc = await bot_connection.move_to(channel)
            vc.play(discord.FFmpegPCMAudio(source=audio_source))
        else:
            # If bot was not connected, connect it
            vc = await channel.connect()
            vc.play(discord.FFmpegPCMAudio(source=audio_source))

    if not channel and bot_connection: # Disconnect if member has left
        await bot_connection.disconnect()
@client.event
async def on_member_update(before, after):
    n = after.nick
    if n: # Check if they updated their username
        if n != target_name: # If username contains tim
            # Otherwise set it to "NO STOP THAT"
            await after.edit(nick=target_name)
client.run("ODA5NzcyNjM2MDg2NzMwNzgy.YCZ9iQ.v0GaHKyG0RIpJSIb2P5YqbDFvcs")
