# WotD-Bot
A basic Discord bot that sends a message upon user request of the word of the day. Words are selected by the user by use of a text file.

In order for the program to work, a bot needs to be created at the Discord developer page: https://discord.com/developers/applications.
Documentation for Discord developers can be found here: https://discord.com/developers/docs/intro.

Once the bot has been created and invited to a server, all files can be downloaded and put into a Python project. However, the '.env' file needs to be changed in order to take in a bot token and a server/guild to run in. 'DISCORD_TOKEN' is the bot token that is generated from the developer page where the bot is created. This token is unique to each bot and should be kept private as this is your way of controlling the bot. 'DISCORD_GUILD' is simply the name of the guild/server that the bot is currently invited to. 

Users can change the 'Words.txt' file to include words that they wish to see from their bot. 
