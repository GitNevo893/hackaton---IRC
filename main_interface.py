import tkinter as tk
import consts

window = tk.Tk()
window.title("ThinkGap")
window.geometry("1200x300")
window.configure(background=consts.BG_MAIN)

topic_frame = tk.Frame(window, bg=consts.BG_CARD,width=900, height=200)
topic_frame.pack(side="top")

def clicked_generate():
    if topic_entry.get() != "":
        topic_entry.delete(0, tk.END)
        answer_text = consts.data["text_with_blanks"]
        text_label = tk.Label(window, bg=consts.BG_MAIN, wraplength=700, fg=consts.TEXT_MAIN, justify= "left",text=answer_text, font="Calibri 16" )
        text_label.pack()
        word_bank_botton()

topic_entry = tk.Entry(topic_frame, bg=consts.BG_CARD, fg=consts.TEXT_MAIN, font="Calibri 16")
generate_button = tk.Button(topic_frame, text="Generate", bg=consts.BG_CARD, width=10, height=1, font="Calibri 24 bold", command=clicked_generate)
current_blank = 1
current_blank_text = "Current Blank is: " + str(current_blank)
current_blank_label = tk.Label(topic_frame, bg=consts.BG_MAIN, fg="white", text=current_blank_text, font="Calibri 16")

def chek_word(word, num):
   if num == consts.data["answers"][word]:
       return True
   else:
       return False


def word_bank_botton():
   word_bank = consts.data["word_bank"]

   for word in word_bank:
       btn = tk.Button(
           window,
           text=word,
           bg=consts.BG_MAIN,
           fg="black",
           font=("Arial", 12)
       )
       btn.pack(side=tk.LEFT, padx=3)

       btn.pack(expand=True)


topic_entry.pack(side="left", padx=(0, 5))
generate_button.pack(side="right")
current_blank_label.pack(side="right")

window.mainloop()
