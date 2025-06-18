import pandas as pd

class ShopDataProvider():    
    def get_data(self) -> pd.DataFrame:
        # Load the CSV file
        df = pd.read_csv("data/shopdata.csv")

        columns = {
            "Customer ID": "id",
            "Age": "leeftijd",
            "Gender": "geslacht",
            "Item Purchased": "gekocht_item",
            "Category": "categorie",
            "Color": "kleur",
            "Season": "seizoen",
            "Payment Method": "betaalmethode",
            "Frequency of Purchases": "frequentie"
        }
        
        df["Gender"] = df["Gender"].replace({"Male": "man", "Female": "vrouw"})
        df_filtered = df[list(columns.keys())]
        df_filtered.columns = list(columns.values())
        
        return df_filtered
    
    def frequency_colors(self) -> pd.DataFrame:
        df: pd.DataFrame = self.get_data()
        
        filtered_df = df[(df["kleur"].isin(["Blue","Red","Black","Beige","White"])) & (df["geslacht"] == "man")]
        
        grouped_df = filtered_df.groupby(["seizoen", "kleur"])
        
        size = grouped_df.size().reset_index(name="Aantal")
        
        print(size)
        
        return size
    
    def frequency_color_female(self) -> pd.DataFrame:
        df: pd.DataFrame = self.get_data()
        
        filtered_df = df[(df["kleur"].isin(["Blue","Red","Black","White"])) & (df["leeftijd"].between(30, 50)) & (df["geslacht"] == "vrouw")]
        
        grouped_df = filtered_df.groupby(["kleur"])
        
        size = grouped_df.size().reset_index(name="Aantal")
        
        print(size)
        
        return size
    
    def sales(self) -> pd.DataFrame:
        df: pd.DataFrame = self.get_data()
        
        filtered_df = df[(df["seizoen"] == "Summer") & (df["frequentie"] == "Weekly")]
        
        age_bins = [20, 40, 60, float('inf')]
        age_labels = ['20-40', '41-60', '60+']

        # Create age categories
        ## right means when the bins end or start
        filtered_df['leeftijd_categorie'] = pd.cut(filtered_df['leeftijd'], bins=age_bins, labels=age_labels, right=True)
        
        grouped_df = filtered_df.groupby(["leeftijd_categorie", "geslacht"])
        
        size = grouped_df.size().reset_index(name="Aantal")
        
        print(size)
        
        return size