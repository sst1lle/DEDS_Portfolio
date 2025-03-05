from graphviz import Digraph
import os

# Maak een nieuw UML-klassendiagram
dot = Digraph('go_staff_train', format='png')

# Definieer de klassen en hun attributen
classes = {
    "Course": ["+CourseCode: Integer", "+CourseDescription: String"],
    "SalesBranch": ["+SalesBranchCode: Integer", "+Address1: String", "+Address2: String", "+City: String", "+Region: String", "+CountryCode: Integer"],
    "SalesStaff": ["+SalesStaffCode: Integer", "+FirstName: String", "+LastName: String", "+PositionEn: String", "+WorkPhone: String", "+Extension: Integer", "+Fax: String", "+Email: String", "+DateHired: String", "+SalesBranchCode: Integer", "+ManagerCode: Integer"],
    "Satisfaction": ["+Year: Integer", "+SalesStaffCode: Integer", "+SatisfactionTypeCode: Integer"],
    "SatisfactionType": ["+SatisfactionTypeCode: Integer", "+SatisfactionTypeDescription: String"],
    "Training": ["+Year: Integer", "+SalesStaffCode: Integer", "+CourseCode: Integer"]
}

# Voeg de klassen toe aan het diagram
for class_name, attributes in classes.items():
    label = f"{class_name}|" + "\l".join(attributes) + "\l"
    dot.node(class_name, label=f"{{ {label} }}", shape="record")

# Definieer de relaties
relations = [
    ("SalesStaff", "SalesBranch", "SalesBranchCode"),
    ("Satisfaction", "SalesStaff", "SalesStaffCode"),
    ("Satisfaction", "SatisfactionType", "SatisfactionTypeCode"),
    ("Training", "SalesStaff", "SalesStaffCode"),
    ("Training", "Course", "CourseCode")
]

# Voeg de relaties toe aan het diagram
for from_class, to_class, label in relations:
    dot.edge(from_class, to_class, label=label)

# Opslaan en weergeven
output_dir = "data/processed"
os.makedirs(output_dir, exist_ok=True)
diagram_path = os.path.join(output_dir, "go_staff_train")

dot.render(diagram_path)
print(f"Diagram saved to {diagram_path}.png")
