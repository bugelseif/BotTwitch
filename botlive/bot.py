from functools import wraps

from twitchio.ext import commands

from .config import BOTS, PROJECT, TOKEN, USERNAME
from .craps import craps
from .divulgation import Divulgation
from .one_per_live import OnePerLive
from .random_list import RandomList


def run():
    bot = Bot()
    bot.run()


def is_mod(f):
    @wraps(f)
    async def wrapper(self, ctx):
        if ctx.author.is_mod:
            await f(self, ctx)
    return wrapper


class Bot(commands.Bot):
    def __init__(self):
        super().__init__(irc_token=TOKEN, nick=USERNAME, prefix='!', initial_channels=[USERNAME])

        self.animals = RandomList('animals.txt')
        self.divulgation = Divulgation('divulgation.ini')
        self.first = OnePerLive('first.tmp')
        self.hello = OnePerLive('hello.tmp')
        self.musics = RandomList('musics.txt')

    # Events

    async def event_ready(self):
        self.channel = self.get_channel(self.nick)

        print(f'Ready | {self.nick}')
        await self.channel.send('O bot chegou')

    async def event_usernotice_subscription(self, metadata):
        await self.obrigada(metadata.user.name)

    async def event_message(self, message):
        print(message.author.name, message.content)
        await self.handle_commands(message)
        await self.handle_raids(message)
        await self.handle_hello(message)

    async def event_command_error(self, ctx, error):
        print(error)

    # Handles

    async def handle_raids(self, message):
        if message.author.name == 'streamelements' and 'just raided the channel' in message.content:
            username = message.content.split()[0]
            await self.obrigada(username)
            await self.gank()
            await self.raid()

    async def handle_hello(self, message):
        name = message.author.name
        if message.content and name not in BOTS and self.hello.add(name):
            await message.channel.send(self.divulgation.get_message(name, f'Olá {name}! Boas vindas <3'))

    # Actions

    async def gank(self):
        await self.channel.send('KPOPfan bugelsHappy 2020Gift 2020Celebrate ' * 6)

    async def obrigada(self, username):
        await self.channel.send_me(f'{username} 𝑀𝓊𝒾𝓉𝑜 𝑜𝒷𝓇𝒾𝑔𝒶𝒹𝒶 𝓅𝑒𝓁𝑜 𝒶𝓅𝑜𝒾𝑜!!')
        await self.channel.send('2020Celebrate 2020Rivalry VirtualHug ' * 4)

    async def raid(self):
        await self.channel.send('twitchRaid ' + '<3 bugelsPyLoves KPOPfan PansexualPride ' * 5)

    # Commands

    @commands.command(name='comandos')
    async def cmd_comandos(self, ctx):
        await ctx.send(
            'Comandos: !projeto | !craps | !musica | !animal | '
            '!caverna | !portfolio | emotes -> !bug | !alert | '
            '!obrigada @name | !raid | !gank | !amor | !dance '
        )

    @commands.command(name='ad')
    @is_mod
    async def cmd_ad(self, ctx):
        await ctx.send('/commercial 30')

    @commands.command(name='alert')
    async def cmd_alert(self, ctx):
        await ctx.send('bugelsPyAlert ' * 13)

    @commands.command(name='amor')
    async def cmd_amor(self, ctx):
        await ctx.send('bugelsPyLoves ' * 13)

    @commands.command(name='animal')
    async def cmd_animal(self, ctx):
        await ctx.send(f'{ctx.author.name} seu bichinho é: {self.animals.get_random()}')

    @commands.command(name='bug')
    async def cmd_bug(self, ctx):
        await ctx.send('bugelsHappy ' * 13)

    @commands.command(name='caverna')
    async def cmd_caverna(self, ctx):
        await ctx.send(
            'Uma comunidade voltada para programação em geral com o objetivo de ajudar uns aos outros, '
            'estudar coletivamente, e outros. http://caverna.live/discord PowerUpL '
            'Por favor, não se esqueça de passar no canal #🆁🅴🅶🆁🅰🆂'
            'para liberar o acesso á todas as salas do nosso servidor PowerUpR'
        )

    @commands.command(name='craps')
    async def cmd_craps(self, ctx):
        await ctx.send(f'{ctx.author.name}: {craps()}')

    @commands.command(name='dance')
    async def cmd_dance(self, ctx):
        await ctx.send('2020Pajamas 2020Party ' * 13)

    @commands.command(name='first')
    async def cmd_first(self, ctx):
        username = ctx.author.name
        if username not in self.first:
            self.first.add(username)
            first_len = len(self.first)
            if first_len == 1:
                await ctx.send(f'{username} Parabéns, chegou cedo Kappa')
            else:
                await ctx.send(f'{username} Hoje não, você foi o {first_len}º')
        else:
            await ctx.send(f'{username} Você já está na lista')

    @commands.command(name='gank')
    async def cmd_gank(self, ctx):
        await self.gank()

    @commands.command(name='meta')
    async def cmd_meta(self, ctx):
        await ctx.send(
            f'{ctx.author.name}: A meta de arrecação de cestas basicas que serão '
            'doadas no final do mês de abril para o instituto dorvalino comandolli.'
        )

    @commands.command(name='musica')
    async def cmd_musica(self, ctx):
        await ctx.send_me(f'{ctx.author.name} - {self.musics.get_random()}. SingsNote')

    @commands.command(name='obrigada')
    async def cmd_obrigada(self, ctx):
        msg = ctx.content.split()
        if len(msg) >= 2:
            username = msg[1].lstrip('@')
            await self.obrigada(username)

    @commands.command(name='portfolio')
    async def cmd_portifolio(self, ctx):
        await ctx.send_me('https://bugelseif.github.io/portfolio/')

    @commands.command(name='projeto')
    async def cmd_projeto(self, ctx):
        await ctx.send_me(f'{ctx.author.name} - {PROJECT}')

    @commands.command(name='raid')
    async def cmd_raid(self, ctx):
        await self.raid()

    @commands.command(name='sz')
    @is_mod
    async def cmd_sz(self, ctx):
        name = ctx.content.split()
        await ctx.send(f'!sh-so {name[1]}')

    # @commands.command(name='buzina')
    # async def cmd_buzina(self, ctx):
    #     await ctx.send('pipi pipi fo fo fo fun')
