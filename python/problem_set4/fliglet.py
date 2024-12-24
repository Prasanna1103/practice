import click
from pyfiglet import Figlet 
import random

@click.command()
@click.option('--f','--font','font', type =str, default= None, help = 'what\'s front')

def main(font):
    figlet = Figlet()
    
    if font:
        if font not in figlet.getFonts():
            click.echo("Invalid font name")
            return
        figlet.setFont(font=font)
    else:
        random_font = random.choice(figlet.getFonts())  
        figlet.setFont(font= random_font)  
    
    user_input = click.prompt("Input: ")
    
    click.echo(figlet.renderText(user_input))
    
if __name__ == "__main__":
    main()    
        
            