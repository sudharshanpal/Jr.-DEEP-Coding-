import tkinter as tk
from tkinter import messagebox
"""
Mad Libs Generator - Jr. DEEP Coding Sample Project

This program creates a fun and interactive Mad Libs story by asking the user
to input various types of words (e.g., nouns, verbs, adjectives). The inputs
are then inserted into a pre-defined story template to generate a humorous and
personalized narrative.
"""

def generate_story():
    """
    Function to create and output the story
    :return: story text with the filled in parameters
    """

    adj1 = entries["Adjective 1"].get()
    noun1 = entries["Noun 1"].get()
    verb_past = entries["Verb (Past Tense)"].get()
    emotion = entries["Emotion"].get()
    game = entries["Sport or Game"].get()
    food = entries["Type of Food"].get()
    place = entries["Place"].get()
    adj2 = entries["Adjective 2"].get()
    celebrity = entries["Celebrity or Fictional Character"].get()
    noun2 = entries["Noun 2"].get()

    # validation (optional but could use as a pivot)
    for field, entry in entries.items():
        if not entry.get().strip():
            messagebox.showwarning("Input Error", f"Please fill in the '{field}' field.")
            return

    story = (
        f"\n--- Your Mad Lib Story ---\n\n"
        f"Meet Sudharshan, a {adj1} second-year computer science student at the University of Toronto.\n"
        f"He spends his days juggling {noun1}, solving math problems, and writing code that once {verb_past} an entire program.\n"
        f"When he's not debugging, he's playing chess, watching the Oilers, or feeling incredibly {emotion} about a close game of {game}.\n"
        f"His favorite snack after a long study session is {food}, preferably shared with friends at {place}.\n"
        f"On weekends, you’ll find him lifting weights while listening to an {adj2} playlist, or binge-watching Avatar: The Last Airbender.\n"
        f"One day, Sudharshan hopes to build a tech tool so helpful that even {celebrity} would use it.\n"
        f"Until then, he’ll keep learning, playing basketball, and eating way too much {noun2}."
    )

    # makes the story appear at the very end of the tkinter window
    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, story)


# defining the main page for the GUI
root = tk.Tk()
root.title("Sudharshan's MadLib")

# user inputs
entries = {}
fields = [
    "Adjective 1", "Noun 1", "Verb (Past Tense)", "Emotion", "Sport or Game",
    "Type of Food", "Place", "Adjective 2", "Celebrity or Fictional Character", "Noun 2"
    ]

# creating text boxes for user input
for i, field in enumerate(fields):
    label = tk.Label(root, text=field + ":")
    label.grid(row=i, column=0, padx=10, pady=2, sticky="e")
    entry = tk.Entry(root, width=30)
    entry.grid(row=i, column=1, padx=10, pady=2)
    entries[field] = entry

# button to generate MadLib
generate_btn = tk.Button(root, text="Create MadLib", command=generate_story, bg="#4CAF50", fg="white")
generate_btn.grid(row=len(fields), columnspan=2, pady=10)

# output box for the story
output_text = tk.Text(root, height=12, width=80, wrap=tk.WORD)
output_text.grid(row=len(fields)+1, columnspan=2, padx=10, pady=10)

# run the GUI loop
root.mainloop()
