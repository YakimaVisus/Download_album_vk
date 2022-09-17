# -*- coding: utf-8 -*-
import os
import sys
import vk_api
import urllib
import urllib.request
import colorama
from colorama import Fore, Style
from colorama import init
init()
def main():
    # Открываем сессию  с VK 


    vk_session = vk_api.VkApi(
        token="ТОК")
    
    try:
        vk = vk_session.get_api()
    except vk_api.AuthError as error_msg:
        print(Fore.LIGHTRED_EX + "Токен невалид")
    
    
    # получаем альбом
    print(Style.RESET_ALL + '''
    Мы имеем:
        https://vk.com/album1488_008
        https://vk.com/albumЭТО_ИЭТО
    Нужно вписать:
        1488_008
    Если с группы:
        -1488_008
    __________________________
    Автор скрипта: Yakima Visus
    ''')
    try:
        yakimavisus = input('[]Введите ссылку на альбом: ')

        id_albom = yakimavisus.split('_')[-1]
        id_user = yakimavisus.split('_')[0]
        
        # начинаем перебирать каждого пользователя
    
        # создаем директорию с именем пользователя, если нет
        newpath = os.path.join(sys.path[0], id_user)
        if not os.path.exists(newpath):
            os.makedirs(newpath)
        
        response = vk.photos.getAll(owner_id = int(id_user), no_service_albums = int(id_albom))#получаем айдишники с альбома
    except:
        print(Fore.LIGHTRED_EX +f'{yakimavisus} - подобное нельзя, пример записи: 1488_008')
        main()
    # работаем с каждой полученной фотографией
    print(Fore.LIGHTGREEN_EX + "[]Загрузка началась...")
    for i in range(len(response["items"])):
        # берём ссылку на максимальный размер фотографии
        photo_url = str(response["items"][i]["sizes"][len(response["items"][i]["sizes"])-1]["url"])
        print(Fore.GREEN + f"[{i}] - фотка загружена " + str(response["items"][i]['id']) + '.jpg')
        # скачиваем фото в папку с ID пользователя
        urllib.request.urlretrieve(photo_url, newpath + '/' + str(response["items"][i]['id']) + '.jpg')
        
    
if __name__ == "__main__":
    main()