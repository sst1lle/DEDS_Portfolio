import os
import graphviz

# Output directory instellen
output_dir = "data/processed"
os.makedirs(output_dir, exist_ok=True)

# Bestandsnaam instellen
diagram_path = os.path.join(output_dir, "sterschema")

# Graphviz Digraph maken
dot = graphviz.Digraph(format="png")

### FEITENTABELLEN (Geel) ###
fact_tables = {
    "Order_Details": ["Order_ID", "Product_ID", "Quantity", "Unit_Cost", "Unit_Price", "Unit_Sale_Price"],
    "Returned_Item": ["Return_ID", "Order_Details_ID", "Return_Quantity", "Return_Reason_ID"],
    "Sales_Demographic": ["Demographic_ID", "Retailer_HQ_ID", "Age_Group_ID", "Sales_Percent"],
    "Inventory_Levels": ["Inventory_ID", "Product_ID", "Inventory_Year", "Inventory_Month", "Inventory_Count"],
    "Product_Forecast": ["Forecast_ID", "Product_ID", "Forecast_Year", "Forecast_Month", "Expected_Volume"],
    "Satisfaction": ["Satisfaction_ID", "Sales_Staff_ID", "Satisfaction_Type_ID", "Satisfaction_Year"]
}

for fact, attributes in fact_tables.items():
    label = f"{fact}|" + "\\l".join(attributes) + "\\l"
    dot.node(fact, label=f"{{ {label} }}", shape="record", style="filled", fillcolor="lightyellow")

### DIMENSIETABELLEN (Groen) ###
dimension_tables = {
    "Order_Header": ["Order_ID", "Order_Date", "Retailer_Site_Code", "Sales_Staff_Code", "Order_Method_ID"],
    "Product": ["Product_ID", "Product_Name", "Product_Type_ID", "Product_Line_ID"],
    "Return_Reason": ["Return_Reason_ID", "Return_Reason_Description"],
    "Retailer_Headquarters": ["Retailer_HQ_ID", "Retailer_ID", "Retailer_Name"],
    "Retailer": ["Retailer_ID", "Retailer_Name", "Retailer_Type_ID", "Retailer_Segment_ID"],
    "Retailer_Type": ["Retailer_Type_ID", "Retailer_Type_Description"],
    "Retailer_Segment": ["Retailer_Segment_ID", "Retailer_Segment_Description"],
    "Country": ["Country_ID", "Country_Name"],
    "Sales_Territory": ["Territory_ID", "Territory_Name"],
    "Age_Group": ["Age_Group_ID", "Lower_Age", "Upper_Age"],
    "Product_Type": ["Product_Type_ID", "Product_Type_Name"],
    "Product_Line": ["Product_Line_ID", "Product_Line_Name"],
    "Sales_Staff": ["Sales_Staff_ID", "Staff_Name", "Sales_Branch_ID", "Course_ID"],
    "Sales_Branch": ["Sales_Branch_ID", "Branch_Location"],
    "Course": ["Course_ID", "Course_Name"],
    "Satisfaction_Type": ["Satisfaction_Type_ID", "Satisfaction_Type_Description"],
    "Order_Method": ["Order_Method_ID", "Order_Method_Description"],
    "Tijd": ["Year", "Month"]
}

for dim, attributes in dimension_tables.items():
    label = f"{dim}|" + "\\l".join(attributes) + "\\l"
    dot.node(dim, label=f"{{ {label} }}", shape="record", style="filled", fillcolor="lightgreen")

### RELATIES TUSSEN FEITEN EN DIMENSIES ###
dot.edge("Order_Details", "Order_Header", label="Order_ID")
dot.edge("Order_Details", "Product", label="Product_ID")

dot.edge("Returned_Item", "Order_Details", label="Order_Details_ID")
dot.edge("Returned_Item", "Return_Reason", label="Return_Reason_ID")

dot.edge("Sales_Demographic", "Retailer_Headquarters", label="Retailer_HQ_ID")
dot.edge("Sales_Demographic", "Age_Group", label="Age_Group_ID")

dot.edge("Inventory_Levels", "Product", label="Product_ID")
dot.edge("Inventory_Levels", "Tijd", label="Inventory_Year, Inventory_Month")

dot.edge("Product_Forecast", "Product", label="Product_ID")
dot.edge("Product_Forecast", "Tijd", label="Forecast_Year, Forecast_Month")

dot.edge("Satisfaction", "Sales_Staff", label="Sales_Staff_ID")
dot.edge("Satisfaction", "Satisfaction_Type", label="Satisfaction_Type_ID")
dot.edge("Satisfaction", "Tijd", label="Satisfaction_Year")

### RELATIES TUSSEN DIMENSIETABELLEN ###
dot.edge("Retailer_Headquarters", "Retailer", label="Retailer_ID")
dot.edge("Retailer", "Retailer_Type", label="Retailer_Type_ID")
dot.edge("Retailer_Type", "Retailer_Segment", label="Retailer_Segment_ID")
dot.edge("Country", "Sales_Territory", label="Country_ID")
dot.edge("Product", "Product_Type", label="Product_Type_ID")
dot.edge("Product_Type", "Product_Line", label="Product_Line_ID")
dot.edge("Sales_Staff", "Sales_Branch", label="Sales_Branch_ID")
dot.edge("Sales_Staff", "Course", label="Course_ID")
dot.edge("Order_Header", "Order_Method", label="Order_Method_ID")

# Diagram opslaan als PNG
dot.render(diagram_path)
print(f"Diagram saved to {diagram_path}.png")
