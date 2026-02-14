import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.title("Text Editor")


# ===== FUNÇÕES =====
def font_helvetica():
    text.config(font=("Helvetica", 12))

def font_courier():
    text.config(font=("Courier", 12))

def font_arial():
    text.config(font=("Arial", 18))

def save_file():
    content = text.get("1.0", "end-1c")
    file_path = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt")]
    )
    if file_path:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)

def open_file():
    file_path = filedialog.askopenfilename(
        filetypes=[("Text Files", "*.txt")]
    )
    if file_path:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
            text.delete("1.0", "end")
            text.insert("1.0", content)

def contador_de_caracterias():
    content = text.get("1.0", "end-1c")
    word_count = len(content.split())
    char_count = len(content)
    tk.messagebox.showinfo("Contador de Caracterias", f"Palavras: {word_count}\nCaracteres: {char_count}")

def tema_claro():
    text.config(bg="white", fg="black")  
    root.config(bg="white")

def tema_escuro():
    text.config(bg="black", fg="white")  
    root.config(bg="black")

def tema_cinza():
    text.config(bg="gray", fg="white")  
    root.config(bg="gray")

# funçao para trocar os temas do editor de texto
def temas():
    tema_menu = tk.Menu(menu_bar, tearoff=0)
    tema_menu.add_command(label="Claro", command=tema_claro)
    tema_menu.add_command(label="Escuro", command=tema_escuro)
    tema_menu.add_command(label="Cinza", command=tema_cinza)
    menu_bar.add_cascade(label="Temas", menu=tema_menu)



# ===== MENU =====
menu_bar = tk.Menu(root)

file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

font_menu = tk.Menu(menu_bar, tearoff=0)
font_menu.add_command(label="Helvetica", command=font_helvetica)
font_menu.add_command(label="Courier", command=font_courier)
font_menu.add_command(label="Arial", command=font_arial)

menu_bar.add_cascade(label="File", menu=file_menu)
menu_bar.add_cascade(label="Font", menu=font_menu)
menu_bar.add_command(label="Open", command=open_file)
menu_bar.add_command(label="Contador de Caracterias", command=contador_de_caracterias)
temas()  

root.config(menu=menu_bar)

# ===== TEXT AREA =====
text = tk.Text(root, font=("Helvetica", 12))
text.pack(expand=True, fill="both")

root.mainloop()
