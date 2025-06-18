from shop_data_provider import ShopDataProvider
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

class ShopDataController():
    def __init__(self) -> None:
        self.data_provider: ShopDataProvider = ShopDataProvider()
    
    def frequency_colors(self):
        df: pd.DataFrame = self.data_provider.frequency_colors()
        
        pivoted = df.pivot(index="kleur", columns="seizoen", values="Aantal").fillna(0)
        
        colors = pivoted.index
        x = np.arange(len(colors))
        
        width = 0.1

        fig, ax = plt.subplots(figsize=(10, 6))
        
        seasons = df["seizoen"].unique()
        num_categories = len(seasons)
        offsets = np.linspace(-width * (num_categories - 1) / 2, width * (num_categories - 1) / 2, num_categories)
        
        for i, season in enumerate(seasons):
            ax.bar(x + offsets[i], pivoted[season], width, label=season)

        ax.set_title('Frequentie van Kleuren per Seizoen voor mannelijke klanten')
        ax.set_xlabel('Kleur')
        ax.set_ylabel('Frequentie')
        ax.set_xticks(x)
        ax.set_xticklabels(colors, rotation=45)
        ax.legend(title='Seizoen')

        plt.tight_layout()
        plt.show()
        
    def frequency_color_female(self):
        df: pd.DataFrame = self.data_provider.frequency_color_female()
        
        plt.pie(df["Aantal"], labels=df["kleur"], autopct="%1.1f%%", startangle=90)
        plt.title("Verdeling kleuren bij vrouwen")
        plt.show()
        
    def sales(self):
        df: pd.DataFrame = self.data_provider.sales()
        genders = df["geslacht"].unique()
        
        fig, axes = plt.subplots(1, len(genders), figsize=(5, 5))
    
        for i, gender in enumerate(genders):
            subset = df[df["geslacht"] == gender]
            subset.plot(kind='bar', ax=axes[i], title=gender, legend=False, x="leeftijd_categorie", xlabel="Leeftijdcategorie")
            axes[i].set_ylabel("Aantal aankopen")
            

        plt.suptitle("Aantal wekelijkse aankopen in de zomer", fontsize=16)
        plt.tight_layout()
        plt.show()
    