import random
from datetime import date

from twitchio.ext import commands

from .animal import b
from .config import BOTS, TOKEN, USERNAME
from .divulgation import Divulgation
from .musica import a
from .one_per_live import OnePerLive


def run():
    bot = Bot()
    bot.run()


class Bot(commands.Bot):

    def __init__(self):
        super().__init__(irc_token=TOKEN, nick=USERNAME, prefix='!',
                         initial_channels=[USERNAME])

        self.divulgation = Divulgation('divulgation.ini')
        self.hello = OnePerLive('hello.tmp')

        with open("first.txt", "r", encoding="utf-8") as file:
            self.lista = file.readlines()
            self.data = str(date.today())
            if not len(self.lista) or self.lista[0] != self.data+"\n":
                with open("first.txt", "w") as file:
                    file.write(self.data + "\n")
                self.lista = [self.data]

    async def obrigada(self, send_msg, user):
        await send_msg(f'/me @{user} 𝑀𝓊𝒾𝓉𝑜 𝑜𝒷𝓇𝒾𝑔𝒶𝒹𝒶 𝓅𝑒𝓁𝑜 𝒶𝓅𝑜𝒾𝑜!!')
        await send_msg('2020Celebrate 2020Rivalry VirtualHug ' * 4)


# ----------------------------------------------------------------------------------------------

    # Events don't need decorators when subclassed
    async def event_ready(self):
        print(f'Ready | {self.nick}')

    async def event_message(self, message):
        print(message.author.name, message.content)
        await self.handle_commands(message)

        if message.author.name == 'streamelements' and 'just raided the channel' in message.content:
            user = message.content.split()[0]
            await self.obrigada(message.channel.send, user)

        # ignora os bots
        if message.content:
            name = message.author.name
            if name not in BOTS and self.hello.add(name):
                await message.channel.send(self.divulgation.get_message(name, f"Olá {name}! Boas vindas <3"))

# Commands use a decorator...

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
        await ctx.send(f'{ctx.author.name}: A meta de arrecação de cestas basicas que serão doadas no final do mês de abril para o instituto dorvalino comandolli.')

    # @commands.command(name='numeros')
    # async def numeros(self, ctx):
    #     await ctx.send(f'{ctx.author.name}: Verifique seus números -> https://docs.google.com/spreadsheets/d/1CMO0ICGg4GFgT0AcdyLJiAL_VEP6REKftdwSPOYipVs/edit?usp=sharing |')

    # @commands.command(name='sorteio')
    # async def sorteio(self, ctx):
    #     await ctx.send(f'Meta de subs -> como participar? SUB/ BIT/ PONTOS | Meta de donate -> como participar? DONATE de qualquer valor | O que será sorteado? Dois chaveiros OU um quadrinho dos que eu produzo (stories -> instagram.com/bug.elseif/) | Foi a forma que eu encontrei de agradecer o apoio de todos vocês. MUITO OBRIGADA <3')

    @commands.command(name='projeto')
    async def projeto(self, ctx):
        await ctx.send(f'/me - {ctx.author.name} - Implementar comandos no bot ')

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
        await ctx.send(f'bugelsHappy bugelsHappy bugelsHappy bugelsHappy bugelsHappy bugelsHappy bugelsHappy bugelsHappy bugelsHappy bugelsHappy bugelsHappy bugelsHappy ')

    @commands.command(name='amor')
    async def amor(self, ctx):
        await ctx.send(f'bugelsPyLoves bugelsPyLoves bugelsPyLoves bugelsPyLoves bugelsPyLoves bugelsPyLoves bugelsPyLoves bugelsPyLoves bugelsPyLoves bugelsPyLoves bugelsPyLoves bugelsPyLoves bugelsPyLoves bugelsPyLoves bugelsPyLoves bugelsPyLoves bugelsPyLoves  ')

    @commands.command(name='raid')
    async def raid(self, ctx):
        await ctx.send(f'twitchRaid <3 bugelsPyLoves KPOPfan PansexualPride <3 bugelsPyLoves  KPOPfan PansexualPride <3 bugelsPyLoves KPOPfan PansexualPride <3 bugelsPyLoves KPOPfan PansexualPride <3 bugelsPyLoves  KPOPfan PansexualPride <3 bugelsPyLoves KPOPfan PansexualPride <3 bugelsPyLoves  KPOPfan PansexualPride <3 bugelsPyLoves KPOPfan PansexualPride <3 bugelsPyLoves KPOPfan PansexualPride <3 bugelsPyLoves  KPOPfan PansexualPride ')

    @commands.command(name='gank')
    async def gank(self, ctx):
        await ctx.send(f'twitchRaid KPOPfan bugelsHappy 2020Gift 2020Celebrate KPOPfan bugelsHappy 2020Gift 2020Celebrate KPOPfan bugelsHappy 2020Gift 2020Celebrate KPOPfan bugelsHappy 2020Gift 2020Celebrate KPOPfan bugelsHappy 2020Gift 2020Celebrate KPOPfan bugelsHappy 2020Gift 2020Celebrate KPOPfan bugelsHappy 2020Gift 2020Celebrate  ')

    @commands.command(name='alert')
    async def gank(self, ctx):
        await ctx.send(f'bugelsPyAlert bugelsPyAlert bugelsPyAlert bugelsPyAlert bugelsPyAlert bugelsPyAlert bugelsPyAlert bugelsPyAlert bugelsPyAlert bugelsPyAlert bugelsPyAlert bugelsPyAlert bugelsPyAlert bugelsPyAlert bugelsPyAlert')

    @commands.command(name='obrigada')
    async def cmd_obrigada(self, ctx):
        subs = ctx.content.split('@' if '@' in ctx.content else None)[1]
        await self.obrigada(ctx.send, subs)


    @commands.command(name='caverna')
    async def caverna(self, ctx):
        await ctx.send(f'Uma comunidade voltada para programação em geral com o objetivo de ajudar uns aos outros, estudar coletivamente, e outros. http://caverna.live/discord PowerUpL Por favor, não se esqueça de passar no canal #🆁🅴🅶🆁🅰🆂 para liberar o acesso á todas as salas do nosso servidor PowerUpR')


    @commands.command(name='dance')
    async def dance(self, ctx):
        await ctx.send(f'2020Pajamas 2020Party 2020Pajamas 2020Party 2020Pajamas 2020Party 2020Pajamas 2020Party 2020Pajamas 2020Party 2020Pajamas 2020Party 2020Pajamas 2020Party 2020Pajamas 2020Party 2020Pajamas 2020Party 2020Pajamas 2020Party ')


    @commands.command(name='comandos')
    async def comandos(self, ctx):
        await ctx.send('Comandos: !projeto | !craps | !musica | !animal |!caverna | !portfolio | emotes -> !bug | !alert | !obrigada @name | !raid | !gank | !amor | !dance ')


    @commands.command(name='musica')
    async def musica(self, ctx):
        msg = random.choice(a)
        await ctx.send(f'/me {ctx.author.name} - {msg}. SingsNote')

    @commands.command(name='animal')
    async def animal(self, ctx):
        msg = random.choice(b)
        await ctx.send(f'{ctx.author.name} seu bichinho é: {msg}')

    @commands.command(name='first')
    async def first(self, ctx):
        nome = f'{ctx.author.name}\n'
        if nome not in self.lista:
            self.lista.append(nome)
            with open("first.txt", "a", encoding="utf-8") as file:
                file.write(nome)
            if len(self.lista)-1 == 1:
                await ctx.send(f'{ctx.author.name} Parabéns, chegou cedo Kappa')
            else:
                await ctx.send(f'{ctx.author.name} Hoje não, você foi o {len(self.lista)-1}º')

            return
        await ctx.send(f'{ctx.author.name} Você ja está na lista ')

    async def event_command_error(self, ctx, error):
        print(error)
