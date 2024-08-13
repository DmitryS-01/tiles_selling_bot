class Tile:
    assortment = []

    def __init__(self, name: str, link: str, dimensions: str, color: str, photos: list[str]) -> None:
        self.name = name
        self.link = link
        self.dimensions = dimensions
        self.color = color
        self.photos = photos

        Tile.assortment.append(self)


def get_all_types_of_dimensions() -> list[str]:
    tiles_list = sorted(set([tile.dimensions for tile in Tile.assortment]))
    return tiles_list


def get_all_types_of_colors() -> list[str]:
    tiles_list = sorted(set([tile.color for tile in Tile.assortment]))
    return tiles_list


# TODO сделать выбор барабаном как в ios
def get_tiles(*, dimensions: str = True, color: str = True) -> list[Tile]:
    tiles_list = sorted([tile for tile in Tile.assortment if tile.dimensions == dimensions and tile.color == color])
    return tiles_list


Tile("Adamant Blue", "https://artkera.ru/collections/Adamant-Blue", "600*1200*8", "blue", ["https://artkera.ru/sites/default/files/faces/60120ADA23HG/60120ADA23HG_01.jpg", "https://artkera.ru/sites/default/files/inter/Adamant_Blue/Adamant_Blue_1.jpg"])
Tile("Bavaro Nova", "https://artkera.ru/collections/Bavaro", "300*900*10.5",  "white", ["https://artkera.ru/sites/default/files/faces/WT93BAV00/WT93BAV00_01.jpg", "https://artkera.ru/sites/default/files/inter/Bavaro/Bavaro_1.jpg"])
Tile("Carrara Cersei", "https://artkera.ru/collections/Carrara-Cersei", "600*1200*9.5", "white", ["https://artkera.ru/sites/default/files/faces/D120208M/D120208M_01.jpg", "https://artkera.ru/sites/default/files/inter/Carrara_Cersei/Carrara_Cersei_1.jpg"])
Tile("Latina", "https://artkera.ru/collections/Latina", "600*1200*8", "black", ["https://artkera.ru/sites/default/files/faces/60120LAN23HG/60120LAN23HG_01.jpg", "https://artkera.ru/sites/default/files/inter/Latina/Latina_1.jpg"])
Tile("Premiere Stone", "https://artkera.ru/collections/Premiere-Stone", "600*1200*8", "grey", ["https://artkera.ru/sites/default/files/faces/60120PRM21HG/60120PRM21HG_01.jpg", "https://artkera.ru/sites/default/files/inter/Premiere_Stone/Premiere_Stone_1.jpg"])
Tile("Bali", "https://artkera.ru/collections/Bali", "200*900*8", "wood", ["https://artkera.ru/sites/default/files/faces/GFA92BAL04R/GFA92BAL04R_01.jpg", "https://artkera.ru/sites/default/files/inter/Bali_200x900/Bali_200x900_1.jpg"])
Tile("Lines Crema", "https://artkera.ru/collections/Pion-Crema", "249*500*7.5", "white", ["https://artkera.ru/sites/default/files/faces/WT9LNS01.jpg", "https://artkera.ru/sites/default/files/inter/Pion_Crema/Pion_Crema_1.jpg"])
Tile("Sanremo White", "https://artkera.ru/collections/Sanremo", "600*600*9", "white", ["https://artkera.ru/sites/default/files/faces/GP40SAM00L/GP40SAM00L_01.jpg", "https://artkera.ru/sites/default/files/inter/Sanremo/Sanremo_1.jpg"])
Tile("Sanremo Black", "https://artkera.ru/collections/Sanremo", "600*600*9", "black", ["https://artkera.ru/sites/default/files/faces/GP40SAM99L/GP40SAM99L_01.jpg", "https://artkera.ru/sites/default/files/inter/Sanremo/Sanremo_2.jpg"])
Tile("Ironwood", "https://artkera.ru/collections/Ironwood", "200*900*8", "wood", ["https://artkera.ru/sites/default/files/faces/GFA92IRW04R/GFA92IRW04R_01.jpg", "https://artkera.ru/sites/default/files/faces/GFA92IRW05R/GFA92IRW05R_01.jpg", "https://artkera.ru/sites/default/files/faces/GFA92IRW40R/GFA92IRW40R_01.jpg", "https://artkera.ru/sites/default/files/faces/GFA92IRW48R/GFA92IRW48R_01.jpg", "https://artkera.ru/sites/default/files/inter/Ironwood_200x900/Ironwood_200x900_1.jpg", "https://artkera.ru/sites/default/files/inter/Ironwood_200x900/Ironwood_200x900_2.jpg", "https://artkera.ru/sites/default/files/inter/Ironwood_200x900/Ironwood_200x900_3.jpg", "https://artkera.ru/sites/default/files/inter/Ironwood_200x900/Ironwood_200x900_4.jpg"])
