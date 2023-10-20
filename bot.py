import discord
import random
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

facts = [
    # Çevre kirliliği nedir?
    "Çevre kirliliği, insan faaliyetleri sonucu çevreye verilen zarardır.",

    # Çevre kirliliğinin çeşitleri nelerdir?
    "Çevre kirliliği, hava, su ve toprak kirliliği olmak üzere üç ana başlıkta incelenebilir.",

    # Hava kirliliği nedir?
    "Hava kirliliği, fabrikalardan ve araçlardan çıkan gazların havaya karışmasıyla oluşur.",

    # Hava kirliliğinin nedenleri nelerdir?
    "Hava kirliliğinin nedenleri arasında fabrika bacalarından çıkan gazlar, araçlardan çıkan egzoz gazı, orman yangınları ve fosil yakıtların yakılması yer alır.",

    # Hava kirliliğinin etkileri nelerdir?
    "Hava kirliliğinin etkileri arasında insan sağlığına zarar verme, küresel ısınmaya neden olma ve bitki örtüsünü olumsuz etkileme yer alır.",

    # Su kirliliği nedir?
    "Su kirliliği, fabrikalardan ve evlerden çıkan atıkların su kaynaklarına karışmasıyla oluşur.",

    # Su kirliliğinin nedenleri nelerdir?
    "Su kirliliğinin nedenleri arasında fabrika atıkları, evsel atıklar, tarımdan kaynaklanan atıklar ve petrol sızıntıları yer alır.",

    # Su kirliliğinin etkileri nelerdir?
    "Su kirliliğinin etkileri arasında insan sağlığına zarar verme, su kaynaklarının tükenmesine neden olma ve balık ölümlerine neden olma yer alır.",

    # Toprak kirliliği nedir?
    "Toprak kirliliği, fabrikalardan ve evlerden çıkan atıkların toprağa karışmasıyla oluşur.",

    # Toprak kirliliğinin nedenleri nelerdir?
    "Toprak kirliliğinin nedenleri arasında fabrika atıkları, evsel atıklar, tarım ilaçları ve gübreler yer alır.",

    # Toprak kirliliğinin etkileri nelerdir?
    "Toprak kirliliğinin etkileri arasında bitki ve hayvanların yaşam alanlarını tehdit etme, besin maddelerinin azalmasına neden olma ve toprak verimliliğini düşürme yer alır.",

    # Çevre kirliliğini önlemek için neler yapılabilir?
    "Çevre kirliliğini önlemek için çevre dostu üretim yöntemleri kullanılmalı, atıklar geri dönüştürülmeli, enerji kaynaklarımız verimli kullanılmalı ve yenilenebilir enerji kaynaklarına yönelilmelidir.",

    # Çevre kirliliği ile mücadelede neler yapılıyor?
    "Çevre kirliliği ile mücadelede, çevre yasalarının ve yönetmeliklerinin uygulanması, çevre bilincinin artırılması ve yeni teknolojilerin geliştirilmesi gibi çalışmalar yapılmaktadır.",

    # Çevre kirliliğinin sonuçları nelerdir?
    "Çevre kirliliğinin sonuçları arasında insan sağlığının olumsuz etkilenmesi, doğal kaynakların tükenmesi ve iklim değişikliğinin hızlanması yer alır.",

    # Çevre kirliliği ile ilgili bazı istatistikler nelerdir?
    "Dünya Sağlık Örgütü'ne göre, her yıl hava kirliliği nedeniyle yaklaşık 7 milyon kişi hayatını kaybetmektedir.",

    # Çevre kirliliği ile ilgili bazı küresel sorunlar nelerdir?
    "Küresel ısınma, iklim değişikliği, ozon tabakasının incelmesi ve asit yağmuru, çevre kirliliği ile ilgili küresel sorunlar arasında yer almaktadır.",

    # Çevre kirliliği ile ilgili bazı yerel sorunlar nelerdir?
    "Su kirliliği, toprak kirliliği, hava kirliliği ve gürültü kirliliği, çevre kirliliği ile ilgili yerel sorunlar arasında yer almaktadır.",
 "Toprak kirliliği, fabrikalardan ve evlerden çıkan atıkların toprağa karışmasıyla oluşur. Toprak kirliliği, bitki ve hayvanların yaşam alanlarını tehdit eder ve besin maddelerinin azalmasına neden olur.",
]

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Merhaba {bot.user}! Ben bir botum!')

@bot.command()
async def fact(ctx):
        fact = random.choice(facts)
        await ctx.send(fact)







bot.run("gizli")