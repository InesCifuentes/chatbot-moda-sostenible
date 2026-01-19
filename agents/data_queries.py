import pandas as pd

class DataQueries:
    def __init__(self, csv_path):
        self.data = pd.read_csv(csv_path)

    def get_top_carbon_country(self):
        # Agrupar por país y calcular la media de huella de carbono
        carbon_means = self.data.groupby("Country")["Carbon_Footprint_MT"].mean()
        top_country = carbon_means.idxmax()
        top_value = carbon_means.max()
        return f"El país con mayor huella de carbono promedio es {top_country} ({top_value:.2f} MT)."

    def get_most_used_material(self):
        material = self.data['Material_Type'].mode()[0]
        return f"El material más utilizado es {material}."

    def get_most_sustainable_brand(self):
        # Aquí también puedes mejorar: elegir la marca con mejor rating promedio
        sustainable_brands = (
            self.data.groupby("Brand_Name")["Sustainability_Rating"]
            .apply(lambda x: (x == "A").mean())  # proporción de rating A
        )
        top_brand = sustainable_brands.idxmax()
        return f"La marca más sostenible es {top_brand}."
