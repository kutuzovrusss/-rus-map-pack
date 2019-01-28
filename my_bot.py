import discord

client = discord.Client()

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('!help'):
        msg = 'Currently available commands are: ' \
              '\n' \
              '\n- !cmpmappack ' \
              '\n- !getfh2 ' \
              '\n- !dl ' \
              '\n- !drive '.format(message)
        await client.send_message(message.channel, msg)
    #elif message.content.startswith ('!bot'):
        #await client.send_message(message.channel, "You rang?")
    if message.content.startswith('!dl'):
        msg = 'Updater is always having the latest version, preferably use that to save on download size!' \
        '\n' \
        '\nLatest map:' \
        '\nhttps://dl.cmp-gaming.com/updater/cmp_t/full/cmp_t_midway-c4.1.zip' \
        '\nLatest mod:' \
        '\nhttps://dl.cmp-gaming.com/updater/cmp_t/full/minimod.zip '.format(message)
        await client.send_message(message.channel, msg)
    if message.content.startswith('!getfh2'):
        msg = 'Get FH2 at http://www.playfh2.com/'.format(message)
        await client.send_message(message.channel, msg)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run('NTM4MjIxNTIzMDczMzY4MDY0.Dy31Iw.ghN_8KXjV-rIoJAwDPOd8wid-cM')
