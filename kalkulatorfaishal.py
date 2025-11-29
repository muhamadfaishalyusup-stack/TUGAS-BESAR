import tkinter as tk
import math

# Fungsi operasi matematika
def calculate(operation):
    
    # --- 1. VALIDASI INPUT ---
    try:
       #  konversi input menjadi float. Jika kosong, dianggap 0.
        a = float(entry1.get().strip() or 0)
        # entry2 hanya diambil nilainya jika ada input.
        b = float(entry2.get().strip() or 0)

    except ValueError:
        label_result.config(text="Error: Format input angka salah!")
        return 

    #  LOGIKA KALKULASI 
    try:
        match operation:
            case 'add': result = a + b
            case 'sub': result = a - b
            case 'mul': result = a * b
            case 'div':
                if b == 0:
                    # Memicu error spesifik
                    raise ValueError("Pembagian dengan nol tidak valid!")
                result = a / b  
            case 'pow': result = a ** b
            case 'sqrt':
                if a < 0:
                    # Memicu error spesifik
                    raise ValueError("Akar kuadrat bilangan negatif tidak valid!")
                result = math.sqrt(a)
            case _: # Default case di Python 3.10+
                result = "Operasi tidak valid!"

        label_result.config(text=f"Hasil: {result}")
        
    except ValueError as e:
        # Menangkap error yang DIRAISKAn di dalam match/case (misalnya bagi 0)
        label_result.config(text=f"Error: {e}")

# Membuat jendela utama
root = tk.Tk()
root.title("KALKULATOR PUNYA FAISHAL")
root.geometry("320x350") 
root.resizable(False, False)

# Widget input
label1 = tk.Label(root, text="Angka 1:")
label1.pack()
entry1 = tk.Entry(root)
entry1.pack()
 
label2 = tk.Label(root, text="Angka 2 (opsional, tidak untuk √):")
label2.pack()
entry2 = tk.Entry(root)
entry2.pack()

# Tombol operasi
buttons = [
    ("Tambah", 'add'),
    ("Kurang", 'sub'),
    ("Kali", 'mul'),
    ("Bagi", 'div'),
    ("Pangkat", 'pow'),
    ("Akar √", 'sqrt')
]

for text, op in buttons:
    tk.Button(root, text=text, width=20,
              command=lambda op=op: calculate(op)).pack(pady=3)

# Label hasil
label_result = tk.Label(root, text="Hasil: ")
label_result.pack(pady=10)

# Jalankan GUI
root.mainloop() 