from graphviz import Digraph
import os

# Maak een nieuw UML-klassendiagram
dot = Digraph('go_sales_train', format='png')

# Definieer de klassen en hun attributen
classes = {
    "Country": ["+CountryCode: Integer", "+Country: String", "+Language: String", "+CurrencyName: String"],
    "OrderDetails": ["+OrderDetailCode: Integer", "+OrderNumber: Integer", "+ProductNumber: Integer", "+Quantity: Integer", "+UnitCost: Real", "+UnitPrice: Real", "+UnitSalePrice: Real"],
    "OrderHeader": ["+OrderNumber: Integer", "+RetailerName: String", "+RetailerSiteCode: Integer", "+RetailerContactCode: Integer", "+SalesStaffCode: Integer", "+SalesBranchCode: Integer", "+OrderDate: String", "+OrderMethodCode: Integer"],
    "OrderMethod": ["+OrderMethodCode: Integer", "+OrderMethodEn: String"],
    "Product": ["+ProductNumber: Integer", "+IntroductionDate: String", "+ProductTypeCode: Integer", "+ProductionCost: Real", "+Margin: Real", "+ProductImage: String", "+Language: String", "+ProductName: String", "+Description: String"],
    "ProductLine": ["+ProductLineCode: Integer", "+ProductLineEn: String"],
    "ProductType": ["+ProductTypeCode: Integer", "+ProductLineCode: Integer", "+ProductTypeEn: String"],
    "RetailerSite": ["+RetailerSiteCode: Integer", "+RetailerCode: Integer", "+Address1: String", "+Address2: String", "+City: String", "+Region: String", "+CountryCode: Integer", "+ActiveIndicator: Integer"],
    "ReturnReason": ["+ReturnReasonCode: Integer", "+ReturnDescriptionEn: String"],
    "ReturnedItem": ["+ReturnCode: Integer", "+ReturnDate: String", "+OrderDetailCode: Integer", "+ReturnReasonCode: Integer", "+ReturnQuantity: Integer"],
    "SalesBranch": ["+SalesBranchCode: Integer", "+Address1: String", "+Address2: String", "+City: String", "+Region: String", "+CountryCode: Integer"],
    "SalesStaff": ["+SalesStaffCode: Integer", "+FirstName: String", "+LastName: String", "+PositionEn: String", "+WorkPhone: String", "+Extension: Integer", "+Fax: String", "+Email: String", "+DateHired: String", "+SalesBranchCode: Integer"]
}

# Voeg de klassen toe aan het diagram
for class_name, attributes in classes.items():
    label = f"{class_name}|" + "\\l".join(attributes) + "\\l"
    dot.node(class_name, label=f"{{ {label} }}", shape="record")

# Definieer de relaties
relations = [
    ("OrderDetails", "OrderHeader", "OrderNumber"),
    ("OrderDetails", "Product", "ProductNumber"),
    ("OrderHeader", "OrderMethod", "OrderMethodCode"),
    ("OrderHeader", "SalesStaff", "SalesStaffCode"),
    ("OrderHeader", "SalesBranch", "SalesBranchCode"),
    ("RetailerSite", "Country", "CountryCode"),
    ("ReturnedItem", "OrderDetails", "OrderDetailCode"),
    ("ReturnedItem", "ReturnReason", "ReturnReasonCode"),
    ("SalesStaff", "SalesBranch", "SalesBranchCode"),
    ("Product", "ProductType", "ProductTypeCode"),
    ("ProductType", "ProductLine", "ProductLineCode"),
    ("RetailerSite", "OrderHeader", "RetailerSiteCode"),

]

# Voeg de relaties toe aan het diagram
for from_class, to_class, label in relations:
    dot.edge(from_class, to_class, label=label)

# Opslaan en weergeven
output_dir = "data/processed"
os.makedirs(output_dir, exist_ok=True)
diagram_path = os.path.join(output_dir, "go_sales_train")

dot.render(diagram_path)
print(f"Diagram saved to {diagram_path}.png")