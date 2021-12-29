from functools import wraps
from datetime import datetime

from twitchio.ext import commands

from .config import BOTS, PROJECT, TOKEN, USERNAME
from .craps import craps
from .divulgation import Divulgation
from .one_per_live import OnePerLive
from .random_list import RandomList
from .turtleDraw import Bixinho
from .turtleChegada import Chegada


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
        self.turtle = None

    # Scheduler
    # tine = sched.scheduler(time.time, time.sleep)
    # def print_tine(a='default'):
    #     print('from time', time.time(), a)


    # def print_some_tines():
    #     print(time.time())
    #     tine.enter(10,2,print_tine)
    #     tine.run(blocking=False)

    # print_some_tines()



    # Events

    async def event_ready(self):
        self.channel = self.get_channel(self.nick)

        print(f'Ready | {self.nick}')
        data = datetime.now().strftime('%H')
        print(data)

        # await self.channel.send('O bot chegou')

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
            a = self.divulgation.get_message(name)
            if a:
                await message.channel.send(a)

    # Actions

    async def gank(self):
        await self.channel.send('KPOPfan bugelsHappy 2020Gift 2020Celebrate ' * 6)

    async def obrigada(self, username):
        await self.channel.send_me(f'{username} 𝑀𝓊𝒾𝓉𝑜 𝑜𝒷𝓇𝒾𝑔𝒶𝒹𝒶 𝓅𝑒𝓁𝑜 𝒶𝓅𝑜𝒾𝑜!!')
        await self.channel.send('2020Celebrate 2020Rivalry VirtualHug ' * 4)

    async def raid(self):
        await self.channel.send('twitchRaid ' + '<3 KPOPfan PansexualPride ' * 6)

    # Commands

    @commands.command(name='comandos')
    async def cmd_comandos(self, ctx):
        await ctx.send(
            'Comandos: !animal | !caverna | !craps | !girls | !github | '
            ' !musica | !projeto | !portfolio | emotes -> !bug | !olhos | '
            '!obrigada @name | !raid | !gank | !dance '
        )

    @commands.command(name='ad')
    @is_mod
    async def cmd_ad(self, ctx):
        await ctx.send('/commercial 30')

    # @commands.command(name='agenda')
    # async def cmd_agenda(self, ctx):
    #     await ctx.send('!sh @syndai | Podcast - Fundação de Noxus | 22/05 às 14h')
    #     await ctx.send('Maratona lindissima | 29/05 às 12h')
    #     await ctx.send('!maratona')

    @commands.command(name='amor')
    async def cmd_amor(self, ctx):
        await ctx.send('GenderFluidPride NonBinaryPride PansexualPride '
        'AsexualPride TransgenderPride GayPride LesbianPride BisexualPride  ' * 4)
# ------------------------------------------------------------------------------------------------
    @commands.command(name='startdraw')
    @is_mod
    async def cmd_startdraw(self, ctx):
        if self.turtle is None:
            print(self.turtle)
            self.turtle = Bixinho()
            print(self.turtle)

    @commands.command(name='startchegada')
    @is_mod
    async def cmd_startchegada(self, ctx):
        if self.turtle is None:
            print(self.turtle)
            self.turtle = Chegada()
            print(self.turtle)

    @commands.command(name='cor')
    async def cmd_cor(self, ctx):
        change = ctx.content.split()
        color = change[1]
        self.turtle.color(color)

    @commands.command(name='andar')
    async def cmd_andar(self, ctx):
        move = ctx.content.split()
        direction = int(move[1])
        distance = int(move[2])
        self.turtle.walk(direction, distance)

    @commands.command(name='stop')
    @is_mod
    async def cmd_stop(self, ctx):
        if self.turtle is not None:
            print(self.turtle)
            self.turtle.stop()
            self.turtle = None
            print(self.turtle)
# ------------------------------------------------------------------------------------------------

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
                await ctx.send(f'!addpoints {username} 50')
            else:
                await ctx.send(f'{username} Hoje não, você foi o {first_len}º')
        else:
            await ctx.send(f'{username} Você já está na lista')

    @commands.command(name='gank')
    async def cmd_gank(self, ctx):
        await self.gank()


    @commands.command(name='geekgroup')
    async def cmd_geekgroup(self, ctx):
        username = ctx.author.name
        await ctx.send(f'{username} Somos um grupo de streamers '
        'voltado pra jogos e cultura geek no geral '
        '| conheça mais: https://www.geekgroup.info/quem-somos')

    @commands.command(name='feministech')
    async def cmd_feministech(self, ctx):
        await ctx.send('Somos um '
        'grupo mulheres e pessoas não binárias que compartilham o interesse '
        'por lives na Twitch e tecnologia no geral. | https://twitter.com/feministech ')

    @commands.command(name='github')
    async def cmd_github(self, ctx):
        await ctx.send_me('https://github.com/bugelseif')

    # @commands.command(name='meta')
    # async def cmd_meta(self, ctx):
    #     await ctx.send(
    #         f'{ctx.author.name}: '
    #     )

    # @commands.command(name='like')
    # async def cmd_like(self, ctx):
    #     await ctx.send_me(f'{ctx.author.name} - https://www.youtube.com/watch?v=SWOCvQhaK3k ')
    #     await ctx.send_me(f' https://www.youtube.com/watch?v=SWOCvQhaK3k ')
    #     await ctx.send_me(f' https://www.youtube.com/watch?v=SWOCvQhaK3k ')

    @commands.command(name='musica')
    async def cmd_musica(self, ctx):
        await ctx.send_me(f'{ctx.author.name} - {self.musics.get_random()}. SingsNote')

    # @commands.command(name='maratona')
    # async def cmd_maratona(self, ctx):
    #     await ctx.send(f'{ctx.author.name} - No dia 29/05/2021, às 12h00, daremos '
    #     ' início a III Edição da Maratona Live Coders Girls. Será um sábado de 12 horas '
    #     ' de conteúdo incrível feito pela própria comunidade para compartilhar '
    #     ' conhecimento, experiências e tudo que há de bom. <3 ')
    #     await ctx.send('https://maratona3.live/')

    @commands.command(name='obrigada')
    async def cmd_obrigada(self, ctx):
        msg = ctx.content.split()
        if len(msg) >= 2:
            username = msg[1].lstrip('@')
            await self.obrigada(username)

    @commands.command(name='olhos')
    async def cmd_olhos(self, ctx):
        await ctx.send('bugelsOlhos ' * 13)

    @commands.command(name='pix')
    async def cmd_pix(self, ctx):
        await ctx.send_me(f'{ctx.author.name} Chave pix -> bferreira.slv@gmail.com')

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

    @commands.command(name='wee')
    async def cmd_wee(self, ctx):
        # await ctx.send('/color red')
        await ctx.send('💖')
        # await ctx.send('/color orange')
        await ctx.send('🧡')
        # await ctx.send('/color yellow')
        await ctx.send('💛')
        # await ctx.send('/color green')
        await ctx.send('💚')
        # await ctx.send('/color blue')
        await ctx.send('💙')
        # await ctx.send('/color purple')
        await ctx.send('💜')
        # await ctx.send('/color #8E055A')
