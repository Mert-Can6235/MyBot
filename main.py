import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')

@bot.command()
async def selam(ctx):
    await ctx.send(f'Merhaba! Ben {bot.user}, sana nasıl yardımcı olabilirim dostum (: ')
    await ctx.send(f'Lütfen komutunda ikiden fazla kelime varsa arasına uzun çizgi koy')
    await ctx.send(f'Ayrıca noktalama işareti ve büyük harf kullanma')

@bot.command()
async def kirlilik_nedir(ctx):
    await ctx.send(f'Dostum kirlilik biz insanoğlunun isteyerek yere attığı çopler veya insan oğlunun istemeden çevreyi kirletmesidir.')
    await ctx.send(f'Örneğin insanoğlu bir roket fırlatır ama roketin motorundan çıkan gazlar havayı kirletir;')
    await ctx.send(f've bu olur ):')

    with open('resimler/Çöplük.jpg', 'rb') as f:
        picture = discord.File(f)
        await ctx.send(file=picture)

@bot.command()
async def espiri_yap(ctx):
    await ctx.send(f'Çöp neden üzgünmüş?')
@bot.command()
async def neden(ctx):
    await ctx.send(f'İçini dökemediği için (:')
    await ctx.send(f'Ha ha ha')

@bot.command()
async def kirliliği_nasıl_önleyebilirim(ctx):
    await ctx.send(f'Bence bunun için en iyi yöntem geri gönüşüm')

    with open('resimler/geri dönüşüm.jpg') as f:
        resim = discord.File(f)
        await ctx.send(file=resim)
    
    await ctx.send(f'Geri dönüşüm kullanılmış kağıt, plastik, metal, cam ve pilleri yeniden kullanılmamış eşyelara dönüştürmektir.')
    await ctx.send(f'Bu nedenle geri dönüştürülebilecek atıkları atılacakları geri dönüşüm kutularına atmalıyız.')
    

@bot.command()
async def yakınımda_bir_geri_dönüşüm_kutusu_yoksa_ne_yapmalıyım(ctx):
    await ctx.send(f'Kendin bu eşyaları değerlendirebilirsin.')
    await ctx.send(f'Çöp dostlarımızı mutlu edelim.')

    with open('resimler/tatlı.png', 'rb') as f:
        dosya = discord.File(f)
        await ctx.send(file=dosya)

@bot.command()
async def kirlilikle_ilgili_karikatür_göster(ctx):
    await ctx.send(f'Hemen gösteriyorum dostum.')

    with open('resimler/karikatur.jpg', 'rb') as f:
        çöp = discord.File(f)
        await ctx.send(file=çöp)

@bot.command()
async def program_bilgilerine_eriş(ctx):
    await ctx.send(f'Lütfen program bilgilerine ulaşmak için ebeveyn şifresini giriniz.')
@bot.command()
async def ZXBANKRP(ctx):
    await(f'Program adı: Temizlematör')
    await(f'Yapım nedeni: çocuk kitleye çevreyi koruma bilincini kazandımak')
    await(f'Yapımcı adı soyadı: Mert Can')
    await(f'Sağlayıcı IDE: Visual Studio Code')
    await(f'Sağlayıcı CMD: Python version 3.11')

bot.run("MTI3MjU5ODU2NjQ1OTY3MDU2OQ.G87CLZ.QYsUZMicFEQBLGQ-fxG6wBz5lTxPrygQkeNVJk")