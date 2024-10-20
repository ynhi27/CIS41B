# Y Nhi Tran
# Exercise TKinter

import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt


class FruitsTab:
    def __init__(self, tab):
        self.tab = tab
        self.label = tk.Label(self.tab, text='The Fruit Group includes all fruits and 100% fruit juice.\nFruits may be '
                                             'fresh, frozen, canned, or dried/dehydrated.\nFruits can be eaten whole, '
                                             'cut up, pureed (mashed), or cooked.')
        self.label.pack(anchor='n', padx=5, pady=3)

        # Create list box
        self.my_frame = tk.Frame(self.tab)
        self.my_scrollbar = tk.Scrollbar(self.my_frame, orient=tk.VERTICAL)
        self.listbox = tk.Listbox(self.my_frame, width=40, yscrollcommand=self.my_scrollbar.set, selectmode=tk.MULTIPLE)
        self.my_scrollbar.config(command=self.listbox.yview)
        self.my_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.my_frame.pack()
        self.listbox.pack(pady=15)

        self.my_list = ["Apple", "Banana", "Blueberries", "Cantaloupe", "Dates", "Grapes", "Guava", "Kumquats", "Mango",
                        "Orange", "Papaya", "Peach", "Pear", "Pineapple", "Plum", "Strawberries", "Watermelon"]
        for item in self.my_list:
            self.listbox.insert(tk.END, item)

        self.my_button1 = tk.Button(self.tab, text="Select", command=self.select)
        self.my_button1.pack(pady=10)
        self.my_button2 = tk.Button(self.tab, text="Delete", command=self.delete)
        self.my_button2.pack(pady=10)
        self.my_button3 = tk.Button(self.tab, text="Delete All", command=self.delete_all)
        self.my_button3.pack(pady=10)

        self.my_label = tk.Label(self.tab, text='')
        self.my_label.pack(pady=5)

    def select(self):
        result = ''
        for item in self.listbox.curselection():
            result = result + str(self.listbox.get(item)) + "\n"
        self.my_label.config(text=result)

    def delete(self):
        for item in reversed(self.listbox.curselection()):
            self.listbox.delete(item)
            self.my_label.config(text='')

    def delete_all(self):
        self.listbox.delete(0, tk.END)
        self.my_button3.config(state=tk.DISABLED)


class GrainsTab:
    def __init__(self, tab):
        self.tab = tab
        self.label = tk.Label(self.tab, text='Foods made from wheat, rice, oats, cornmeal, barley, or another cereal '
                                             'grain is a grain product.\nBread, pasta, breakfast cereals, grits, and '
                                             'tortillas are examples of grain products.\nFoods such as popcorn, rice, '
                                             'and oatmeal are also included in the Grains Group.')
        self.label.pack(anchor='n', padx=5, pady=3)
        self.Modes = [("Biscuits", "1 small biscuits"),
                      ("Breads", "1 regular slice of bread\n 1 small slice of French bread\n4 snack-size slices of "
                                 "rye bread"),
                      ("Crackers", "5 whole wheat crackers\n2 rye crisp breads"),
                      ("Oatmeal", "½ cup, cooked\n1 packet instant"),
                      ("Rice", "½ cup, cooked\n1 ounce, dry")
        ]

        self.grains = tk.StringVar()
        for text, mode in self.Modes:
            tk.Radiobutton(self.tab, text=text, variable=self.grains, value=mode).pack()

        self.myButton = tk.Button(self.tab, text="Click to see 1-Ounce Equivalence", command=self.clicked)
        self.myButton.pack()

        self.myLabel = tk.Label(self.tab, text=self.grains.get())
        self.myLabel.pack()

    def clicked(self):
        self.myLabel.config(text=self.grains.get())


class VegetablesTab:
    def __init__(self, tab):
        self.tab = tab
        self.label = tk.Label(self.tab, text='Any vegetable or 100% vegetable juice counts as part of the Vegetable '
                                             'Group.\nVegetables may be raw or cooked and can be fresh, frozen, canned,'
                                             ' or dried.\nThey can be whole, cut-up, or mashed.')
        self.label.pack(anchor='n', padx=5, pady=3)
        self.sample_text = tk.Text(self.tab, width=60, height=20, font=("Helvetica", 8), wrap=tk.NONE)
        self.sample_text.pack(pady=10)

        self.set_up_button = tk.Button(self.tab, height=1, width=20, text="Click for more information",
                                       command=self.set_text_by_button)
        self.set_up_button.pack()

    def set_text_by_button(self):
        self.sample_text.insert(tk.END, '')
        self.sample_text.insert(tk.END, "How many vegetables are needed daily?\n"
                            "The amount of vegetables you need to eat depends on your age, sex, \n"
                            "height, weight, and physical activity. It can also depend on \n"
                            "whether you are pregnant or breastfeeding.\n\n"
                            "Find the right amount for you by getting your MyPlate Plan.\n"
                            "For general guidance by age, see the table below.\n\n"
                            "What counts as a cup of vegetables?\n"
                            "The following examples count as 1 cup from the\n"
                            "Vegetables Group:\n\n"
                            "1 cup of raw or cooked vegetables or vegetable juice\n"
                            "2 cups of raw leafy salad greens\n"
                            "The table below lists specific amounts that count as\n"
                            "1 cup of vegetables for your recommended consumption.\n\n\n")


class ProteinTab:
    def __init__(self, tab):
        self.myLabel1 = None
        self.tab = tab
        self.label = tk.Label(self.tab, text='Protein Foods include all foods made from seafood; meat, poultry, and '
                                             'eggs; beans, peas, lentils;\nand nuts, seeds, and soy products. Beans, '
                                             'peas, and lentils are also part of the Vegetable Group.')
        self.label.pack(anchor='n', padx=5, pady=3)
        self.click = tk.StringVar()
        self.click.set("Daily Recommendation")

        self.options = [
            ("Children 2-8yrs", "2 to 5½ oz-equiv"),
            ("Girls 9-18yrs", "4 to 6½ oz-equiv"),
            ("Boys 9-18yrs", "5 to 7 oz-equiv"),
            ("Women 19-30yrs", "5 to 6½ oz-equiv"),
            ("Men 19-30yrs", "6½ to 7 oz-equiv")
        ]

        self.drop = tk.OptionMenu(self.tab, self.click, *self.options)
        self.drop.pack()

        self.button = tk.Button(self.tab, text='Show Selection', command=self.show)
        self.button.pack()

    def show(self):
        self.myLabel1 = tk.Label(self.tab, text=self.click.get())
        self.myLabel1.pack()


class DairyTab:
    def __init__(self, tab):
        self.tab = tab
        self.label = tk.Label(self.tab, text='The Dairy Group includes milk, yogurt, cheese, lactose-free milk and '
                                             'fortified soy milk and yogurt. \nThe Dairy Group does not include foods '
                                             'made from milk that have little calcium and a high fat content.\nExamples'
                                             ' of this are cream cheese, sour cream, cream, and butter.')
        self.label.pack(anchor='n', padx=5, pady=3)
        self.button_graph = tk.Button(self.tab, text="MyPlate Food Guide", command=self.graph)
        self.button_graph.pack()

    def graph(self):
        sizes = [50, 25, 25]
        labels = ['Fruits & Vegetable', 'Grains', 'Protein']

        fig, ax = plt.subplots()
        ax.pie(sizes, labels=labels, autopct='%1.1f%%')
        ax.axis('equal')
        fig.patch.set_facecolor('#EEEEEE')

        canvas = FigureCanvasTkAgg(fig, master=self.tab)
        canvas.draw()
        canvas.get_tk_widget().pack()


class App:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry('600x600')
        self.root.title("Welcome to MyPlate information")

        # Create tabs control
        self.tab_control = ttk.Notebook(self.root)
        self.tab_control.pack(pady=15)

        self.tab1 = tk.Frame(self.tab_control)
        self.tab2 = tk.Frame(self.tab_control)
        self.tab3 = tk.Frame(self.tab_control)
        self.tab4 = tk.Frame(self.tab_control)
        self.tab5 = tk.Frame(self.tab_control)

        self.tab1.pack(fill="both", expand=1)
        self.tab2.pack(fill="both", expand=1)
        self.tab3.pack(fill="both", expand=1)
        self.tab4.pack(fill="both", expand=1)
        self.tab5.pack(fill="both", expand=1)

        self.tab_control.add(self.tab1, text='Fruits')
        self.tab_control.add(self.tab2, text='Grains')
        self.tab_control.add(self.tab3, text='Vegetables')
        self.tab_control.add(self.tab4, text='Protein')
        self.tab_control.add(self.tab5, text='Dairy')

        self.fruits_tab = FruitsTab(self.tab1)
        self.grains_tab = GrainsTab(self.tab2)
        self.vegetables_tab = VegetablesTab(self.tab3)
        self.protein_tab = ProteinTab(self.tab4)
        self.dairy_tab = DairyTab(self.tab5)

        self.root.mainloop()


app = App()
