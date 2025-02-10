from utils.constructor import Constructor
from visuals.menu import Menu
from ttkthemes import ThemedTk

def main():
    
    root = ThemedTk()
    Menu(root)
    root.mainloop()

if __name__ == "__main__":
    main()