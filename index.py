from config import *
from musica import *
from animal import *
from datetime import date, datetime
from twitchio.ext import commands


class Bot(commands.Bot):

    def __init__(self):
        super().__init__(irc_token=TOKEN, nick='COLOQUE O SEU NICK AQUI', prefix='!',
                         initial_channels=['COLOQUE O SEU CANAL CAQUI'])

# inicia os arquivos first.txt e divulga.txt junto com o bot e cria uma copia local
# adiciona a data atual caso o valor na primeira posição for diferente ou se a lista estiver vazia
        with open ("first.txt", "r", encoding="utf-8") as file:
            self.lista = file.readlines()
            self.data = str(date.today())
            if not len(self.lista) or self.lista[0] != self.data+"\n" :
                with open ("first.txt", "w") as file:
                    file.write(self.data + "\n")
                self.lista = [self.data]

        with open ("divulga.txt", "r") as file:
            self.divulga = file.readlines()
            if not len(self.divulga) or self.divulga[0] != self.data+"\n" :
                with open ("divulga.txt", "w") as file:
                    file.write(self.data+"\n")
                self.divulga = [self.data]
            



    # Events don't need decorators when subclassed
    async def event_ready(self):
        print(f'Ready | {self.nick}')
        
    async def event_message(self, message):
        print(message.author, message.content)
        await self.handle_commands(message)

    



    async def event_message(self, message):
        print(message.author, message.content)
        await self.handle_commands(message)

        if message.content:
            nome = f'{message.author.name}\n'
            sh = nome.rstrip('\n')
            if nome not in self.divulga:
                self.divulga.append(nome)
                with open ("divulga.txt", "a", encoding="utf-8") as file:
                    file.write(nome)
                if msgDivulga.get(sh):
                    await message.channel.send(f"{msgDivulga[sh]}")
                    # await message.channel.send(f"!sh {sh}")
                else:
                    await message.channel.send(f"Olá {sh}! Boas vindas <3")


                


    # Commands use a decorator...

    @commands.command(name='first')
    async def first(self, ctx):
        nome = f'{ctx.author.name}\n'
        if nome not in self.lista:
            self.lista.append(nome)
            with open ("first.txt", "a", encoding="utf-8") as file:
                file.write(nome)
            if len(self.lista)-1 == 1:
                await ctx.send(f'{ctx.author.name} Parabéns, chegou cedo Kappa')
            else:
                await ctx.send(f'{ctx.author.name} Hoje não, você foi o {len(self.lista)-1}º')

            return
        await ctx.send(f'{ctx.author.name} Você ja está na lista ')
    
    @commands.command(name='projeto')
    async def projeto(self, ctx):
        await ctx.send(f'/me - {ctx.author.name} - Implementar comandos no bot ')

# Jogo criado a partir de uma lista de regras
# Até hoje não entendi xD

    @commands.command(name='craps')
    async def craps(self, ctx):
        nJogada = 1
        ponto = 0
        while True:
            d1 = random.randint(1,7)
            d2 = random.randint(1,7)
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
        #-----------------------------------------------------
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
    

    @commands.command(name='obrigada')
    async def obrigada(self, ctx):
        subs = ctx.content.split('@' if '@' in ctx.content else None)[1]
        await ctx.send(f'/me @{subs} 𝑀𝓊𝒾𝓉𝑜 𝑜𝒷𝓇𝒾𝑔𝒶𝒹𝒶 𝓅𝑒𝓁𝑜 𝒶𝓅𝑜𝒾𝑜!! ')
        await ctx.send('2020Celebrate 2020Rivalry VirtualHug 2020Celebrate 2020Rivalry VirtualHug 2020Celebrate 2020Rivalry VirtualHug 2020Celebrate 2020Rivalry VirtualHug 2020Celebrate 2020Rivalry VirtualHug')

    @commands.command(name='caverna')
    async def caverna(self, ctx):
        await ctx.send(f'Uma comunidade voltada para programação em geral com o objetivo de ajudar uns aos outros, estudar coletivamente, e outros. http://caverna.live/discord PowerUpL Por favor, não se esqueça de passar no canal #🆁🅴🅶🆁🅰🆂 para liberar o acesso á todas as salas do nosso servidor PowerUpR')

    
    @commands.command(name='dance')
    async def dance(self, ctx):
        await ctx.send(f'2020Pajamas 2020Party 2020Pajamas 2020Party 2020Pajamas 2020Party 2020Pajamas 2020Party 2020Pajamas 2020Party 2020Pajamas 2020Party 2020Pajamas 2020Party 2020Pajamas 2020Party 2020Pajamas 2020Party 2020Pajamas 2020Party ')

    @commands.command(name='comandos')
    async def comandos(self, ctx):
        await ctx.send(f'Comandos: LISTA DE COMANDOS ')

# Acessa a lista musica.py e retorna um dos indices, aleatóriamente
    @commands.command(name='musica')
    async def musica(self, ctx):
        msg = random.choice(a)
        await ctx.send(f'/me {ctx.author.name} - {msg}. SingsNote')

# Acessa a lista animal.py e retorna um dos indices, aleatóriamente
    @commands.command(name='animal')
    async def animal(self, ctx):
        msg = random.choice(b)
        await ctx.send(f'{ctx.author.name} seu bichinho é: {msg}')
    

    async def event_command_error(self,ctx,error):
        print(error)
        pass


bot = Bot()
bot.run()