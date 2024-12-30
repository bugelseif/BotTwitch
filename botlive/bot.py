from functools import wraps

from twitchio.ext import commands

from .config import BOTS, TOKEN, USERNAME
from.tempo import clima_mensagem
from .craps import craps
from .divulgation import Divulgation
from .one_per_live import OnePerLive
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
        # Initialise our Bot with our access token, prefix and a list of channels to join on boot...
        # prefix can be a callable, which returns a list of strings or a string...
        # initial_channels can also be a callable which returns a list of strings...
        super().__init__(token=TOKEN, prefix='!', initial_channels=[USERNAME])

        self.first = OnePerLive('first.tmp')
        self.hello = OnePerLive('hello.tmp')
        self.divulgation = Divulgation('divulgation.ini')
        self.turtle = None


    async def event_ready(self):
        # Notify us when everything is ready!
        # We are logged in and ready to chat and use commands...
        print(f'Logged in as | {self.nick}')

    async def event_message(self, message):
        # Messages with echo set to True are messages sent by the bot...
        # For now we just want to ignore them...
        if message.echo:
            return

        # Print the contents of our message to console...
        print(f"{message.author.name}: {message.content}")

        await self.handle_commands(message)
        await self.handle_hello(message)   
        
    # Handles

    async def handle_hello(self, message):
        name = message.author.name
        if message.content and name not in BOTS and self.hello.add(name):
            await message.channel.send(
                self.divulgation.get_message(name, f'{name} boas-vindas! <3')
            )

    # Commands ------------------

    @commands.command(name='comandos')
    async def cmd_comandos(self, ctx):
        comandos = list(self.commands.keys())
        await ctx.send(f'Comandos: {" | ".join(comandos)}')

    @commands.command(name='codeshow')
    async def cmd_codeshow(self, ctx: commands.Context):
        await ctx.send(f'{ctx.author.name}: @codeshow canal é um coletivo de criadores de conteúdo educacional voltado para programação. Inscava-se: https://www.youtube.com/@codeshowbr')

    @commands.command(name='cumbucadev')
    async def cmd_cumbucadev(self, ctx: commands.Context):
        await ctx.send(f'{ctx.author.name}: CumbucaDev é uma iniciativa que promove a diversidade em tecnologia com educação e código aberto. Minorias no topo! Inscava-se: https://www.youtube.com/@CumbucaDev')

    @commands.command(name='feministech')
    async def cmd_feministech(self, ctx: commands.Context):
        await ctx.send(f'{ctx.author.name}: Feministech é uma comunidade feminista de mulheres cis e trans e pessoas não-binárias que compartilham conhecimento sobre tecnologia. Conheça nossas redes: https://feministech.com.br/')

    @commands.command(name='clima')
    async def cmd_clima(self, ctx: commands.Context):
        cidade = ctx.message.content.strip("!clima ")
        await ctx.send(f'{ctx.author.name}: {clima_mensagem(cidade)}')

    @commands.command(name='craps')
    async def cmd_craps(self, ctx: commands.Context):
        await ctx.send(f'{ctx.author.name}: {craps()}')
    
    @commands.command(name='love')
    async def cmd_wee(self, ctx: commands.Context):
        await ctx.send('💖💖💖')
        await ctx.send('🧡🧡🧡')
        await ctx.send('💛💛💛')
        await ctx.send('💚💚💚')
        await ctx.send('💙💙💙')
        await ctx.send('💜💜💜')

    @commands.command(name='redes')
    async def cmd_redes(self, ctx: commands.Context):
        await ctx.send(f'{ctx.author.name}: Siga nas redes: Github: https://github.com/bugelseif | LinkedIn: https://www.linkedin.com/in/bugelseif/ | Colabi: https://colabi.io/members/bugelseif/')

    @commands.command(name='pix')
    async def cmd_pix(self, ctx: commands.Context):
        await ctx.send(f'{ctx.author.name}: https://livepix.gg/bugs')


    # Joguinho -----------------

    @commands.command(name='start')
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
    async def cmd_cor(self, ctx: commands.Context):
        change = ctx.message.content.split()
        color = change[1]
        self.turtle.color(color)

    @commands.command(name='andar')
    async def cmd_andar(self, ctx: commands.Context):
        move = ctx.message.content.split()
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
