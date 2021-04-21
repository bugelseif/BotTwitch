import random

from twitchio.ext import commands

from .config import BOTS, TOKEN, USERNAME
from .divulgation import Divulgation
from .one_per_live import OnePerLive
from .random_list import RandomList


def run():
    bot = Bot()
    bot.run()


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
        await self.channel.send_me(f'@{username} 𝑀𝓊𝒾𝓉𝑜 𝑜𝒷𝓇𝒾𝑔𝒶𝒹𝒶 𝓅𝑒𝓁𝑜 𝒶𝓅𝑜𝒾𝑜!!')
        await self.channel.send('2020Celebrate 2020Rivalry VirtualHug ' * 4)

    async def raid(self):
        await self.channel.send('twitchRaid' + '<3 bugelsPyLoves KPOPfan PansexualPride ' * 13)

    # Commands

    @commands.command(name='comandos')
    async def cmd_comandos(self, ctx):
        await ctx.send(
            'Comandos: !projeto | !craps | !musica | !animal | '
            '!caverna | !portfolio | emotes -> !bug | !alert | '
            '!obrigada @name | !raid | !gank | !amor | !dance '
        )

    @commands.command(name='animal')
    async def cmd_animal(self, ctx):
        await ctx.send(f'{ctx.author.name} seu bichinho é: {self.animals.get_random()}')

    @commands.command(name='caverna')
    async def cmd_caverna(self, ctx):
        await ctx.send(
            'Uma comunidade voltada para programação em geral com o objetivo de ajudar uns aos outros, '
            'estudar coletivamente, e outros. http://caverna.live/discord PowerUpL '
            'Por favor, não se esqueça de passar no canal #🆁🅴🅶🆁🅰🆂'
            'para liberar o acesso á todas as salas do nosso servidor PowerUpR'
        )

    @commands.command(name='first')
    async def cmd_first(self, ctx):
        username = ctx.author.name
        if not self.first.is_in(username):
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

    @commands.command(name='musica')
    async def cmd_musica(self, ctx):
        await ctx.send_me(f'{ctx.author.name} - {self.musics.get_random()}. SingsNote')

    @commands.command(name='obrigada')
    async def cmd_obrigada(self, ctx):
        subs = ctx.content.split('@' if '@' in ctx.content else None)[1]
        await self.obrigada(ctx.send, subs)

    @commands.command(name='raid')
    async def cmd_raid(self, ctx):
        await self.raid()

    @commands.command(name='ad')
    async def ad(self, ctx):
        if not ctx.author.is_mod:
            return
        await ctx.send('/commercial 30')

    @commands.command(name='sz')
    async def sz(self, ctx):
        if not ctx.author.is_mod:
            return
        name = ctx.content.split()
        await ctx.send(f'!sh-so {name[1]}')

    @commands.command(name='meta')
    async def meta(self, ctx):
        await ctx.send(
            f'{ctx.author.name}: A meta de arrecação de cestas basicas que serão '
            'doadas no final do mês de abril para o instituto dorvalino comandolli.'
        )

    @commands.command(name='projeto')
    async def projeto(self, ctx):
        await ctx.send(f'/me - {ctx.author.name} - Refactor do bot ')

    @commands.command(name='buzina')
    async def buzina(self, ctx):
        await ctx.send('pipi pipi fo fo fo fun')

    @commands.command(name='portfolio')
    async def portifolio(self, ctx):
        await ctx.send('/me https://bugelseif.github.io/portfolio/')

    @commands.command(name='craps')
    async def craps(self, ctx):
        nJogada = 1
        ponto = 0
        while True:
            d1 = random.randint(1, 7)
            d2 = random.randint(1, 7)
            soma = d1+d2
            if nJogada == 1 and (soma == 7 or soma == 11):
                mensagem = "2020Pajamas Parabéns!! | Pontos: 999 FortOne  2020Party "
                break
            elif nJogada == 1 and (soma == 2 or soma == 3 or soma == 12):
                mensagem = f"Craps - perdeu | Pontos = {ponto} NotLikeThis"
                break
            elif nJogada == 1 and (4 <= soma <= 6 or 8 <= soma <= 10):
                ponto += soma
                nJogada += 1
                continue
        # -----------------------------------------------------
            elif nJogada == 2:
                if soma == 7:
                    mensagem = f"Craps - perdeu | Pontos = {ponto} SeemsGood"
                    break
                else:
                    ponto += soma
                    nJogada += 1
                    continue
            elif nJogada > 2:
                if 4 <= soma <= 6 or 8 <= soma <= 10:
                    ponto += soma
                    nJogada += 1
                    continue
                else:
                    mensagem = f"Craps - perdeu | Pontos = {ponto} LUL"
                    break

        await ctx.send(f'{ctx.author.name}: {mensagem}')

    @commands.command(name='bug')
    async def bug(self, ctx):
        await ctx.send('bugelsHappy ' * 13)

    @commands.command(name='amor')
    async def amor(self, ctx):
        await ctx.send('bugelsPyLoves ' * 13)

    @commands.command(name='alert')
    async def alert(self, ctx):
        await ctx.send('bugelsPyAlert ' * 13)

    @commands.command(name='dance')
    async def dance(self, ctx):
        await ctx.send('2020Pajamas 2020Party ' * 13)
