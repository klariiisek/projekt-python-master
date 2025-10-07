import tkinter as tk
import random


class App:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Demo GUI")
        self.root.geometry("800x600")
        
        self.canvas = tk.Canvas(self.root, width=800,height=600,bg="white")
        self.canvas.pack(fill="both", expand=True)

        menubar = tk.Menu(self.root)
        self.root.config(menu=menubar)

        m_tasks = tk.Menu(menubar, tearoff=False)
        m_tasks.add_command(label="Konec", command=self.root.destroy)
        menubar.add_cascade(label="System", menu=m_tasks)
        
        m_colors = tk.Menu(menubar, tearoff=False)
        m_colors.add_command(label="Red", command=lambda: self.set_bg("red"))
        m_colors.add_command(label="Green", command=lambda: self.set_bg("green"))
        m_colors.add_command(label="Blue", command=lambda: self.set_bg("blue"))
        menubar.add_cascade(label="Colors", menu=m_colors)
        
        m_grafics = tk.Menu(menubar, tearoff=False)
        m_grafics.add_command(label="Magické čáry", command=lambda: self.magic_barcode(1,20))
        m_grafics.add_command(label="Šachovnice", command=lambda: self.set_bg("green"))
        m_grafics.add_command(label="Terč", command=lambda: self.set_bg("blue"))
        menubar.add_cascade(label="Color", menu=m_grafics)
        
    def _canvas_size(self) -> tuple[int,int]:
        w = self.canvas.winfo_width() or self.root.winfo_width() or 800
        h = self.canvas.winfo_height() or self.root.winfo_height() or 600
        return w,h

    def magic_barcode(self,min:int,max:int) -> None:
        self.clear()
        self.canvas.configure(bg="white")
        x = 0
        w,h = self.canvas_size()
        while x < w:
            width = random.randint(min,max)
            color = f"#{random.randint(0, 0xffffff):06x}"
            self.canvas.create_line(x,0,x,h,fill=color,width=width)
            x += width

    def set_bg(self,color: str) -> None:
        self.root.configure(background=color)
        
    def clear(self) -> None:
        self.canvas.delete("all")
        

    def run(self):
        self.root.mainloop()

if __name__ == '__main__':
    App().run()
