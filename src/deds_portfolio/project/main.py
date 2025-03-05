from script import function
import settings
import pandas as pd
import os

def save_to_excel():
    output_dir = "data/processed"
    os.makedirs(output_dir, exist_ok=True)  # Zorgt ervoor dat de map bestaat
    
    output_path = os.path.join(output_dir, "output.xlsx")  # Pad binnen data/processed
    filtered_dataframes = function()

    with pd.ExcelWriter(output_path, engine="xlsxwriter") as writer:
        for sheet_name, df in filtered_dataframes.items():
            df.to_excel(writer, sheet_name=sheet_name, index=False)  
      
    print(f"Dataframes saved to {output_path}")

def main():
    function()  # Roep de functie aan (indien nodig)
    save_to_excel()  # Zorgt ervoor dat de Excel in data/processed wordt opgeslagen

if __name__ == "__main__":
    main()
