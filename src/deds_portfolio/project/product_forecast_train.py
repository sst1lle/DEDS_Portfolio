from graphviz import Digraph
import os

dot = Digraph('product_forecast_train', format='png')   

classes = {
        "product_forecast": ["+Product_Number: Integer", "+Year: Integer", "+Month: Integer", "+Expected_volume: Integer"]
    }

for class_name, attributes in classes.items():
    label = f"{class_name}|" + "\\l".join(attributes) + "\\l"
    dot.node(class_name, label=f"{{ {label} }}", shape="record")

output_dir = "data/processed"
os.makedirs(output_dir, exist_ok=True)
diagram_path = os.path.join(output_dir, "product_forecast_train")

dot.render(diagram_path)
print(f"Diagram saved to {diagram_path}.png")