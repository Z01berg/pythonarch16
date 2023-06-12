import tkinter as tk
from tkinter import messagebox, ttk
from tkinter import filedialog
import sqlite3

import joblib
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt


class PredictDialog:
    def __init__(self, parent, model):
        self.top = tk.Toplevel(parent)
        self.top.title("Predict Data")

        self.model = model

        # Create input fields
        self.labels = ["Alcohol", "Malic_acid", "Ash", "Alcalinity_of_ash", "Magnesium", "Total_phenols", "Flavanoids",
                       "Nonflavanoid_phenols", "Proanthocyanins", "Color_intensity", "Hue", "OD280_OD315_of_diluted_wines", "Proline"]
        self.entries = []

        for label in self.labels:
            attr_label = tk.Label(self.top, text=label + ":", width=20, font=("Arial", 12))
            attr_label.pack()
            attr_entry = tk.Entry(self.top)
            attr_entry.pack()
            self.entries.append(attr_entry)

        self.predict_button = tk.Button(self.top, text="Predict", command=self.predict, width=20, font=("Arial", 12))
        self.predict_button.pack()

    def predict(self):
        data = []
        for entry in self.entries:
            attr = float(entry.get())
            data.append(attr)

        if self.model is not None:
            prediction = self.model.predict([data])
            messagebox.showinfo("Prediction Result", f"Predicted class: {prediction[0]}")
        else:
            messagebox.showerror("Error", "Model is not available.")



class AddDataDialog:
    def __init__(self, parent, conn):
        self.top = tk.Toplevel(parent)
        self.top.title("Add Data")

        self.conn = conn

        # Create input fields
        self.labels = ["Class", "Alcohol", "Malic_acid", "Ash", "Alcalinity_of_ash", "Magnesium", "Total_phenols",
                       "Flavanoids", "Nonflavanoid_phenols", "Proanthocyanins", "Color_intensity", "Hue",
                       "OD280_OD315_of_diluted_wines", "Proline"]
        self.entries = []

        for label in self.labels:
            attr_label = tk.Label(self.top, text=label + ":", width=20, font=("Arial", 12))
            attr_label.pack()
            attr_entry = tk.Entry(self.top)
            attr_entry.pack()
            self.entries.append(attr_entry)

        self.add_button = tk.Button(self.top, text="Add", command=self.add_data, width=20, font=("Arial", 12))
        self.add_button.pack()

    def add_data(self):
        data = []
        for entry in self.entries:
            attr = entry.get()
            data.append(attr)

        self.conn.execute("INSERT INTO ml_data (class, Alcohol, Malic_acid, Ash, Alcalinity_of_ash, Magnesium, "
                          "Total_phenols, Flavanoids, Nonflavanoid_phenols, Proanthocyanins, Color_intensity, Hue, "
                          "OD280_OD315_of_diluted_wines, Proline) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                          tuple(data))
        self.conn.commit()

        messagebox.showinfo("Data Added", "Data added successfully.")


class RebuildModelDialog:
    def __init__(self, parent, conn, model):
        self.top = tk.Toplevel(parent)
        self.top.title("Rebuild Model")

        self.conn = conn
        self.model = model

        self.rebuild_button = tk.Button(self.top, text="Rebuild", command=self.rebuild, width=20, font=("Arial", 12))
        self.rebuild_button.pack()

    def rebuild(self):
        df = pd.read_sql_query("SELECT * FROM ml_data", self.conn)
        X = df.drop("class", axis=1)
        y = df["class"]

        self.model.fit(X, y)

        messagebox.showinfo("Model Rebuilt", "Model rebuilt successfully.")


class MLApp:
    def __init__(self, root):
        self.root = root
        self.root.geometry("400x300")
        self.root.title("ML App")

        # Database connection
        self.conn = sqlite3.connect("ml_app.db")
        self.cursor = self.conn.cursor()

        # Create table if not exists
        self.cursor.execute("CREATE TABLE IF NOT EXISTS ml_data (id INTEGER PRIMARY KEY AUTOINCREMENT, "
                            "class INTEGER, Alcohol REAL, Malic_acid REAL, Ash REAL, Alcalinity_of_ash REAL, Magnesium REAL, "
                            "Total_phenols REAL, Flavanoids REAL, Nonflavanoid_phenols REAL, Proanthocyanins REAL, Color_intensity REAL, Hue REAL, "
                            "OD280_OD315_of_diluted_wines REAL, Proline  REAL)")

        # Load data from files
        self.load_data("train_data.txt")
        self.load_data("test_data.txt")

        # Model
        self.model = None

        # Interface
        self.train_button = tk.Button(self.root, text="Train Model", command=self.train_model, width=20, font=("Arial", 12))
        self.train_button.pack()

        self.test_button = tk.Button(self.root, text="Test Model", command=self.test_model, width=20, font=("Arial", 12))
        self.test_button.pack()

        self.predict_button = tk.Button(self.root, text="Predict", command=self.predict_data, width=20, font=("Arial", 12))
        self.predict_button.pack()

        self.add_button = tk.Button(self.root, text="Add Data", command=self.add_data, width=20, font=("Arial", 12))
        self.add_button.pack()

        self.rebuild_button = tk.Button(self.root, text="Rebuild Model", command=self.rebuild_model, width=20, font=("Arial", 12))
        self.rebuild_button.pack()

        self.view_button = tk.Button(self.root, text="View Data", command=self.view_data, width=20, font=("Arial", 12))
        self.view_button.pack()

        self.save_model_button = tk.Button(self.root, text="Save Model", command=self.save_model, width=20, font=("Arial", 12))
        self.save_model_button.pack()

        self.load_model_button = tk.Button(self.root, text="Load Model", command=self.load_model, width=20, font=("Arial", 12))
        self.load_model_button.pack()

        self.plot_button = tk.Button(self.root, text="Plot Data", command=self.plot_data, width=20, font=("Arial", 12))
        self.plot_button.pack()

    def load_data(self, filename):
        df = pd.read_csv(filename, header=None, delimiter=',')
        df.columns = ["class", "Alcohol", "Malic_Acid", "Ash", "Alcalinity_of_ash", "Magnesium", "Total_phenols", "Flavanoids",
                      "Nonflavanoid_phenols", "Proanthocyanins", "Color_intensity", "Hue", "OD280_OD315_of_diluted_wines", "Proline"]
        df.to_sql("ml_data", self.conn, if_exists="append", index=False)

    def train_model(self):
        df = pd.read_sql_query("SELECT * FROM ml_data", self.conn)
        X = df.drop("class", axis=1)
        y = df["class"]

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        self.model = LogisticRegression(max_iter=10000)
        self.model.fit(X_train, y_train)

        y_train_pred = self.model.predict(X_train)
        train_accuracy = accuracy_score(y_train, y_train_pred)
        train_correct_count = sum(y_train == y_train_pred)
        train_total_count = len(y_train)

        messagebox.showinfo("Training Results", f"Train Accuracy: {train_accuracy:.2f}\n"
                                                f"Train Correct: {train_correct_count}/{train_total_count}")

    def test_model(self):
        df = pd.read_sql_query("SELECT * FROM ml_data", self.conn)
        X = df.drop("class", axis=1)
        y = df["class"]

        y_pred = self.model.predict(X)
        test_accuracy = accuracy_score(y, y_pred)
        test_correct_count = sum(y == y_pred)
        test_total_count = len(y)

        messagebox.showinfo("Testing Results", f"Test Accuracy: {test_accuracy:.2f}\n"
                                               f"Test Correct: {test_correct_count}/{test_total_count}")

    def predict_data(self):
        dialog = self.PredictDialog(self.root, self.model)
        self.root.wait_window(dialog.top)

    def add_data(self):
        dialog = AddDataDialog(self.root, self.conn)
        self.root.wait_window(dialog.top)

    def rebuild_model(self):
        dialog = RebuildModelDialog(self.root, self.conn, self.model)
        self.root.wait_window(dialog.top)

    def view_data(self):
        df = pd.read_sql_query("SELECT * FROM ml_data", self.conn)

        data_window = tk.Toplevel(self.root)
        data_window.title("View Data")

        treeview = ttk.Treeview(data_window)
        treeview.pack(fill=tk.BOTH, expand=True)

        treeview["columns"] = df.columns.tolist()
        treeview.column("#0", width=0, stretch=tk.NO)
        treeview.delete(*treeview.get_children())

        for column in df.columns.tolist():
            treeview.heading(column, text=column)
            treeview.column(column, anchor=tk.CENTER)

        treeview["padding"] = 5

        for i, row in df.iterrows():
            values = row.tolist()
            treeview.insert("", tk.END, text=i, values=values)

    def save_model(self):
        filename = filedialog.asksaveasfilename(defaultextension=".joblib")
        if filename:
            joblib.dump(self.model, filename)
            messagebox.showinfo("Model Saved", "Model saved successfully.")

    def load_model(self):
        filename = filedialog.askopenfilename(filetypes=[("Joblib files", "*.joblib")])
        if filename:
            self.model = joblib.load(filename)
            messagebox.showinfo("Model Loaded", "Model loaded successfully.")

    def plot_data(self):
        df = pd.read_sql_query("SELECT * FROM ml_data", self.conn)
        classes = df['class'].unique()

        for wine_class in classes:
            data = df[df['class'] == wine_class]
            plt.scatter(data['Alcohol'], data['Malic_acid'], label='Class {}'.format(wine_class))

        plt.xlabel('Alcohol')
        plt.ylabel('Malic acid')
        plt.title('Data Plot')
        plt.legend(title='Wine Clases:')
        plt.show()

    class PredictDialog:
        def __init__(self, parent, model):
            self.top = tk.Toplevel(parent)
            self.top.title("Predict Data")

            self.model = model

            # Create input fields
            self.attr1_label = tk.Label(self.top, text="Alcohol:", width=20, font=("Arial", 12))
            self.attr1_label.pack()
            self.attr1_entry = tk.Entry(self.top)
            self.attr1_entry.pack()

            self.attr2_label = tk.Label(self.top, text="Malic_acid:", width=20, font=("Arial", 12))
            self.attr2_label.pack()
            self.attr2_entry = tk.Entry(self.top)
            self.attr2_entry.pack()

            self.predict_button = tk.Button(self.top, text="Predict", command=self.predict, width=20, font=("Arial", 12))
            self.predict_button.pack()

        def predict(self):
            attr1 = float(self.attr1_entry.get())
            attr2 = float(self.attr2_entry.get())

            data = [[attr1, attr2] + [0] * 12]
            prediction = self.model.predict(data)
            messagebox.showinfo("Prediction Result", f"Predicted class: {prediction[0]}")

    class AddDataDialog:
        def __init__(self, parent, conn):
            self.top = tk.Toplevel(parent)
            self.top.title("Add Data")

            self.conn = conn

            # Create input fields
            self.class_label = tk.Label(self.top, text="Class:", width=20, font=("Arial", 12))
            self.class_label.pack()
            self.class_entry = tk.Entry(self.top)
            self.class_entry.pack()

            self.attr1_label = tk.Label(self.top, text="Alcohol:", width=20, font=("Arial", 12))
            self.attr1_label.pack()
            self.attr1_entry = tk.Entry(self.top)
            self.attr1_entry.pack()

            self.attr2_label = tk.Label(self.top, text="Malic_acid:", width=20, font=("Arial", 12))
            self.attr2_label.pack()
            self.attr2_entry = tk.Entry(self.top)
            self.attr2_entry.pack()

            self.add_button = tk.Button(self.top, text="Add", command=self.add_data, width=20, font=("Arial", 12))
            self.add_button.pack()

        def add_data(self):
            class_value = int(self.class_entry.get())
            attr1 = float(self.attr1_entry.get())
            attr2 = float(self.attr2_entry.get())

            self.conn.execute("INSERT INTO ml_data (class, Alcohol, Malic_acid) VALUES (?, ?, ?)",
                              (class_value, attr1, attr2))
            self.conn.commit()

            messagebox.showinfo("Data Added", "Data added successfully.")

    class RebuildModelDialog:
        def __init__(self, parent, conn, model):
            self.top = tk.Toplevel(parent)
            self.top.title("Rebuild Model")

            self.conn = conn
            self.model = model

            self.rebuild_button = tk.Button(self.top, text="Rebuild", command=self.rebuild, width=20, font=("Arial", 12))
            self.rebuild_button.pack()

        def rebuild(self):
            df = pd.read_sql_query("SELECT * FROM ml_data", self.conn)
            X = df.drop("class", axis=1)
            y = df["class"]

            self.model.fit(X, y)

            messagebox.showinfo("Model Rebuilt", "Model rebuilt successfully.")

root = tk.Tk()
app = MLApp(root)
root.mainloop()

