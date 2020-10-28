import app.config as config
from app.service.order_service import OrderService
from app.service.file_reader_factory import FileReaderFactory
import dialog.dialog as Dialog
import os



def main():


    # Start the intro dialog
    Dialog.displayIntro()

    # Read menus from a file
    menus = FileReaderFactory().get_menus(config.MENU_FILE_PATH)

    # Launch the application
    print('----[Meal Suggestor Adventures (Total Menus Loaded = {})]----'.format(len(menus)))

    # Recommend menu options, and make an order
    OrderService(menus).make_order(config.MAX_MENU_RECOMMENDATIONS, 0, 0, 1)

if __name__ == "__main__":
    # os.system is used to make the background of the Powershell black to give it a little front-end feature
    os.system('color 0f')
    main()