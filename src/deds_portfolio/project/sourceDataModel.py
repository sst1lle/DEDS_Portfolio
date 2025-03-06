from graphviz import Digraph
import os

# Maak een nieuw UML-klassendiagram
dot = Digraph('sourceDataModel', format='png')

# Definitie van de klassen (gebaseerd op het samengevoegde RIM)
classes = {
    # Sales & algemene tabellen (op basis van go_sales_train)
    "Country": [
        "+CountryCode: Integer", 
        "+Country: String", 
        "+Language: String", 
        "+CurrencyName: String",
        "+FlagImage: String",
        "+SalesTerritoryCode: Integer"
    ],
    "OrderDetails": [
        "+OrderDetailCode: Integer", 
        "+OrderNumber: Integer", 
        "+ProductNumber: Integer", 
        "+Quantity: Integer", 
        "+UnitCost: Real", 
        "+UnitPrice: Real", 
        "+UnitSalePrice: Real"
    ],
    "OrderHeader": [
        "+OrderNumber: Integer", 
        "+RetailerName: String", 
        "+RetailerSiteCode: Integer", 
        "+RetailerContactCode: Integer", 
        "+SalesStaffCode: Integer", 
        "+SalesBranchCode: Integer", 
        "+OrderDate: String", 
        "+OrderMethodCode: Integer"
    ],
    "OrderMethod": [
        "+OrderMethodCode: Integer", 
        "+OrderMethodEn: String"
    ],
    "Product": [
        "+ProductNumber: Integer", 
        "+IntroductionDate: String", 
        "+ProductTypeCode: Integer", 
        "+ProductionCost: Real", 
        "+Margin: Real", 
        "+ProductImage: String", 
        "+Language: String", 
        "+ProductName: String", 
        "+Description: String"
    ],
    "ProductLine": [
        "+ProductLineCode: Integer", 
        "+ProductLineEn: String"
    ],
    "ProductType": [
        "+ProductTypeCode: Integer", 
        "+ProductLineCode: Integer", 
        "+ProductTypeEn: String"
    ],
    "RetailerSite": [
        "+RetailerSiteCode: Integer", 
        "+RetailerCode: Integer", 
        "+Address1: String", 
        "+Address2: String", 
        "+City: String", 
        "+Region: String", 
        "+CountryCode: Integer", 
        "+ActiveIndicator: Integer",
        "+PostalZone: String"
    ],
    "ReturnReason": [
        "+ReturnReasonCode: Integer", 
        "+ReturnDescriptionEn: String"
    ],
    "ReturnedItem": [
        "+ReturnCode: Integer", 
        "+ReturnDate: String", 
        "+OrderDetailCode: Integer", 
        "+ReturnReasonCode: Integer", 
        "+ReturnQuantity: Integer"
    ],
    "SalesBranch": [
        "+SalesBranchCode: Integer", 
        "+Address1: String", 
        "+Address2: String", 
        "+City: String", 
        "+Region: String", 
        "+CountryCode: Integer", 
        "ManagerCode: Integer"
    ],
    # Staff & training tabellen (go_staff_train)
    "Course": [
        "+CourseCode: Integer", 
        "+CourseDescription: String"
    ],
    "SalesStaff": [
        "+SalesStaffCode: Integer", 
        "+FirstName: String", 
        "+LastName: String", 
        "+PositionEn: String", 
        "+WorkPhone: String", 
        "+Extension: Integer", 
        "+Fax: String", 
        "+Email: String", 
        "+DateHired: String", 
        "+SalesBranchCode: Integer", 
        "+ManagerCode: Integer"
    ],
    "Satisfaction": [
        "+Year: Integer", 
        "+SalesStaffCode: Integer", 
        "+SatisfactionTypeCode: Integer"
    ],
    "SatisfactionType": [
        "+SatisfactionTypeCode: Integer", 
        "+SatisfactionTypeDescription: String"
    ],
    "Training": [
        "+Year: Integer", 
        "+SalesStaffCode: Integer", 
        "+CourseCode: Integer"
    ],
    # Inventaris & forecast
    "inventory_levels_train": [
        "+Inventory_Year: Integer", 
        "+Inventory_Month: Integer", 
        "+Product_Number: Integer", 
        "+Inventory_Count: Integer"
    ],
    "product_forecast": [
        "+Product_Number: Integer", 
        "+Year: Integer", 
        "+Month: Integer", 
        "+Expected_volume: Integer"
    ],
    # CRM-specifieke tabellen (go_crm_db)
    "age_group": [
        "+AgeGroupCode: Integer", 
        "+UpperAge: Integer", 
        "+LowerAge: Integer"
    ],
    "sales_demographic": [
        "+DemographicCode: Integer", 
        "+Retailer_CodeMR: Integer", 
        "+Age_Group_Code: Integer", 
        "+Percent: Integer"
    ],
    "retailer_headquarters": [
        "+Retailer_CodeMR: Integer", 
        "+RetailerName: String", 
        "+Address1: String", 
        "+Address2: String", 
        "+City: String", 
        "+Region: String", 
        "+PostalZone: String", 
        "+CountryCode: Integer", 
        "+Phone: String", 
        "+Segment_code: Integer"
    ],
    "retailer_segment": [
        "+Segment_code: Integer", 
        "+Language: String", 
        "+SegmentName: String", 
        "+SegmentDescription: String"
    ],
    "retailer": [
        "+RetailerCode: Integer", 
        "+Retailer_CodeMR: Integer", 
        "+Company_Name: String", 
        "+Retailer_Type_Code: Integer"
    ],
    "retailer_type": [
        "+Retailer_Type_Code: Integer", 
        "+Retailer_Type_EN: String"
    ],
    "retailer_contact": [
        "+RetailerContactCode: Integer", 
        "+RetailerSiteCode: Integer", 
        "+FirstName: String", 
        "+LastName: String", 
        "+Job_Position_EN: String", 
        "+Extension: Integer", 
        "+Fax: String", 
        "+Email: String", 
        "+Gender: String"
    ],
    "sales_territory": [
        "+Territory_Code: Integer", 
        "+Territory_Name_EN: String"
    ]
}

# Voeg de klassen toe aan het diagram
for class_name, attributes in classes.items():
    label = f"{class_name}|" + "\\l".join(attributes) + "\\l"
    dot.node(class_name, label=f"{{ {label} }}", shape="record")

# Definitie van de relaties met correcte multipliciteiten.
relations = [
    # Sales train relaties
    ("OrderHeader", "OrderDetails", "OrderNumber", "1", "0..*"),
    ("Product", "OrderDetails", "ProductNumber", "1", "0..*"),
    ("OrderMethod", "OrderHeader", "OrderMethodCode", "1", "0..*"),
    ("SalesStaff", "OrderHeader", "SalesStaffCode", "1", "0..*"),
    ("SalesBranch", "OrderHeader", "SalesBranchCode", "1", "0..*"),
    ("Country", "RetailerSite", "CountryCode", "1", "0..*"),
    ("OrderDetails", "ReturnedItem", "OrderDetailCode", "1", "0..*"),
    ("ReturnReason", "ReturnedItem", "ReturnReasonCode", "1", "0..*"),
    ("SalesBranch", "SalesStaff", "SalesBranchCode", "1", "0..*"),
    ("ProductType", "Product", "ProductTypeCode", "1", "0..*"),
    ("ProductLine", "ProductType", "ProductLineCode", "1", "0..*"),
    ("RetailerSite", "OrderHeader", "RetailerSiteCode", "1", "0..*"),
    # Staff train relaties
    ("SalesStaff", "Satisfaction", "SalesStaffCode", "1", "0..*"),
    ("SatisfactionType", "Satisfaction", "SatisfactionTypeCode", "1", "0..*"),
    ("SalesStaff", "Training", "SalesStaffCode", "1", "0..*"),
    ("Course", "Training", "CourseCode", "1", "0..*"),
    # Inventaris & forecast relaties
    ("Product", "inventory_levels_train", "Product_Number", "1", "0..*"),
    ("Product", "product_forecast", "Product_Number", "1", "0..*"),
    # CRM relaties
    ("age_group", "sales_demographic", "Age_Group_Code", "1", "0..*"),
    ("retailer_headquarters", "sales_demographic", "Retailer_CodeMR", "1", "0..*"),
    ("retailer_headquarters", "retailer", "Retailer_CodeMR", "1", "0..*"),
    ("retailer_segment", "retailer_headquarters", "Segment_code", "1", "0..*"),
    ("retailer_type", "retailer", "Retailer_Type_Code", "1", "0..*"),
    ("RetailerSite", "retailer_contact", "RetailerSiteCode", "1", "0..*"),
    ("sales_territory", "Country", "SalesTerritoryCode", "1", "0..*"),
    ("retailer", "RetailerSite", "RetailerCode", "1", "0..*")
]

# Voeg de relaties toe aan het diagram
for from_class, to_class, attr, tail_mult, head_mult in relations:
    dot.edge(from_class, to_class, label=attr, taillabel=tail_mult, headlabel=head_mult, labeldistance="2", labelfontsize="10")

# Opslaan en weergeven
output_dir = "data/processed"
os.makedirs(output_dir, exist_ok=True)
diagram_path = os.path.join(output_dir, "sourceDataModel")
dot.render(diagram_path)
print(f"Diagram saved to {diagram_path}.png")
