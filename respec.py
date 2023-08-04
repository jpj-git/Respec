
import json
import shutil
import tkinter as tk
from tkinter import filedialog


def respec_runes(sf):
    p = sf['points']
    runes = sf['runeUnlocks']['unlocks']
    # print(runes)

    tier1 = [0, 1, 2, 12, 13, 14]
    tier2 = [3, 4, 5, 15, 16, 17]
    tier3 = [6, 7, 8, 18, 19, 20]
    tier4 = [9, 10, 11, 21, 22, 23]

    all_tiers = [tier1, tier2, tier3, tier4]
    costs = [1350, 3150, 6300, 12800]

    for tier in all_tiers:
        for i in tier:
            p += (runes[i] * costs[all_tiers.index(tier)])
            runes[i] = 0

    # print(runes)
    # print(p)

    sf['runeUnlocks']['unlocks'] = runes
    sf['points'] = p
    return sf


if __name__ == '__main__':

    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename()

    ## Used when testing
    # shutil.copyfile(file_path, 'data/copydata.json')
    # file_path = 'data/copydata.json'

    fr = open(file_path, 'r')
    save_file = json.load(fr)
    fr.close()

    min_json = json.dumps(respec_runes(save_file), separators=(',', ':'))

    fw = open(file_path, 'w')
    fw.write(min_json)
    fw.close()

