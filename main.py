from controller.shop_data_controller import ShopDataController
from util.action_handler import ActionHandler
from util.terminal_logger import TerminalLogger


def main():
    shop_data_controller = ShopDataController()
    
    action_handler = ActionHandler(TerminalLogger())
    
    action_handler.add_action(
        "Hoeveel keer zijn de kleuren( “blue,red,black,beige,white) per seizoen verkocht voor de mannen.",
        lambda: shop_data_controller.frequency_colors()
    )
    
    action_handler.add_action(
        "Wat is de verdeling van de kleuren(blue,red,black,white) bij vrouwen tussen de 30 en 50",
        lambda: shop_data_controller.frequency_color_female()
    )
    
    action_handler.add_action(
        "Hoeveel mannen en vrouwen kopen wekelijks in de zomer. Verdeel dit per leeftijdscategorie (20-40,41-60,60+) 2 Subgrafieken(1 kolomdiagram(mannen), 1 kolomdiagram(vrouwen)",
        lambda: shop_data_controller.sales()
    )
    
    while(True):
        action_handler.handle_actions()

if __name__ == "__main__":
    main()