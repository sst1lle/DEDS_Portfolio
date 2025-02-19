# %% [markdown]
# # Werkcollege-opdrachten Week 1.3

# %% [markdown]
# ## Dependencies importeren

# %% [markdown]
# Kopieer in het codeblok hieronder van het vorige practicum de import-code voor de dependencies die het vaakst worden gebruikt om data in te lezen. Geef er ook de gebruikelijke aliassen aan.<br>
# Zet eventuele warnings uit.

# %%
import pandas 
import sqlite3
import warnings
warnings.simplefilter('ignore')

# %% [markdown]
# Zet het bestand go_sales_train.sqlite in een makkelijk te vinden map

# %% [markdown]
# ## Databasetabellen inlezen

# %% [markdown]
# Kopieer in het codeblok hieronder van het vorige practicum de code om een connectie met het bestand go_sales_train.sqlite te maken.

# %%

conn = sqlite3.connect('sql/go_sales_train2.sqlite')
print("SQLite3 Connection: ",conn)



# %% [markdown]
# Lees van de ingelezen go_sales_train-database te volgende tabellen in met behulp van "SELECT * FROM *tabel*".
# - product
# - product_type
# - product_line
# - sales_staff
# - sales_branch
# - retailer_site
# - country
# - order_header
# - order_details
# - returned_item
# - return_reason

# %%
tabellen = [
    "product", "product_type", "product_line", "sales_staff", 
    "sales_branch", "retailer_site", "country", "order_header", 
    "order_details", "returned_item", "return_reason"
]

dataframes = {}

for tabel in tabellen:
    dataframes[tabel] = pandas.read_sql_query(f"SELECT * FROM {tabel}", conn)
    print(f"Tabel '{tabel}' ingelezen met {len(dataframes[tabel])} rijen.")



# %% [markdown]
# Krijg je een "no such table" error? Dan heb je misschien met .connect() per ongeluk een leeg  databasebestand (.sqlite) aangemaakt. <u>Let op:</u> lees eventueel de informatie uit het Notebook van werkcollege 1.1b nog eens goed door.

# %% [markdown]
# Als je tijdens onderstaande opdrachten uit het oog verliest welke tabellen er allemaal zijn, kan je deze Pythoncode uitvoeren:

# %%
sql_query = "SELECT name FROM sqlite_master WHERE type='table';"
#Vul dit codeblok verder in
pandas.read_sql(sql_query, conn)
#Op de puntjes hoort de connectie naar go_sales_train óf go_staff_train óf go_crm_train te staan.

# %% [markdown]
# erachter 

# %% [markdown]
# Let op! Voor alle onderstaande opdrachten mag je <u>alleen Python</u> gebruiken, <u>geen SQL!</u>

# %% [markdown]
# ## Selecties op één tabel zonder functies

# %% [markdown]
# Geef een overzicht met daarin de producten en hun productiekosten waarvan de productiekosten lager dan 100 dollar en hoger dan 50 dollar ligt. (2 kolommen, 23 rijen)

# %%
filtered_producten = dataframes["product"][['PRODUCT_NAME','PRODUCTION_COST']]
filtered_producten = filtered_producten[
    (filtered_producten["PRODUCTION_COST"] > 50) & (filtered_producten["PRODUCTION_COST"] < 100)
]
print(filtered_producten)

# %% [markdown]
# Geef een overzicht met daarin de producten en hun marge waarvan de marge lager dan 20 % of hoger dan 60 % ligt. (2 kolommen, 7 rijen) 

# %%
filtered_marges = dataframes["product"][["PRODUCT_NAME","MARGIN"]]
filtered_marges = filtered_marges[
    (filtered_marges["MARGIN"] > 0.60) | (filtered_marges["MARGIN"] < 0.20)
]
print(filtered_marges)

# %% [markdown]
# Geef een overzicht met daarin de landen waar met francs wordt betaald. Sorteer de uitkomst op land.  (1 kolom, 3 rijen)

# %%
filter_francs = dataframes["country"][
    dataframes["country"]["CURRENCY_NAME"] == "francs"
][["COUNTRY"]].sort_values("COUNTRY")

print(filter_francs)


# %% [markdown]
# Geef een overzicht met daarin de verschillende introductiedatums waarop producten met meer dan 50% marge worden geïntroduceerd (1 kolom, 7 rijen) 

# %%
filter_introdatum_marge_meer_dan_vijftig = dataframes["product"][
    dataframes["product"]["MARGIN"] > 0.50
][["INTRODUCTION_DATE"]].drop_duplicates()

print(filter_introdatum_marge_meer_dan_vijftig)

# %% [markdown]
# Geef een overzicht met daarin het eerste adres en de stad van verkoopafdelingen waarvan zowel het tweede adres als de regio bekend is (2 kolommen, 7 rijen)

# %%
filter_verkoopafdeling = dataframes["retailer_site"].loc[
    (dataframes["retailer_site"]["ADDRESS2"].notnull()) & 
    (dataframes["retailer_site"]["REGION"].notnull()),
    ["ADDRESS1", "CITY"]
].drop_duplicates()

print(filter_verkoopafdeling)
#ik begrijp niet hoe je hier 7 rijen als uitkomst kan hebben, heb ook database gecheckt en er zijn wel meer dan 7 rijen die een address1 en region aanwezig hebben.

# %% [markdown]
# Geef een overzicht met daarin de landen waar met dollars (dollars of new dollar) wordt betaald. Sorteer de uitkomst op land. (1 kolom, 4 rijen) 

# %%
filter_landen_dollar = dataframes["country"].loc[
    (dataframes["country"]["CURRENCY_NAME"] == "dollars") | (dataframes["country"]["CURRENCY_NAME"] == "new dollar"),
    ["COUNTRY"]
]
print(filter_landen_dollar)

# %% [markdown]
# Geef een overzicht met daarin beide adressen en de stad van vestigingen van klanten waarvan de postcode begint met een ‘D’ (van duitsland). Filter op vestigingen die een tweede adres hebben. (3 kolommen, 2 rijen) 

# %%
filter_beide_adressen_filliaal = dataframes["retailer_site"].loc[
    (dataframes["retailer_site"]["POSTAL_ZONE"].str.startswith("D", na=False)) &
    (dataframes["retailer_site"]["ADDRESS2"].notnull()),
    ["ADDRESS1","ADDRESS2","CITY"]
].sort_values(by="ADDRESS2")

print(filter_beide_adressen_filliaal)

# %% [markdown]
# ## Selecties op één tabel met functies

# %% [markdown]
# Geef het totaal aantal producten dat is teruggebracht (1 waarde) 

# %%
return_count = dataframes["returned_item"]["RETURN_QUANTITY"].sum()

print(return_count)

# %% [markdown]
# Geef het aantal regio’s waarin verkoopafdelingen gevestigd zijn. (1 waarde)

# %%
aantal_regios = dataframes["retailer_site"]["REGION"].nunique()

print(aantal_regios)

# %% [markdown]
# Maak 3 variabelen:
# - Een met de laagste
# - Een met de hoogste
# - Een met de gemiddelde (afgerond op 2 decimalen)
# 
# marge van producten (3 kolommen, 1 rij) 

# %%
hoogste = dataframes["product"]["MARGIN"].max()
laagste = dataframes["product"]["MARGIN"].min()
gem = dataframes["product"]["MARGIN"].mean()

print(f"Hoogste winstmarge: {hoogste}")
print(f"laagste winstmarge: {laagste}")
print(f"Gemiddelde winstmarge: {gem.round(2)}")

# %% [markdown]
# Geef het aantal vestigingen van klanten waarvan het 2e adres niet bekend is (1 waarde)

# %%
count_vestiging = dataframes["retailer_site"][dataframes["retailer_site"]["ADDRESS2"].isnull()].shape[0]
print(count_vestiging)

# %% [markdown]
# Geef de gemiddelde kostprijs van de verkochte producten waarop korting (unit_sale_price < unit_price) is verleend (1 waarde) 

# %%
gem_kostprijs = dataframes["order_details"][
    (dataframes)["order_details"]["UNIT_SALE_PRICE"] < (dataframes)["order_details"]["UNIT_PRICE"]
]["UNIT_COST"].mean()

print(gem_kostprijs)

# %% [markdown]
# Geef een overzicht met daarin het aantal medewerkers per medewerkersfunctie (2 kolommen, 7 rijen) 

# %%
medewerkers_per_functie = dataframes["sales_staff"].groupby("POSITION_EN").size().reset_index(name="AANTAL MEDEWERKERS")

print(medewerkers_per_functie)

# %% [markdown]
# Geef een overzicht met daarin per telefoonnummer het aantal medewerkers dat op dat telefoonnummer bereikbaar is. Toon alleen de telefoonnummer waarop meer dan 4 medewerkers bereikbaar zijn. (2 kolommen, 10 rijen) 

# %%
medewerkers_per_telefoon = dataframes["sales_staff"].groupby("WORK_PHONE").size().reset_index(name="AANTAL_MEDEWERKERS")

medewerkers_per_telefoon_filtered = medewerkers_per_telefoon[medewerkers_per_telefoon["AANTAL_MEDEWERKERS"] > 4]

print(medewerkers_per_telefoon_filtered)

# %% [markdown]
# ## Selecties op meerdere tabellen zonder functies

# %% [markdown]
# Geef een overzicht met daarin het eerste adres en de stad van vestigingen van klanten uit ‘Netherlands’ (2 kolommen, 20 rijen) 

# %%
adres_filliaal = dataframes["retailer_site"].merge(dataframes["country"], on="COUNTRY_CODE")
adres_ned_filliaal = adres_filliaal[adres_filliaal["COUNTRY"] == "Netherlands"]
resultaat = adres_ned_filliaal[["ADDRESS1","CITY"]]
print(resultaat)

# %% [markdown]
# Geef een overzicht met daarin de productnamen die tot het producttype ‘Eyewear’ behoren. (1 kolom, 5 rijen) 

# %%
merge_product_type_en_product = dataframes["product"].merge(dataframes["product_type"], on="PRODUCT_TYPE_CODE")
eyewear_producten = merge_product_type_en_product[merge_product_type_en_product["PRODUCT_TYPE_EN"] == "Eyewear"]
eyewear_producten = eyewear_producten[["PRODUCT_NAME"]]

print(eyewear_producten)

# %% [markdown]
# Geef een overzicht met daarin alle unieke eerste adressen van klantvestigingen en de voornaam en achternaam van de verkopers die ‘Branch Manager’ zijn en aan deze vestigingen hebben verkocht (3 kolommen, 1 rij) 

# %%
merge_sales_branch_met_sales_staff = dataframes["sales_branch"].merge(dataframes["sales_staff"], on="SALES_BRANCH_CODE")
overzicht_adres_naam = merge_sales_branch_met_sales_staff[merge_sales_branch_met_sales_staff["POSITION_EN"] == "Branch Manager"][["ADDRESS1","FIRST_NAME","LAST_NAME"]].drop_duplicates()

print(overzicht_adres_naam)


# %% [markdown]
# Geef een overzicht met daarin van de verkopers hun functie en indien zij iets hebben verkocht de datum waarop de verkoop heeft plaatsgevonden. Laat alleen de verschillende namen van de posities zien van de verkopers die het woord ‘Manager’ in hun positienaam hebben staan. (2 kolommen, 7 rijen) 

# %%
merge_order_header_met_sales_staff = dataframes["order_header"].merge(dataframes["sales_staff"], on="SALES_STAFF_CODE")
managers = merge_order_header_met_sales_staff[merge_order_header_met_sales_staff["POSITION_EN"].str.contains(" Manager")][["POSITION_EN","ORDER_DATE"]]

print(managers)

# %% [markdown]
# Geef een overzicht met daarin de verschillende namen van producten en bijbehorende namen van producttypen van de producten waarvoor ooit meer dan 750 stuks tegelijk verkocht zijn. (2 kolommen, 9 rijen) 

# %%
merge_order_details_met_product = dataframes["product"].merge(dataframes["order_details"],on="PRODUCT_NUMBER")
merged_order_details_product_en_product_name = merge_order_details_met_product.merge(dataframes["product_type"],on="PRODUCT_TYPE_CODE")

merged_order_details_product_en_product_name = merged_order_details_product_en_product_name[merged_order_details_product_en_product_name["QUANTITY"] > 750][["PRODUCT_NAME","PRODUCT_TYPE_EN"]].drop_duplicates()

print(merged_order_details_product_en_product_name)

# %% [markdown]
# Geef een overzicht met daarin de productnamen waarvan ooit meer dan 40% korting is verleend. De formule voor korting is: (unit_price - unit_sale_price) / unit_price (1 kolom, 8 rijen) 

# %%
filter_korting = (merge_order_details_met_product["UNIT_PRICE"] - merge_order_details_met_product["UNIT_SALE_PRICE"]) / merge_order_details_met_product["UNIT_PRICE"] > 0.40
filter_korting_resultaat = merge_order_details_met_product.loc[filter_korting, ["PRODUCT_NAME"]].drop_duplicates()

print(filter_korting_resultaat)


# %% [markdown]
# Geef een overzicht met daarin de retourreden van producten waarvan ooit meer dan 90% van de aangeschafte hoeveelheid is teruggebracht (return_quantity/quantity). (1 kolom, 3 rijen) 

# %%
merge_order_details_met_returned_item = dataframes["order_details"].merge(dataframes["returned_item"],on="ORDER_DETAIL_CODE")

merge_met_product = merge_order_details_met_returned_item.merge(
    dataframes["return_reason"], on="RETURN_REASON_CODE"
)

filter_returned_item_meer_dan_90_procent = merge_met_product [ 
    merge_met_product["RETURN_QUANTITY"] / merge_met_product["QUANTITY"] > 0.90
]

resultaat90 = filter_returned_item_meer_dan_90_procent[["RETURN_DESCRIPTION_EN"]].drop_duplicates()

print(resultaat90)

# %% [markdown]
# ## Selecties op meerdere tabellen met functies

# %% [markdown]
# Geef een overzicht met daarin per producttype het aantal producten die tot dat producttype behoren. (2 kolommen, 21 rijen) 

# %%
aantal_producten_per_type = merge_product_type_en_product.groupby("PRODUCT_TYPE_EN")["PRODUCT_NUMBER"].count().reset_index()

aantal_producten_per_type.columns = ["Product Type", "Aantal Producten"]


print(aantal_producten_per_type)

# %% [markdown]
# Geef een overzicht met daarin per land het aantal vestigingen van klanten die zich in dat land bevinden. (2 kolommen, 21 rijen) 

# %%
merge_retailer_site_met_country = dataframes["retailer_site"].merge(dataframes["country"], on="COUNTRY_CODE")

aantal_vestiging_per_land = merge_retailer_site_met_country.groupby("COUNTRY")["RETAILER_SITE_CODE"].count().reset_index()

aantal_vestiging_per_land.columns = ["Land","Aantal vestigingen"]

print(aantal_vestiging_per_land)


# %% [markdown]
# Geef een overzicht met daarin van de producten behorend tot het producttype ‘Cooking Gear’ per productnaam de totaal verkochte hoeveelheid en de gemiddelde verkoopprijs. Sorteer de uitkomst op totaal verkochte hoeveelheid. (4 kolommen, 10 rijen) 

# %%
merge_order_details_met_product_met_product_type = merge_order_details_met_product.merge(dataframes["product_type"],on="PRODUCT_TYPE_CODE")

cooking_gear = merge_order_details_met_product_met_product_type[merge_order_details_met_product_met_product_type["PRODUCT_TYPE_EN"] == "Cooking Gear"]

cooking_gear_hvlheid_en_gem_verkoopprijs = cooking_gear.groupby("PRODUCT_NAME").agg(
    totaal_verkocht = ("QUANTITY",sum),
    gemiddeld_verkoop = ("UNIT_PRICE","mean")
).reset_index().sort_values(
    by="totaal_verkocht", ascending=False
)

cooking_gear_hvlheid_en_gem_verkoopprijs["gemiddeld_verkoop"] = cooking_gear_hvlheid_en_gem_verkoopprijs["gemiddeld_verkoop"].round(2)


print(cooking_gear_hvlheid_en_gem_verkoopprijs)




# %% [markdown]
# Geef een overzicht met daarin per land de naam van het land, de naam van de stad waar de verkoopafdeling is gevestigd (noem de kolomnaam in het overzicht ‘verkoper’) en het aantal steden waar zich klanten bevinden in dat land (noem de kolomnaam in het overzicht ‘klanten’) (3 kolommen, 29 rijen) 

# %%
overizicht_land_stad_count = merge_retailer_site_met_country.groupby("COUNTRY").agg(
    verkoper = ("CITY","first"),
    klanten = ("CITY","nunique")
).reset_index()

print(overizicht_land_stad_count)

#verkoper_df = merge_retailer_site_met_country[["COUNTRY", "CITY"]].drop_duplicates()
#klanten_count = merge_retailer_site_met_country.groupby("COUNTRY")["CITY"].nunique().reset_index(name="klanten")
#overzicht_land_stad_count = verkoper_df.merge(klanten_count, on="COUNTRY", how="left")
#overzicht_land_stad_count = overzicht_land_stad_count.rename(columns={"CITY": "verkoper"})
#print(overzicht_land_stad_count)


# %% [markdown]
# ## Pythonvertalingen van SUBSELECT en UNION met o.a. for-loops

# %% [markdown]
# Geef een overzicht met daarin de voornaam en de achternaam van de medewerkers die nog nooit wat hebben verkocht (2 kolommen, 25 rijen) 

# %%
wel_verkocht = set(dataframes["order_header"]["SALES_STAFF_CODE"].unique())
niet_verkocht = dataframes["sales_staff"][~dataframes["sales_staff"]["SALES_STAFF_CODE"].isin(wel_verkocht)].reset_index()

resultaat_niet_verkocht = niet_verkocht[["FIRST_NAME","LAST_NAME"]]

print(resultaat_niet_verkocht)


# %% [markdown]
# Geef een overzicht met daarin het aantal producten waarvan de marge lager is dan de gemiddelde marge van alle producten samen. Geef in het overzicht tevens aan wat de gemiddelde marge is van dit aantal producten waarvan de marge lager dan de gemiddelde marge van alle producten samen is. (1 kolom, 2 rijen) 

# %%
gem_marge = dataframes["product"]["MARGIN"].mean()
lager_dan_marge = dataframes["product"][dataframes["product"]["MARGIN"] < gem_marge]
aantal_producten_lager = lager_dan_marge.shape[0]
gem_marge_lager = round(lager_dan_marge["MARGIN"].mean(), 2)

overzicht_marges_lager = pandas.DataFrame(
    {"Waarde" : [aantal_producten_lager,gem_marge_lager]},
    index=["Aantal Producten","Gemiddelde Marge"]
)
print(overzicht_marges_lager)



# %% [markdown]
# Geef een overzicht met daarin de namen van de producten die voor meer dan 500 (verkoopprijs) zijn verkocht maar nooit zijn teruggebracht. (1 kolom, 13 rijen) 

# %%


merge_nieuw = merge_order_details_met_returned_item.merge(
    dataframes["product"],on="PRODUCT_NUMBER"
)
expensive_sales = merge_order_details_met_product[ merge_order_details_met_product["UNIT_SALE_PRICE"] > 500 ]
expensive_products = set(expensive_sales["PRODUCT_NAME"].unique())

returned_merged = dataframes["returned_item"].merge(
    dataframes["order_details"][["ORDER_DETAIL_CODE", "PRODUCT_NUMBER"]],
    on="ORDER_DETAIL_CODE", how="left"
)
returned_merged = returned_merged.merge(
    dataframes["product"][["PRODUCT_NUMBER", "PRODUCT_NAME"]],
    on="PRODUCT_NUMBER", how="left"
)
returned_products = set(returned_merged["PRODUCT_NAME"].unique())

# Stap 4: Bepaal de producten die wel duur verkocht zijn maar nooit zijn teruggebracht
never_returned_products = expensive_products - returned_products

# Stap 5: Maak een overzicht DataFrame (1 kolom, verwacht 13 rijen)
result_df = pandas.DataFrame(list(never_returned_products), columns=["PRODUCT_NAME"])
result_df = result_df.sort_values("PRODUCT_NAME")  # Optioneel, voor nettere output

print(result_df)

# %% [markdown]
# Geef een overzicht met daarin per (achternaam van) medewerker of hij/zij manager is of niet, door deze informatie toe te voegen als extra 'Ja/Nee'-kolom.<br>
# Hint: gebruik een for-loop waarin je o.a. bepaalt of het woord 'Manager' in de functie (position_en) staat. (2 kolommen, 102 rijen).

# %%
sales_staff = dataframes["sales_staff"][["LAST_NAME","POSITION_EN"]].copy()

sales_staff["IS_MANAGER"] = ["Ja" if "Manager" in pos else "Nee" for pos in sales_staff["POSITION_EN"]]

resultaat_managers = sales_staff[["LAST_NAME", "IS_MANAGER"]]

print(resultaat_managers)

# %% [markdown]
# Met de onderstaande code laat je Python het huidige jaar uitrekenen.

# %%
from datetime import date
date.today().year

# %% [markdown]
# Met de onderstaande code selecteer je op een bepaald jaartal uit een datum.

# %%
from datetime import datetime

date_str = '16-8-2013'
date_format = '%d-%m-%Y'
date_obj = datetime.strptime(date_str, date_format)

date_obj.year

# %% [markdown]
# Geef met behulp van bovenstaande hulpcode een overzicht met daarin op basis van het aantal jaar dat iemand in dienst is of een medewerker ‘kort in dienst’ (minder dan 25 jaar in dienst) of een ‘lang in dienst’ (groter gelijk dan 12 jaar in dienst) is. Geef daarbij per medewerker in een aparte kolom zowel ‘kort in dienst’ als ‘lang in dienst’ aan. Gebruik (wederom) een for-loop.<br>
# (2 kolommen, 102 rijen) 

# %%
sales_staff_jong_of_oud = dataframes["sales_staff"][["LAST_NAME","DATE_HIRED"]].copy()

sales_staff_jong_of_oud["DATE_HIRED"] = pandas.to_datetime(sales_staff_jong_of_oud["DATE_HIRED"], format="%Y-%m-%d")

current_year = date.today().year

sales_staff_jong_of_oud["YEARS_IN_SERVICE"] = current_year - sales_staff_jong_of_oud["DATE_HIRED"].dt.year

sales_staff_jong_of_oud["KORT_IN_DIENST"] = ["Ja" if years < 25 else "Nee" for years in sales_staff_jong_of_oud["YEARS_IN_SERVICE"]]
sales_staff_jong_of_oud["LANG_IN_DIENST"] = ["Ja" if years >= 12 else "Nee" for years in sales_staff_jong_of_oud["YEARS_IN_SERVICE"]]

resultaat_dienstjaren = sales_staff_jong_of_oud[["KORT_IN_DIENST", "LANG_IN_DIENST"]]

print(resultaat_dienstjaren)

# %% [markdown]
# ## Van Jupyter Notebook naar Pythonproject

# %% [markdown]
# 1. Richt de map waarin jullie tot nu toe hebben gewerkt in volgens de mappenstructuur uit de slides.
# 2. Maak van de ontstane mappenstructuur een Pythonproject dat uitvoerbaar is vanuit de terminal. Maak daarin een .py-bestand dat minstens 5 antwoorden uit dit notebook (in de vorm van een DataFrame) exporteert naar Excelbestanden. Alle notebooks mogen als notebook blijven bestaan.
# 3. Zorg ervoor dat dit Pythonproject zijn eigen repo heeft op Github. Let op: je virtual environment moet <b><u>niet</u></b> meegaan naar Github.
# 
# Je mag tijdens dit proces je uit stap 1 ontstane mappenstructuur aanpassen, zolang je bij het beoordelingsmoment kan verantwoorden wat de motivatie hierachter is. De slides verplichten je dus nergens toe.


