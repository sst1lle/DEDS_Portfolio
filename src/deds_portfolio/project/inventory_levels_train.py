from graphviz import Digraph
import os

dot = Digraph('inventory_levels_train', format='png')   

classes = {
        "inventory_levels_train": ["+Inventory_Year: Integer", "+Inventory_Month: Integer", "+Product_Number: Integer", "+Inventory_Count: Integer"]
    }

for class_name, attributes in classes.items():
    label = f"{class_name}|" + "\\l".join(attributes) + "\\l"
    dot.node(class_name, label=f"{{ {label} }}", shape="record")

output_dir = "data/processed"
os.makedirs(output_dir, exist_ok=True)
diagram_path = os.path.join(output_dir, "inventory_levels_train")

dot.render(diagram_path)
print(f"Diagram saved to {diagram_path}.png")