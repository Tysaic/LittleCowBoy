from consolemenu import ConsoleMenu
from consolemenu.items import SelectionMenu, SubmenuItem
from modules import local_info

if __name__ == '__main__':
    menu = ConsoleMenu("Little CowBow Main Menu", "Enjoy the hack party")
    #First Option
    knowing_enviroment_title = "Choose your prefer option"
    selection_menu = SelectionMenu(["item1", "item2", "item3"], title=knowing_enviroment_title)
    knowing_enviroment = SubmenuItem("Knowing your enviroment", selection_menu, menu)
    
    #Second Option
    menu.append_item(knowing_enviroment)
    menu.show()
