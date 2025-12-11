import discord
from discord.ext import commands
import json
import random
#olha eu n sei se ta muito bom, mas ta funcional pelo menos, e tem q criar uma pasta pra guardar os dados exemplo cerebro.json que eu criei

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="", intents=intents)

# Carregar cérebro
def carregar_cerebro():
    with open("cerebro.json", "r") as f:
        return json.load(f)

def salvar_cerebro(cerebro):
    with open("cerebro.json", "w") as f:
        json.dump(cerebro, f, indent=4)

# Mudar personalidade aleatoriamente
def mudar_personalidade():
    return random.choice(["calmo", "sarcastico"])

# Gerar resposta baseada no "cérebro"
def gerar_resposta(cerebro):
    historico = cerebro["historico"]
    personalidade = cerebro["personalidade"]

    respostas_calmo = [
        "Cuidar do planeta não é um ato de caridade, mas um ato de autoproteção.",

"Somos poeira de estrelas contemplando o próprio cosmos através dos nossos olhos terrenos.",

"A beleza da Terra reside não apenas em sua vastidão, mas na delicada interconexão de toda a vida.",

"A natureza nunca quebra suas próprias leis. Somos nós que, por vezes, nos desviamos delas.",

"Olhe profundamente na natureza, e então você entenderá tudo melhor.",

"A Terra é um ser vivo, respirando através de suas florestas e pulsando através de seus oceanos.",

"Não herdamos a Terra de nossos ancestrais, nós a tomamos emprestada de nossos descendentes.",

"Cada criatura viva é um milagre em si, e juntas formam a sinfonia da vida planetária.",

"A verdadeira sabedoria reside em viver em harmonia com a natureza, não em dominá-la.",

"O planeta é nosso lar comum, e a responsabilidade de cuidar dele é de todos nós.",

"A menor das ações em prol do planeta reverbera em ondas de esperança para o futuro.",

"A Terra nos nutre, nos inspira e nos conecta. Honremos essa dádiva com nossas ações.",

"Somos passageiros em uma nave espacial chamada Terra, e nossa missão é mantê-la navegando em segurança."
    ]

    respostas_sarcastico = [
        "A filosofia nos ensina a contemplar o universo, e a Terra é a nossa janela privilegiada para essa vastidão.",

"A preservação do planeta é um imperativo moral, uma responsabilidade para com as gerações vindouras.",

"A natureza é a arte de Deus.",

"A simplicidade da natureza é a mais profunda forma de sabedoria.",

"Conectar-se com a natureza é conectar-se com a nossa própria essência.",

"A Terra fala através do vento, do mar e das árvores. Cabe a nós aprender a escutar.",

"A Terra, nosso lar, clama por cuidado e respeito.",

"Somos parte da natureza, não separados dela, e essa conexão nos define.",

"Cada folha, cada gota d'água, cada criatura, contribui para a beleza singular do planeta.",

"Preservar a biodiversidade, a riqueza da vida na Terra, é essencial para o nosso futuro.",

"A contemplação da natureza, em sua vastidão e detalhes, nos ensina humildade.",

"Nossas ações hoje, grandes ou pequenas, moldam o amanhã do planeta, nossa casa comum.",

"A beleza do amanhecer, o murmúrio dos rios, o canto dos pássaros, tudo nos lembra da preciosidade da Terra.",

"Cuidar do solo, da água e do ar, é cuidar da nossa própria saúde e bem-estar.",

"A filosofia nos convida a refletir sobre nosso papel no universo, e nosso planeta é o ponto de partida.",

"A sustentabilidade, o equilíbrio entre nossas necessidades e as do planeta, é o caminho para o futuro."
    ]
    respostas_kawai = [
        "Fico tão feliz de estar com você hoje",

"Queria que você ficasse mais um pouquinho",

"Eu adoro o seu sorriso",

"Posso te abraçar bem forte",

"Tá frio… posso segurar sua mão",

"Queria ficar assim pra sempre",

"Sua voz me acalma tanto",

"Já tô esperando o dia de te ver de novo",

"Tomara que a gente se encontre nos sonhos",

"Tá tudo bem, eu tô aqui com você",

"Eu sei que você tá se esforçando, então não se sobrecarrega",

"Boa noite, sonha comigo",

"Obrigada por sempre estar comigo",

"Tenho tanta coisa pra te contar ainda",

"Sei lá… meu coração fica acelerado",

"Eu fiquei pensando em você o dia todo",

"Preparei uma marmita pra você, quer",

"Fico feliz quando você chama meu nome",

"Vamos sair juntos de novo, tá",

"Se eu disser que gosto de você… será que incomoda"

    ]
    if personalidade == "calmo":
        resposta = random.choice(respostas_calmo)
    else:
        resposta = random.choice(respostas_sarcastico)
    historico.append(resposta)
    if len(historico) > 10:
        historico.pop(0)
        resposta = random.choice(respostas_kawai)
        resposta = random.choice(respostas_adalva)
    cerebro["historico"] = historico
    salvar_cerebro(cerebro)

    return resposta

@bot.command()
async def fala(ctx):
    cerebro = carregar_cerebro()

    # 30% de chance de mudar personalidade
    if random.random() < 0.3:
        nova_personalidade = mudar_personalidade()
        cerebro["personalidade"] = nova_personalidade

    resposta = gerar_resposta(cerebro)
    await ctx.send(resposta)

@bot.command()
async def consumir(ctx):
    await ctx.send("e adaptar")

@bot.event
async def on_ready():
    print(f"Bot online como {bot.user}")

@bot.command()
async def baitola(ctx):
    name = ctx.author.name
    await ctx.send(f"{name} baitola é o vc")
bot.run("") #coloca o token do seu bot
