import pandas 
import sqlite3
import warnings
import settings


def function():
    dataframes = settings.settings.dataframes
    filtered_dataframes = {}


    filtered_producten = dataframes["product"][['PRODUCT_NAME','PRODUCTION_COST']]
    filtered_producten = filtered_producten[
        (filtered_producten["PRODUCTION_COST"] > 50) & (filtered_producten["PRODUCTION_COST"] < 100)
    ]
    print(filtered_producten)
    filtered_dataframes["filtered_producten"] = filtered_producten

    filtered_marges = dataframes["product"][["PRODUCT_NAME","MARGIN"]]
    filtered_marges = filtered_marges[
        (filtered_marges["MARGIN"] > 0.60) | (filtered_marges["MARGIN"] < 0.20)
    ]
    print(filtered_marges)
    filtered_dataframes["filtered_marges"] = filtered_marges


    filter_francs = dataframes["country"][
        dataframes["country"]["CURRENCY_NAME"] == "francs"
    ][["COUNTRY"]].sort_values("COUNTRY")
    print(filter_francs)
    filtered_dataframes["filter_francs"] = filter_francs


    filter_introdatum_marge = dataframes["product"][
        dataframes["product"]["MARGIN"] > 0.50
    ][["INTRODUCTION_DATE"]].drop_duplicates()
    print(filter_introdatum_marge)
    filtered_dataframes["filter_introdatum_marge"] = filter_introdatum_marge


    filter_verkoopafdeling = dataframes["retailer_site"].loc[
        (dataframes["retailer_site"]["ADDRESS2"].notnull()) & 
        (dataframes["retailer_site"]["REGION"].notnull()),
        ["ADDRESS1", "CITY"]
    ].drop_duplicates()
    print(filter_verkoopafdeling)
    filtered_dataframes["filter_verkoopafdeling"] = filter_verkoopafdeling


    filter_landen_dollar = dataframes["country"].loc[
        (dataframes["country"]["CURRENCY_NAME"] == "dollars") | (dataframes["country"]["CURRENCY_NAME"] == "new dollar"),
        ["COUNTRY"]
    ]
    print(filter_landen_dollar)
    filtered_dataframes["filter_landen_dollar"] = filter_landen_dollar

    return filtered_dataframes
