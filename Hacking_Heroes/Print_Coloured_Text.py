import colorama
from colorama import Fore, Back, Style

class ColorTextPrinter:
    """Class to print colored text with additional features."""

    def __init__(self):
        colorama.init(autoreset=True)
        self.fg_colors = {
            'BLACK': Fore.BLACK,
            'RED': Fore.RED,
            'GREEN': Fore.GREEN,
            'YELLOW': Fore.YELLOW,
            'BLUE': Fore.BLUE,
            'MAGENTA': Fore.MAGENTA,
            'CYAN': Fore.CYAN,
            'WHITE': Fore.WHITE,
        }

        self.bg_colors = {
            'BLACK': Back.BLACK,
            'RED': Back.RED,
            'GREEN': Back.GREEN,
            'YELLOW': Back.YELLOW,
            'BLUE': Back.BLUE,
            'MAGENTA': Back.MAGENTA,
            'CYAN': Back.CYAN,
            'WHITE': Back.WHITE,
        }

        self.styles = {
            'NORMAL': Style.NORMAL,
            'BOLD': Style.BRIGHT,
            'DIM': Style.DIM,
            'UNDERLINE': '\033[4m',
            'REVERSED': '\033[7m',
        }

        self.color_history = []

    def get_color_input(self, prompt, color_map):
        """Get validated color input from the user."""
        while True:
            user_input = input(prompt).strip().upper()
            if user_input in color_map:
                self.color_history.append(user_input)
                return color_map[user_input]
            else:
                print(f"Invalid input '{user_input}'. Please choose from the following: {', '.join(color_map.keys())}")

    def print_colored_text(self, text, fg_color, bg_color, style):
        """Prints text with specified colors and styles.

        Args:
            text (str): The text to print.
            fg_color (str): The foreground color.
            bg_color (str): The background color.
            style (str): The text style.
        """
        formatted_text = f"{style}{fg_color}{bg_color}{text}{Style.RESET_ALL}"
        print(formatted_text)

    def show_color_history(self):
        """Display the color history."""
        print("Color History:", ', '.join(self.color_history) if self.color_history else "No colors used yet.")

def main():
    """Main function to execute the program."""
    printer = ColorTextPrinter()
    
    print("Available Foreground Colors: ", ', '.join(printer.fg_colors.keys()))
    print("Available Background Colors: ", ', '.join(printer.bg_colors.keys()))
    print("Available Text Styles: ", ', '.join(printer.styles.keys()))

    text = input("Enter the text you want to print: ")
    fg_color = printer.get_color_input("Enter the foreground color: ", printer.fg_colors)
    bg_color = printer.get_color_input("Enter the background color: ", printer.bg_colors)
    style = printer.get_color_input("Enter the text style: ", printer.styles)

    printer.print_colored_text(text, fg_color, bg_color, style)
    printer.show_color_history()

if __name__ == "__main__":
    main()
