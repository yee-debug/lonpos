#%%
import sys  # 停止コマンド

#%%
# 複素数平面で回転する計算
import math
sin90 = math.sin(math.radians(90))
cos90 = math.cos(math.radians(90))

#%%
#無理数をまとめる
sin90 = round(sin90, 1)
cos90 = round(cos90, 1)

#%%
# コマの回転、反転をカウント
rotecounter = 0



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
print(mo)


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


# 灰色
if 灰stop == True:
    print("●灰色右上")
    a = 灰a
    b = 灰b
    rote = 灰rote

    pp = -a-b*1j

    pp1 = pp + 1
    pp2 = pp - 1
    pp3 = pp - 1j
    pp4 = pp + 1j

    while rotecounter != 4:

        if rotecounter == rote + 1:
            break

        # 90度回転
        elif 1<= rotecounter <=3:
            pp1 = (cos90 + sin90*1j)*(pp1 - pp) + pp
            pp2 = (cos90 + sin90*1j)*(pp2 - pp) + pp
            pp3 = (cos90 + sin90*1j)*(pp3 - pp) + pp
            pp4 = (cos90 + sin90*1j)*(pp4 - pp) + pp

        pp5 = [pp,pp1,pp2,pp3,pp4]

        if rotecounter == rote:
            print("  " + str(rotecounter) + "回" + "_" + str(pp5))

        rotecounter += 1

        if rotecounter == rote + 1:
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
                print("  灰色のPPは" + str(pp))

    ko.extend(pp5)
    mo = list(set(mo) - set(ko))

    rotecounter = 0
else:
    pass

# 紅色右上
if 紅stop == True:
    print("●紅色右上")  # 名前確認
    a = 紅a
    b = 紅b
    rote = 紅rote

    pp = -a-b*1j

    pp1 = pp + 1  # コマの玉の数を確認
    pp2 = pp + 1 - 1j
    pp3 = pp + 1j
    pp4 = pp + 1j - 1

    while rotecounter != 8: # 左右対称コマなら3

        if rotecounter == rote + 1:
            break

        # 90度回転
        elif 1<= rotecounter <=3 or 5 <= rotecounter <=7:
            pp1 = (cos90 + sin90*1j)*(pp1 - pp) + pp
            pp2 = (cos90 + sin90*1j)*(pp2 - pp) + pp
            pp3 = (cos90 + sin90*1j)*(pp3 - pp) + pp
            pp4 = (cos90 + sin90*1j)*(pp4 - pp) + pp

        # 左右反転
        elif rotecounter == 4:  #左右対称コマなら消す
            pp1 = pp1 - pp
            pp1 = -pp1.conjugate() + pp
            pp2 = pp2 - pp
            pp2 = -pp2.conjugate() + pp
            pp3 = pp3 - pp
            pp3 = -pp3.conjugate() + pp
            pp4 = pp4 - pp
            pp4 = -pp4.conjugate() + pp

        pp5 = [pp,pp1,pp2,pp3,pp4]

        if rotecounter == rote:
            print("  " + str(rotecounter) + "回" + "_" + str(pp5))

        rotecounter += 1

        if rotecounter == rote + 1:
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

    rotecounter = 0
else:
    pass


#空色右上
if 空stop == True:
    print("●空色右上")
    a = 空a
    b = 空b
    rote = 空rote

    pp = -a-b*1j

    pp1 = pp + 1
    pp2 = pp + 2
    pp3 = pp + 1j
    pp4 = pp + 2j

    while rotecounter != 4: # 左右対称コマなら4
        if rotecounter == rote + 1:
            break

        # 90度回転
        elif 1<= rotecounter <=3:
            pp1 = (cos90 + sin90*1j)*(pp1 - pp) + pp
            pp2 = (cos90 + sin90*1j)*(pp2 - pp) + pp
            pp3 = (cos90 + sin90*1j)*(pp3 - pp) + pp
            pp4 = (cos90 + sin90*1j)*(pp4 - pp) + pp

        pp5 = [pp,pp1,pp2,pp3,pp4]

        if rotecounter == rote:
            print("  " + str(rotecounter) + "回" + "_" + str(pp5))

        rotecounter += 1

        if rotecounter == rote + 1:
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
                print("  空色のPPは" + str(pp))

    ko.extend(pp5)
    mo = list(set(mo) - set(ko))

    rotecounter = 0
else:
    pass


#黄色右上
if 黄stop != 0:
    print("●黄色右上")
    a = 黄a
    b = 黄b
    rote = 黄rote

    pp = -a-b*1j

    pp1 = pp + 1j
    pp2 = pp + 1
    pp3 = pp + 2
    pp4 = pp + 2 + 1j

    while rotecounter != 4:

        if rotecounter == rote + 1:
            break

        # 90度回転
        elif 1<= rotecounter <=3 or 5 <= rotecounter <=7:
            pp1 = (cos90 + sin90*1j)*(pp1 - pp) + pp
            pp2 = (cos90 + sin90*1j)*(pp2 - pp) + pp
            pp3 = (cos90 + sin90*1j)*(pp3 - pp) + pp
            pp4 = (cos90 + sin90*1j)*(pp4 - pp) + pp

        pp5 = [pp,pp1,pp2,pp3,pp4]

        if rotecounter == rote:
            print("  " + str(rotecounter) + "回" + "_" + str(pp5))

        rotecounter += 1

        if rotecounter == rote + 1:
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
                print("  黄色のPPは" + str(pp))

    ko.extend(pp5)
    mo = list(set(mo) - set(ko))

    rotecounter = 0
else:
    pass


#緑右上
if 緑stop != 0:
    print("●緑色右上")
    a = 緑a
    b = 緑b
    rote = 緑rote

    pp = -a-b*1j

    pp1 = pp + 1j
    pp2 = pp - 1 + 1j
    pp3 = pp + 1
    pp4 = pp + 2

    while rotecounter != 8:

        if rotecounter == rote + 1:
            break

        # 90度回転
        elif 1<= rotecounter <=3 or 5 <= rotecounter <=7:
            pp1 = (cos90 + sin90*1j)*(pp1 - pp) + pp
            pp2 = (cos90 + sin90*1j)*(pp2 - pp) + pp
            pp3 = (cos90 + sin90*1j)*(pp3 - pp) + pp
            pp4 = (cos90 + sin90*1j)*(pp4 - pp) + pp

        # 左右反転
        elif rotecounter == 4:
            pp1 = pp1 - pp
            pp1 = -pp1.conjugate() + pp
            pp2 = pp2 - pp
            pp2 = -pp2.conjugate() + pp
            pp3 = pp3 - pp
            pp3 = -pp3.conjugate() + pp
            pp4 = pp4 - pp
            pp4 = -pp4.conjugate() + pp

        pp5 = [pp,pp1,pp2,pp3,pp4]

        if rotecounter == rote:
            print("  " + str(rotecounter) + "回" + "_" + str(pp5))

        rotecounter += 1

        if rotecounter == rote + 1:
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
                print("  緑色のPPは" + str(pp))

    ko.extend(pp5)
    mo = list(set(mo) - set(ko))

    rotecounter = 0
else:
    pass


#肌色右上
if 肌stop != 0:
    print("●肌色右上")
    a = 肌a
    b = 肌b
    rote = 肌rote

    pp = -a-b*1j

    pp1 = pp + 1j
    pp2 = pp + 1
    pp3 = pp + 2
    pp4 = pp - 1

    while rotecounter != 8:

        if rotecounter == rote + 1:
            break

        # 90度回転
        elif 1<= rotecounter <=3 or 5 <= rotecounter <=7:
            pp1 = (cos90 + sin90*1j)*(pp1 - pp) + pp
            pp2 = (cos90 + sin90*1j)*(pp2 - pp) + pp
            pp3 = (cos90 + sin90*1j)*(pp3 - pp) + pp
            pp4 = (cos90 + sin90*1j)*(pp4 - pp) + pp

        # 左右反転
        elif rotecounter == 4:
            pp1 = pp1 - pp
            pp1 = -pp1.conjugate() + pp
            pp2 = pp2 - pp
            pp2 = -pp2.conjugate() + pp
            pp3 = pp3 - pp
            pp3 = -pp3.conjugate() + pp
            pp4 = pp4 - pp
            pp4 = -pp4.conjugate() + pp

        pp5 = [pp,pp1,pp2,pp3,pp4]

        if rotecounter == rote:
            print("  " + str(rotecounter) + "回" + "_" + str(pp5))

        rotecounter += 1

        if rotecounter == rote + 1:
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
                print("  肌色のPPは" + str(pp))

    ko.extend(pp5)
    mo = list(set(mo) - set(ko))

    rotecounter = 0
else:
    pass


#赤色右上
if 赤stop != 0:
    print("●赤色右上")
    a = 赤a
    b = 赤b
    rote = 赤rote

    pp = -a-b*1j

    pp1 = pp + 1
    pp2 = pp + 2
    pp3 = pp + 1j
    pp4 = pp + 1j + 1

    while rotecounter != 8:

        if rotecounter == rote + 1:
            break

        # 90度回転
        elif 1<= rotecounter <=3 or 5 <= rotecounter <=7:
            pp1 = (cos90 + sin90*1j)*(pp1 - pp) + pp
            pp2 = (cos90 + sin90*1j)*(pp2 - pp) + pp
            pp3 = (cos90 + sin90*1j)*(pp3 - pp) + pp
            pp4 = (cos90 + sin90*1j)*(pp4 - pp) + pp

        # 左右反転
        elif rotecounter == 4:
            pp1 = pp1 - pp
            pp1 = -pp1.conjugate() + pp
            pp2 = pp2 - pp
            pp2 = -pp2.conjugate() + pp
            pp3 = pp3 - pp
            pp3 = -pp3.conjugate() + pp
            pp4 = pp4 - pp
            pp4 = -pp4.conjugate() + pp

        pp5 = [pp,pp1,pp2,pp3,pp4]

        if rotecounter == rote:
            print("  " + str(rotecounter) + "回" + "_" + str(pp5))

        rotecounter += 1

        if rotecounter == rote + 1:
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
                print("  赤色のPPは" + str(pp))

    ko.extend(pp5)
    mo = list(set(mo) - set(ko))

    rotecounter = 0
else:
    pass


#青色右上
if 青stop != 0:
    print("●青色右上")
    a = 青a
    b = 青b
    rote = 青rote

    pp = -a-b*1j

    pp1 = pp + 1
    pp2 = pp + 2
    pp3 = pp + 3
    pp4 = pp + 1j

    while rotecounter != 8:

        if rotecounter == rote + 1:
            break

        # 90度回転
        elif 1<= rotecounter <=3 or 5 <= rotecounter <=7:
            pp1 = (cos90 + sin90*1j)*(pp1 - pp) + pp
            pp2 = (cos90 + sin90*1j)*(pp2 - pp) + pp
            pp3 = (cos90 + sin90*1j)*(pp3 - pp) + pp
            pp4 = (cos90 + sin90*1j)*(pp4 - pp) + pp

        # 左右反転
        elif rotecounter == 4:
            pp1 = pp1 - pp
            pp1 = -pp1.conjugate() + pp
            pp2 = pp2 - pp
            pp2 = -pp2.conjugate() + pp
            pp3 = pp3 - pp
            pp3 = -pp3.conjugate() + pp
            pp4 = pp4 - pp
            pp4 = -pp4.conjugate() + pp

        pp5 = [pp,pp1,pp2,pp3,pp4]

        if rotecounter == rote:
            print("  " + str(rotecounter) + "回" + "_" + str(pp5))

        rotecounter += 1

        if rotecounter == rote + 1:
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
                print("  青色のPPは" + str(pp))

    ko.extend(pp5)
    mo = list(set(mo) - set(ko))

    rotecounter = 0
else:
    pass


# 橙色右上
if 橙stop != 0:
    print("●橙色右上")
    a = 橙a
    b = 橙b
    rote = 橙rote

    pp = -a-b*1j

    pp1 = pp + 1
    pp2 = pp + 2
    pp3 = pp + 1j

    while rotecounter != 8:

        if rotecounter == rote + 1:
            break

        # 90度回転
        if 1<= rotecounter <=3 or 5 <= rotecounter <=7:
            pp1 = (cos90 + sin90*1j)*(pp1 - pp) + pp
            pp2 = (cos90 + sin90*1j)*(pp2 - pp) + pp
            pp3 = (cos90 + sin90*1j)*(pp3 - pp) + pp

        # 左右反転
        elif rotecounter == 4:
            
            pp1 = pp1 - pp
            pp1 = -pp1.conjugate() + pp
            pp2 = pp2 - pp
            pp2 = -pp2.conjugate() + pp
            pp3 = pp3 - pp
            pp3 = -pp3.conjugate() + pp

        pp5 = [pp,pp1,pp2,pp3]

        if rotecounter == rote:
            print("  " + str(rotecounter) + "回" + "_" + str(pp5))

        rotecounter += 1

        if rotecounter == rote + 1:
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
                print("  橙色のPPは" + str(pp))
        
    ko.extend(pp5)
    mo = list(set(mo) - set(ko))

    rotecounter = 0
else:
    pass


#紫色右
if 紫stop != 0:
    print("●紫色右")
    a = 紫a
    b = 紫b
    rote = 紫rote

    pp = -a-b*1j

    pp1 = pp + 1
    pp2 = pp + 2
    pp3 = pp + 3

    while rotecounter != 4:

        if rotecounter == rote + 1:
            break

        # 90度回転
        elif 1<= rotecounter <=3 or 5 <= rotecounter <=7:
            pp1 = (cos90 + sin90*1j)*(pp1 - pp) + pp
            pp2 = (cos90 + sin90*1j)*(pp2 - pp) + pp
            pp3 = (cos90 + sin90*1j)*(pp3 - pp) + pp

        pp5 = [pp,pp1,pp2,pp3,]

        if rotecounter == rote:
            print("  " + str(rotecounter) + "回" + "_" + str(pp5))

        rotecounter += 1

        if rotecounter == rote + 1:
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
                print("  紫色のPPは" + str(pp))

    ko.extend(pp5)
    mo = list(set(mo) - set(ko))

    rotecounter = 0
else:
    pass


#若草色右上
if 若草stop != 0:
    print("●若草色右上")
    a = 若草a
    b = 若草b
    rote = 若草rote

    pp = -a-b*1j

    pp1 = pp + 1
    pp2 = pp + 1j
    pp3 = pp + 1j + 1

    while rotecounter != 4:

        if rotecounter == rote + 1:
            break

        # 90度回転
        elif 1<= rotecounter <=3:
            pp1 = (cos90 + sin90*1j)*(pp1 - pp) + pp
            pp2 = (cos90 + sin90*1j)*(pp2 - pp) + pp
            pp3 = (cos90 + sin90*1j)*(pp3 - pp) + pp

        pp5 = [pp,pp1,pp2,pp3]

        if rotecounter == rote:
            print("  " + str(rotecounter) + "回" + "_" + str(pp5))

        rotecounter += 1

        if rotecounter == rote + 1:
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
                print("  若草色のPPは" + str(pp))

    ko.extend(pp5)
    mo = list(set(mo) - set(ko))

    rotecounter = 0
else:
    pass


# 白色右上
if 白stop != 0:
    print("●白色右上")
    a = 白a
    b = 白b
    rote = 白rote

    pp = -a-b*1j

    pp1 = pp + 1
    pp2 = pp + 1j

    while rotecounter != 4:

        if rotecounter == rote + 1:
            break

        # 90度回転
        elif 1<= rotecounter <=3:
            pp1 = (cos90 + sin90*1j)*(pp1 - pp) + pp
            pp2 = (cos90 + sin90*1j)*(pp2 - pp) + pp

        pp5 = [pp,pp1,pp2]

        if rotecounter == rote:
            print("  " + str(rotecounter) + "回" + "_" + str(pp5))

        rotecounter += 1

        if rotecounter == rote + 1:
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
                print("  白色のPPは" + str(pp))

    ko.extend(pp5)
    mo = list(set(mo) - set(ko))
    print("残りのマス" + str(mo))
    
    rotecounter = 0
else:
    pass
# %%
