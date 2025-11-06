from dotenv import load_dotenv
import os
import discord

load_dotenv()

bot = discord.Bot()


@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user}")


@bot.slash_command(name="ping", description="Responds with Pong!")
async def hello(ctx):
    await ctx.respond("Pong!")


@bot.slash_command(name="listroles", description="Lists all roles in the server")
async def listroles(ctx):
    if not ctx.author.guild_permissions.manage_roles:
        await ctx.respond("You don’t have permission to manage roles.", ephemeral=True)
        return

    roles = ctx.guild.roles
    roles_names = [role.name for role in roles]
    await ctx.respond("Roles in this server:\n" + "\n".join(roles_names))


@bot.slash_command(name="addrole", description="Add role to a user")
async def addrole(ctx, member: discord.Member, role: discord.Role):
    if not ctx.author.guild_permissions.manage_roles:
        await ctx.respond("You don’t have permission to manage roles.", ephemeral=True)
        return

    await member.add_roles(role)
    await ctx.respond(f"Added role {role.name} to {member.display_name}")


@bot.slash_command(name="removerole", description="Remove role from a user")
async def removerole(ctx, member: discord.Member, role: discord.Role):
    if not ctx.author.guild_permissions.manage_roles:
        await ctx.respond("You don’t have permission to manage roles.", ephemeral=True)
        return

    await member.remove_roles(role)
    await ctx.respond(f"Removed role {role.name} from {member.display_name}")


bot.run(os.getenv("DISCORD_TOKEN"))
