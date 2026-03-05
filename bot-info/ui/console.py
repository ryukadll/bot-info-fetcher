from pystyle import Colorate, Colors, Write

def slow_print(text: str, delay: float = 0.02):
    Write.Print(
        text + "\n",
        Colors.blue_to_purple,
        interval=delay
    )

def divider():
    print(Colorate.Horizontal(Colors.blue_to_purple, "-" * 60, 1))
