from functools import wraps

from twitchio.ext import commands

from .config import BOTS, TOKEN, USERNAME
from.tempo import clima_mensagem
from .craps import craps
from .divulgation import Divulgation
from .one_per_live import OnePerLive
from .turtleDraw import Bixinho
from .turtleChegada import Chegada
from .widget import add_task_to_html
from .espera import espera
from .perguntas import pergunta
from .contagem import contagem_regressiva


ja = []


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
        super().__init__(token=TOKEN, prefix='!', initial_channels=[USERNAME, "codeshow"])

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

    @commands.command(name='codeshow')
    async def cmd_codeshow(self, ctx: commands.Context):
        await ctx.send(f'''{ctx.author.name}: @codeshow canal é um coletivo 
        de criadores de conteúdo educacional voltado para programação. 
        Inscava-se: https://www.youtube.com/@codeshowbr''')

    @commands.command(name='cumbucadev')
    async def cmd_cumbucadev(self, ctx: commands.Context):
        await ctx.send(f'''{ctx.author.name}: CumbucaDev é uma iniciativa 
        que promove a diversidade em tecnologia com educação e código aberto. 
        Minorias no topo! Inscava-se: https://www.youtube.com/@CumbucaDev''')

    @commands.command(name='feministech')
    async def cmd_feministech(self, ctx: commands.Context):
        await ctx.send(f'''{ctx.author.name}: Feministech é uma comunidade 
        feminista de mulheres cis e trans e pessoas não-binárias que compartilham 
        conhecimento sobre tecnologia. Conheça nossas redes: https://feministech.com.br/''')

    @commands.command(name='clima')
    async def cmd_clima(self, ctx: commands.Context):
        cidade = ctx.message.content.strip("!clima ")
        await ctx.send(f'{ctx.author.name}: {clima_mensagem(cidade)}')

    # @commands.command(name='add')
    # async def cmd_add(self, ctx: commands.Context):
    #     tarefa = ctx.message.content.strip("!add")
    #     pessoa = ctx.author.name
    #     ftask = f"{pessoa}: {tarefa}"
    #     add_task_to_html(ftask)
    #     await ctx.send(f'{ctx.author.name}: tarefa "{tarefa}" adicionada.')

    @commands.command(name='presente')
    async def cmd_presente(self, ctx: commands.Context):
        if ctx.author.name in ja:
            await ctx.send(f'{ctx.author.name}: já está na sala.')
        else:
            espera(ctx.author.name)
            ja.append(ctx.author.name)
            await ctx.send(f'{ctx.author.name}: entrou na sala.')


    @commands.command(name='craps')
    async def cmd_craps(self, ctx: commands.Context):
        await ctx.send(f'{ctx.author.name}: {craps()}')

    @commands.command(name='telegram')
    async def cmd_telegram(self, ctx: commands.Context):
        await ctx.send(f'{ctx.author.name}: https://t.me/+VSGi9iZfQI83NGU5')

    @commands.command(name='rusty')
    async def cmd_rusty(self, ctx: commands.Context):
        await ctx.send(f'''{ctx.author.name} os comandos são: !join !leave !plant
        !water !harvest !biofuel !build !pick !feed !collect (or) !poop !fertilize 
        !bench (or) !sit !pink !blue !green !orange !red !purple !gray !gold''')
    
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
        await ctx.send(f'''{ctx.author.name}: Siga nas redes: 
        Github: https://github.com/bugelseif | 
        LinkedIn: https://www.linkedin.com/in/bugelseif/ | 
        Site: https://bugelseif.github.io/website/ | 
        Colabi: https://colabi.io/members/bugelseif/''')

    @commands.command(name='pix')
    async def cmd_pix(self, ctx: commands.Context):
        await ctx.send(f'{ctx.author.name}: https://livepix.gg/bugs')

    @commands.command(name='help')
    async def cmd_help(self, ctx: commands.Context):
        await ctx.send(f'{ctx.author.name}: Quer me ajudar a ir para a PyBR 2025? Você pode: •Enviar um pix: https://livepix.gg/bugs | •Deixar um sub/bits na live | •Ficar de lurk por aqui bugelsCore')


    # @commands.command(name='slide')
    # async def cmd_slide(self, ctx: commands.Context):
    #     await ctx.send(f'{ctx.author.name}: https://www.canva.com/design/DAGc9VA0YQI/BwiilhCEQMfze9pdwtpeLQ/view?utm_content=DAGc9VA0YQI&utm_campaign=designshare&utm_medium=link2&utm_source=uniquelinks&utlId=h4db5908967')


    @commands.command(name='post')
    async def cmd_post(self, ctx: commands.Context):
        await ctx.send(f'''{ctx.author.name}: Compartilha aí!
        Mastodon: https://bolha.us/@bug_elseif/114002805949088059 | 
        LinkedIn: https://www.linkedin.com/feed/update/urn:li:activity:7296180567652368384/ ''')
        
    @commands.command(name='pergunta')
    async def cmd_pergunta(self, ctx: commands.Context):
        mensagem = ctx.message.content[9:]
        pergunta(ctx.author.name, mensagem)
        await ctx.send(f'{ctx.author.name}: a sua pergunta entrou na lista.')

    @commands.command(name='pomo')
    @is_mod
    async def cmd_pomo(self, ctx: commands.Context):
        contagem = ctx.message.content.strip("!pomo ")
        await ctx.send(f'Começando foco de {contagem} minutos!')
        contagem_regressiva(int(contagem))
    
    # @commands.command(name='form')
    # async def cmd_form(self, ctx: commands.Context):
    #     await ctx.send(f'{ctx.author.name} quer receber o certificado de participação na live? Preencha o form: https://forms.gle/L5RAafMeFz1KQGjW7')


    # Joguinho -----------------

    # @commands.command(name='start')
    # @is_mod
    # async def cmd_startdraw(self, ctx):
    #     if self.turtle is None:
    #         print(self.turtle)
    #         self.turtle = Bixinho()
    #         print(self.turtle)

    # @commands.command(name='startchegada')
    # @is_mod
    # async def cmd_startchegada(self, ctx):
    #     if self.turtle is None:
    #         print(self.turtle)
    #         self.turtle = Chegada()
    #         print(self.turtle)

    # @commands.command(name='cor')
    # async def cmd_cor(self, ctx: commands.Context):
    #     change = ctx.message.content.split()
    #     color = change[1]
    #     self.turtle.color(color)

    # @commands.command(name='andar')
    # async def cmd_andar(self, ctx: commands.Context):
    #     move = ctx.message.content.split()
    #     direction = int(move[1])
    #     distance = int(move[2])
    #     self.turtle.walk(direction, distance)

    # @commands.command(name='stop')
    # @is_mod
    # async def cmd_stop(self, ctx):
    #     if self.turtle is not None:
    #         print(self.turtle)
    #         self.turtle.stop()
    #         self.turtle = None
    #         print(self.turtle)
