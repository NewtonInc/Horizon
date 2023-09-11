import discord, dotenv, os
dotenv.load_dotenv()

client = discord.Bot()

@client.event
async def on_ready():
    print(f"{client.user} has been activated.")

@client.slash_command(name="hello", description = "Say hi!")
async def hello(ctx):
    await ctx.respond(f"Hello {ctx.author.name}!", ephemeral=True)

@client.slash_command(name="about", description="Get some more information about ObjectVI.")
async def about(ctx):
    emoji=discord.PartialEmoji(name="av", id=1150494647068676176, animated=False)
    pycord = discord.PartialEmoji(name="pycord", id=1150495971193667655, animated=False)
    e = discord.Embed(title=f"{emoji}   **About ObjectVI**", description="ObjectVI is going to be the most advanced Discord bot ever created.")
    e.set_footer(text=f'Made with ❤️ using Pycord', icon_url="https://guide.pycord.dev/img/logo.png")
    await ctx.respond(embed=e)
client.run(str(os.getenv("token")))