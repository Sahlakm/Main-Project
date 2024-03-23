import pickle
import tkinter as tk
from tkinter import messagebox

# Load the logistic regression model from the pickled file
loaded_model = pickle.load(open('phishing.pkl', 'rb'))


def detect():
    url = entry.get()

    # Perform the prediction using the loaded logistic regression model
    # Assuming the model has a predict method
    result = loaded_model.predict([url])  # Pass the actual URL in a list

    if result == 'bad':
        result = 'This is a phishing site!!!'
    elif result == 'good':
        result = 'This is a legitimate site.'
    else:
        result = 'Prediction not available.'

    # Provide a title for showinfo
    messagebox.showinfo("Result", result)
    entry.delete(0, tk.END)


# Create the main window
window = tk.Tk()
window.title("Phishing URL Detection")

# Create and place the entry widget
entry = tk.Entry(window, width=40)
entry.pack(pady=10)

# Create and place the detection button
detect_button = tk.Button(window, text="Detect", command=detect)
detect_button.pack()
    

# Start the Tkinter event loop
window.mainloop()
