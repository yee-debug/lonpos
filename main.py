#%%　import
import sys  # 停止コマンド
import math

#%%　定数の定義
# 複素数平面で回転する計算
SIN90 = math.sin(math.radians(90))
COS90 = math.cos(math.radians(90))
SIN90 = round(SIN90, 1)
COS90 = round(COS90, 1)

#%%
# コマの回転、反転をカウント
rot_counter = 0

used_cells = []   #コマオブジェクト
vacant_cells = {
    -1-1j,-2-1j,-3-1j,-4-1j,-5-1j,-6-1j,
    -1-2j,-2-2j,-3-2j,-4-2j,-5-2j,-6-2j,-7-2j,
    -1-3j,-2-3j,-3-3j,-5-3j,-6-3j,-7-3j,-8-3j,
    -1-4j,-2-4j,-3-4j,-4-4j,-5-4j,-6-4j,-7-4j,-8-4j,-9-4j,
    -1-5j,-2-5j,-3-5j,-4-5j,-5-5j,-6-5j,-7-5j,-8-5j,-9-5j,
    -1-6j,-2-6j,-3-6j,-4-6j,-5-6j,-6-6j,-7-6j,
    -2-7j,-3-7j,-4-7j,-5-7j,-6-7j,
    -3-8j,-4-8j,-5-8j,
    -4-9j,-5-9j
}

#%%
灰koma = {
    "name": "灰",
    "pos": {0+0j, 0+1j, 0-1j, 1+0j, -1+0j},
    "use": True 
}

紅koma = {
    "name": "紅",
    "pos": {0+0j, 0+1j, -1+1j, 1+0j, 1-1j},
    "use": True 
}

空koma = {
    "name": "空",
    "pos": {0+0j, 1+0j, 2+0j, 0+1j, 0+2j},
    "use": True 
}

黄koma = {
    "name": "黄",
    "pos": {0+0j, 1+0j, 0+1j, 0+2j, 1+2j},
    "use": True 
}

緑koma = {
    "name": "緑",
    "pos": {0+0j, 0+1j, -1+1j, 1+0j, 2+0j},
    "use": True 
}

肌koma = {
    "name": "肌",
    "pos": {0+0j, 0+1j, -1+0j, 1+0j, 2+0j},
    "use": True 
}

赤koma = {
    "name": "赤",
    "pos": {0+0j, 0+1j, 1+1j, 1+0j, 2+0j},
    "use": True 
}

青koma = {
    "name": "青",
    "pos": {0+0j, 0+1j, 1+0j, 2+0j, 3+0j},
    "use": True 
}

橙koma = {
    "name": "橙",
    "pos": {0+0j, 0+1j, 1+0j, 2+0j},
    "use": True 
}

紫koma = {
    "name": "紫",
    "pos": {0+0j, 1+0j, 2+0j, 3+0j},
    "use": True 
}

若草koma = {
    "name": "若草",
    "pos": {0+0j, 0+1j, 1+0j, 1+1j},
    "use": True 
}

白koma = {
    "name": "白",
    "pos": {0+0j, 0+1j, 1+0j},
    "use": True 
}

#%%
def search_position(vacant_cells, koma):
    name = koma["name"]
    rel_pos_orig = koma["pos"].copy() # 相対ポジション NOTE: 後で変更する際に元データが変わらないようにcopyする
    use = koma["use"]

    # use = Falseの場合なにもしない
    if not use:
        return None
    
    # 空いているマスごとに探索
    avail_pos = []
    for vacant_cell in vacant_cells:
        a = vacant_cell.real
        b = vacant_cell.imag

        pp = a + b*1j
        rel_pos = rel_pos_orig.copy()
        rel_pos_history = []
        for flip in [False, True]:
            for rot in range(4):
                if flip:
                    rel_pos = set(map(lambda x:-x.conjugate(), rel_pos)) # 実部を反転
                rel_pos = set(map(lambda x:x*(COS90 + SIN90*1j)**rot, rel_pos)) # 回転
                
                # 一度探索した形・向きは再度探索しない
                if rel_pos in rel_pos_history:
                    break

                abs_pos = set(map(lambda x:x+pp, rel_pos)) # 絶対座標に変換

                rel_pos_history.append(rel_pos) # 探索した形・向きを保存
                                
                if abs_pos.issubset(vacant_cells):
                    avail_pos.append(abs_pos)
                else:
                    continue

    return avail_pos

# %%
