import discord
from discord.ext import commands
import random
import datetime
import time,os


bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())
welcome_message = 'Добро пожаловать на наш сервер,{member.mention}! Мы рады видеть тебя.'


@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')


@bot.event
async def on_member_join(member):
    role = discord.utils.get(member.guild.roles,name = 'Новенький')
    await member.add_roles(role)
    

@bot.event
async def on_member_join(member):
    greet = welcome_message.format(member = member)
    await member.send(greet)


def generator_pass(pass_length = 10):
    elements = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    password = ""

    for i in range(pass_length):
        password += random.choice(elements)

    return password
    

@bot.command()
async def password(ctx):
    password = generator_pass()
    await ctx.send(password)


@bot.command()
async def game(ctx,player):
        comp = random.randint(1,3)
        if comp == 1:
            comp = "камень"
        elif comp ==2:
            comp = "ножницы"
        elif comp == 2:
            comp = "ножницы"
        else:
            comp = "бумага"
        await ctx.send(f"Компьютер выбрал: {comp}")
        if ((player == "камень" and comp == "ножницы") or (player == "ножницы" and comp == "бумага") or (player  == "бумага" and comp == "камень")):
            time.sleep(1)
            await ctx.send("You win")
        elif ((player == "камень" and comp == "камень") or (player == "ножницы" and comp == "ножницы") or (player  == "бумага" and comp == "бумага")):
            time.sleep(1)
            await ctx.send("Ничья!")
        else:
            time.sleep(1)
            await ctx.send("You lost")


@bot.command()
async def clear(ctx,ammount = 100):
    await ctx.channel.purge(limit = ammount + 1)
    await ctx.send(f"Успешно удаленно {ammount} сообщений ")
    

@bot.command()
async def ping(ctx):
    await ctx.send('pong!')


@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)


@bot.command()
async def hello(ctx):
    await ctx.send(f'Привет {ctx.author.mention}! Я {bot.user}!')


@bot.command()
async def coinflip(ctx):
    result = random.randint(0,1)
    if result == 0:
        coin = "орел"
    else:
        coin = "решка"
    await ctx.send(f"Выпал(а) {coin}")


@bot.command()
async def animals_meme(ctx):
    list_img = os.listdir('images2')
    img_name = random.choice(list_img)
    with open (f'images2/{img_name}', 'rb') as file:
        img = discord.File (file)
    await ctx.send(file=img)


@bot.command()
async def meme(ctx):
    list_img = os.listdir('images')
    img_name = random.choice(list_img)
    with open (f'images/{img_name}', 'rb') as file:
        img = discord.File (file)
    await ctx.send(file=img)


@bot.command()
async def date(ctx):
    now = datetime.datetime.now()
    await ctx.send(now)


@bot.command()
@commands.has_permissions(administrator = True)
async def kick(ctx , member:discord.Member,reason = None):
    await member.kick( reason = reason )
    await ctx.send(f"участник {member.mention} был кикнут ")


@bot.command()
@commands.has_permissions(administrator = True)
async def ban(ctx , member:discord.Member,reason = None):
    await member.ban( reason = reason )
    await ctx.send(f"участник {member.mention} был забанен ")


@bot.command()
async def embed(ctx):
    embed = discord.Embed(title = "botinok pro",description ='creator : meliodas.def ,Youtube channel:[Click here](https://youtu.be/dQw4w9WgXcQ?si=68dvtlEqQ2QVK9Y2) '  , color = discord.Color.random() )
    embed.set_image(url = "https://yt3.googleusercontent.com/ytc/AMLnZu8OTQ4CsqMVKAiNU4gMgsxd2DRSkh89JpHEFcagTw=s900-c-k-c0x00ffffff-no-rj")
    embed.set_thumbnail(url = "https://yt3.googleusercontent.com/ytc/AMLnZu8OTQ4CsqMVKAiNU4gMgsxd2DRSkh89JpHEFcagTw=s900-c-k-c0x00ffffff-no-rj")
    await ctx.send(embed = embed)


@bot.command()
async def joined(ctx,who:discord.Member):
    await ctx.send( who.joined_at)

@bot.command()
async def right_way(ctx):
    await ctx.send("Привет!Ты знаешь что окружающая среда загрязняется?Я дам тебе пару советов о том, как ты можешь помочь окружающей среде.Если ты хочешь,чтобы мир стал лучше, напиши команду !do_it")


@bot.command()
async def do_it(ctx):
    list_img = os.listdir('images3')
    img_name = random.choice(list_img)
    with open (f'images3/{img_name}', 'rb') as file:
        img = discord.File (file)
    await ctx.send(file=img)
    

@bot.command()
async def check_it(ctx):
    fact1 = "Ученые из нидерландского Утрехтского университета выяснили, что ежегодно в Мировой океан попадает около 500 тыс. т пластикового мусора. На сегодняшний день его общее количество в водах оценивается более чем в 25 млн т, причем большая часть фрагментов плавает на поверхности океана на протяжении десятилетий."
    fact2 = 'Среднее время разложения пластмассовых изделий, созданных по разным технологиям, колеблется от 400 до 700 лет. Полиэтиленовые пакеты, которые повседневно используются людьми, в природе разлагаются от 100 до 200 лет. Это обратная сторона прочности и долговечности пластиковых изделий. При этом стеклянная бутылка может разлагаться до 1 млн лет.'
    fact4 = 'Из одного дерева можно получить 50-120 кг бумаги в зависимости от размера и породы дерева (чаще используются сосна, береза и осина). С учетом потерь одно дерево будет спасено примерно 60-100 кг макулатуры.'
    fact3 = 'Во всем мире каждый год более 100000 млекопитающих, птиц и рыб погибают из-за выброшенных полиэтиленовых пакетов. Животные съедают их или задыхаются.'
    list = [fact1,fact2,fact3,fact4]
    random_fact = random.choice(list)
    await ctx.send(random_fact)


@bot.command()
async def how_many(ctx,items):
    facts = {
        "железная":"10 лет",
        "фольга" :'100 лет',
        'резина' : '100 лет',
        'пластик' : '100 лет'

    }
    if items in facts.keys():
        await ctx.send(facts[items])
    else:
        await ctx.send("Такого слова нет в словаре!")

bot.run("MTE2MDE3NzY0NjI2OTkwNjk3NQ.GzmvTF.yD2jYWcf-WSouUTXxkKP-pGEj8hTzUULftDyq0")