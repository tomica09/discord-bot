import discord
import asyncio
import datetime
import pytz

client =discord.Client()

token = 'ODUxNjY1NTIzODQyNDgyMTc3.YL7lVA.U4Sy5ZrrRQ0QQwR7SfFByJmy37Q'

@client.event
async def on_ready():

    print(client.user.name)
    print('성공적으로 봇이 시작되었습니다')
    game = discord.Game('사나고샵 광고에요! 우잉')
    await client.change_presence(status=discord.Status.online, activity=game)

@client.event
async def on_message(message):
    if message.content == "징어야":
        await message.channel.send("네!")

    if message.content == "징어야 낚시":
        await message.channel.send("낚시는 간징어나 이프한테 시키셈")
    
    if message.content =='임베드 내놔':
        embed = discord.Embed(title='시른데요', description='헤헷')
        embed.set_footer(text='메에롱')
        await message.channel.send(embed=embed)

    if message.content == '&이프':
        embed = discord.Embed(title='묵납자루를 낚았다! 전설전설전설', description='전설전설전설전설')
        embed.set_thumbnail(url='https://media.discordapp.net/attachments/842356270803845120/848726187802099712/fishcard.png')
        await message.channel.send(embed=embed)

    if message.content == '임베드':
        embed = discord.Embed(title='제목', description='부제목', timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x00ff00)

        embed.add_field(name='임베드라인 1 -inline =false로 책정', value='라인 이름에 해당하는 값', inline=False)

        embed.set_footer(text='Bot made by. 요란해물고기', icon_url='https://cdn.discordapp.com/emojis/834425885926621255.png?v=1')
        embed.set_thumbnail(url='https://tenor.com/view/ko-scream-fish-bricked-spongebob-gif-15821831')
        await message.channel.send (embed=embed)


    if message.content.startswith ("청소해라"):
        i = (message.author.guild_permissions.administrator)

        if i is True:
            amount = message.content[4:]
            await message.channel.purge(limit=1)
            await message.channel.purge(limit=int(amount))

            embed = discord.Embed(title="메시지 삭제 알림", description="최근 디스코드 채팅 {}개가\n관리자 {}님의 요청으로 인해 정상 삭제 조치 되었습니다".format(amount, message.author), color=0x000000)
            embed.set_footer(text="Bot Made by. 요롼해물고기", icon_url="https://images-ext-1.discordapp.net/external/36GnGqJIv2fpKJGu1NyGswlsZv8uaOCVlMWNcCD632c/https/media.discordapp.net/attachments/842356270803845120/848726187802099712/fishcard.png")
            await message.channel.send(embed=embed)
        
        if i is False:
            await message.channel.purge(limit=1)
            await message.channel.send("{}, 당신은 명령어를 사용할 수 있는 권한이 없습니다".format(message.author.mention))



    if message.content.startswith ("!공지임"):
        i = (message.author.guild_permissions.administrator)
        if i is True:
            notice = message.content[5:]
            channel = client.get_channel(765191971576741928)
            embed = discord.Embed(title="'공지사항 제목 (볼드)'", description="공지사항 내용은 항상 숙지 해주시기 바랍니다\n――――――――――――――――――――――――――――\n\n{}\n\n――――――――――――――――――――――――――――".format(notice),timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x00ff00)
            embed.set_footer(text="Bot Made by. 바코드 #1741 | 담당 관리자 : {}".format(message.author))
            await message.channel.send("**[ BOT 자동 알림 ]** | 정상적으로 공지가 채널에 작성이 완료되었습니다 : )\n\n[ 기본 작성 설정 채널 ] : {}\n[ 공지 발신자 ] : {}\n\n[ 내용 ]\n{}".format(channel, message.author, notice))
            await message.channel.send(embed=embed)
        if i is False:
            await message.channel.send("{}, 당신은 관리자가 아닙니다".format(message.author.mention))

    
client.run(token)