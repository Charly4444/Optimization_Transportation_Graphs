import tkinter as tk
from tkinter import messagebox
from northwest import northwest_algo
from PDsolver import pdsolver

class MainApplication:
    def __init__(self, root):
        self.root = root
        self.root.title("Transportation Problem Solver")
        self.root.geometry("400x400") 
        self.root.configure(bg="lightgray")
        self.transport_matrix = None

        # Create a menu bar
        self.menu_bar = tk.Menu(self.root)

        # Create a "File" menu
        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.file_menu.add_command(label="New", command=self.open_new_window)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit", command=self.root.quit)

        # Add "File" menu to the menu bar
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)

        # Configure the menu bar
        self.root.config(menu=self.menu_bar)

    def open_new_window(self):
        new_window = tk.Toplevel(self.root)
        NewTransportProblemWindow(new_window,self)

    
    def update_transport_matrix(self, transport_matrix):
        # Update the transport matrix on the main window
        self.transport_matrix = transport_matrix
        self.display_transport_matrix()


    def display_transport_matrix(self):
        # Display the generated transport matrix
        for i in range(len(self.transport_matrix)):
            for j in range(len(self.transport_matrix[0])):
                label = tk.Label(self.root, text=str(self.transport_matrix[i][j]))
                label.grid(row=i, column=j + 3, padx=5, pady=5)

        # Create and pack a button to adjust the matrix
        self.adjust_matrix_button = tk.Button(self.root, text="Adjust Matrix", command=self.adjust_matrix)
        self.adjust_matrix_button.grid(row=i + 4, column=0, columnspan=len(self.transport_matrix[0]), padx=5, pady=5)

    
    def adjust_matrix(self):
        # Call the pdsolver to adjust the matrix
        adjusted_matrix, cycle, cost = pdsolver(self.transport_matrix)
        print('TRANSPORT: ', [row for row in self.transport_matrix] )
        

        # Display the adjusted matrix:: very clever adjusting with \n and \t
        adjusted_matrix_str = "\n".join(["\t".join(map(str, row)) for row in adjusted_matrix])
        adjusted_matrix_label = tk.Label(self.root, text=adjusted_matrix_str)
        adjusted_matrix_label.grid(row=len(self.transport_matrix) + 4, column=0, columnspan=len(self.transport_matrix[0]), padx=5, pady=5)
        
        # Display the cost beside the adjusted matrix
        cost_label = tk.Label(self.root, text=f"Total Cost: {cost}")
        cost_label.grid(row=len(self.transport_matrix) + 4, column=len(self.transport_matrix[0]) + 1, padx=5, pady=5)
        
        # Display the cycle below the adjusted matrix and cost
        cycle_str = "Cycle: " + ", ".join([str(item) for item in cycle])
        cycle_label = tk.Label(self.root, text=cycle_str)
        cycle_label.grid(row=len(self.transport_matrix) + 5, column=0, columnspan=len(self.transport_matrix[0]) + 1, padx=5, pady=5)

        # Set the background color of label cells corresponding to cycle entries to red
        for x, y in cycle:
            for slave in self.root.grid_slaves():
                if int(slave.grid_info()["row"]) == x and int(slave.grid_info()["column"]) == y+3:
                    slave.config(bg="red")

        messagebox.showinfo("done")




# like another tkapp built off this class
class NewTransportProblemWindow:
    def __init__(self, root, main_window):
        self.root = root
        self.main_window = main_window
        self.root.title("New Transportation Problem")

        # Initialize variables for storing the number of product and demand constraints
        self.num_products = tk.StringVar()
        self.num_demands = tk.StringVar()

        # Create and pack fields for entering the number of product and demand constraints
        self.product_label = tk.Label(self.root, text="Number of Product Constraints:")
        self.product_label.grid(row=0, column=0, padx=5, pady=5)
        self.product_entry = tk.Entry(self.root, textvariable=self.num_products)
        self.product_entry.grid(row=0, column=1, padx=5, pady=5)

        self.demand_label = tk.Label(self.root, text="Number of Demand Constraints:")
        self.demand_label.grid(row=1, column=0, padx=5, pady=5)
        self.demand_entry = tk.Entry(self.root, textvariable=self.num_demands)
        self.demand_entry.grid(row=1, column=1, padx=5, pady=5)

        # Create and pack a "Next" button
        self.next_button = tk.Button(self.root, text="Next", command=self.create_constraint_entries)
        self.next_button.grid(row=2, columnspan=2, pady=10)

        

    def create_constraint_entries(self):
        # Validate and get the number of product and demand constraints entered
        num_products = self.num_products.get()
        num_demands = self.num_demands.get()

        if not num_products.isdigit() or not num_demands.isdigit():
            messagebox.showerror("Error", "Please enter valid numbers for product and demand constraints.")
            return

        # Convert the entered numbers to integers
        num_products = int(num_products)
        num_demands = int(num_demands)

        # Remove the number entry fields and the "Next" button
        self.product_label.destroy()
        self.product_entry.destroy()
        self.demand_label.destroy()
        self.demand_entry.destroy()
        self.next_button.destroy()

        # Create and pack fields for entering product constraints
        self.product_constraints = []
        for i in range(num_products):
            label = tk.Label(self.root, text=f"Product Constraint {i + 1}:")
            label.grid(row=i, column=0, padx=5, pady=5)
            entry = tk.Entry(self.root)
            entry.grid(row=i, column=1, padx=5, pady=5)
            self.product_constraints.append(entry)

        # Create and pack fields for entering demand constraints
        self.demand_constraints = []
        for i in range(num_demands):
            label = tk.Label(self.root, text=f"Demand Constraint {i + 1}:")
            label.grid(row=i, column=2, padx=5, pady=5)
            entry = tk.Entry(self.root)
            entry.grid(row=i, column=3, padx=5, pady=5)
            self.demand_constraints.append(entry)

        # Create and pack a "Generate Init" button
        self.generate_init_button = tk.Button(self.root, text="Generate Init", command=self.generate_init)
        self.generate_init_button.grid(row=max(num_products, num_demands), columnspan=4, pady=10)

    def generate_init(self):
        # Validate and get the entered product and demand constraints
        product_constraints = [constraint.get() for constraint in self.product_constraints]
        demand_constraints = [constraint.get() for constraint in self.demand_constraints]

        if not all(constraint.isdigit() for constraint in product_constraints) or \
           not all(constraint.isdigit() for constraint in demand_constraints):
            messagebox.showerror("Error", "Please enter valid numbers for product and demand constraints.")
            return

        # Convert the entered constraints to integers
        product_constraints = [int(constraint) for constraint in product_constraints]
        demand_constraints = [int(constraint) for constraint in demand_constraints]

        # CALL NORTHWEST FOR ORIGINAL SOLUTION
        self.generate_initial_matrix(product_constraints, demand_constraints)

    def generate_initial_matrix(self, product_constraints, demand_constraints):
        transport_matrix = northwest_algo(demand_constraints, product_constraints,)
        self.main_window.update_transport_matrix(transport_matrix)
    
    

if __name__ == "__main__":
    root = tk.Tk()
    app = MainApplication(root)
    root.mainloop()
