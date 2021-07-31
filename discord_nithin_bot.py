from random import randint

import discord,time

global friends,target_name,audio_source,server_id
##########################################################
friends = ["Phantom_Blaze"] # Here you put the IDs of the people you consider as friends
target_name = "sample"
audio_source = [["audio1.mp3",3],["audio2.mp3",9]]#[your audio file,length of audio file]

##########################################################
server_id = "Your Server iD"

client = discord.Client()
with open('token.txt','r') as f:
    token = f.readline()

@client.event
async def on_ready():
    print("\njoined succesfully")
    guild = client.get_guild(server_id)

@client.event
async def on_voice_state_update(member, before, after):
    channel = after.channel # Voice channel
    bot_connection = member.guild.voice_client

    if channel and member.name in friends and channel != "AFK":
        if bot_connection:
            # Move to new channel if bot was connected to a previous one
            await bot_connection.disconnect()
            vc = await channel.connect()
            r = randint(0,len(audio_source)-1)
            vc.play(
                discord.FFmpegPCMAudio(source=audio_source[r][0]))
            vc.source = discord.PCMVolumeTransformer(vc.source)
            vc.source.volume = 6
            time.sleep(audio_source[r][1])
            await vc.disconnect()
        else:
            # If bot was not connected, connect it
            vc = await channel.connect()
            r = randint(0, len(audio_source) - 1)
            vc.play(
                discord.FFmpegPCMAudio(source=audio_source[r][0]))
            vc.source = discord.PCMVolumeTransformer(vc.source)
            vc.source.volume = 6
            time.sleep(audio_source[r][1])
            await vc.disconnect()

    if not channel and bot_connection: # Disconnect if member has left
        await bot_connection.disconnect()

@client.event
async def on_member_update(before, after):
    n = after.nick
    if n: # Check if they updated their username
        if n != target_name: # If username contains tim
            # Otherwise set it to "NO STOP THAT"
            await after.edit(nick=target_name)

client.run(token)
