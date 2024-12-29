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


jo = [-4-3j]  #邪魔オブジェクト
ko = [0+0j]   #コマオブジェクト
mo = {-1-1j,-2-1j,-3-1j,-4-1j,-5-1j,-6-1j,
      -1-2j,-2-2j,-3-2j,-4-2j,-5-2j,-6-2j,-7-2j,
      -1-3j,-2-3j,-3-3j,-5-3j,-6-3j,-7-3j,-8-3j,
      -1-4j,-2-4j,-3-4j,-4-4j,-5-4j,-6-4j,-7-4j,-8-4j,-9-4j,
      -1-5j,-2-5j,-3-5j,-4-5j,-5-5j,-6-5j,-7-5j,-8-5j,-9-5j,
      -1-6j,-2-6j,-3-6j,-4-6j,-5-6j,-6-6j,-7-6j,
      -2-7j,-3-7j,-4-7j,-5-7j,-6-7j,
      -3-8j,-4-8j,-5-8j,
      -4-9j,-5-9j}


灰stop = True
灰a = 2
灰b = 4
灰rote = 0

紅stop = True
紅a = 5
紅b = 4
紅rote = 0

空stop = True
空a = 1
空b = 1
空rote = 2

黄stop = True
黄a = 3
黄b = 6
黄rote = 0

緑stop = True
緑a = 6
緑b = 1
緑rote = 5

肌stop = True
肌a = 3
肌b = 2
肌rote = 2

赤stop = True
赤a = 4
赤b = 7
赤rote = 5

青stop = True
青a = 7
青b = 3
青rote = 4

橙stop = True
橙a = 5
橙b = 9
橙rote = 6

紫stop = True
紫a = 6
紫b = 7
紫rote = 1

若草stop = True
若草a = 9
若草b = 5
若草rote = 0

白stop = True
白a = 5
白b = 6
白rote = 0


# 紅色右上
def koma():
    if 紅stop == True:
        for a in mo:
            print(name)  # 名前確認
            a = a.real
            b = a.imag
            rote = 紅rote

            pp = -a-b*1j

            pp1 = pp + 1  # コマの玉の数を確認
            pp2 = pp + 1 - 1j
            pp3 = pp + 1j
            pp4 = pp + 1j - 1

            while rot_counter != 8: # 左右対称コマなら3

                if rot_counter == rote + 1:
                    break

                # 90度回転
                elif 1<= rot_counter <=3 or 5 <= rot_counter <=7:
                    pp1 = (COS90 + SIN90*1j)*(pp1 - pp) + pp
                    pp2 = (COS90 + SIN90*1j)*(pp2 - pp) + pp
                    pp3 = (COS90 + SIN90*1j)*(pp3 - pp) + pp
                    pp4 = (COS90 + SIN90*1j)*(pp4 - pp) + pp

                # 左右反転
                elif rot_counter == 4:  #左右対称コマなら消す
                    pp1 = pp1 - pp
                    pp1 = -pp1.conjugate() + pp
                    pp2 = pp2 - pp
                    pp2 = -pp2.conjugate() + pp
                    pp3 = pp3 - pp
                    pp3 = -pp3.conjugate() + pp
                    pp4 = pp4 - pp
                    pp4 = -pp4.conjugate() + pp

                pp5 = [pp,pp1,pp2,pp3,pp4]

                if rot_counter == rote:
                    print("  " + str(rot_counter) + "回" + "_" + str(pp5))

                rot_counter += 1

                if rot_counter == rote + 1:
                    if not set(ko).isdisjoint(pp5):
                        x = set(ko) & set(pp5)
                        print("【ko不可】" + str(x))
                        #sys.exit()
                        #pass

                    elif not set(pp5).isdisjoint(jo):
                        print("【jo不可】")
                        #sys.exit()
                        #pass

                    else:
                        print("  紅色のPPは" + str(pp))

            ko.extend(pp5)
            mo = list(set(mo) - set(ko))

            rot_counter = 0
    else:
        pass

name = "あか"
print(koma())
