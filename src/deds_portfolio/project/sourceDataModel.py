from graphviz import Digraph
import os

# Maak een nieuw UML-klassendiagram
dot = Digraph('sourceDataModel', format='png')

# Definieer de klassen en hun attributen
classes = {
    # got sales train database
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
    "SalesBranch": ["+SalesBranchCode: Integer", "+Address1: String", "+Address2: String", "+City: String", "+Region: String", "+CountryCode: Integer", "ManagerCode: Integer"],
    # go staff train database
    "Course": ["+CourseCode: Integer", "+CourseDescription: String"],
    "SalesStaff": ["+SalesStaffCode: Integer", "+FirstName: String", "+LastName: String", "+PositionEn: String", "+WorkPhone: String", "+Extension: Integer", "+Fax: String", "+Email: String", "+DateHired: String", "+SalesBranchCode: Integer", "+ManagerCode: Integer"],
    "Satisfaction": ["+Year: Integer", "+SalesStaffCode: Integer", "+SatisfactionTypeCode: Integer"],
    "SatisfactionType": ["+SatisfactionTypeCode: Integer", "+SatisfactionTypeDescription: String"],
    "Training": ["+Year: Integer", "+SalesStaffCode: Integer", "+CourseCode: Integer"],
    # inventory levels train database
    "inventory_levels_train": ["+Inventory_Year: Integer", "+Inventory_Month: Integer", "+Product_Number: Integer", "+Inventory_Count: Integer"],
    # product forecast database
    "product_forecast": ["+Product_Number: Integer", "+Year: Integer", "+Month: Integer", "+Expected_volume: Integer"],
    # go crm databasemodel
    "age_group": ["+AgeGroupCode: Integer", "+UpperAge: Integer", "+LowerAge: Integer"],
    "sales_demographic": ["+DemographicCode: Integer", "+Retailer_CodeMR: Integer", "+Age_Group_Code: Integer", "+Percent: Integer"],
    "retailer_headquarters": ["+Retailer_CodeMR: Integer", "+RetailerName: String", "+Address1: String", "+Address2: String", "+City: String", "+Region: String", "+Postal_Zone: String", "+CountryCode: Integer", "+Phone: String", "+Segment_code: Integer"],
    "retailer_segment": ["+Segment_code: Integer", "+Language: String", "+SegmentName: String", "+SegmentDescription: String"],
    "retailer": ["+RetailerCode: Integer", "+Retailer_CodeMR: Integer", "+Company_Name: String", "+Retailer_Type_Code: Integer"],
    "retailer_type": ["+Retailer_Type_Code: Integer", "+Retailer_Type_EN: String"],
    "crm_retailer_site": ["+RetailerSiteCode: Integer", "+RetailerCode: Integer", "+Address1: String", "+Address2: String", "+City: String", "+Region: String", "+Postal_Zone: String", "+CountryCode: Integer",  "+ActiveIndicator: Integer"],
    "retailer_contact": ["+RetailerContactCode: Integer", "+RetailerSiteCode: Integer", "+FirstName: String", "+LastName: String", "+Job_Position_EN: String", "+Extension: Integer", "+Fax: String", "+Email: String", "+Gender: String"],
    "crm_country": ["Country_Code: Integer", "Country_EN: String", "Flag_Image: String", "Territory_Code: Integer"],
    "sales_territory": ["+Territory_Code: Integer", "+Territory_Name_EN: String"],
}

# Voeg de klassen toe aan het diagram
for class_name, attributes in classes.items():
    label = f"{class_name}|" + "\\l".join(attributes) + "\\l"
    dot.node(class_name, label=f"{{ {label} }}", shape="record")

# Definieer de relaties met multipliciteiten.
# Elke tuple bevat: (van, naar, attribuut, taillabel (vanzijde), headlabel (naarzijde))
relations = [
    # Relations from go sales train database
    ("OrderHeader", "OrderDetails", "OrderNumber", "1", "0..*"),
    ("OrderDetails", "Product", "ProductNumber", "1", "0..*"),
    ("OrderHeader", "OrderMethod", "OrderMethodCode", "0..*", "1"),
    ("OrderHeader", "SalesStaff", "SalesStaffCode",  "0..*", "1"),
    ("OrderHeader", "SalesBranch", "SalesBranchCode",  "0..*", "1"),
    ("RetailerSite", "Country", "CountryCode",  "0..*", "1"),
    ("ReturnedItem", "OrderDetails", "OrderDetailCode",  "0..*", "1"),
    ("ReturnedItem", "ReturnReason", "ReturnReasonCode", "0..*", "1"),
    ("SalesStaff", "SalesBranch", "SalesBranchCode", "0..*", "1"),
    ("Product", "ProductType", "ProductTypeCode", "0..*", "1"),
    ("ProductType", "ProductLine", "ProductLineCode", "0..*", "1"),
    ("RetailerSite", "OrderHeader", "RetailerSiteCode", "1", "0..*"),
    # Relations from go staff train database
    ("Satisfaction", "SalesStaff", "SalesStaffCode", "0..*", "1"),
    ("Satisfaction", "SatisfactionType", "SatisfactionTypeCode", "0..*", "1"),
    ("Training", "SalesStaff", "SalesStaffCode", "0..*", "1"),
    ("Training", "Course", "CourseCode", "0..*", "1"),
    # Relations from inventory levels train database
    ("inventory_levels_train", "Product", "Product_Number", "0..*", "1"),
    # Relations from product forecast database
    ("product_forecast", "Product", "Product_Number", "0..*", "1"),
    # Relations from go crm database
    ("sales_demographic", "age_group", "Age_Group_Code", "0..*", "1"),
    ("sales_demographic", "retailer_headquarters", "Retailer_CodeMR", "0..*", "1"),
    ("retailer_headquarters", "retailer", "Retailer_CodeMR", "0..*", "1"),
    ("retailer_segment", "retailer_headquarters", "Segment_code",  "0..*", "1"),
    ("retailer", "retailer_type", "Retailer_Type_Code", "0..*", "1"),
    ("crm_retailer_site", "retailer", "RetailerCode", "0..*", "1"),
    ("retailer_contact", "crm_retailer_site", "RetailerSiteCode", "0..*", "1"),
    ("crm_country", "sales_territory", "Territory_Code",  "0..*", "1"),
    ("crm_country", "crm_retailer_site", "CountryCode",  "0..*", "1"),
    ("OrderHeader", "crm_retailer_site", "RetailerSiteCode", "0..*", "1"),
    ("RetailerSite", "retailer", "RetailerCode", "0..*", "1")
]

# Voeg de relaties met multipliciteiten toe aan het diagram
for from_class, to_class, attr, tail_mult, head_mult in relations:
    dot.edge(from_class, to_class, label=attr, taillabel=tail_mult, headlabel=head_mult, labeldistance="2", labelfontsize="10")

# Opslaan en weergeven
output_dir = "data/processed"
os.makedirs(output_dir, exist_ok=True)
diagram_path = os.path.join(output_dir, "sourceDataModel")
dot.render(diagram_path)
print(f"Diagram saved to {diagram_path}.png")
