import os  # Import the os module to access environment variables

from dotenv import load_dotenv  # Import function to load environment variables from a .env file
import discord  # Import the discord library for interacting with Discord's API

# Import custom modules from the src directory
from src.discordBot import DiscordClient, Sender  # Custom Discord bot classes
from src.logger import logger  # Logger for logging messages
from src.chatgpt import ChatGPT, DALLE  # ChatGPT and DALL-E utilities for AI interactions
from src.models import OpenAIModel  # OpenAI model wrapper
from src.memory import Memory  # Module for managing memory
from src.server import keep_alive  # Function to keep the server online

load_dotenv() # Load environment variables from .env file

models = OpenAIModel(api_key=os.getenv('OPENAI_API'), model_engine=os.getenv('OPENAI_MODEL_ENGINE')) # Initialize the OpenAI model with API key and model engine fetched from environment variables

# Initialize the Memory, ChatGPT, and DALL-E classes with configurations
memory = Memory(system_message=os.getenv('SYSTEM_MESSAGE'))  # Memory for system messages
chatgpt = ChatGPT(models, memory)  # ChatGPT instance using the OpenAI model and memory
dalle = DALLE(models)  # DALL-E instance for image generation

# Main function to run the bot
def run():
    client = DiscordClient()  # Create an instance of the custom Discord client
    sender = Sender()  # Create an instance of the message sender utility

    @client.tree.command(name="chat", description="Have a chat with ChatGPT") # Define a slash command for chatting with ChatGPT
    async def chat(interaction: discord.Interaction, *, message: str):
        user_id = interaction.user.id  # Get the user ID of the interaction author
        if interaction.user == client.user:  # Ignore if the bot is interacting with itself
            return
        await interaction.response.defer()  # Defer the interaction response for asynchronous handling
        receive = chatgpt.get_response(user_id, message)  # Get ChatGPT's response to the user's message
        await sender.send_message(interaction, message, receive)  # Send the user's message and ChatGPT's response

    # Define a slash command for generating images with DALL-E
    @client.tree.command(name="imagine", description="Generate image from text")
    async def imagine(interaction: discord.Interaction, *, prompt: str):
        if interaction.user == client.user:  # Ignore if the bot is interacting with itself
            return
        await interaction.response.defer()  # Defer the interaction response
        image_url = dalle.generate(prompt)  # Generate an image using the provided prompt
        await sender.send_image(interaction, prompt, image_url)  # Send the generated image back to the user

    # Define a slash command for resetting ChatGPT's conversation history
    @client.tree.command(name="reset", description="Reset ChatGPT conversation history")
    async def reset(interaction: discord.Interaction):
        user_id = interaction.user.id  # Get the user ID
        logger.info(f"resetting memory from {user_id}")  # Log the reset action
        try:
            chatgpt.clean_history(user_id)  # Clear the user's conversation history
            await interaction.response.defer(ephemeral=True)  # Defer the interaction and set the response to be private
            await interaction.followup.send(f'> Reset ChatGPT conversation history < - <@{user_id}>')  # Notify the user
        except Exception as e:
            logger.error(f"Error resetting memory: {e}")  # Log errors if any occur
            await interaction.followup.send('> Oops! Something went wrong. <')  # Notify the user of the error

    # Start the bot by running the Discord client with the token from environment variables
    client.run(os.getenv('DISCORD_TOKEN'))

# Entry point of the script
if __name__ == '__main__':
    keep_alive()  # Keep the bot server online
    run()  # Run the bot
