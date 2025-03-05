from script import function
import settings
import pandas as pd

def save_to_excel():
    output_path = "output.xlsx"
    filtered_dataframes = function()
    var = 1

    with pd.ExcelWriter(output_path, engine="xlsxwriter") as writer:
        for sheet_name, df in filtered_dataframes.items():
            df.to_excel(writer, sheet_name=sheet_name, index=False)  
            var += 1
      
    print(f"Dataframes saved to {output_path}")



def main() :
   function()
   save_to_excel()
    

if __name__ == "__main__":
    main()