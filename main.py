
import discord
import os
import sys
from discord.ext import commands
from dotenv import load_dotenv
from keepalive import keep_alive

# 👇 IMPORT DO BANCO
from db import init_db

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
load_dotenv()


class RizeBot(commands.Bot):
    def __init__(self):
        intents = discord.Intents.all()
        super().__init__(
            command_prefix=",",
            intents=intents,
            help_command=None,
            activity=discord.Game(name="resenha confirmada")
        )

    async def setup_hook(self):
        # 📦 Carregar cogs
        await self.load_extension("cogs.admin")
        

        print("Lumi: Cogs carregados")

        # 🔁 Sync dos slash
        await self.tree.sync()
        print("Lumi: Comandos sincronizados brother")

        # 🎫 View persistente do painel (IMPORTANTE)
        from cogs.admin import TicketView
        self.add_view(TicketView())

    async def on_ready(self):
        # 🧱 CRIA AS TABELAS AUTOMATICAMENTE
        init_db()

        print(f"Conectado: {self.user} (ID: {self.user.id})")
        print("------")


keep_alive()
TOKEN = os.getenv("DISCORD_TOKEN")
bot.run(TOKEN)
