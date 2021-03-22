def hJpn(word):
    Hex = list(word)
    List = []
    for i in range(0, len(Hex)-1, 6):
        if(i+6 > len(Hex)):
            break
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "99 40"):
            List.append("　")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "99 41"):
            List.append("，")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "99 42"):
            List.append("．")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "99 43"):
            List.append("・")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "99 44"):
            List.append("：")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "99 45"):
            List.append("？")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "99 46"):
            List.append("！")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "99 47"):
            List.append("ー")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "99 48"):
            List.append("／")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "99 49"):
            List.append("”")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "99 4A"):
            List.append("（")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "99 4B"):
            List.append("）")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "99 4C"):
            List.append("％")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "99 4D"):
            List.append("０")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "99 4E"):
            List.append("１")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "99 4F"):
            List.append("２")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "99 50"):
            List.append("３")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "99 51"):
            List.append("４")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "99 52"):
            List.append("５")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "99 53"):
            List.append("６")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "99 54"):
            List.append("７")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "99 55"):
            List.append("８")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "99 56"):
            List.append("９")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "99 57"):
            List.append("Ａ")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "99 58"):
            List.append("Ｂ")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "99 59"):
            List.append("Ｃ")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "99 5A"):
            List.append("Ｄ")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "99 5B"):
            List.append("Ｅ")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "99 5C"):
            List.append("Ｆ")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "99 5E"):
            List.append("Ｇ")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "99 5F"):
            List.append("Ｈ")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "99 60"):
            List.append("Ｉ")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "99 61"):
            List.append("Ｊ")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "99 62"):
            List.append("Ｋ")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "99 63"):
            List.append("Ｌ")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "99 64"):
            List.append("Ｍ")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "99 65"):
            List.append("Ｎ")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "99 66"):
            List.append("Ｏ")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "99 67"):
            List.append("Ｐ")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "99 68"):
            List.append("Ｑ")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "99 69"):
            List.append("Ｒ")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "99 6A"):
            List.append("Ｓ")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "99 6B"):
            List.append("Ｔ")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "99 6C"):
            List.append("Ｕ")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "99 6D"):
            List.append("Ｖ")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "99 6E"):
            List.append("Ｗ")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "99 6F"):
            List.append("Ｘ")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "99 70"):
            List.append("Ｙ")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "99 71"):
            List.append("Ｚ")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "99 72"):
            List.append("ぁ")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "99 73"):
            List.append("あ")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "99 74"):
            List.append("ぃ")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "99 75"):
            List.append("い")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "99 76"):
            List.append("ぅ")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "99 77"):
            List.append("う")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "99 78"):
            List.append("ぇ")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "99 79"):
            List.append("え")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "99 7A"):
            List.append("ぉ")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "99 7B"):
            List.append("お")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "99 7C"):
            List.append("か")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "99 7D"):
            List.append("が")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "99 7E"):
            List.append("き")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "99 80"):
            List.append("ぎ")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "99 81"):
            List.append("く")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "99 82"):
            List.append("ぐ")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "99 83"):
            List.append("け")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "99 84"):
            List.append("げ")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "99 85"):
            List.append("こ")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "99 86"):
            List.append("ご")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "99 87"):
            List.append("さ")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "99 88"):
            List.append("ざ")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "99 89"):
            List.append("し")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "99 8A"):
            List.append("じ")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "99 8B"):
            List.append("す")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "99 8C"):
            List.append("ず")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "99 8D"):
            List.append("せ")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "99 8E"):
            List.append("ぜ")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "99 8F"):
            List.append("そ")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "99 90"):
            List.append("ぞ")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "99 91"):
            List.append("た")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "99 92"):
            List.append("だ")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "99 93"):
            List.append("ち")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "99 94"):
            List.append("ぢ")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "99 95"):
            List.append("っ")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "99 96"):
            List.append("つ")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "99 97"):
            List.append("づ")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "99 98"):
            List.append("て")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "99 99"):
            List.append("で")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "99 9A"):
            List.append("と")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "99 9B"):
            List.append("ど")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "99 9C"):
            List.append("な")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "99 9D"):
            List.append("に")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "99 9E"):
            List.append("ぬ")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "99 9F"):
            List.append("ね")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "99 A0"):
            List.append("の")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "99 A1"):
            List.append("は")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "99 A2"):
            List.append("ば")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "99 A3"):
            List.append("ぱ")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "99 A4"):
            List.append("ひ")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "99 A5"):
            List.append("び")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "99 A6"):
            List.append("ぴ")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "99 A7"):
            List.append("ふ")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "99 A8"):
            List.append("ぶ")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "99 A9"):
            List.append("ぷ")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "99 AA"):
            List.append("へ")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "99 AB"):
            List.append("べ")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "99 AC"):
            List.append("ぺ")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "99 AD"):
            List.append("ほ")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "99 AE"):
            List.append("ぼ")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "99 AF"):
            List.append("ぽ")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "99 B0"):
            List.append("ま")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "99 B1"):
            List.append("み")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "99 B2"):
            List.append("む")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "99 B3"):
            List.append("め")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "99 B4"):
            List.append("も")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "99 B5"):
            List.append("ゃ")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "99 B6"):
            List.append("や")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "99 B7"):
            List.append("ゅ")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "99 B8"):
            List.append("ゆ")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "99 B9"):
            List.append("ょ")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "99 BA"):
            List.append("よ")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "99 BB"):
            List.append("ら")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "99 BC"):
            List.append("り")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "99 BD"):
            List.append("る")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "99 BE"):
            List.append("れ")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "99 BF"):
            List.append("ろ")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "99 C0"):
            List.append("ゎ")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "99 C1"):
            List.append("わ")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "99 C2"):
            List.append("ゐ")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "99 C3"):
            List.append("ゑ")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "99 C4"):
            List.append("を")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "99 C5"):
            List.append("ん")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "99 C6"):
            List.append("ァ")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "99 C7"):
            List.append("ア")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "99 C8"):
            List.append("ィ")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "99 C9"):
            List.append("イ")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "99 CA"):
            List.append("ゥ")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "99 CB"):
            List.append("ウ")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "99 CC"):
            List.append("ェ")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "99 CD"):
            List.append("エ")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "99 CE"):
            List.append("ォ")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "99 CF"):
            List.append("オ")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "99 D0"):
            List.append("カ")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "99 D1"):
            List.append("ガ")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "99 D2"):
            List.append("キ")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "99 D3"):
            List.append("ギ")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "99 D4"):
            List.append("ク")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "99 D5"):
            List.append("グ")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "99 D6"):
            List.append("ケ")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "99 D7"):
            List.append("ゲ")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "99 D8"):
            List.append("コ")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "99 D9"):
            List.append("ゴ")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "99 DA"):
            List.append("サ")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "99 DB"):
            List.append("ザ")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "99 DC"):
            List.append("シ")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "99 DD"):
            List.append("ジ")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "99 DE"):
            List.append("ス")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "99 DF"):
            List.append("ズ")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "99 E0"):
            List.append("セ")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "99 E1"):
            List.append("ゼ")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "99 E2"):
            List.append("ソ")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "99 E3"):
            List.append("ゾ")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "99 E4"):
            List.append("タ")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "99 E5"):
            List.append("ダ")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "99 E6"):
            List.append("チ")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "99 E7"):
            List.append("ヂ")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "99 E8"):
            List.append("ッ")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "99 E9"):
            List.append("ツ")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "99 EA"):
            List.append("ヅ")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "99 EB"):
            List.append("テ")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "99 EC"):
            List.append("デ")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "99 ED"):
            List.append("ト")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "99 EE"):
            List.append("ド")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "99 EF"):
            List.append("ナ")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "99 F0"):
            List.append("ニ")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "99 F1"):
            List.append("ヌ")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "99 F2"):
            List.append("ネ")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "99 F3"):
            List.append("ノ")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "99 F4"):
            List.append("ハ")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "99 F5"):
            List.append("バ")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "99 F6"):
            List.append("パ")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "99 F7"):
            List.append("ヒ")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "99 F8"):
            List.append("ビ")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "99 F9"):
            List.append("ピ")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "99 FA"):
            List.append("フ")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "99 FB"):
            List.append("ブ")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "99 FC"):
            List.append("プ")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9A 40"):
            List.append("ヘ")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9A 41"):
            List.append("ベ")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9A 42"):
            List.append("ペ")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9A 43"):
            List.append("ホ")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9A 44"):
            List.append("ボ")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9A 45"):
            List.append("ポ")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9A 46"):
            List.append("マ")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9A 47"):
            List.append("ミ")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9A 48"):
            List.append("＆")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9A 49"):
            List.append("ム")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9A 4A"):
            List.append("メ")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9A 4B"):
            List.append("モ")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9A 4C"):
            List.append("ャ")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9A 4D"):
            List.append("ヤ")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9A 4E"):
            List.append("ュ")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9A 4F"):
            List.append("ユ")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9A 50"):
            List.append("ョ")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9A 51"):
            List.append("ヨ")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9A 52"):
            List.append("ラ")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9A 53"):
            List.append("リ")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9A 54"):
            List.append("ル")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9A 55"):
            List.append("レ")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9A 56"):
            List.append("ロ")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9A 57"):
            List.append("−")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9A 58"):
            List.append("ワ")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9A 59"):
            List.append("＝")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9A 5A"):
            List.append("☆")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9A 5B"):
            List.append("ヲ")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9A 5D"):
            List.append("ン")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9A 5E"):
            List.append("ヴ")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9A 7A"):
            List.append("△")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9A 7B"):
            List.append("○")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9A 7C"):
            List.append("×")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9A 7D"):
            List.append("＜")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9A 7E"):
            List.append("＞")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9A 80"):
            List.append("♪")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9A 81"):
            List.append("〜")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9A 82"):
            List.append("▽")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9A 83"):
            List.append("『")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9A 84"):
            List.append("』")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9A 85"):
            List.append("、")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9A 86"):
            List.append("。")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9A 87"):
            List.append("一")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9A 88"):
            List.append("二")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9A 89"):
            List.append("十")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9A 8A"):
            List.append("千")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9A 8B"):
            List.append("万")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9A 8C"):
            List.append("地")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9A 8D"):
            List.append("水")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9A 8E"):
            List.append("火")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9A 8F"):
            List.append("風")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9A 90"):
            List.append("光")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9A 91"):
            List.append("闇")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9A 92"):
            List.append("南")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9A 93"):
            List.append("西")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9A 94"):
            List.append("北")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9A 95"):
            List.append("赤")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9A 96"):
            List.append("白")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9A 97"):
            List.append("黒")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9A 98"):
            List.append("年")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9A 99"):
            List.append("月")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9A 9A"):
            List.append("日")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9A 9B"):
            List.append("時")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9A 9C"):
            List.append("戦")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9A 9D"):
            List.append("闘")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9A 9E"):
            List.append("攻")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9A 9F"):
            List.append("撃")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9A A0"):
            List.append("防")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9A A1"):
            List.append("御")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9A A2"):
            List.append("回")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9A A3"):
            List.append("避")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9A A4"):
            List.append("術")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9A A5"):
            List.append("技")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9A A6"):
            List.append("道")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9A A7"):
            List.append("具")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9A A8"):
            List.append("合")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9A A9"):
            List.append("成")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9A AA"):
            List.append("神")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9A AB"):
            List.append("座")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9A AC"):
            List.append("都")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9A AD"):
            List.append("市")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9A AE"):
            List.append("格")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9A AF"):
            List.append("先")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9A B0"):
            List.append("行")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9A B1"):
            List.append("世")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9A B2"):
            List.append("楽")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9A B3"):
            List.append("園")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9A B4"):
            List.append("案")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9A B5"):
            List.append("外")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9A B6"):
            List.append("所")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9A B7"):
            List.append("知")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9A B8"):
            List.append("大")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9A B9"):
            List.append("昔")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9A BA"):
            List.append("人")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9A BB"):
            List.append("間")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9A BC"):
            List.append("自")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9A BD"):
            List.append("分")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9A BE"):
            List.append("生")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9A BF"):
            List.append("毎")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9A C0"):
            List.append("祈")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9A C1"):
            List.append("決")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9A C2"):
            List.append("上")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9A C3"):
            List.append("降")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9A C4"):
            List.append("今")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9A C5"):
            List.append("度")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9A C6"):
            List.append("来")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9A C7"):
            List.append("待")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9A C8"):
            List.append("乗")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9A C9"):
            List.append("空")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9A CA"):
            List.append("何")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9A CB"):
            List.append("手")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9A CC"):
            List.append("入")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9A CD"):
            List.append("以")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9A CE"):
            List.append("持")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9A CF"):
            List.append("武")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9A D0"):
            List.append("器")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9A D1"):
            List.append("屋")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9A D2"):
            List.append("教")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9A D3"):
            List.append("会")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9A D4"):
            List.append("食")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9A D5"):
            List.append("材")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9A D6"):
            List.append("宿")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9A D7"):
            List.append("客")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9A D8"):
            List.append("室")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9A D9"):
            List.append("階")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9A DA"):
            List.append("廊")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9A DB"):
            List.append("下")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9A DC"):
            List.append("変")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9A DD"):
            List.append("第")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9A DE"):
            List.append("章")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9A DF"):
            List.append("代")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9A E0"):
            List.append("更")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9A E1"):
            List.append("広")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9A E2"):
            List.append("場")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9A E3"):
            List.append("旧")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9A E4"):
            List.append("街")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9A E5"):
            List.append("前")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9A E6"):
            List.append("悪")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9A E7"):
            List.append("夢")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9A E8"):
            List.append("帰")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9A E9"):
            List.append("王")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9A EA"):
            List.append("開")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9A EB"):
            List.append("放")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9A EC"):
            List.append("土")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9A ED"):
            List.append("新")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9A EE"):
            List.append("活")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9A EF"):
            List.append("気")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9A F0"):
            List.append("住")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9A F1"):
            List.append("恩")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9A F2"):
            List.append("最")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9A F3"):
            List.append("近")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9A F4"):
            List.append("国")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9A F5"):
            List.append("団")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9A F6"):
            List.append("進")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9A F7"):
            List.append("出")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9A F8"):
            List.append("信")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9A F9"):
            List.append("助")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9A FA"):
            List.append("話")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9A FB"):
            List.append("顔")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9A FC"):
            List.append("心")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9A FD"):
            List.append("底")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9A FE"):
            List.append("城")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9A FF"):
            List.append("音")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9B 40"):
            List.append("底")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9B 41"):
            List.append("城")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9B 42"):
            List.append("音")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9B 43"):
            List.append("聞")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9B 44"):
            List.append("急")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9B 45"):
            List.append("身")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9B 46"):
            List.append("賊")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9B 47"):
            List.append("込")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9B 48"):
            List.append("狙")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9B 49"):
            List.append("率")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9B 4A"):
            List.append("精")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9B 4B"):
            List.append("鋭")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9B 4C"):
            List.append("保")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9B 4D"):
            List.append("証")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9B 4E"):
            List.append("襲")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9B 4F"):
            List.append("負")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9B 50"):
            List.append("傷")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9B 51"):
            List.append("奪")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9B 52"):
            List.append("言")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9B 53"):
            List.append("英")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9B 54"):
            List.append("雄")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9B 55"):
            List.append("男")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9B 56"):
            List.append("見")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9B 57"):
            List.append("目")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9B 58"):
            List.append("朝")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9B 59"):
            List.append("早")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9B 5A"):
            List.append("女")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9B 5B"):
            List.append("子")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9B 5C"):
            List.append("止")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9B 5D"):
            List.append("止")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9B 5E"):
            List.append("殿")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9B 5F"):
            List.append("向")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9B 60"):
            List.append("雪")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9B 61"):
            List.append("書")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9B 62"):
            List.append("界")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9B 63"):
            List.append("中")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9B 64"):
            List.append("思")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9B 65"):
            List.append("泣")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9B 66"):
            List.append("馬")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9B 67"):
            List.append("足")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9B 68"):
            List.append("恋")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9B 69"):
            List.append("盗")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9B 6A"):
            List.append("現")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9B 6B"):
            List.append("歌")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9B 6C"):
            List.append("隠")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9B 6D"):
            List.append("事")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9B 6E"):
            List.append("情")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9B 6F"):
            List.append("色")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9B 70"):
            List.append("感")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9B 71"):
            List.append("動")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9B 72"):
            List.append("運")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9B 73"):
            List.append("命")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9B 74"):
            List.append("明")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9B 75"):
            List.append("寒")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9B 76"):
            List.append("暖")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9B 77"):
            List.append("房")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9B 78"):
            List.append("図")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9B 79"):
            List.append("館")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9B 7A"):
            List.append("本")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9B 7B"):
            List.append("読")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9B 7C"):
            List.append("番")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9B 7D"):
            List.append("単")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9B 7E"):
            List.append("文")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9B 7F"):
            List.append("化")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9B 80"):
            List.append("化")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9B 81"):
            List.append("民")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9B 82"):
            List.append("与")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9B 83"):
            List.append("建")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9B 84"):
            List.append("歴")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9B 85"):
            List.append("史")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9B 86"):
            List.append("的")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9B 87"):
            List.append("美")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9B 88"):
            List.append("私")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9B 89"):
            List.append("語")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9B 8A"):
            List.append("禁")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9B 8B"):
            List.append("公")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9B 8C"):
            List.append("静")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9B 8D"):
            List.append("落")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9B 8E"):
            List.append("方")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9B 8F"):
            List.append("爆")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9B 90"):
            List.append("発")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9B 91"):
            List.append("起")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9B 92"):
            List.append("直")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9B 93"):
            List.append("後")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9B 94"):
            List.append("戻")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9B 95"):
            List.append("好")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9B 96"):
            List.append("乱")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9B 97"):
            List.append("終")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9B 98"):
            List.append("平")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9B 99"):
            List.append("和")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9B 9A"):
            List.append("若")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9B 9B"):
            List.append("旅")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9B 9C"):
            List.append("諸")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9B 9D"):
            List.append("温")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9B 9E"):
            List.append("育")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9B 9F"):
            List.append("机")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9B A0"):
            List.append("学")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9B A1"):
            List.append("葉")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9B A2"):
            List.append("庶")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9B A3"):
            List.append("政")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9B A4"):
            List.append("治")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9B A5"):
            List.append("必")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9B A6"):
            List.append("要")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9B A7"):
            List.append("我")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9B A8"):
            List.append("視")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9B A9"):
            List.append("察")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9B AA"):
            List.append("笑")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9B AB"):
            List.append("遠")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9B AC"):
            List.append("存")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9B AD"):
            List.append("在")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9B AE"):
            List.append("危")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9B AF"):
            List.append("険")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9B B0"):
            List.append("彼")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9B B1"):
            List.append("野")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9B B2"):
            List.append("望")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9B B3"):
            List.append("積")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9B B4"):
            List.append("到")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9B B5"):
            List.append("着")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9B B6"):
            List.append("遅")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9B B7"):
            List.append("誘")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9B B8"):
            List.append("導")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9B B9"):
            List.append("家")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9B BA"):
            List.append("小")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9B BB"):
            List.append("社")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9B BC"):
            List.append("廃")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9B BD"):
            List.append("坑")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9B BE"):
            List.append("宝")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9B BF"):
            List.append("部")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9B C0"):
            List.append("悔")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9B C1"):
            List.append("特")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9B C2"):
            List.append("別")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9B C3"):
            List.append("暗")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9B C4"):
            List.append("号")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9B C5"):
            List.append("者")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9B C6"):
            List.append("繁")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9B C7"):
            List.append("栄")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9B C8"):
            List.append("願")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9B C9"):
            List.append("記")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9B CA"):
            List.append("貧")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9B CB"):
            List.append("富")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9B CC"):
            List.append("差")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9B CD"):
            List.append("税")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9B CE"):
            List.append("制")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9B CF"):
            List.append("弱")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9B D0"):
            List.append("救")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9B D1"):
            List.append("済")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9B D2"):
            List.append("予")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9B D3"):
            List.append("算")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9B D4"):
            List.append("確")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9B D5"):
            List.append("安")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9B D6"):
            List.append("守")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9B D7"):
            List.append("警")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9B D8"):
            List.append("組")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9B D9"):
            List.append("織")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9B DA"):
            List.append("支")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9B DB"):
            List.append("援")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9B DC"):
            List.append("意")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9B DD"):
            List.append("識")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9B DE"):
            List.append("改")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9B DF"):
            List.append("革")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9B E0"):
            List.append("愛")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9B E1"):
            List.append("条")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9B E2"):
            List.append("想")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9B E3"):
            List.append("素")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9B E4"):
            List.append("敵")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9B E5"):
            List.append("当")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9B E6"):
            List.append("考")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9B E7"):
            List.append("誤")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9B E8"):
            List.append("理")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9B E9"):
            List.append("実")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9B EA"):
            List.append("即")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9B EB"):
            List.append("効")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9B EC"):
            List.append("性")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9B ED"):
            List.append("求")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9B EE"):
            List.append("劇")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9B EF"):
            List.append("薬")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9B F0"):
            List.append("選")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9B F1"):
            List.append("約")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9B F2"):
            List.append("束")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9B F3"):
            List.append("届")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9B F4"):
            List.append("型")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9B F5"):
            List.append("引")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9B F6"):
            List.append("力")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9B F7"):
            List.append("作")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9B F8"):
            List.append("内")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9B F9"):
            List.append("設")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9B FA"):
            List.append("備")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9B FB"):
            List.append("数")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9B FC"):
            List.append("枚")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9C 40"):
            List.append("句")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9C 41"):
            List.append("仕")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9C 42"):
            List.append("幸")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9C 43"):
            List.append("奥")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9C 44"):
            List.append("採")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9C 45"):
            List.append("掘")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9C 46"):
            List.append("探")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9C 47"):
            List.append("掛")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9C 48"):
            List.append("未")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9C 49"):
            List.append("稼")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9C 4A"):
            List.append("略")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9C 4B"):
            List.append("切")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9C 4C"):
            List.append("替")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9C 4D"):
            List.append("電")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9C 4E"):
            List.append("源")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9C 4F"):
            List.append("右")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9C 50"):
            List.append("段")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9C 51"):
            List.append("突")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9C 52"):
            List.append("壁")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9C 53"):
            List.append("調")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9C 54"):
            List.append("港")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9C 55"):
            List.append("船")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9C 56"):
            List.append("定")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9C 57"):
            List.append("期")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9C 58"):
            List.append("長")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9C 59"):
            List.append("修")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9C 5A"):
            List.append("菜")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9C 5B"):
            List.append("商")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9C 5C"):
            List.append("品")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9C 5D"):
            List.append("台")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9C 5F"):
            List.append("不")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9C 60"):
            List.append("故")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9C 61"):
            List.append("側")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9C 62"):
            List.append("責")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9C 63"):
            List.append("任")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9C 64"):
            List.append("処")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9C 65"):
            List.append("欲")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9C 66"):
            List.append("海")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9C 67"):
            List.append("路")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9C 68"):
            List.append("他")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9C 69"):
            List.append("法")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9C 6A"):
            List.append("退")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9C 6B"):
            List.append("屈")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9C 6C"):
            List.append("失")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9C 6D"):
            List.append("礼")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9C 6E"):
            List.append("腕")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9C 6F"):
            List.append("立")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9C 70"):
            List.append("芸")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9C 71"):
            List.append("受")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9C 72"):
            List.append("参")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9C 73"):
            List.append("然")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9C 74"):
            List.append("勇")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9C 75"):
            List.append("折")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9C 76"):
            List.append("越")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9C 77"):
            List.append("印")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9C 78"):
            List.append("陸")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9C 79"):
            List.append("暮")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9C 7A"):
            List.append("準")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9C 7B"):
            List.append("飛")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9C 7C"):
            List.append("振")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9C 7D"):
            List.append("応")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9C 7E"):
            List.append("使")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9C 7F"):
            List.append("僕")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9C 80"):
            List.append("頼")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9C 81"):
            List.append("企")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9C 82"):
            List.append("業")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9C 83"):
            List.append("滅")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9C 84"):
            List.append("金")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9C 85"):
            List.append("庫")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9C 86"):
            List.append("収")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9C 87"):
            List.append("霧")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9C 88"):
            List.append("眠")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9C 89"):
            List.append("依")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9C 8B"):
            List.append("申")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9C 8C"):
            List.append("遺")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9C 8D"):
            List.append("産")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9C 8E"):
            List.append("状")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9C 8F"):
            List.append("貴")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9C 90"):
            List.append("様")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9C 91"):
            List.append("偶")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9C 92"):
            List.append("主")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9C 93"):
            List.append("取")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9C 94"):
            List.append("跡")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9C 95"):
            List.append("敷")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9C 96"):
            List.append("買")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9C 97"):
            List.append("途")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9C 98"):
            List.append("死")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9C 99"):
            List.append("被")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9C 9A"):
            List.append("害")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9C 9B"):
            List.append("売")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9C 9C"):
            List.append("配")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9C 9D"):
            List.append("晴")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9C 9E"):
            List.append("装")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9C 9F"):
            List.append("飾")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9C A0"):
            List.append("名")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9C A1"):
            List.append("工")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9C A2"):
            List.append("嬢")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9C A3"):
            List.append("石")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9C A4"):
            List.append("箱")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9C A5"):
            List.append("渡")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9C A6"):
            List.append("結")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9C A7"):
            List.append("局")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9C A8"):
            List.append("比")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9C A9"):
            List.append("山")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9C AA"):
            List.append("疲")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9C AB"):
            List.append("端")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9C AC"):
            List.append("位")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9C AD"):
            List.append("置")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9C AE"):
            List.append("町")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9C AF"):
            List.append("俺")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9C B0"):
            List.append("仮")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9C B1"):
            List.append("面")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9C B2"):
            List.append("臣")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9C B3"):
            List.append("逃")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9C B4"):
            List.append("秘")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9C B5"):
            List.append("密")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9C B6"):
            List.append("多")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9C B7"):
            List.append("仲")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9C B8"):
            List.append("経")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9C B9"):
            List.append("追")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9C BA"):
            List.append("相")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9C BB"):
            List.append("返")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9C BC"):
            List.append("父")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9C BD"):
            List.append("少")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9C BE"):
            List.append("関")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9C BF"):
            List.append("係")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9C C0"):
            List.append("形")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9C C1"):
            List.append("歩")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9C C2"):
            List.append("論")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9C C3"):
            List.append("夜")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9C C4"):
            List.append("休")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9C C5"):
            List.append("指")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9C C6"):
            List.append("覚")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9C C7"):
            List.append("君")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9C C8"):
            List.append("体")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9C C9"):
            List.append("全")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9C CA"):
            List.append("包")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9C CB"):
            List.append("浮")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9C CC"):
            List.append("無")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9C CD"):
            List.append("郷")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9C CE"):
            List.append("同")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9C CF"):
            List.append("普")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9C D0"):
            List.append("通")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9C D1"):
            List.append("元")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9C D2"):
            List.append("寝")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9C D3"):
            List.append("付")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9C D4"):
            List.append("絶")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9C D5"):
            List.append("対")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9C D6"):
            List.append("勝")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9C D7"):
            List.append("利")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9C D8"):
            List.append("詳")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9C D9"):
            List.append("忘")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9C DA"):
            List.append("兄")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9C DB"):
            List.append("婚")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9C DC"):
            List.append("田")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9C DD"):
            List.append("舎")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9C DE"):
            List.append("村")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9C DF"):
            List.append("親")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9C E0"):
            List.append("声")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9C E1"):
            List.append("叫")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9C E2"):
            List.append("打")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9C E3"):
            List.append("兵")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9C E4"):
            List.append("士")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9C E5"):
            List.append("機")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9C E6"):
            List.append("派")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9C E7"):
            List.append("晩")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9C E8"):
            List.append("泊")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9C E9"):
            List.append("似")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9C EA"):
            List.append("母")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9C EB"):
            List.append("連")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9C EC"):
            List.append("用")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9C ED"):
            List.append("達")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9C EE"):
            List.append("息")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9C EF"):
            List.append("尊")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9C F0"):
            List.append("敬")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9C F1"):
            List.append("遊")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9C F2"):
            List.append("観")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9C F3"):
            List.append("強")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9C F4"):
            List.append("倉")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9C F5"):
            List.append("怪")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9C F6"):
            List.append("物")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9C F7"):
            List.append("倒")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9C F8"):
            List.append("沈")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9C F9"):
            List.append("問")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9C FA"):
            List.append("題")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9C FB"):
            List.append("脱")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9C FC"):
            List.append("員")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9C FD"):
            List.append("程")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9C FE"):
            List.append("犠")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9C FF"):
            List.append("牲")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9D 43"):
            List.append("割")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9D 44"):
            List.append("操")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9D 45"):
            List.append("舵")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9D 46"):
            List.append("激")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9D 47"):
            List.append("初")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9D 48"):
            List.append("航")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9D 49"):
            List.append("続")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9D 4A"):
            List.append("補")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9D 4B"):
            List.append("寸")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9D 4C"):
            List.append("際")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9D 4D"):
            List.append("照")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9D 4E"):
            List.append("完")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9D 4F"):
            List.append("舞")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9D 50"):
            List.append("等")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9D 51"):
            List.append("由")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9D 52"):
            List.append("難")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9D 53"):
            List.append("認")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9D 54"):
            List.append("得")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9D 55"):
            List.append("件")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9D 56"):
            List.append("審")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9D 57"):
            List.append("次")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9D 58"):
            List.append("幹")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9D 59"):
            List.append("崩")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9D 5A"):
            List.append("壊")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9D 5B"):
            List.append("共")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9D 5C"):
            List.append("歳")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9D 5D"):
            List.append("原")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9D 5E"):
            List.append("因")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9D 60"):
            List.append("真")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9D 61"):
            List.append("協")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9D 62"):
            List.append("説")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9D 63"):
            List.append("唯")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9D 64"):
            List.append("預")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9D 65"):
            List.append("没")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9D 66"):
            List.append("態")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9D 67"):
            List.append("談")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9D 68"):
            List.append("羽")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9D 69"):
            List.append("潮")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9D 6A"):
            List.append("香")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9D 6B"):
            List.append("議")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9D 6C"):
            List.append("軽")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9D 6D"):
            List.append("伝")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9D 6E"):
            List.append("絡")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9D 6F"):
            List.append("張")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9D 70"):
            List.append("増")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9D 71"):
            List.append("損")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9D 72"):
            List.append("呼")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9D 73"):
            List.append("油")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9D 74"):
            List.append("断")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9D 75"):
            List.append("穴")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9D 76"):
            List.append("鼻")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9D 77"):
            List.append("興")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9D 78"):
            List.append("味")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9D 79"):
            List.append("便")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9D 7A"):
            List.append("拝")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9D 7B"):
            List.append("堂")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9D 7C"):
            List.append("線")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9D 7D"):
            List.append("簡")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9D 7E"):
            List.append("供")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9D 80"):
            List.append("騎")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9D 81"):
            List.append("属")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9D 82"):
            List.append("敗")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9D 83"):
            List.append("走")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9D 84"):
            List.append("集")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9D 85"):
            List.append("背")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9D 86"):
            List.append("景")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9D 87"):
            List.append("果")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9D 88"):
            List.append("停")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9D 89"):
            List.append("煮")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9D 8A"):
            List.append("炒")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9D 8B"):
            List.append("米")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9D 8C"):
            List.append("緒")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9D 8D"):
            List.append("役")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9D 8E"):
            List.append("熱")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9D 8F"):
            List.append("鮮")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9D 90"):
            List.append("料")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9D 91"):
            List.append("揚")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9D 92"):
            List.append("口")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9D 93"):
            List.append("卵")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9D 94"):
            List.append("焼")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9D 95"):
            List.append("抜")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9D 96"):
            List.append("肉")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9D 97"):
            List.append("統")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9D 98"):
            List.append("加")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9D 99"):
            List.append("減")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9D 9A"):
            List.append("賞")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9D 9B"):
            List.append("太")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9D 9C"):
            List.append("刺")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9D 9D"):
            List.append("烈")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9D 9E"):
            List.append("夏")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9D 9F"):
            List.append("浴")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9D A0"):
            List.append("波")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9D A1"):
            List.append("漂")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9D A2"):
            List.append("幻")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9D A3"):
            List.append("酔")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9D A4"):
            List.append("瞬")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9D A5"):
            List.append("魚")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9D A6"):
            List.append("重")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9D A7"):
            List.append("深")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9D A8"):
            List.append("冷")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9D A9"):
            List.append("宇")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9D AA"):
            List.append("宙")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9D AB"):
            List.append("星")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9D AC"):
            List.append("輝")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9D AD"):
            List.append("豪")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9D AE"):
            List.append("快")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9D AF"):
            List.append("麻")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9D B0"):
            List.append("婆")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9D B1"):
            List.append("豆")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9D B2"):
            List.append("腐")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9D B3"):
            List.append("辛")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9D B4"):
            List.append("妙")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9D B5"):
            List.append("極")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9D B6"):
            List.append("違")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9D B7"):
            List.append("異")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9D B8"):
            List.append("魔")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9D B9"):
            List.append("養")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9D BA"):
            List.append("豊")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9D BB"):
            List.append("盛")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9D BC"):
            List.append("絵")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9D BD"):
            List.append("画")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9D BE"):
            List.append("描")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9D BF"):
            List.append("構")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9D C0"):
            List.append("甘")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9D C1"):
            List.append("巻")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9D C2"):
            List.append("染")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9D C3"):
            List.append("高")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9D C4"):
            List.append("互")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9D C5"):
            List.append("称")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9D C6"):
            List.append("誰")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9D C7"):
            List.append("幼")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9D C8"):
            List.append("頃")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9D C9"):
            List.append("演")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9D CA"):
            List.append("汁")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9D CB"):
            List.append("介")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9D CC"):
            List.append("類")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9D CD"):
            List.append("腹")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9D CE"):
            List.append("式")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9D CF"):
            List.append("吸")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9D D0"):
            List.append("酸")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9D D1"):
            List.append("清")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9D D2"):
            List.append("奇")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9D D3"):
            List.append("贈")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9D D4"):
            List.append("飲")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9D D5"):
            List.append("熟")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9D D6"):
            List.append("須")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9D D7"):
            List.append("交")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9D D8"):
            List.append("響")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9D D9"):
            List.append("曲")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9D DA"):
            List.append("奏")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9D DB"):
            List.append("速")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9D DC"):
            List.append("半")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9D DD"):
            List.append("拡")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9D DE"):
            List.append("縮")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9D DF"):
            List.append("了")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9D E0"):
            List.append("径")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9D E1"):
            List.append("冒")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9D E2"):
            List.append("賛")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9D E3"):
            List.append("離")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9D E4"):
            List.append("迷")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9D E5"):
            List.append("惑")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9D E6"):
            List.append("孤")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9D E7"):
            List.append("児")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9D E8"):
            List.append("院")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9D E9"):
            List.append("孝")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9D EA"):
            List.append("逆")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9D EB"):
            List.append("転")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9D EC"):
            List.append("塔")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9D ED"):
            List.append("報")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9D EE"):
            List.append("査")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9D EF"):
            List.append("隊")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9D F0"):
            List.append("護")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9D F1"):
            List.append("衛")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9D F2"):
            List.append("価")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9D F3"):
            List.append("値")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9D F4"):
            List.append("紙")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9D F5"):
            List.append("苦")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9D F6"):
            List.append("慣")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9D F7"):
            List.append("血")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9D F8"):
            List.append("流")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9D F9"):
            List.append("労")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9D FA"):
            List.append("惜")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9D FB"):
            List.append("捨")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9D FC"):
            List.append("質")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9D FD"):
            List.append("胸")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9E 41"):
            List.append("整")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9E 42"):
            List.append("店")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9E 43"):
            List.append("踏")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9E 44"):
            List.append("巨")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9E 45"):
            List.append("破")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9E 46"):
            List.append("衣")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9E 47"):
            List.append("犯")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9E 48"):
            List.append("捕")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9E 49"):
            List.append("牢")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9E 4A"):
            List.append("始")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9E 4B"):
            List.append("嫌")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9E 4C"):
            List.append("過")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9E 4D"):
            List.append("去")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9E 4E"):
            List.append("功")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9E 4F"):
            List.append("績")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9E 50"):
            List.append("両")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9E 51"):
            List.append("貸")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9E 52"):
            List.append("耳")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9E 53"):
            List.append("趣")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9E 54"):
            List.append("剣")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9E 55"):
            List.append("幕")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9E 56"):
            List.append("誓")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9E 57"):
            List.append("歯")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9E 58"):
            List.append("眼")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9E 59"):
            List.append("悟")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9E 5A"):
            List.append("吹")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9E 5B"):
            List.append("昨")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9E 5C"):
            List.append("玉")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9E 5E"):
            List.append("送")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9E 5F"):
            List.append("字")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9E 60"):
            List.append("暴")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9E 61"):
            List.append("里")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9E 62"):
            List.append("恐")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9E 63"):
            List.append("謝")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9E 64"):
            List.append("聖")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9E 65"):
            List.append("総")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9E 66"):
            List.append("適")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9E 67"):
            List.append("順")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9E 68"):
            List.append("納")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9E 69"):
            List.append("捧")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9E 6A"):
            List.append("偉")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9E 6B"):
            List.append("祝")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9E 6C"):
            List.append("福")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9E 6D"):
            List.append("痛")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9E 6E"):
            List.append("友")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9E 6F"):
            List.append("髪")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9E 70"):
            List.append("短")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9E 71"):
            List.append("残")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9E 72"):
            List.append("念")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9E 73"):
            List.append("抱")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9E 74"):
            List.append("悩")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9E 75"):
            List.append("砕")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9E 76"):
            List.append("威")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9E 77"):
            List.append("勢")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9E 78"):
            List.append("僧")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9E 79"):
            List.append("正")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9E 7A"):
            List.append("解")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9E 7B"):
            List.append("虫")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9E 7C"):
            List.append("仇")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9E 7D"):
            List.append("討")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9E 7E"):
            List.append("払")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9E 80"):
            List.append("黙")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9E 81"):
            List.append("示")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9E 82"):
            List.append("従")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9E 83"):
            List.append("忙")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9E 84"):
            List.append("謁")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9E 85"):
            List.append("週")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9E 86"):
            List.append("毒")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9E 87"):
            List.append("頭")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9E 88"):
            List.append("驚")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9E 89"):
            List.append("有")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9E 8A"):
            List.append("荒")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9E 8B"):
            List.append("復")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9E 8C"):
            List.append("境")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9E 8D"):
            List.append("遇")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9E 8E"):
            List.append("健")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9E 8F"):
            List.append("康")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9E 90"):
            List.append("病")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9E 91"):
            List.append("影")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9E 92"):
            List.append("硬")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9E 93"):
            List.append("慮")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9E 94"):
            List.append("雲")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9E 95"):
            List.append("訳")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9E 96"):
            List.append("許")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9E 97"):
            List.append("換")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9E 98"):
            List.append("拒")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9E 99"):
            List.append("災")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9E 9A"):
            List.append("拠")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9E 9B"):
            List.append("肩")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9E 9C"):
            List.append("可")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9E 9D"):
            List.append("能")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9E 9E"):
            List.append("偽")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9E 9F"):
            List.append("善")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9E A0"):
            List.append("鳥")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9E A1"):
            List.append("巣")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9E A2"):
            List.append("憧")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9E A3"):
            List.append("資")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9E A4"):
            List.append("誇")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9E A5"):
            List.append("管")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9E A6"):
            List.append("量")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9E A7"):
            List.append("縁")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9E A8"):
            List.append("愚")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9E A9"):
            List.append("邪")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9E AA"):
            List.append("容")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9E AB"):
            List.append("赦")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9E AC"):
            List.append("像")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9E AD"):
            List.append("仰")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9E AE"):
            List.append("困")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9E AF"):
            List.append("択")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9E B0"):
            List.append("夕")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9E B1"):
            List.append("扱")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9E B2"):
            List.append("啓")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9E B3"):
            List.append("汚")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9E B4"):
            List.append("罰")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9E B5"):
            List.append("胆")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9E B6"):
            List.append("猫")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9E B7"):
            List.append("棒")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9E B8"):
            List.append("細")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9E B9"):
            List.append("点")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9E BA"):
            List.append("製")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9E BB"):
            List.append("矢")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9E BC"):
            List.append("居")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9E BD"):
            List.append("肝")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9E BE"):
            List.append("答")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9E BF"):
            List.append("義")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9E C0"):
            List.append("務")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9E C1"):
            List.append("留")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9E C2"):
            List.append("障")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9E C3"):
            List.append("訓")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9E C4"):
            List.append("弟")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9E C5"):
            List.append("妹")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9E C6"):
            List.append("首")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9E C7"):
            List.append("迎")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9E C8"):
            List.append("姉")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9E C9"):
            List.append("姿")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9E CA"):
            List.append("将")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9E CB"):
            List.append("散")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9E CC"):
            List.append("練")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9E CD"):
            List.append("猟")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9E CE"):
            List.append("働")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9E CF"):
            List.append("例")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9E D0"):
            List.append("志")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9E D1"):
            List.append("判")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9E D2"):
            List.append("冗")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9E D3"):
            List.append("官")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9E D4"):
            List.append("臨")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9E D5"):
            List.append("刻")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9E D6"):
            List.append("潜")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9E D7"):
            List.append("服")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9E D8"):
            List.append("余")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9E D9"):
            List.append("計")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9E DA"):
            List.append("争")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9E DB"):
            List.append("悲")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9E DC"):
            List.append("閉")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9E DD"):
            List.append("永")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9E DE"):
            List.append("耐")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9E DF"):
            List.append("移")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9E E0"):
            List.append("候")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9E E1"):
            List.append("習")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9E E2"):
            List.append("罪")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9E E3"):
            List.append("独")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9E E4"):
            List.append("昼")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9E E5"):
            List.append("反")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9E E6"):
            List.append("氷")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9E E7"):
            List.append("妻")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9E E8"):
            List.append("注")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9E E9"):
            List.append("表")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9E EA"):
            List.append("究")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9E EB"):
            List.append("徳")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9E EC"):
            List.append("刃")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9E ED"):
            List.append("倍")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9E EE"):
            List.append("洗")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9E EF"):
            List.append("缶")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9E F0"):
            List.append("押")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9E F1"):
            List.append("登")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9E F2"):
            List.append("提")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9E F3"):
            List.append("常")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9E F4"):
            List.append("刀")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9E F5"):
            List.append("怒")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9E F6"):
            List.append("才")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9E F7"):
            List.append("木")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9E F8"):
            List.append("彫")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9E F9"):
            List.append("夫")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9E FA"):
            List.append("婦")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9E FB"):
            List.append("花")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9E FC"):
            List.append("鳴")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9E FD"):
            List.append("祭")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9E FE"):
            List.append("騒")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9F 42"):
            List.append("況")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9F 43"):
            List.append("嫉")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9F 44"):
            List.append("妬")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9F 45"):
            List.append("借")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9F 46"):
            List.append("寄")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9F 47"):
            List.append("茶")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9F 48"):
            List.append("酒")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9F 49"):
            List.append("燃")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9F 4A"):
            List.append("投")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9F 4B"):
            List.append("希")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9F 4C"):
            List.append("費")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9F 4D"):
            List.append("並")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9F 4E"):
            List.append("喜")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9F 4F"):
            List.append("辺")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9F 50"):
            List.append("仔")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9F 51"):
            List.append("徴")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9F 52"):
            List.append("坊")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9F 53"):
            List.append("飼")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9F 54"):
            List.append("肖")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9F 55"):
            List.append("博")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9F 56"):
            List.append("天")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9F 57"):
            List.append("軍")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9F 58"):
            List.append("祖")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9F 59"):
            List.append("棚")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9F 5B"):
            List.append("講")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9F 5C"):
            List.append("呪")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9F 5D"):
            List.append("医")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9F 5E"):
            List.append("勉")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9F 5F"):
            List.append("布")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9F 60"):
            List.append("訪")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9F 61"):
            List.append("混")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9F 62"):
            List.append("侵")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9F 63"):
            List.append("疑")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9F 64"):
            List.append("儀")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9F 65"):
            List.append("努")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9F 66"):
            List.append("益")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9F 67"):
            List.append("門")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9F 68"):
            List.append("試")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9F 69"):
            List.append("厳")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9F 6A"):
            List.append("裏")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9F 6B"):
            List.append("腰")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9F 6C"):
            List.append("帥")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9F 6D"):
            List.append("封")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9F 6E"):
            List.append("柱")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9F 6F"):
            List.append("繋")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9F 70"):
            List.append("丘")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9F 71"):
            List.append("畑")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9F 72"):
            List.append("忍")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9F 73"):
            List.append("厄")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9F 74"):
            List.append("嫁")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9F 75"):
            List.append("展")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9F 76"):
            List.append("汗")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9F 77"):
            List.append("車")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9F 78"):
            List.append("接")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9F 79"):
            List.append("絹")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9F 7A"):
            List.append("肌")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9F 7B"):
            List.append("魂")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9F 7C"):
            List.append("票")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9F 7D"):
            List.append("橋")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9F 7E"):
            List.append("娘")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9F 80"):
            List.append("根")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9F 81"):
            List.append("怖")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9F 82"):
            List.append("幅")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9F 83"):
            List.append("衝")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9F 84"):
            List.append("射")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9F 85"):
            List.append("罠")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9F 86"):
            List.append("床")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9F 87"):
            List.append("丈")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9F 88"):
            List.append("区")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9F 89"):
            List.append("随")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9F 8A"):
            List.append("枝")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9F 8B"):
            List.append("古")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9F 8C"):
            List.append("頂")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9F 8D"):
            List.append("横")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9F 8E"):
            List.append("拾")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9F 8F"):
            List.append("良")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9F 90"):
            List.append("穫")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9F 91"):
            List.append("承")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9F 92"):
            List.append("森")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9F 93"):
            List.append("雑")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9F 94"):
            List.append("貨")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9F 95"):
            List.append("族")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9F 96"):
            List.append("省")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9F 97"):
            List.append("掃")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9F 98"):
            List.append("除")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9F 99"):
            List.append("粧")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9F 9A"):
            List.append("恥")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9F 9B"):
            List.append("濯")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9F 9C"):
            List.append("帯")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9F 9D"):
            List.append("策")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9F 9E"):
            List.append("裕")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9F 9F"):
            List.append("施")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9F A0"):
            List.append("営")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9F A1"):
            List.append("優")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9F A2"):
            List.append("骨")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9F A3"):
            List.append("埋")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9F A4"):
            List.append("躍")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9F A5"):
            List.append("冬")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9F A6"):
            List.append("遙")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9F A7"):
            List.append("圧")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9F A8"):
            List.append("迫")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9F A9"):
            List.append("獄")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9F AA"):
            List.append("再")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9F AB"):
            List.append("亡")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9F AC"):
            List.append("雨")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9F AD"):
            List.append("枯")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9F AE"):
            List.append("噴")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9F AF"):
            List.append("久")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9F B0"):
            List.append("衰")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9F B1"):
            List.append("鈍")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9F B2"):
            List.append("凍")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9F B3"):
            List.append("昇")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9F B4"):
            List.append("低")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9F B5"):
            List.append("砂")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9F B6"):
            List.append("含")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9F B7"):
            List.append("晶")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9F B8"):
            List.append("溜")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9F B9"):
            List.append("珠")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9F BA"):
            List.append("黄")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9F BB"):
            List.append("霊")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9F BC"):
            List.append("召")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9F BD"):
            List.append("喚")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9F BE"):
            List.append("蒼")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9F BF"):
            List.append("紅")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9F C0"):
            List.append("翠")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9F C1"):
            List.append("草")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9F C2"):
            List.append("種")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9F C3"):
            List.append("瓶")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9F C4"):
            List.append("鱗")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9F C5"):
            List.append("珍")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9F C6"):
            List.append("獣")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9F C7"):
            List.append("蓋")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9F C8"):
            List.append("鑑")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9F C9"):
            List.append("欠")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9F CA"):
            List.append("各")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9F CB"):
            List.append("煙")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9F CC"):
            List.append("筒")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9F CD"):
            List.append("造")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9F CE"):
            List.append("炭")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9F CF"):
            List.append("炉")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9F D0"):
            List.append("槽")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9F D1"):
            List.append("苗")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9F D2"):
            List.append("植")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9F D3"):
            List.append("周")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9F D4"):
            List.append("囲")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9F D5"):
            List.append("鍵")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9F D6"):
            List.append("級")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9F D7"):
            List.append("干")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9F D8"):
            List.append("匂")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9F D9"):
            List.append("涙")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9F DA"):
            List.append("球")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9F DB"):
            List.append("漬")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9F DC"):
            List.append("瓜")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9F DD"):
            List.append("臭")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9F DE"):
            List.append("毛")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9F DF"):
            List.append("芳")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9F E0"):
            List.append("皮")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9F E1"):
            List.append("丸")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9F E2"):
            List.append("牛")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9F E3"):
            List.append("乳")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9F E4"):
            List.append("酵")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9F E5"):
            List.append("胃")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9F E6"):
            List.append("腸")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9F E7"):
            List.append("炊")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9F E8"):
            List.append("穀")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9F E9"):
            List.append("農")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9F EA"):
            List.append("八")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9F EB"):
            List.append("孫")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9F EC"):
            List.append("柔")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9F ED"):
            List.append("麦")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9F EE"):
            List.append("粉")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9F EF"):
            List.append("般")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9F F0"):
            List.append("脂")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9F F1"):
            List.append("肪")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9F F2"):
            List.append("塊")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9F F3"):
            List.append("塗")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9F F4"):
            List.append("雅")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9F F5"):
            List.append("斬")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9F F6"):
            List.append("基")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9F F7"):
            List.append("偃")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9F F8"):
            List.append("厚")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9F F9"):
            List.append("雰")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9F FA"):
            List.append("典")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9F FB"):
            List.append("湾")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "9F FC"):
            List.append("鎌")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E0 40"):
            List.append("殺")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E0 41"):
            List.append("尾")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E0 42"):
            List.append("冠")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E0 43"):
            List.append("匠")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E0 44"):
            List.append("鍛")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E0 45"):
            List.append("旋")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E0 46"):
            List.append("誉")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E0 47"):
            List.append("炎")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E0 48"):
            List.append("竜")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E0 49"):
            List.append("爪")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E0 4A"):
            List.append("隼")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E0 4B"):
            List.append("紋")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E0 4C"):
            List.append("創")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E0 4D"):
            List.append("牙")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E0 4E"):
            List.append("岩")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E0 4F"):
            List.append("剛")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E0 50"):
            List.append("柩")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E0 51"):
            List.append("副")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E0 52"):
            List.append("葬")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E0 53"):
            List.append("鋼")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E0 54"):
            List.append("易")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E0 55"):
            List.append("裂")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E0 56"):
            List.append("妖")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E0 57"):
            List.append("稲")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E0 58"):
            List.append("慈")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E0 59"):
            List.append("忠")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E0 5A"):
            List.append("円")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E0 5B"):
            List.append("卓")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E0 5C"):
            List.append("帝")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E0 5E"):
            List.append("嵐")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E0 5F"):
            List.append("乙")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E0 60"):
            List.append("杖")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E0 61"):
            List.append("職")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E0 62"):
            List.append("殴")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E0 63"):
            List.append("権")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E0 64"):
            List.append("標")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E0 65"):
            List.append("笏")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E0 66"):
            List.append("狂")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E0 67"):
            List.append("節")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E0 68"):
            List.append("孔")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E0 69"):
            List.append("雀")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E0 6A"):
            List.append("如")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E0 6B"):
            List.append("角")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E0 6C"):
            List.append("青")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E0 6D"):
            List.append("紡")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E0 6E"):
            List.append("慟")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E0 6F"):
            List.append("哭")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E0 70"):
            List.append("銀")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E0 71"):
            List.append("左")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E0 72"):
            List.append("東")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E0 73"):
            List.append("蛮")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E0 74"):
            List.append("錫")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E0 75"):
            List.append("匹")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E0 76"):
            List.append("蛇")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E0 77"):
            List.append("祓")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E0 78"):
            List.append("詠")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E0 79"):
            List.append("唱")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E0 7A"):
            List.append("柄")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E0 7B"):
            List.append("斧")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E0 7C"):
            List.append("槍")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E0 7D"):
            List.append("槌")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E0 7E"):
            List.append("叉")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E0 80"):
            List.append("矛")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E0 81"):
            List.append("鉄")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E0 82"):
            List.append("陣")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E0 83"):
            List.append("賜")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E0 84"):
            List.append("堅")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E0 85"):
            List.append("固")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E0 86"):
            List.append("杭")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E0 87"):
            List.append("灰")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E0 88"):
            List.append("冶")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E0 89"):
            List.append("科")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E0 8A"):
            List.append("駆")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E0 8B"):
            List.append("逐")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E0 8C"):
            List.append("逸")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E0 8D"):
            List.append("骸")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E0 8E"):
            List.append("緑")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E0 8F"):
            List.append("薙")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E0 90"):
            List.append("傑")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E0 91"):
            List.append("狩")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E0 92"):
            List.append("弓")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E0 93"):
            List.append("弾")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E0 94"):
            List.append("扉")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E0 95"):
            List.append("貫")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E0 96"):
            List.append("鎧")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E0 97"):
            List.append("七")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E0 98"):
            List.append("軌")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E0 99"):
            List.append("吐")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E0 9A"):
            List.append("尽")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E0 9B"):
            List.append("浄")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E0 9C"):
            List.append("環")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E0 9D"):
            List.append("縫")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E0 9E"):
            List.append("板")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E0 9F"):
            List.append("糸")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E0 A0"):
            List.append("甲")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E0 A1"):
            List.append("殊")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E0 A2"):
            List.append("継")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E0 A3"):
            List.append("塞")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E0 A4"):
            List.append("赴")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E0 A5"):
            List.append("網")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E0 A6"):
            List.append("編")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E0 A7"):
            List.append("洋")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E0 A8"):
            List.append("島")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E0 A9"):
            List.append("巫")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E0 AA"):
            List.append("兜")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E0 AB"):
            List.append("頬")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E0 AC"):
            List.append("築")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E0 AD"):
            List.append("頑")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E0 AE"):
            List.append("漢")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E0 AF"):
            List.append("帽")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E0 B0"):
            List.append("薄")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E0 B1"):
            List.append("濃")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E0 B2"):
            List.append("愉")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E0 B3"):
            List.append("輪")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E0 B4"):
            List.append("及")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E0 B5"):
            List.append("喰")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E0 B6"):
            List.append("鮫")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E0 B7"):
            List.append("致")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E0 B8"):
            List.append("鉈")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E0 B9"):
            List.append("駄")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E0 BA"):
            List.append("篭")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E0 BB"):
            List.append("授")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E0 BC"):
            List.append("袋")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E0 BD"):
            List.append("瑠")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E0 BE"):
            List.append("璃")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E0 BF"):
            List.append("佐")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E0 C0"):
            List.append("賢")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E0 C1"):
            List.append("癒")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E0 C2"):
            List.append("偏")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E0 C3"):
            List.append("疾")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E0 C4"):
            List.append("巧")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E0 C5"):
            List.append("伴")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E0 C6"):
            List.append("徐")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E0 C7"):
            List.append("縞")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E0 C8"):
            List.append("瑪")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E0 C9"):
            List.append("瑙")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E0 CA"):
            List.append("験")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E0 CB"):
            List.append("華")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E0 CC"):
            List.append("姫")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E0 CD"):
            List.append("象")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E0 CE"):
            List.append("靴")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E0 CF"):
            List.append("膝")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E0 D0"):
            List.append("蹴")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E0 D1"):
            List.append("枠")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E0 D2"):
            List.append("謎")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E0 D3"):
            List.append("隣")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E0 D4"):
            List.append("徒")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E0 D5"):
            List.append("携")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E0 D6"):
            List.append("塵")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E0 D7"):
            List.append("繰")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E0 D8"):
            List.append("翔")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E0 D9"):
            List.append("閃")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E0 DA"):
            List.append("渦")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E0 DB"):
            List.append("纏")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E0 DC"):
            List.append("垂")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E0 DD"):
            List.append("屠")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E0 DE"):
            List.append("龍")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E0 DF"):
            List.append("叩")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E0 E0"):
            List.append("片")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E0 E1"):
            List.append("跳")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E0 E2"):
            List.append("招")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E0 E3"):
            List.append("規")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E0 E4"):
            List.append("模")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E0 E5"):
            List.append("雷")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E0 E6"):
            List.append("鐘")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E0 E7"):
            List.append("震")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E0 E8"):
            List.append("撼")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E0 E9"):
            List.append("範")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E0 EA"):
            List.append("複")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E0 EB"):
            List.append("弧")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E0 EC"):
            List.append("距")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E0 ED"):
            List.append("鉱")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E0 EE"):
            List.append("棺")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E0 EF"):
            List.append("焉")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E0 F0"):
            List.append("裁")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E0 F1"):
            List.append("漆")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E0 F2"):
            List.append("淵")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E0 F3"):
            List.append("系")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E0 F4"):
            List.append("列")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E0 F5"):
            List.append("限")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E0 F6"):
            List.append("控")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E0 F7"):
            List.append("満")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E0 F8"):
            List.append("隔")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E0 F9"):
            List.append("嘘")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E0 FA"):
            List.append("漏")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E0 FB"):
            List.append("披")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E0 FC"):
            List.append("露")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E1 40"):
            List.append("令")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E1 41"):
            List.append("抵")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E1 42"):
            List.append("抗")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E1 43"):
            List.append("痺")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E1 44"):
            List.append("僅")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E1 45"):
            List.append("延")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E1 46"):
            List.append("秒")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E1 47"):
            List.append("縛")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E1 48"):
            List.append("遭")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E1 49"):
            List.append("促")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E1 4A"):
            List.append("械")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E1 4B"):
            List.append("瀕")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E1 4C"):
            List.append("微")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E1 4D"):
            List.append("熊")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E1 4E"):
            List.append("洞")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E1 4F"):
            List.append("窟")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E1 50"):
            List.append("消")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E1 51"):
            List.append("三")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E1 52"):
            List.append("々")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E1 53"):
            List.append("★")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E1 54"):
            List.append("ｚ")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E1 55"):
            List.append("…")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E1 56"):
            List.append("壺")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E1 57"):
            List.append("鎚")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E1 58"):
            List.append("亜")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E1 59"):
            List.append("翼")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E1 5A"):
            List.append("殻")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E1 5B"):
            List.append("棲")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E1 5C"):
            List.append("爬")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E1 5D"):
            List.append("閲")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E1 5E"):
            List.append("覧")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E1 5F"):
            List.append("個")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E1 61"):
            List.append("削")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E1 62"):
            List.append("辞")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E1 63"):
            List.append("揺")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E1 64"):
            List.append("魅")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E1 65"):
            List.append("哀")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E1 66"):
            List.append("検")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E1 67"):
            List.append("還")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E1 68"):
            List.append("艇")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E1 69"):
            List.append("獲")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E1 6A"):
            List.append("憎")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E1 6B"):
            List.append("恵")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E1 6C"):
            List.append("稽")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E1 6D"):
            List.append("磨")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E1 6E"):
            List.append("銘")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E1 6F"):
            List.append("侍")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E1 70"):
            List.append("緊")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E1 71"):
            List.append("壺")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E1 72"):
            List.append("鎚")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E1 73"):
            List.append("亜")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E1 74"):
            List.append("翼")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E1 75"):
            List.append("殻")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E1 76"):
            List.append("棲")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E1 77"):
            List.append("爬")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E1 78"):
            List.append("閲")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E1 79"):
            List.append("覧")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E1 7A"):
            List.append("個")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E1 7B"):
            List.append("削")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E1 7C"):
            List.append("瞳")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E1 7D"):
            List.append("墜")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E1 7E"):
            List.append("燐")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E1 7F"):
            List.append("砲")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E1 81"):
            List.append("双")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E1 82"):
            List.append("拳")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E1 83"):
            List.append("覆")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E1 84"):
            List.append("推")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E1 85"):
            List.append("測")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E1 86"):
            List.append("貼")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E1 87"):
            List.append("触")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E1 88"):
            List.append("憶")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E1 89"):
            List.append("讃")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E1 8A"):
            List.append("非")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E1 8B"):
            List.append("握")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E1 8C"):
            List.append("映")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E1 8D"):
            List.append("写")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E1 8E"):
            List.append("渉")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E1 8F"):
            List.append("軸")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E1 90"):
            List.append("述")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E1 91"):
            List.append("粋")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E1 92"):
            List.append("妨")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E1 93"):
            List.append("吉")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E1 94"):
            List.append("鍋")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E1 95"):
            List.append("銅")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E1 96"):
            List.append("柳")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E1 97"):
            List.append("丁")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E1 98"):
            List.append("凶")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E1 99"):
            List.append("陽")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E1 9A"):
            List.append("河")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E1 9B"):
            List.append("脈")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E1 9C"):
            List.append("超")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E1 9D"):
            List.append("領")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E1 9E"):
            List.append("域")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E1 9F"):
            List.append("飯")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E1 A0"):
            List.append("寿")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E1 A1"):
            List.append("餓")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E1 A2"):
            List.append("司")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E1 A3"):
            List.append("荷")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E1 A4"):
            List.append("担")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E1 A5"):
            List.append("臓")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E1 A6"):
            List.append("ヶ")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E1 A7"):
            List.append("告")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E1 A8"):
            List.append("析")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E1 A9"):
            List.append("透")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E1 AA"):
            List.append("筋")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E1 AB"):
            List.append("励")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E1 AC"):
            List.append("看")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E1 AD"):
            List.append("皿")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E1 AE"):
            List.append("誌")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E1 AF"):
            List.append("碑")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E1 B0"):
            List.append("焚")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E1 B1"):
            List.append("萌")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E1 B2"):
            List.append("吼")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E1 B3"):
            List.append("齢")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E1 B4"):
            List.append("陛")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E1 B5"):
            List.append("姑")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E1 B6"):
            List.append("歓")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E1 B7"):
            List.append("挨")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E1 B8"):
            List.append("拶")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E1 B9"):
            List.append("繊")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E1 BA"):
            List.append("粛")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E1 BB"):
            List.append("専")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E1 BC"):
            List.append("己")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E1 BD"):
            List.append("紹")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E1 BE"):
            List.append("粗")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E1 BF"):
            List.append("往")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E1 C0"):
            List.append("郎")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E1 C1"):
            List.append("懸")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E1 C2"):
            List.append("逢")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E1 C3"):
            List.append("瀬")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E1 C4"):
            List.append("杯")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E1 C5"):
            List.append("岸")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E1 C6"):
            List.append("泳")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E1 C7"):
            List.append("詰")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E1 C8"):
            List.append("耗")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E1 C9"):
            List.append("酬")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E1 CA"):
            List.append("噛")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E1 CB"):
            List.append("虚")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E1 CC"):
            List.append("蓮")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E1 CD"):
            List.append("踊")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E1 CE"):
            List.append("拓")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E1 CF"):
            List.append("崇")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E1 D0"):
            List.append("伸")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E1 D1"):
            List.append("芝")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E1 D2"):
            List.append("脚")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E1 D3"):
            List.append("四")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E1 D4"):
            List.append("墓")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E1 D5"):
            List.append("駒")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E1 D6"):
            List.append("卑")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E1 D7"):
            List.append("劣")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E1 D8"):
            List.append("末")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E1 D9"):
            List.append("克")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E1 DA"):
            List.append("否")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E1 DB"):
            List.append("旗")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E1 DC"):
            List.append("秩")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E1 DD"):
            List.append("序")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E1 DE"):
            List.append("絆")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E1 DF"):
            List.append("酷")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E1 E0"):
            List.append("層")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E1 E1"):
            List.append("研")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E1 E2"):
            List.append("媒")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E1 E3"):
            List.append("閣")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E1 E4"):
            List.append("巡")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E1 E5"):
            List.append("駐")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E1 E6"):
            List.append("屯")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E1 E7"):
            List.append("挑")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E1 E8"):
            List.append("慎")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E1 E9"):
            List.append("臆")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E1 EA"):
            List.append("怯")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E1 EB"):
            List.append("揮")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E1 EC"):
            List.append("謹")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E1 ED"):
            List.append("誕")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E1 EE"):
            List.append("班")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E1 EF"):
            List.append("攪")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E1 F0"):
            List.append("戒")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E1 F1"):
            List.append("老")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E1 F2"):
            List.append("排")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E1 F3"):
            List.append("伏")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E1 F4"):
            List.append("刑")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E1 F5"):
            List.append("乾")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E1 F6"):
            List.append("陥")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E1 F7"):
            List.append("乞")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E1 F8"):
            List.append("至")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E1 F9"):
            List.append("聴")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E1 FA"):
            List.append("符")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E1 FB"):
            List.append("宣")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E1 FC"):
            List.append("脳")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E1 FD"):
            List.append("凌")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E2 41"):
            List.append("駕")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E2 42"):
            List.append("歪")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E2 43"):
            List.append("ｍ")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E2 44"):
            List.append("ｋ")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E2 45"):
            List.append("ｇ")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E2 46"):
            List.append("把")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E2 47"):
            List.append("漠")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E2 48"):
            List.append("隆")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E2 49"):
            List.append("録")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E2 4A"):
            List.append("徹")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E2 4B"):
            List.append("氏")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E2 4C"):
            List.append("撹")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E2 4D"):
            List.append("阻")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E2 4E"):
            List.append("渇")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E2 4F"):
            List.append("讐")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E2 50"):
            List.append("恨")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E2 51"):
            List.append("却")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E2 52"):
            List.append("顛")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E2 53"):
            List.append("岐")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E2 54"):
            List.append("哲")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E2 55"):
            List.append("凝")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E2 56"):
            List.append("彗")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E2 57"):
            List.append("膨")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E2 58"):
            List.append("陰")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E2 59"):
            List.append("謀")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E2 5B"):
            List.append("川")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E2 5C"):
            List.append("沿")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E2 5D"):
            List.append("泉")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E2 5E"):
            List.append("犬")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E2 5F"):
            List.append("璧")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E2 60"):
            List.append("傲")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E2 61"):
            List.append("慢")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E2 62"):
            List.append("鹿")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E2 63"):
            List.append("委")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E2 64"):
            List.append("憩")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E2 65"):
            List.append("扇")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E2 66"):
            List.append("給")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E2 67"):
            List.append("冑")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E2 68"):
            List.append("宮")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E2 69"):
            List.append("紫")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E2 6A"):
            List.append("燭")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E2 6B"):
            List.append("灯")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E2 6C"):
            List.append("憐")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E2 6D"):
            List.append("舗")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E2 6E"):
            List.append("菌")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E2 6F"):
            List.append("課")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E2 70"):
            List.append("庭")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E2 71"):
            List.append("衆")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E2 72"):
            List.append("厨")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E2 73"):
            List.append("遥")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E2 74"):
            List.append("仙")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E2 75"):
            List.append("央")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E2 76"):
            List.append("湯")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E2 77"):
            List.append("呂")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E2 78"):
            List.append("浸")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E2 79"):
            List.append("寺")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E2 7B"):
            List.append("挿")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E2 7C"):
            List.append("昏")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E2 7D"):
            List.append("為")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E2 7E"):
            List.append("刷")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E2 7F"):
            List.append("暑")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E2 80"):
            List.append("季")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E2 81"):
            List.append("償")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E2 82"):
            List.append("奴")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E2 83"):
            List.append("捜")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E2 84"):
            List.append("財")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E2 85"):
            List.append("奉")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E2 86"):
            List.append("師")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E2 87"):
            List.append("購")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E2 88"):
            List.append("療")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E2 89"):
            List.append("池")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E2 8A"):
            List.append("羅")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E2 8B"):
            List.append("憂")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E2 8C"):
            List.append("評")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E2 8D"):
            List.append("噌")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E2 8E"):
            List.append("轟")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E2 8F"):
            List.append("五")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E2 90"):
            List.append("縦")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E2 91"):
            List.append("輩")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E2 92"):
            List.append("勅")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E2 93"):
            List.append("請")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E2 94"):
            List.append("棄")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E2 95"):
            List.append("惧")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E2 96"):
            List.append("監")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E2 97"):
            List.append("滝")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E2 98"):
            List.append("銭")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E2 99"):
            List.append("奮")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E2 9A"):
            List.append("純")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E2 9B"):
            List.append("塹")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E2 9C"):
            List.append("壕")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E2 9D"):
            List.append("郭")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E2 9E"):
            List.append("貯")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E2 9F"):
            List.append("蔵")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E2 A0"):
            List.append("斉")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E2 A1"):
            List.append("維")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E2 A2"):
            List.append("校")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E2 A3"):
            List.append("錬")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E2 A4"):
            List.append("挺")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E2 A5"):
            List.append("猟")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E2 A6"):
            List.append("尉")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E2 A7"):
            List.append("佳")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E2 A8"):
            List.append("慌")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E2 A9"):
            List.append("遂")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E2 AA"):
            List.append("凄")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E2 AB"):
            List.append("炸")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E2 AC"):
            List.append("昌")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E2 AD"):
            List.append("耕")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E2 AE"):
            List.append("批")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E2 AF"):
            List.append("宗")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E2 B0"):
            List.append("爺")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E2 B1"):
            List.append("礎")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E2 B2"):
            List.append("糧")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E2 B3"):
            List.append("蓄")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E2 B4"):
            List.append("輸")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E2 B5"):
            List.append("艦")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E2 B6"):
            List.append("搭")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E2 B7"):
            List.append("載")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E2 B8"):
            List.append("勧")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E2 B9"):
            List.append("卒")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E2 BA"):
            List.append("噂")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E2 BB"):
            List.append("湖")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E2 BC"):
            List.append("宅")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E2 BD"):
            List.append("勤")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E2 BE"):
            List.append("猛")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E2 BF"):
            List.append("皆")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E2 C0"):
            List.append("潔")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E2 C1"):
            List.append("鏡")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E2 C2"):
            List.append("麗")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E2 C3"):
            List.append("曹")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E2 C4"):
            List.append("玄")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E2 C5"):
            List.append("寂")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E2 C6"):
            List.append("壇")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E2 C7"):
            List.append("堕")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E2 C8"):
            List.append("架")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E2 C9"):
            List.append("擬")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E2 CA"):
            List.append("銃")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E2 CB"):
            List.append("貢")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E2 CC"):
            List.append("献")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E2 CD"):
            List.append("砦")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E2 CE"):
            List.append("隅")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E2 CF"):
            List.append("詩")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E2 D0"):
            List.append("吟")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E2 D1"):
            List.append("著")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E2 D2"):
            List.append("膠")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E2 D3"):
            List.append("占")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E2 D4"):
            List.append("百")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E2 D5"):
            List.append("傘")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E2 D6"):
            List.append("敢")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E2 D7"):
            List.append("惨")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E2 D8"):
            List.append("索")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E2 D9"):
            List.append("樹")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E2 DA"):
            List.append("林")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E2 DB"):
            List.append("遮")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E2 DC"):
            List.append("涼")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E2 DD"):
            List.append("粒")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E2 DE"):
            List.append("拍")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E2 DF"):
            List.append("楼")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E2 E0"):
            List.append("鎮")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E2 E1"):
            List.append("牧")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E2 E2"):
            List.append("朴")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E2 E3"):
            List.append("盾")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E2 E4"):
            List.append("核")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E2 E5"):
            List.append("皇")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E2 E6"):
            List.append("律")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E2 E7"):
            List.append("倶")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E2 E8"):
            List.append("幽")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E2 E9"):
            List.append("某")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E2 EA"):
            List.append("淑")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E2 EB"):
            List.append("六")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E2 EC"):
            List.append("冥")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E2 ED"):
            List.append("井")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E2 EE"):
            List.append("戸")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E2 EF"):
            List.append("懐")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E2 F0"):
            List.append("充")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E2 F1"):
            List.append("軟")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E2 F2"):
            List.append("冊")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E2 F3"):
            List.append("僚")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E2 F4"):
            List.append("弁")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E2 F5"):
            List.append("詞")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E2 F6"):
            List.append("督")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E2 F7"):
            List.append("滞")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E2 F8"):
            List.append("慕")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E2 F9"):
            List.append("嘆")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E2 FA"):
            List.append("溶")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E2 FB"):
            List.append("卸")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E2 FC"):
            List.append("兼")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E2 FD"):
            List.append("晰")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E2 FE"):
            List.append("煥")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E2 FF"):
            List.append("凡")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E3 43"):
            List.append("釣")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E3 44"):
            List.append("秋")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E3 45"):
            List.append("洒")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E3 46"):
            List.append("羊")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E3 47"):
            List.append("呑")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E3 48"):
            List.append("禄")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E3 49"):
            List.append("狭")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E3 4A"):
            List.append("童")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E3 4B"):
            List.append("贅")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E3 4C"):
            List.append("沢")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E3 4D"):
            List.append("需")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E3 4E"):
            List.append("滑")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E3 4F"):
            List.append("額")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E3 50"):
            List.append("袖")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E3 51"):
            List.append("販")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E3 52"):
            List.append("帳")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E3 53"):
            List.append("簿")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E3 54"):
            List.append("掠")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E3 55"):
            List.append("陶")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E3 56"):
            List.append("偵")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E3 57"):
            List.append("患")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E3 58"):
            List.append("症")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E3 59"):
            List.append("咲")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E3 5A"):
            List.append("煎")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E3 5B"):
            List.append("俊")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E3 5C"):
            List.append("版")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E3 5E"):
            List.append("又")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E3 5F"):
            List.append("逝")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E3 60"):
            List.append("鎖")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E3 61"):
            List.append("猿")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E3 62"):
            List.append("窓")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E3 63"):
            List.append("慨")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E3 64"):
            List.append("俗")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E3 65"):
            List.append("睨")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E3 66"):
            List.append("競")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E3 67"):
            List.append("紳")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E3 68"):
            List.append("浪")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E3 69"):
            List.append("癖")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E3 6A"):
            List.append("掴")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E3 6B"):
            List.append("惚")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E3 6C"):
            List.append("執")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E3 6D"):
            List.append("彷")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E3 6E"):
            List.append("徨")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E3 6F"):
            List.append("楚")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E3 70"):
            List.append("尋")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E3 71"):
            List.append("釈")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E3 72"):
            List.append("札")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E3 73"):
            List.append("秀")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E3 74"):
            List.append("肥")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E3 75"):
            List.append("雌")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E3 76"):
            List.append("飢")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E3 77"):
            List.append("繕")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E3 78"):
            List.append("姓")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E3 79"):
            List.append("墨")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E3 7A"):
            List.append("慰")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E3 7B"):
            List.append("飽")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E3 7C"):
            List.append("概")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E3 7D"):
            List.append("免")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E3 7E"):
            List.append("疫")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E3 7F"):
            List.append("泥")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E3 81"):
            List.append("尻")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E3 82"):
            List.append("脇")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E3 83"):
            List.append("蒸")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E3 84"):
            List.append("湿")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E3 85"):
            List.append("澄")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E3 86"):
            List.append("征")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E3 87"):
            List.append("締")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E3 88"):
            List.append("春")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E3 89"):
            List.append("曇")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E3 8A"):
            List.append("捉")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E3 8B"):
            List.append("剖")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E3 8C"):
            List.append("謙")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E3 8D"):
            List.append("群")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E3 8E"):
            List.append("暇")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E3 8F"):
            List.append("焦")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E3 90"):
            List.append("妥")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E3 91"):
            List.append("俄")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E3 92"):
            List.append("逮")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E3 93"):
            List.append("拘")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E3 94"):
            List.append("脅")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E3 95"):
            List.append("潤")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E3 96"):
            List.append("譲")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E3 97"):
            List.append("肺")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E3 98"):
            List.append("涯")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E3 99"):
            List.append("摘")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E3 9A"):
            List.append("芽")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E3 9B"):
            List.append("九")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E3 9C"):
            List.append("撤")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E3 9D"):
            List.append("勘")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E3 9E"):
            List.append("融")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E3 9F"):
            List.append("賭")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E3 A0"):
            List.append("傾")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E3 A1"):
            List.append("匿")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E3 A2"):
            List.append("誠")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E3 A3"):
            List.append("‥")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E3 A4"):
            List.append("叔")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E3 A5"):
            List.append("浜")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E3 A6"):
            List.append("席")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E3 A7"):
            List.append("彩")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E3 A8"):
            List.append("頻")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E3 A9"):
            List.append("壮")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E3 AA"):
            List.append("液")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E3 AB"):
            List.append("墟")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E3 AC"):
            List.append("谷")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E3 AD"):
            List.append("膳")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E3 AE"):
            List.append("仁")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E3 AF"):
            List.append("盆")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E3 B0"):
            List.append("栽")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E3 B1"):
            List.append("培")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E3 B2"):
            List.append("欄")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E3 B3"):
            List.append("鬼")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E3 B4"):
            List.append("縄")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E3 B5"):
            List.append("梯")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E3 B6"):
            List.append("籠")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E3 B7"):
            List.append("京")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E3 B8"):
            List.append("凛")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E3 B9"):
            List.append("刊")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E3 BA"):
            List.append("漫")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E3 BB"):
            List.append("琢")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E3 BC"):
            List.append("刊")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E3 BD"):
            List.append("漫")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E3 BE"):
            List.append("摩")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E3 BF"):
            List.append("煉")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E3 C0"):
            List.append("刹")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E3 C1"):
            List.append("伯")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E3 C2"):
            List.append("蚊")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E3 C3"):
            List.append("脆")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E3 C4"):
            List.append("餌")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E3 C5"):
            List.append("桃")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E3 C6"):
            List.append("廷")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E3 C7"):
            List.append("掲")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E3 C8"):
            List.append("疎")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E3 C9"):
            List.append("沌")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E3 CA"):
            List.append("菓")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E3 CB"):
            List.append("翌")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E3 CC"):
            List.append("愕")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E3 CD"):
            List.append("釜")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E3 CE"):
            List.append("茹")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E3 CF"):
            List.append("針")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E3 D0"):
            List.append("沼")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E3 D1"):
            List.append("紀")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E3 D2"):
            List.append("礁")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E3 D3"):
            List.append("菓")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E3 D4"):
            List.append("寧")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E3 D5"):
            List.append("聡")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E3 D6"):
            List.append("舌")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E3 D7"):
            List.append("菓")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E3 D8"):
            List.append("畳")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E3 D9"):
            List.append("懲")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E3 DA"):
            List.append("契")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E3 DB"):
            List.append("肢")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E3 DC"):
            List.append("藤")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E3 DD"):
            List.append("α")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E3 DE"):
            List.append("β")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E3 DF"):
            List.append("禍")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E3 E0"):
            List.append("壷")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E3 E1"):
            List.append("馴")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E3 E2"):
            List.append("樺")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E3 E3"):
            List.append("貰")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E3 E4"):
            List.append("馳")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E3 E5"):
            List.append("掟")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E3 E6"):
            List.append("懇")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E3 E7"):
            List.append("嬉")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E3 E8"):
            List.append("挫")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E3 E9"):
            List.append("松")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E3 EA"):
            List.append("鼓")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E3 EB"):
            List.append("較")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E3 EC"):
            List.append("亀")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E3 ED"):
            List.append("貿")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E3 EE"):
            List.append("綿")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E3 EF"):
            List.append("邸")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E3 F0"):
            List.append("雇")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E3 F1"):
            List.append("烏")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E3 F2"):
            List.append("唄")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E3 F3"):
            List.append("剃")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E3 F4"):
            List.append("稿")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E3 F5"):
            List.append("椅")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E3 F6"):
            List.append("旺")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E3 F7"):
            List.append("託")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E3 F8"):
            List.append("盟")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E3 F9"):
            List.append("虐")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E3 FA"):
            List.append("覗")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E3 FB"):
            List.append("戯")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E3 FC"):
            List.append("撮")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E3 FD"):
            List.append("ヱ")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E4 41"):
            List.append("泡")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E4 42"):
            List.append("隕")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E4 43"):
            List.append("磁")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E4 44"):
            List.append("洩")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E4 45"):
            List.append("窃")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E4 46"):
            List.append("滴")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E4 47"):
            List.append("虎")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E4 48"):
            List.append("怨")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E4 49"):
            List.append("凱")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E4 4A"):
            List.append("旦")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E4 4B"):
            List.append("那")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E4 4C"):
            List.append("崖")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E4 4D"):
            List.append("ｅ")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E4 4E"):
            List.append("ｙ")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E4 4F"):
            List.append("ｔ")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E4 50"):
            List.append("ｏ")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E4 51"):
            List.append("ｙ")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E4 52"):
            List.append("ｈ")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E4 53"):
            List.append("ｅ")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E4 54"):
            List.append("ａ")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E4 55"):
            List.append("ｒ")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E4 56"):
            List.append("ｔ")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E4 57"):
            List.append("妄")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E4 58"):
            List.append("鼬")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E4 59"):
            List.append("也")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E4 5A"):
            List.append("貌")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E4 5B"):
            List.append("髭")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E4 5C"):
            List.append("紛")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E4 5E"):
            List.append("盤")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E4 5F"):
            List.append("苛")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E4 60"):
            List.append("碧")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E4 61"):
            List.append("桜")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E4 62"):
            List.append("丼")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E4 63"):
            List.append("迅")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E4 64"):
            List.append("州")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E4 65"):
            List.append("燥")
        elif(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4] == "E4 66"):
            List.append("軒")
        else:
            List.append(str(Hex[i] + Hex[i+1] + " " + Hex[i+3] + Hex[i+4]))
    return "".join(List)
