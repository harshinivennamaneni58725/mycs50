import random
import sys
from pyfiglet import Figlet


def main():
    figlet = Figlet()
    fonts = figlet.getFonts()

    if len(sys.argv) == 1:
        font_name = random.choice(fonts)
    elif len(sys.argv) == 3 and sys.argv[1] in ["-f", "--font"]:
        font_name = sys.argv[2]
        if font_name not in fonts:
            sys.exit("Invalid usage")
    else:
        sys.exit("Invalid usage")

    user_input = input("Input: ")
    figlet.setFont(font=font_name)
    print(figlet.renderText(user_input))


if __name__ == "__main__":
    main()
