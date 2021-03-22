def jHex(word):
    jap = list(word)
    List = []
    for i in jap:
        if i == "　":
            List.append("9940")
        elif i == "，":
            List.append("9941")
        elif i == "．":
            List.append("9942")
        elif i == "・":
            List.append("9943")
        elif i == "：":
            List.append("9944")
        elif i == "？":
            List.append("9945")
        elif i == "！":
            List.append("9946")
        elif i == "ー":
            List.append("9947")
        elif i == "／":
            List.append("9948")
        elif i == "”":
            List.append("9949")
        elif i == "（":
            List.append("994A")
        elif i == "）":
            List.append("994B")
        elif i == "％":
            List.append("994C")
        elif i == "０":
            List.append("994D")
        elif i == "１":
            List.append("994E")
        elif i == "２":
            List.append("994F")
        elif i == "３":
            List.append("9950")
        elif i == "４":
            List.append("9951")
        elif i == "５":
            List.append("9952")
        elif i == "６":
            List.append("9953")
        elif i == "７":
            List.append("9954")
        elif i == "８":
            List.append("9955")
        elif i == "９":
            List.append("9956")
        elif i == "Ａ":
            List.append("9957")
        elif i == "Ｂ":
            List.append("9958")
        elif i == "Ｃ":
            List.append("9959")
        elif i == "Ｄ":
            List.append("995A")
        elif i == "Ｅ":
            List.append("995B")
        elif i == "Ｆ":
            List.append("995C")
        elif i == "Ｇ":
            List.append("995E")
        elif i == "Ｈ":
            List.append("995F")
        elif i == "Ｉ":
            List.append("9960")
        elif i == "Ｊ":
            List.append("9961")
        elif i == "Ｋ":
            List.append("9962")
        elif i == "Ｌ":
            List.append("9963")
        elif i == "Ｍ":
            List.append("9964")
        elif i == "Ｎ":
            List.append("9965")
        elif i == "Ｏ":
            List.append("9966")
        elif i == "Ｐ":
            List.append("9967")
        elif i == "Ｑ":
            List.append("9968")
        elif i == "Ｒ":
            List.append("9969")
        elif i == "Ｓ":
            List.append("996A")
        elif i == "Ｔ":
            List.append("996B")
        elif i == "Ｕ":
            List.append("996C")
        elif i == "Ｖ":
            List.append("996D")
        elif i == "Ｗ":
            List.append("996E")
        elif i == "Ｘ":
            List.append("996F")
        elif i == "Ｙ":
            List.append("9970")
        elif i == "Ｚ":
            List.append("9971")
        elif i == "ぁ":
            List.append("9972")
        elif i == "あ":
            List.append("9973")
        elif i == "ぃ":
            List.append("9974")
        elif i == "い":
            List.append("9975")
        elif i == "ぅ":
            List.append("9976")
        elif i == "う":
            List.append("9977")
        elif i == "ぇ":
            List.append("9978")
        elif i == "え":
            List.append("9979")
        elif i == "ぉ":
            List.append("997A")
        elif i == "お":
            List.append("997B")
        elif i == "か":
            List.append("997C")
        elif i == "が":
            List.append("997D")
        elif i == "き":
            List.append("997E")
        elif i == "ぎ":
            List.append("9980")
        elif i == "く":
            List.append("9981")
        elif i == "ぐ":
            List.append("9982")
        elif i == "け":
            List.append("9983")
        elif i == "げ":
            List.append("9984")
        elif i == "こ":
            List.append("9985")
        elif i == "ご":
            List.append("9986")
        elif i == "さ":
            List.append("9987")
        elif i == "ざ":
            List.append("9988")
        elif i == "し":
            List.append("9989")
        elif i == "じ":
            List.append("998A")
        elif i == "す":
            List.append("998B")
        elif i == "ず":
            List.append("998C")
        elif i == "せ":
            List.append("998D")
        elif i == "ぜ":
            List.append("998E")
        elif i == "そ":
            List.append("998F")
        elif i == "ぞ":
            List.append("9990")
        elif i == "た":
            List.append("9991")
        elif i == "だ":
            List.append("9992")
        elif i == "ち":
            List.append("9993")
        elif i == "ぢ":
            List.append("9994")
        elif i == "っ":
            List.append("9995")
        elif i == "つ":
            List.append("9996")
        elif i == "づ":
            List.append("9997")
        elif i == "て":
            List.append("9998")
        elif i == "で":
            List.append("9999")
        elif i == "と":
            List.append("999A")
        elif i == "ど":
            List.append("999B")
        elif i == "な":
            List.append("999C")
        elif i == "に":
            List.append("999D")
        elif i == "ぬ":
            List.append("999E")
        elif i == "ね":
            List.append("999F")
        elif i == "の":
            List.append("99A0")
        elif i == "は":
            List.append("99A1")
        elif i == "ば":
            List.append("99A2")
        elif i == "ぱ":
            List.append("99A3")
        elif i == "ひ":
            List.append("99A4")
        elif i == "び":
            List.append("99A5")
        elif i == "ぴ":
            List.append("99A6")
        elif i == "ふ":
            List.append("99A7")
        elif i == "ぶ":
            List.append("99A8")
        elif i == "ぷ":
            List.append("99A9")
        elif i == "へ":
            List.append("99AA")
        elif i == "べ":
            List.append("99AB")
        elif i == "ぺ":
            List.append("99AC")
        elif i == "ほ":
            List.append("99AD")
        elif i == "ぼ":
            List.append("99AE")
        elif i == "ぽ":
            List.append("99AF")
        elif i == "ま":
            List.append("99B0")
        elif i == "み":
            List.append("99B1")
        elif i == "む":
            List.append("99B2")
        elif i == "め":
            List.append("99B3")
        elif i == "も":
            List.append("99B4")
        elif i == "ゃ":
            List.append("99B5")
        elif i == "や":
            List.append("99B6")
        elif i == "ゅ":
            List.append("99B7")
        elif i == "ゆ":
            List.append("99B8")
        elif i == "ょ":
            List.append("99B9")
        elif i == "よ":
            List.append("99BA")
        elif i == "ら":
            List.append("99BB")
        elif i == "り":
            List.append("99BC")
        elif i == "る":
            List.append("99BD")
        elif i == "れ":
            List.append("99BE")
        elif i == "ろ":
            List.append("99BF")
        elif i == "ゎ":
            List.append("99C0")
        elif i == "わ":
            List.append("99C1")
        elif i == "ゐ":
            List.append("99C2")
        elif i == "ゑ":
            List.append("99C3")
        elif i == "を":
            List.append("99C4")
        elif i == "ん":
            List.append("99C5")
        elif i == "ァ":
            List.append("99C6")
        elif i == "ア":
            List.append("99C7")
        elif i == "ィ":
            List.append("99C8")
        elif i == "イ":
            List.append("99C9")
        elif i == "ゥ":
            List.append("99CA")
        elif i == "ウ":
            List.append("99CB")
        elif i == "ェ":
            List.append("99CC")
        elif i == "エ":
            List.append("99CD")
        elif i == "ォ":
            List.append("99CE")
        elif i == "オ":
            List.append("99CF")
        elif i == "カ":
            List.append("99D0")
        elif i == "ガ":
            List.append("99D1")
        elif i == "キ":
            List.append("99D2")
        elif i == "ギ":
            List.append("99D3")
        elif i == "ク":
            List.append("99D4")
        elif i == "グ":
            List.append("99D5")
        elif i == "ケ":
            List.append("99D6")
        elif i == "ゲ":
            List.append("99D7")
        elif i == "コ":
            List.append("99D8")
        elif i == "ゴ":
            List.append("99D9")
        elif i == "サ":
            List.append("99DA")
        elif i == "ザ":
            List.append("99DB")
        elif i == "シ":
            List.append("99DC")
        elif i == "ジ":
            List.append("99DD")
        elif i == "ス":
            List.append("99DE")
        elif i == "ズ":
            List.append("99DF")
        elif i == "セ":
            List.append("99E0")
        elif i == "ゼ":
            List.append("99E1")
        elif i == "ソ":
            List.append("99E2")
        elif i == "ゾ":
            List.append("99E3")
        elif i == "タ":
            List.append("99E4")
        elif i == "ダ":
            List.append("99E5")
        elif i == "チ":
            List.append("99E6")
        elif i == "ヂ":
            List.append("99E7")
        elif i == "ッ":
            List.append("99E8")
        elif i == "ツ":
            List.append("99E9")
        elif i == "ヅ":
            List.append("99EA")
        elif i == "テ":
            List.append("99EB")
        elif i == "デ":
            List.append("99EC")
        elif i == "ト":
            List.append("99ED")
        elif i == "ド":
            List.append("99EE")
        elif i == "ナ":
            List.append("99EF")
        elif i == "ニ":
            List.append("99F0")
        elif i == "ヌ":
            List.append("99F1")
        elif i == "ネ":
            List.append("99F2")
        elif i == "ノ":
            List.append("99F3")
        elif i == "ハ":
            List.append("99F4")
        elif i == "バ":
            List.append("99F5")
        elif i == "パ":
            List.append("99F6")
        elif i == "ヒ":
            List.append("99F7")
        elif i == "ビ":
            List.append("99F8")
        elif i == "ピ":
            List.append("99F9")
        elif i == "フ":
            List.append("99FA")
        elif i == "ブ":
            List.append("99FB")
        elif i == "プ":
            List.append("99FC")
        elif i == "ヘ":
            List.append("9A40")
        elif i == "ベ":
            List.append("9A41")
        elif i == "ペ":
            List.append("9A42")
        elif i == "ホ":
            List.append("9A43")
        elif i == "ボ":
            List.append("9A44")
        elif i == "ポ":
            List.append("9A45")
        elif i == "マ":
            List.append("9A46")
        elif i == "ミ":
            List.append("9A47")
        elif i == "＆":
            List.append("9A48")
        elif i == "ム":
            List.append("9A49")
        elif i == "メ":
            List.append("9A4A")
        elif i == "モ":
            List.append("9A4B")
        elif i == "ャ":
            List.append("9A4C")
        elif i == "ヤ":
            List.append("9A4D")
        elif i == "ュ":
            List.append("9A4E")
        elif i == "ユ":
            List.append("9A4F")
        elif i == "ョ":
            List.append("9A50")
        elif i == "ヨ":
            List.append("9A51")
        elif i == "ラ":
            List.append("9A52")
        elif i == "リ":
            List.append("9A53")
        elif i == "ル":
            List.append("9A54")
        elif i == "レ":
            List.append("9A55")
        elif i == "ロ":
            List.append("9A56")
        elif i == "?":
            List.append("9A57")
        elif i == "ワ":
            List.append("9A58")
        elif i == "＝":
            List.append("9A59")
        elif i == "☆":
            List.append("9A5A")
        elif i == "ヲ":
            List.append("9A5B")
        elif i == "ン":
            List.append("9A5D")
        elif i == "ヴ":
            List.append("9A5E")
        elif i == "△":
            List.append("9A7A")
        elif i == "○":
            List.append("9A7B")
        elif i == "×":
            List.append("9A7C")
        elif i == "＜":
            List.append("9A7D")
        elif i == "＞":
            List.append("9A7E")
        elif i == "♪":
            List.append("9A80")
        elif i == "?":
            List.append("9A81")
        elif i == "▽":
            List.append("9A82")
        elif i == "『":
            List.append("9A83")
        elif i == "』":
            List.append("9A84")
        elif i == "、":
            List.append("9A85")
        elif i == "。":
            List.append("9A86")
        elif i == "一":
            List.append("9A87")
        elif i == "二":
            List.append("9A88")
        elif i == "十":
            List.append("9A89")
        elif i == "千":
            List.append("9A8A")
        elif i == "万":
            List.append("9A8B")
        elif i == "地":
            List.append("9A8C")
        elif i == "水":
            List.append("9A8D")
        elif i == "火":
            List.append("9A8E")
        elif i == "風":
            List.append("9A8F")
        elif i == "光":
            List.append("9A90")
        elif i == "闇":
            List.append("9A91")
        elif i == "南":
            List.append("9A92")
        elif i == "西":
            List.append("9A93")
        elif i == "北":
            List.append("9A94")
        elif i == "赤":
            List.append("9A95")
        elif i == "白":
            List.append("9A96")
        elif i == "黒":
            List.append("9A97")
        elif i == "年":
            List.append("9A98")
        elif i == "月":
            List.append("9A99")
        elif i == "日":
            List.append("9A9A")
        elif i == "時":
            List.append("9A9B")
        elif i == "戦":
            List.append("9A9C")
        elif i == "闘":
            List.append("9A9D")
        elif i == "攻":
            List.append("9A9E")
        elif i == "撃":
            List.append("9A9F")
        elif i == "防":
            List.append("9AA0")
        elif i == "御":
            List.append("9AA1")
        elif i == "回":
            List.append("9AA2")
        elif i == "避":
            List.append("9AA3")
        elif i == "術":
            List.append("9AA4")
        elif i == "技":
            List.append("9AA5")
        elif i == "道":
            List.append("9AA6")
        elif i == "具":
            List.append("9AA7")
        elif i == "合":
            List.append("9AA8")
        elif i == "成":
            List.append("9AA9")
        elif i == "神":
            List.append("9AAA")
        elif i == "座":
            List.append("9AAB")
        elif i == "都":
            List.append("9AAC")
        elif i == "市":
            List.append("9AAD")
        elif i == "格":
            List.append("9AAE")
        elif i == "先":
            List.append("9AAF")
        elif i == "行":
            List.append("9AB0")
        elif i == "世":
            List.append("9AB1")
        elif i == "楽":
            List.append("9AB2")
        elif i == "園":
            List.append("9AB3")
        elif i == "案":
            List.append("9AB4")
        elif i == "外":
            List.append("9AB5")
        elif i == "所":
            List.append("9AB6")
        elif i == "知":
            List.append("9AB7")
        elif i == "大":
            List.append("9AB8")
        elif i == "昔":
            List.append("9AB9")
        elif i == "人":
            List.append("9ABA")
        elif i == "間":
            List.append("9ABB")
        elif i == "自":
            List.append("9ABC")
        elif i == "分":
            List.append("9ABD")
        elif i == "生":
            List.append("9ABE")
        elif i == "毎":
            List.append("9ABF")
        elif i == "祈":
            List.append("9AC0")
        elif i == "決":
            List.append("9AC1")
        elif i == "上":
            List.append("9AC2")
        elif i == "降":
            List.append("9AC3")
        elif i == "今":
            List.append("9AC4")
        elif i == "度":
            List.append("9AC5")
        elif i == "来":
            List.append("9AC6")
        elif i == "待":
            List.append("9AC7")
        elif i == "乗":
            List.append("9AC8")
        elif i == "空":
            List.append("9AC9")
        elif i == "何":
            List.append("9ACA")
        elif i == "手":
            List.append("9ACB")
        elif i == "入":
            List.append("9ACC")
        elif i == "以":
            List.append("9ACD")
        elif i == "持":
            List.append("9ACE")
        elif i == "武":
            List.append("9ACF")
        elif i == "器":
            List.append("9AD0")
        elif i == "屋":
            List.append("9AD1")
        elif i == "教":
            List.append("9AD2")
        elif i == "会":
            List.append("9AD3")
        elif i == "食":
            List.append("9AD4")
        elif i == "材":
            List.append("9AD5")
        elif i == "宿":
            List.append("9AD6")
        elif i == "客":
            List.append("9AD7")
        elif i == "室":
            List.append("9AD8")
        elif i == "階":
            List.append("9AD9")
        elif i == "廊":
            List.append("9ADA")
        elif i == "下":
            List.append("9ADB")
        elif i == "変":
            List.append("9ADC")
        elif i == "第":
            List.append("9ADD")
        elif i == "章":
            List.append("9ADE")
        elif i == "代":
            List.append("9ADF")
        elif i == "更":
            List.append("9AE0")
        elif i == "広":
            List.append("9AE1")
        elif i == "場":
            List.append("9AE2")
        elif i == "旧":
            List.append("9AE3")
        elif i == "街":
            List.append("9AE4")
        elif i == "前":
            List.append("9AE5")
        elif i == "悪":
            List.append("9AE6")
        elif i == "夢":
            List.append("9AE7")
        elif i == "帰":
            List.append("9AE8")
        elif i == "王":
            List.append("9AE9")
        elif i == "開":
            List.append("9AEA")
        elif i == "放":
            List.append("9AEB")
        elif i == "土":
            List.append("9AEC")
        elif i == "新":
            List.append("9AED")
        elif i == "活":
            List.append("9AEE")
        elif i == "気":
            List.append("9AEF")
        elif i == "住":
            List.append("9AF0")
        elif i == "恩":
            List.append("9AF1")
        elif i == "最":
            List.append("9AF2")
        elif i == "近":
            List.append("9AF3")
        elif i == "国":
            List.append("9AF4")
        elif i == "団":
            List.append("9AF5")
        elif i == "進":
            List.append("9AF6")
        elif i == "出":
            List.append("9AF7")
        elif i == "信":
            List.append("9AF8")
        elif i == "助":
            List.append("9AF9")
        elif i == "話":
            List.append("9AFA")
        elif i == "顔":
            List.append("9AFB")
        elif i == "心":
            List.append("9AFC")
        elif i == "底":
            List.append("9AFD")
        elif i == "城":
            List.append("9AFE")
        elif i == "音":
            List.append("9AFF")
        elif i == "底":
            List.append("9B40")
        elif i == "城":
            List.append("9B41")
        elif i == "音":
            List.append("9B42")
        elif i == "聞":
            List.append("9B43")
        elif i == "急":
            List.append("9B44")
        elif i == "身":
            List.append("9B45")
        elif i == "賊":
            List.append("9B46")
        elif i == "込":
            List.append("9B47")
        elif i == "狙":
            List.append("9B48")
        elif i == "率":
            List.append("9B49")
        elif i == "精":
            List.append("9B4A")
        elif i == "鋭":
            List.append("9B4B")
        elif i == "保":
            List.append("9B4C")
        elif i == "証":
            List.append("9B4D")
        elif i == "襲":
            List.append("9B4E")
        elif i == "負":
            List.append("9B4F")
        elif i == "傷":
            List.append("9B50")
        elif i == "奪":
            List.append("9B51")
        elif i == "言":
            List.append("9B52")
        elif i == "英":
            List.append("9B53")
        elif i == "雄":
            List.append("9B54")
        elif i == "男":
            List.append("9B55")
        elif i == "見":
            List.append("9B56")
        elif i == "目":
            List.append("9B57")
        elif i == "朝":
            List.append("9B58")
        elif i == "早":
            List.append("9B59")
        elif i == "女":
            List.append("9B5A")
        elif i == "子":
            List.append("9B5B")
        elif i == "止":
            List.append("9B5C")
        elif i == "止":
            List.append("9B5D")
        elif i == "殿":
            List.append("9B5E")
        elif i == "向":
            List.append("9B5F")
        elif i == "雪":
            List.append("9B60")
        elif i == "書":
            List.append("9B61")
        elif i == "界":
            List.append("9B62")
        elif i == "中":
            List.append("9B63")
        elif i == "思":
            List.append("9B64")
        elif i == "泣":
            List.append("9B65")
        elif i == "馬":
            List.append("9B66")
        elif i == "足":
            List.append("9B67")
        elif i == "恋":
            List.append("9B68")
        elif i == "盗":
            List.append("9B69")
        elif i == "現":
            List.append("9B6A")
        elif i == "歌":
            List.append("9B6B")
        elif i == "隠":
            List.append("9B6C")
        elif i == "事":
            List.append("9B6D")
        elif i == "情":
            List.append("9B6E")
        elif i == "色":
            List.append("9B6F")
        elif i == "感":
            List.append("9B70")
        elif i == "動":
            List.append("9B71")
        elif i == "運":
            List.append("9B72")
        elif i == "命":
            List.append("9B73")
        elif i == "明":
            List.append("9B74")
        elif i == "寒":
            List.append("9B75")
        elif i == "暖":
            List.append("9B76")
        elif i == "房":
            List.append("9B77")
        elif i == "図":
            List.append("9B78")
        elif i == "館":
            List.append("9B79")
        elif i == "本":
            List.append("9B7A")
        elif i == "読":
            List.append("9B7B")
        elif i == "番":
            List.append("9B7C")
        elif i == "単":
            List.append("9B7D")
        elif i == "文":
            List.append("9B7E")
        elif i == "化":
            List.append("9B7F")
        elif i == "化":
            List.append("9B80")
        elif i == "民":
            List.append("9B81")
        elif i == "与":
            List.append("9B82")
        elif i == "建":
            List.append("9B83")
        elif i == "歴":
            List.append("9B84")
        elif i == "史":
            List.append("9B85")
        elif i == "的":
            List.append("9B86")
        elif i == "美":
            List.append("9B87")
        elif i == "私":
            List.append("9B88")
        elif i == "語":
            List.append("9B89")
        elif i == "禁":
            List.append("9B8A")
        elif i == "公":
            List.append("9B8B")
        elif i == "静":
            List.append("9B8C")
        elif i == "落":
            List.append("9B8D")
        elif i == "方":
            List.append("9B8E")
        elif i == "爆":
            List.append("9B8F")
        elif i == "発":
            List.append("9B90")
        elif i == "起":
            List.append("9B91")
        elif i == "直":
            List.append("9B92")
        elif i == "後":
            List.append("9B93")
        elif i == "戻":
            List.append("9B94")
        elif i == "好":
            List.append("9B95")
        elif i == "乱":
            List.append("9B96")
        elif i == "終":
            List.append("9B97")
        elif i == "平":
            List.append("9B98")
        elif i == "和":
            List.append("9B99")
        elif i == "若":
            List.append("9B9A")
        elif i == "旅":
            List.append("9B9B")
        elif i == "諸":
            List.append("9B9C")
        elif i == "温":
            List.append("9B9D")
        elif i == "育":
            List.append("9B9E")
        elif i == "机":
            List.append("9B9F")
        elif i == "学":
            List.append("9BA0")
        elif i == "葉":
            List.append("9BA1")
        elif i == "庶":
            List.append("9BA2")
        elif i == "政":
            List.append("9BA3")
        elif i == "治":
            List.append("9BA4")
        elif i == "必":
            List.append("9BA5")
        elif i == "要":
            List.append("9BA6")
        elif i == "我":
            List.append("9BA7")
        elif i == "視":
            List.append("9BA8")
        elif i == "察":
            List.append("9BA9")
        elif i == "笑":
            List.append("9BAA")
        elif i == "遠":
            List.append("9BAB")
        elif i == "存":
            List.append("9BAC")
        elif i == "在":
            List.append("9BAD")
        elif i == "危":
            List.append("9BAE")
        elif i == "険":
            List.append("9BAF")
        elif i == "彼":
            List.append("9BB0")
        elif i == "野":
            List.append("9BB1")
        elif i == "望":
            List.append("9BB2")
        elif i == "積":
            List.append("9BB3")
        elif i == "到":
            List.append("9BB4")
        elif i == "着":
            List.append("9BB5")
        elif i == "遅":
            List.append("9BB6")
        elif i == "誘":
            List.append("9BB7")
        elif i == "導":
            List.append("9BB8")
        elif i == "家":
            List.append("9BB9")
        elif i == "小":
            List.append("9BBA")
        elif i == "社":
            List.append("9BBB")
        elif i == "廃":
            List.append("9BBC")
        elif i == "坑":
            List.append("9BBD")
        elif i == "宝":
            List.append("9BBE")
        elif i == "部":
            List.append("9BBF")
        elif i == "悔":
            List.append("9BC0")
        elif i == "特":
            List.append("9BC1")
        elif i == "別":
            List.append("9BC2")
        elif i == "暗":
            List.append("9BC3")
        elif i == "号":
            List.append("9BC4")
        elif i == "者":
            List.append("9BC5")
        elif i == "繁":
            List.append("9BC6")
        elif i == "栄":
            List.append("9BC7")
        elif i == "願":
            List.append("9BC8")
        elif i == "記":
            List.append("9BC9")
        elif i == "貧":
            List.append("9BCA")
        elif i == "富":
            List.append("9BCB")
        elif i == "差":
            List.append("9BCC")
        elif i == "税":
            List.append("9BCD")
        elif i == "制":
            List.append("9BCE")
        elif i == "弱":
            List.append("9BCF")
        elif i == "救":
            List.append("9BD0")
        elif i == "済":
            List.append("9BD1")
        elif i == "予":
            List.append("9BD2")
        elif i == "算":
            List.append("9BD3")
        elif i == "確":
            List.append("9BD4")
        elif i == "安":
            List.append("9BD5")
        elif i == "守":
            List.append("9BD6")
        elif i == "警":
            List.append("9BD7")
        elif i == "組":
            List.append("9BD8")
        elif i == "織":
            List.append("9BD9")
        elif i == "支":
            List.append("9BDA")
        elif i == "援":
            List.append("9BDB")
        elif i == "意":
            List.append("9BDC")
        elif i == "識":
            List.append("9BDD")
        elif i == "改":
            List.append("9BDE")
        elif i == "革":
            List.append("9BDF")
        elif i == "愛":
            List.append("9BE0")
        elif i == "条":
            List.append("9BE1")
        elif i == "想":
            List.append("9BE2")
        elif i == "素":
            List.append("9BE3")
        elif i == "敵":
            List.append("9BE4")
        elif i == "当":
            List.append("9BE5")
        elif i == "考":
            List.append("9BE6")
        elif i == "誤":
            List.append("9BE7")
        elif i == "理":
            List.append("9BE8")
        elif i == "実":
            List.append("9BE9")
        elif i == "即":
            List.append("9BEA")
        elif i == "効":
            List.append("9BEB")
        elif i == "性":
            List.append("9BEC")
        elif i == "求":
            List.append("9BED")
        elif i == "劇":
            List.append("9BEE")
        elif i == "薬":
            List.append("9BEF")
        elif i == "選":
            List.append("9BF0")
        elif i == "約":
            List.append("9BF1")
        elif i == "束":
            List.append("9BF2")
        elif i == "届":
            List.append("9BF3")
        elif i == "型":
            List.append("9BF4")
        elif i == "引":
            List.append("9BF5")
        elif i == "力":
            List.append("9BF6")
        elif i == "作":
            List.append("9BF7")
        elif i == "内":
            List.append("9BF8")
        elif i == "設":
            List.append("9BF9")
        elif i == "備":
            List.append("9BFA")
        elif i == "数":
            List.append("9BFB")
        elif i == "枚":
            List.append("9BFC")
        elif i == "句":
            List.append("9C40")
        elif i == "仕":
            List.append("9C41")
        elif i == "幸":
            List.append("9C42")
        elif i == "奥":
            List.append("9C43")
        elif i == "採":
            List.append("9C44")
        elif i == "掘":
            List.append("9C45")
        elif i == "探":
            List.append("9C46")
        elif i == "掛":
            List.append("9C47")
        elif i == "未":
            List.append("9C48")
        elif i == "稼":
            List.append("9C49")
        elif i == "略":
            List.append("9C4A")
        elif i == "切":
            List.append("9C4B")
        elif i == "替":
            List.append("9C4C")
        elif i == "電":
            List.append("9C4D")
        elif i == "源":
            List.append("9C4E")
        elif i == "右":
            List.append("9C4F")
        elif i == "段":
            List.append("9C50")
        elif i == "突":
            List.append("9C51")
        elif i == "壁":
            List.append("9C52")
        elif i == "調":
            List.append("9C53")
        elif i == "港":
            List.append("9C54")
        elif i == "船":
            List.append("9C55")
        elif i == "定":
            List.append("9C56")
        elif i == "期":
            List.append("9C57")
        elif i == "長":
            List.append("9C58")
        elif i == "修":
            List.append("9C59")
        elif i == "菜":
            List.append("9C5A")
        elif i == "商":
            List.append("9C5B")
        elif i == "品":
            List.append("9C5C")
        elif i == "台":
            List.append("9C5D")
        elif i == "不":
            List.append("9C5F")
        elif i == "故":
            List.append("9C60")
        elif i == "側":
            List.append("9C61")
        elif i == "責":
            List.append("9C62")
        elif i == "任":
            List.append("9C63")
        elif i == "処":
            List.append("9C64")
        elif i == "欲":
            List.append("9C65")
        elif i == "海":
            List.append("9C66")
        elif i == "路":
            List.append("9C67")
        elif i == "他":
            List.append("9C68")
        elif i == "法":
            List.append("9C69")
        elif i == "退":
            List.append("9C6A")
        elif i == "屈":
            List.append("9C6B")
        elif i == "失":
            List.append("9C6C")
        elif i == "礼":
            List.append("9C6D")
        elif i == "腕":
            List.append("9C6E")
        elif i == "立":
            List.append("9C6F")
        elif i == "芸":
            List.append("9C70")
        elif i == "受":
            List.append("9C71")
        elif i == "参":
            List.append("9C72")
        elif i == "然":
            List.append("9C73")
        elif i == "勇":
            List.append("9C74")
        elif i == "折":
            List.append("9C75")
        elif i == "越":
            List.append("9C76")
        elif i == "印":
            List.append("9C77")
        elif i == "陸":
            List.append("9C78")
        elif i == "暮":
            List.append("9C79")
        elif i == "準":
            List.append("9C7A")
        elif i == "飛":
            List.append("9C7B")
        elif i == "振":
            List.append("9C7C")
        elif i == "応":
            List.append("9C7D")
        elif i == "使":
            List.append("9C7E")
        elif i == "僕":
            List.append("9C7F")
        elif i == "頼":
            List.append("9C80")
        elif i == "企":
            List.append("9C81")
        elif i == "業":
            List.append("9C82")
        elif i == "滅":
            List.append("9C83")
        elif i == "金":
            List.append("9C84")
        elif i == "庫":
            List.append("9C85")
        elif i == "収":
            List.append("9C86")
        elif i == "霧":
            List.append("9C87")
        elif i == "眠":
            List.append("9C88")
        elif i == "依":
            List.append("9C89")
        elif i == "申":
            List.append("9C8B")
        elif i == "遺":
            List.append("9C8C")
        elif i == "産":
            List.append("9C8D")
        elif i == "状":
            List.append("9C8E")
        elif i == "貴":
            List.append("9C8F")
        elif i == "様":
            List.append("9C90")
        elif i == "偶":
            List.append("9C91")
        elif i == "主":
            List.append("9C92")
        elif i == "取":
            List.append("9C93")
        elif i == "跡":
            List.append("9C94")
        elif i == "敷":
            List.append("9C95")
        elif i == "買":
            List.append("9C96")
        elif i == "途":
            List.append("9C97")
        elif i == "死":
            List.append("9C98")
        elif i == "被":
            List.append("9C99")
        elif i == "害":
            List.append("9C9A")
        elif i == "売":
            List.append("9C9B")
        elif i == "配":
            List.append("9C9C")
        elif i == "晴":
            List.append("9C9D")
        elif i == "装":
            List.append("9C9E")
        elif i == "飾":
            List.append("9C9F")
        elif i == "名":
            List.append("9CA0")
        elif i == "工":
            List.append("9CA1")
        elif i == "嬢":
            List.append("9CA2")
        elif i == "石":
            List.append("9CA3")
        elif i == "箱":
            List.append("9CA4")
        elif i == "渡":
            List.append("9CA5")
        elif i == "結":
            List.append("9CA6")
        elif i == "局":
            List.append("9CA7")
        elif i == "比":
            List.append("9CA8")
        elif i == "山":
            List.append("9CA9")
        elif i == "疲":
            List.append("9CAA")
        elif i == "端":
            List.append("9CAB")
        elif i == "位":
            List.append("9CAC")
        elif i == "置":
            List.append("9CAD")
        elif i == "町":
            List.append("9CAE")
        elif i == "俺":
            List.append("9CAF")
        elif i == "仮":
            List.append("9CB0")
        elif i == "面":
            List.append("9CB1")
        elif i == "臣":
            List.append("9CB2")
        elif i == "逃":
            List.append("9CB3")
        elif i == "秘":
            List.append("9CB4")
        elif i == "密":
            List.append("9CB5")
        elif i == "多":
            List.append("9CB6")
        elif i == "仲":
            List.append("9CB7")
        elif i == "経":
            List.append("9CB8")
        elif i == "追":
            List.append("9CB9")
        elif i == "相":
            List.append("9CBA")
        elif i == "返":
            List.append("9CBB")
        elif i == "父":
            List.append("9CBC")
        elif i == "少":
            List.append("9CBD")
        elif i == "関":
            List.append("9CBE")
        elif i == "係":
            List.append("9CBF")
        elif i == "形":
            List.append("9CC0")
        elif i == "歩":
            List.append("9CC1")
        elif i == "論":
            List.append("9CC2")
        elif i == "夜":
            List.append("9CC3")
        elif i == "休":
            List.append("9CC4")
        elif i == "指":
            List.append("9CC5")
        elif i == "覚":
            List.append("9CC6")
        elif i == "君":
            List.append("9CC7")
        elif i == "体":
            List.append("9CC8")
        elif i == "全":
            List.append("9CC9")
        elif i == "包":
            List.append("9CCA")
        elif i == "浮":
            List.append("9CCB")
        elif i == "無":
            List.append("9CCC")
        elif i == "郷":
            List.append("9CCD")
        elif i == "同":
            List.append("9CCE")
        elif i == "普":
            List.append("9CCF")
        elif i == "通":
            List.append("9CD0")
        elif i == "元":
            List.append("9CD1")
        elif i == "寝":
            List.append("9CD2")
        elif i == "付":
            List.append("9CD3")
        elif i == "絶":
            List.append("9CD4")
        elif i == "対":
            List.append("9CD5")
        elif i == "勝":
            List.append("9CD6")
        elif i == "利":
            List.append("9CD7")
        elif i == "詳":
            List.append("9CD8")
        elif i == "忘":
            List.append("9CD9")
        elif i == "兄":
            List.append("9CDA")
        elif i == "婚":
            List.append("9CDB")
        elif i == "田":
            List.append("9CDC")
        elif i == "舎":
            List.append("9CDD")
        elif i == "村":
            List.append("9CDE")
        elif i == "親":
            List.append("9CDF")
        elif i == "声":
            List.append("9CE0")
        elif i == "叫":
            List.append("9CE1")
        elif i == "打":
            List.append("9CE2")
        elif i == "兵":
            List.append("9CE3")
        elif i == "士":
            List.append("9CE4")
        elif i == "機":
            List.append("9CE5")
        elif i == "派":
            List.append("9CE6")
        elif i == "晩":
            List.append("9CE7")
        elif i == "泊":
            List.append("9CE8")
        elif i == "似":
            List.append("9CE9")
        elif i == "母":
            List.append("9CEA")
        elif i == "連":
            List.append("9CEB")
        elif i == "用":
            List.append("9CEC")
        elif i == "達":
            List.append("9CED")
        elif i == "息":
            List.append("9CEE")
        elif i == "尊":
            List.append("9CEF")
        elif i == "敬":
            List.append("9CF0")
        elif i == "遊":
            List.append("9CF1")
        elif i == "観":
            List.append("9CF2")
        elif i == "強":
            List.append("9CF3")
        elif i == "倉":
            List.append("9CF4")
        elif i == "怪":
            List.append("9CF5")
        elif i == "物":
            List.append("9CF6")
        elif i == "倒":
            List.append("9CF7")
        elif i == "沈":
            List.append("9CF8")
        elif i == "問":
            List.append("9CF9")
        elif i == "題":
            List.append("9CFA")
        elif i == "脱":
            List.append("9CFB")
        elif i == "員":
            List.append("9CFC")
        elif i == "程":
            List.append("9CFD")
        elif i == "犠":
            List.append("9CFE")
        elif i == "牲":
            List.append("9CFF")
        elif i == "割":
            List.append("9D43")
        elif i == "操":
            List.append("9D44")
        elif i == "舵":
            List.append("9D45")
        elif i == "激":
            List.append("9D46")
        elif i == "初":
            List.append("9D47")
        elif i == "航":
            List.append("9D48")
        elif i == "続":
            List.append("9D49")
        elif i == "補":
            List.append("9D4A")
        elif i == "寸":
            List.append("9D4B")
        elif i == "際":
            List.append("9D4C")
        elif i == "照":
            List.append("9D4D")
        elif i == "完":
            List.append("9D4E")
        elif i == "舞":
            List.append("9D4F")
        elif i == "等":
            List.append("9D50")
        elif i == "由":
            List.append("9D51")
        elif i == "難":
            List.append("9D52")
        elif i == "認":
            List.append("9D53")
        elif i == "得":
            List.append("9D54")
        elif i == "件":
            List.append("9D55")
        elif i == "審":
            List.append("9D56")
        elif i == "次":
            List.append("9D57")
        elif i == "幹":
            List.append("9D58")
        elif i == "崩":
            List.append("9D59")
        elif i == "壊":
            List.append("9D5A")
        elif i == "共":
            List.append("9D5B")
        elif i == "歳":
            List.append("9D5C")
        elif i == "原":
            List.append("9D5D")
        elif i == "因":
            List.append("9D5E")
        elif i == "真":
            List.append("9D60")
        elif i == "協":
            List.append("9D61")
        elif i == "説":
            List.append("9D62")
        elif i == "唯":
            List.append("9D63")
        elif i == "預":
            List.append("9D64")
        elif i == "没":
            List.append("9D65")
        elif i == "態":
            List.append("9D66")
        elif i == "談":
            List.append("9D67")
        elif i == "羽":
            List.append("9D68")
        elif i == "潮":
            List.append("9D69")
        elif i == "香":
            List.append("9D6A")
        elif i == "議":
            List.append("9D6B")
        elif i == "軽":
            List.append("9D6C")
        elif i == "伝":
            List.append("9D6D")
        elif i == "絡":
            List.append("9D6E")
        elif i == "張":
            List.append("9D6F")
        elif i == "増":
            List.append("9D70")
        elif i == "損":
            List.append("9D71")
        elif i == "呼":
            List.append("9D72")
        elif i == "油":
            List.append("9D73")
        elif i == "断":
            List.append("9D74")
        elif i == "穴":
            List.append("9D75")
        elif i == "鼻":
            List.append("9D76")
        elif i == "興":
            List.append("9D77")
        elif i == "味":
            List.append("9D78")
        elif i == "便":
            List.append("9D79")
        elif i == "拝":
            List.append("9D7A")
        elif i == "堂":
            List.append("9D7B")
        elif i == "線":
            List.append("9D7C")
        elif i == "簡":
            List.append("9D7D")
        elif i == "供":
            List.append("9D7E")
        elif i == "騎":
            List.append("9D80")
        elif i == "属":
            List.append("9D81")
        elif i == "敗":
            List.append("9D82")
        elif i == "走":
            List.append("9D83")
        elif i == "集":
            List.append("9D84")
        elif i == "背":
            List.append("9D85")
        elif i == "景":
            List.append("9D86")
        elif i == "果":
            List.append("9D87")
        elif i == "停":
            List.append("9D88")
        elif i == "煮":
            List.append("9D89")
        elif i == "炒":
            List.append("9D8A")
        elif i == "米":
            List.append("9D8B")
        elif i == "緒":
            List.append("9D8C")
        elif i == "役":
            List.append("9D8D")
        elif i == "熱":
            List.append("9D8E")
        elif i == "鮮":
            List.append("9D8F")
        elif i == "料":
            List.append("9D90")
        elif i == "揚":
            List.append("9D91")
        elif i == "口":
            List.append("9D92")
        elif i == "卵":
            List.append("9D93")
        elif i == "焼":
            List.append("9D94")
        elif i == "抜":
            List.append("9D95")
        elif i == "肉":
            List.append("9D96")
        elif i == "統":
            List.append("9D97")
        elif i == "加":
            List.append("9D98")
        elif i == "減":
            List.append("9D99")
        elif i == "賞":
            List.append("9D9A")
        elif i == "太":
            List.append("9D9B")
        elif i == "刺":
            List.append("9D9C")
        elif i == "烈":
            List.append("9D9D")
        elif i == "夏":
            List.append("9D9E")
        elif i == "浴":
            List.append("9D9F")
        elif i == "波":
            List.append("9DA0")
        elif i == "漂":
            List.append("9DA1")
        elif i == "幻":
            List.append("9DA2")
        elif i == "酔":
            List.append("9DA3")
        elif i == "瞬":
            List.append("9DA4")
        elif i == "魚":
            List.append("9DA5")
        elif i == "重":
            List.append("9DA6")
        elif i == "深":
            List.append("9DA7")
        elif i == "冷":
            List.append("9DA8")
        elif i == "宇":
            List.append("9DA9")
        elif i == "宙":
            List.append("9DAA")
        elif i == "星":
            List.append("9DAB")
        elif i == "輝":
            List.append("9DAC")
        elif i == "豪":
            List.append("9DAD")
        elif i == "快":
            List.append("9DAE")
        elif i == "麻":
            List.append("9DAF")
        elif i == "婆":
            List.append("9DB0")
        elif i == "豆":
            List.append("9DB1")
        elif i == "腐":
            List.append("9DB2")
        elif i == "辛":
            List.append("9DB3")
        elif i == "妙":
            List.append("9DB4")
        elif i == "極":
            List.append("9DB5")
        elif i == "違":
            List.append("9DB6")
        elif i == "異":
            List.append("9DB7")
        elif i == "魔":
            List.append("9DB8")
        elif i == "養":
            List.append("9DB9")
        elif i == "豊":
            List.append("9DBA")
        elif i == "盛":
            List.append("9DBB")
        elif i == "絵":
            List.append("9DBC")
        elif i == "画":
            List.append("9DBD")
        elif i == "描":
            List.append("9DBE")
        elif i == "構":
            List.append("9DBF")
        elif i == "甘":
            List.append("9DC0")
        elif i == "巻":
            List.append("9DC1")
        elif i == "染":
            List.append("9DC2")
        elif i == "高":
            List.append("9DC3")
        elif i == "互":
            List.append("9DC4")
        elif i == "称":
            List.append("9DC5")
        elif i == "誰":
            List.append("9DC6")
        elif i == "幼":
            List.append("9DC7")
        elif i == "頃":
            List.append("9DC8")
        elif i == "演":
            List.append("9DC9")
        elif i == "汁":
            List.append("9DCA")
        elif i == "介":
            List.append("9DCB")
        elif i == "類":
            List.append("9DCC")
        elif i == "腹":
            List.append("9DCD")
        elif i == "式":
            List.append("9DCE")
        elif i == "吸":
            List.append("9DCF")
        elif i == "酸":
            List.append("9DD0")
        elif i == "清":
            List.append("9DD1")
        elif i == "奇":
            List.append("9DD2")
        elif i == "贈":
            List.append("9DD3")
        elif i == "飲":
            List.append("9DD4")
        elif i == "熟":
            List.append("9DD5")
        elif i == "須":
            List.append("9DD6")
        elif i == "交":
            List.append("9DD7")
        elif i == "響":
            List.append("9DD8")
        elif i == "曲":
            List.append("9DD9")
        elif i == "奏":
            List.append("9DDA")
        elif i == "速":
            List.append("9DDB")
        elif i == "半":
            List.append("9DDC")
        elif i == "拡":
            List.append("9DDD")
        elif i == "縮":
            List.append("9DDE")
        elif i == "了":
            List.append("9DDF")
        elif i == "径":
            List.append("9DE0")
        elif i == "冒":
            List.append("9DE1")
        elif i == "賛":
            List.append("9DE2")
        elif i == "離":
            List.append("9DE3")
        elif i == "迷":
            List.append("9DE4")
        elif i == "惑":
            List.append("9DE5")
        elif i == "孤":
            List.append("9DE6")
        elif i == "児":
            List.append("9DE7")
        elif i == "院":
            List.append("9DE8")
        elif i == "孝":
            List.append("9DE9")
        elif i == "逆":
            List.append("9DEA")
        elif i == "転":
            List.append("9DEB")
        elif i == "塔":
            List.append("9DEC")
        elif i == "報":
            List.append("9DED")
        elif i == "査":
            List.append("9DEE")
        elif i == "隊":
            List.append("9DEF")
        elif i == "護":
            List.append("9DF0")
        elif i == "衛":
            List.append("9DF1")
        elif i == "価":
            List.append("9DF2")
        elif i == "値":
            List.append("9DF3")
        elif i == "紙":
            List.append("9DF4")
        elif i == "苦":
            List.append("9DF5")
        elif i == "慣":
            List.append("9DF6")
        elif i == "血":
            List.append("9DF7")
        elif i == "流":
            List.append("9DF8")
        elif i == "労":
            List.append("9DF9")
        elif i == "惜":
            List.append("9DFA")
        elif i == "捨":
            List.append("9DFB")
        elif i == "質":
            List.append("9DFC")
        elif i == "胸":
            List.append("9DFD")
        elif i == "整":
            List.append("9E41")
        elif i == "店":
            List.append("9E42")
        elif i == "踏":
            List.append("9E43")
        elif i == "巨":
            List.append("9E44")
        elif i == "破":
            List.append("9E45")
        elif i == "衣":
            List.append("9E46")
        elif i == "犯":
            List.append("9E47")
        elif i == "捕":
            List.append("9E48")
        elif i == "牢":
            List.append("9E49")
        elif i == "始":
            List.append("9E4A")
        elif i == "嫌":
            List.append("9E4B")
        elif i == "過":
            List.append("9E4C")
        elif i == "去":
            List.append("9E4D")
        elif i == "功":
            List.append("9E4E")
        elif i == "績":
            List.append("9E4F")
        elif i == "両":
            List.append("9E50")
        elif i == "貸":
            List.append("9E51")
        elif i == "耳":
            List.append("9E52")
        elif i == "趣":
            List.append("9E53")
        elif i == "剣":
            List.append("9E54")
        elif i == "幕":
            List.append("9E55")
        elif i == "誓":
            List.append("9E56")
        elif i == "歯":
            List.append("9E57")
        elif i == "眼":
            List.append("9E58")
        elif i == "悟":
            List.append("9E59")
        elif i == "吹":
            List.append("9E5A")
        elif i == "昨":
            List.append("9E5B")
        elif i == "玉":
            List.append("9E5C")
        elif i == "送":
            List.append("9E5E")
        elif i == "字":
            List.append("9E5F")
        elif i == "暴":
            List.append("9E60")
        elif i == "里":
            List.append("9E61")
        elif i == "恐":
            List.append("9E62")
        elif i == "謝":
            List.append("9E63")
        elif i == "聖":
            List.append("9E64")
        elif i == "総":
            List.append("9E65")
        elif i == "適":
            List.append("9E66")
        elif i == "順":
            List.append("9E67")
        elif i == "納":
            List.append("9E68")
        elif i == "捧":
            List.append("9E69")
        elif i == "偉":
            List.append("9E6A")
        elif i == "祝":
            List.append("9E6B")
        elif i == "福":
            List.append("9E6C")
        elif i == "痛":
            List.append("9E6D")
        elif i == "友":
            List.append("9E6E")
        elif i == "髪":
            List.append("9E6F")
        elif i == "短":
            List.append("9E70")
        elif i == "残":
            List.append("9E71")
        elif i == "念":
            List.append("9E72")
        elif i == "抱":
            List.append("9E73")
        elif i == "悩":
            List.append("9E74")
        elif i == "砕":
            List.append("9E75")
        elif i == "威":
            List.append("9E76")
        elif i == "勢":
            List.append("9E77")
        elif i == "僧":
            List.append("9E78")
        elif i == "正":
            List.append("9E79")
        elif i == "解":
            List.append("9E7A")
        elif i == "虫":
            List.append("9E7B")
        elif i == "仇":
            List.append("9E7C")
        elif i == "討":
            List.append("9E7D")
        elif i == "払":
            List.append("9E7E")
        elif i == "黙":
            List.append("9E80")
        elif i == "示":
            List.append("9E81")
        elif i == "従":
            List.append("9E82")
        elif i == "忙":
            List.append("9E83")
        elif i == "謁":
            List.append("9E84")
        elif i == "週":
            List.append("9E85")
        elif i == "毒":
            List.append("9E86")
        elif i == "頭":
            List.append("9E87")
        elif i == "驚":
            List.append("9E88")
        elif i == "有":
            List.append("9E89")
        elif i == "荒":
            List.append("9E8A")
        elif i == "復":
            List.append("9E8B")
        elif i == "境":
            List.append("9E8C")
        elif i == "遇":
            List.append("9E8D")
        elif i == "健":
            List.append("9E8E")
        elif i == "康":
            List.append("9E8F")
        elif i == "病":
            List.append("9E90")
        elif i == "影":
            List.append("9E91")
        elif i == "硬":
            List.append("9E92")
        elif i == "慮":
            List.append("9E93")
        elif i == "雲":
            List.append("9E94")
        elif i == "訳":
            List.append("9E95")
        elif i == "許":
            List.append("9E96")
        elif i == "換":
            List.append("9E97")
        elif i == "拒":
            List.append("9E98")
        elif i == "災":
            List.append("9E99")
        elif i == "拠":
            List.append("9E9A")
        elif i == "肩":
            List.append("9E9B")
        elif i == "可":
            List.append("9E9C")
        elif i == "能":
            List.append("9E9D")
        elif i == "偽":
            List.append("9E9E")
        elif i == "善":
            List.append("9E9F")
        elif i == "鳥":
            List.append("9EA0")
        elif i == "巣":
            List.append("9EA1")
        elif i == "憧":
            List.append("9EA2")
        elif i == "資":
            List.append("9EA3")
        elif i == "誇":
            List.append("9EA4")
        elif i == "管":
            List.append("9EA5")
        elif i == "量":
            List.append("9EA6")
        elif i == "縁":
            List.append("9EA7")
        elif i == "愚":
            List.append("9EA8")
        elif i == "邪":
            List.append("9EA9")
        elif i == "容":
            List.append("9EAA")
        elif i == "赦":
            List.append("9EAB")
        elif i == "像":
            List.append("9EAC")
        elif i == "仰":
            List.append("9EAD")
        elif i == "困":
            List.append("9EAE")
        elif i == "択":
            List.append("9EAF")
        elif i == "夕":
            List.append("9EB0")
        elif i == "扱":
            List.append("9EB1")
        elif i == "啓":
            List.append("9EB2")
        elif i == "汚":
            List.append("9EB3")
        elif i == "罰":
            List.append("9EB4")
        elif i == "胆":
            List.append("9EB5")
        elif i == "猫":
            List.append("9EB6")
        elif i == "棒":
            List.append("9EB7")
        elif i == "細":
            List.append("9EB8")
        elif i == "点":
            List.append("9EB9")
        elif i == "製":
            List.append("9EBA")
        elif i == "矢":
            List.append("9EBB")
        elif i == "居":
            List.append("9EBC")
        elif i == "肝":
            List.append("9EBD")
        elif i == "答":
            List.append("9EBE")
        elif i == "義":
            List.append("9EBF")
        elif i == "務":
            List.append("9EC0")
        elif i == "留":
            List.append("9EC1")
        elif i == "障":
            List.append("9EC2")
        elif i == "訓":
            List.append("9EC3")
        elif i == "弟":
            List.append("9EC4")
        elif i == "妹":
            List.append("9EC5")
        elif i == "首":
            List.append("9EC6")
        elif i == "迎":
            List.append("9EC7")
        elif i == "姉":
            List.append("9EC8")
        elif i == "姿":
            List.append("9EC9")
        elif i == "将":
            List.append("9ECA")
        elif i == "散":
            List.append("9ECB")
        elif i == "練":
            List.append("9ECC")
        elif i == "猟":
            List.append("9ECD")
        elif i == "働":
            List.append("9ECE")
        elif i == "例":
            List.append("9ECF")
        elif i == "志":
            List.append("9ED0")
        elif i == "判":
            List.append("9ED1")
        elif i == "冗":
            List.append("9ED2")
        elif i == "官":
            List.append("9ED3")
        elif i == "臨":
            List.append("9ED4")
        elif i == "刻":
            List.append("9ED5")
        elif i == "潜":
            List.append("9ED6")
        elif i == "服":
            List.append("9ED7")
        elif i == "余":
            List.append("9ED8")
        elif i == "計":
            List.append("9ED9")
        elif i == "争":
            List.append("9EDA")
        elif i == "悲":
            List.append("9EDB")
        elif i == "閉":
            List.append("9EDC")
        elif i == "永":
            List.append("9EDD")
        elif i == "耐":
            List.append("9EDE")
        elif i == "移":
            List.append("9EDF")
        elif i == "候":
            List.append("9EE0")
        elif i == "習":
            List.append("9EE1")
        elif i == "罪":
            List.append("9EE2")
        elif i == "独":
            List.append("9EE3")
        elif i == "昼":
            List.append("9EE4")
        elif i == "反":
            List.append("9EE5")
        elif i == "氷":
            List.append("9EE6")
        elif i == "妻":
            List.append("9EE7")
        elif i == "注":
            List.append("9EE8")
        elif i == "表":
            List.append("9EE9")
        elif i == "究":
            List.append("9EEA")
        elif i == "徳":
            List.append("9EEB")
        elif i == "刃":
            List.append("9EEC")
        elif i == "倍":
            List.append("9EED")
        elif i == "洗":
            List.append("9EEE")
        elif i == "缶":
            List.append("9EEF")
        elif i == "押":
            List.append("9EF0")
        elif i == "登":
            List.append("9EF1")
        elif i == "提":
            List.append("9EF2")
        elif i == "常":
            List.append("9EF3")
        elif i == "刀":
            List.append("9EF4")
        elif i == "怒":
            List.append("9EF5")
        elif i == "才":
            List.append("9EF6")
        elif i == "木":
            List.append("9EF7")
        elif i == "彫":
            List.append("9EF8")
        elif i == "夫":
            List.append("9EF9")
        elif i == "婦":
            List.append("9EFA")
        elif i == "花":
            List.append("9EFB")
        elif i == "鳴":
            List.append("9EFC")
        elif i == "祭":
            List.append("9EFD")
        elif i == "騒":
            List.append("9EFE")
        elif i == "況":
            List.append("9F42")
        elif i == "嫉":
            List.append("9F43")
        elif i == "妬":
            List.append("9F44")
        elif i == "借":
            List.append("9F45")
        elif i == "寄":
            List.append("9F46")
        elif i == "茶":
            List.append("9F47")
        elif i == "酒":
            List.append("9F48")
        elif i == "燃":
            List.append("9F49")
        elif i == "投":
            List.append("9F4A")
        elif i == "希":
            List.append("9F4B")
        elif i == "費":
            List.append("9F4C")
        elif i == "並":
            List.append("9F4D")
        elif i == "喜":
            List.append("9F4E")
        elif i == "辺":
            List.append("9F4F")
        elif i == "仔":
            List.append("9F50")
        elif i == "徴":
            List.append("9F51")
        elif i == "坊":
            List.append("9F52")
        elif i == "飼":
            List.append("9F53")
        elif i == "肖":
            List.append("9F54")
        elif i == "博":
            List.append("9F55")
        elif i == "天":
            List.append("9F56")
        elif i == "軍":
            List.append("9F57")
        elif i == "祖":
            List.append("9F58")
        elif i == "棚":
            List.append("9F59")
        elif i == "講":
            List.append("9F5B")
        elif i == "呪":
            List.append("9F5C")
        elif i == "医":
            List.append("9F5D")
        elif i == "勉":
            List.append("9F5E")
        elif i == "布":
            List.append("9F5F")
        elif i == "訪":
            List.append("9F60")
        elif i == "混":
            List.append("9F61")
        elif i == "侵":
            List.append("9F62")
        elif i == "疑":
            List.append("9F63")
        elif i == "儀":
            List.append("9F64")
        elif i == "努":
            List.append("9F65")
        elif i == "益":
            List.append("9F66")
        elif i == "門":
            List.append("9F67")
        elif i == "試":
            List.append("9F68")
        elif i == "厳":
            List.append("9F69")
        elif i == "裏":
            List.append("9F6A")
        elif i == "腰":
            List.append("9F6B")
        elif i == "帥":
            List.append("9F6C")
        elif i == "封":
            List.append("9F6D")
        elif i == "柱":
            List.append("9F6E")
        elif i == "繋":
            List.append("9F6F")
        elif i == "丘":
            List.append("9F70")
        elif i == "畑":
            List.append("9F71")
        elif i == "忍":
            List.append("9F72")
        elif i == "厄":
            List.append("9F73")
        elif i == "嫁":
            List.append("9F74")
        elif i == "展":
            List.append("9F75")
        elif i == "汗":
            List.append("9F76")
        elif i == "車":
            List.append("9F77")
        elif i == "接":
            List.append("9F78")
        elif i == "絹":
            List.append("9F79")
        elif i == "肌":
            List.append("9F7A")
        elif i == "魂":
            List.append("9F7B")
        elif i == "票":
            List.append("9F7C")
        elif i == "橋":
            List.append("9F7D")
        elif i == "娘":
            List.append("9F7E")
        elif i == "根":
            List.append("9F80")
        elif i == "怖":
            List.append("9F81")
        elif i == "幅":
            List.append("9F82")
        elif i == "衝":
            List.append("9F83")
        elif i == "射":
            List.append("9F84")
        elif i == "罠":
            List.append("9F85")
        elif i == "床":
            List.append("9F86")
        elif i == "丈":
            List.append("9F87")
        elif i == "区":
            List.append("9F88")
        elif i == "随":
            List.append("9F89")
        elif i == "枝":
            List.append("9F8A")
        elif i == "古":
            List.append("9F8B")
        elif i == "頂":
            List.append("9F8C")
        elif i == "横":
            List.append("9F8D")
        elif i == "拾":
            List.append("9F8E")
        elif i == "良":
            List.append("9F8F")
        elif i == "穫":
            List.append("9F90")
        elif i == "承":
            List.append("9F91")
        elif i == "森":
            List.append("9F92")
        elif i == "雑":
            List.append("9F93")
        elif i == "貨":
            List.append("9F94")
        elif i == "族":
            List.append("9F95")
        elif i == "省":
            List.append("9F96")
        elif i == "掃":
            List.append("9F97")
        elif i == "除":
            List.append("9F98")
        elif i == "粧":
            List.append("9F99")
        elif i == "恥":
            List.append("9F9A")
        elif i == "濯":
            List.append("9F9B")
        elif i == "帯":
            List.append("9F9C")
        elif i == "策":
            List.append("9F9D")
        elif i == "裕":
            List.append("9F9E")
        elif i == "施":
            List.append("9F9F")
        elif i == "営":
            List.append("9FA0")
        elif i == "優":
            List.append("9FA1")
        elif i == "骨":
            List.append("9FA2")
        elif i == "埋":
            List.append("9FA3")
        elif i == "躍":
            List.append("9FA4")
        elif i == "冬":
            List.append("9FA5")
        elif i == "遙":
            List.append("9FA6")
        elif i == "圧":
            List.append("9FA7")
        elif i == "迫":
            List.append("9FA8")
        elif i == "獄":
            List.append("9FA9")
        elif i == "再":
            List.append("9FAA")
        elif i == "亡":
            List.append("9FAB")
        elif i == "雨":
            List.append("9FAC")
        elif i == "枯":
            List.append("9FAD")
        elif i == "噴":
            List.append("9FAE")
        elif i == "久":
            List.append("9FAF")
        elif i == "衰":
            List.append("9FB0")
        elif i == "鈍":
            List.append("9FB1")
        elif i == "凍":
            List.append("9FB2")
        elif i == "昇":
            List.append("9FB3")
        elif i == "低":
            List.append("9FB4")
        elif i == "砂":
            List.append("9FB5")
        elif i == "含":
            List.append("9FB6")
        elif i == "晶":
            List.append("9FB7")
        elif i == "溜":
            List.append("9FB8")
        elif i == "珠":
            List.append("9FB9")
        elif i == "黄":
            List.append("9FBA")
        elif i == "霊":
            List.append("9FBB")
        elif i == "召":
            List.append("9FBC")
        elif i == "喚":
            List.append("9FBD")
        elif i == "蒼":
            List.append("9FBE")
        elif i == "紅":
            List.append("9FBF")
        elif i == "翠":
            List.append("9FC0")
        elif i == "草":
            List.append("9FC1")
        elif i == "種":
            List.append("9FC2")
        elif i == "瓶":
            List.append("9FC3")
        elif i == "鱗":
            List.append("9FC4")
        elif i == "珍":
            List.append("9FC5")
        elif i == "獣":
            List.append("9FC6")
        elif i == "蓋":
            List.append("9FC7")
        elif i == "鑑":
            List.append("9FC8")
        elif i == "欠":
            List.append("9FC9")
        elif i == "各":
            List.append("9FCA")
        elif i == "煙":
            List.append("9FCB")
        elif i == "筒":
            List.append("9FCC")
        elif i == "造":
            List.append("9FCD")
        elif i == "炭":
            List.append("9FCE")
        elif i == "炉":
            List.append("9FCF")
        elif i == "槽":
            List.append("9FD0")
        elif i == "苗":
            List.append("9FD1")
        elif i == "植":
            List.append("9FD2")
        elif i == "周":
            List.append("9FD3")
        elif i == "囲":
            List.append("9FD4")
        elif i == "鍵":
            List.append("9FD5")
        elif i == "級":
            List.append("9FD6")
        elif i == "干":
            List.append("9FD7")
        elif i == "匂":
            List.append("9FD8")
        elif i == "涙":
            List.append("9FD9")
        elif i == "球":
            List.append("9FDA")
        elif i == "漬":
            List.append("9FDB")
        elif i == "瓜":
            List.append("9FDC")
        elif i == "臭":
            List.append("9FDD")
        elif i == "毛":
            List.append("9FDE")
        elif i == "芳":
            List.append("9FDF")
        elif i == "皮":
            List.append("9FE0")
        elif i == "丸":
            List.append("9FE1")
        elif i == "牛":
            List.append("9FE2")
        elif i == "乳":
            List.append("9FE3")
        elif i == "酵":
            List.append("9FE4")
        elif i == "胃":
            List.append("9FE5")
        elif i == "腸":
            List.append("9FE6")
        elif i == "炊":
            List.append("9FE7")
        elif i == "穀":
            List.append("9FE8")
        elif i == "農":
            List.append("9FE9")
        elif i == "八":
            List.append("9FEA")
        elif i == "孫":
            List.append("9FEB")
        elif i == "柔":
            List.append("9FEC")
        elif i == "麦":
            List.append("9FED")
        elif i == "粉":
            List.append("9FEE")
        elif i == "般":
            List.append("9FEF")
        elif i == "脂":
            List.append("9FF0")
        elif i == "肪":
            List.append("9FF1")
        elif i == "塊":
            List.append("9FF2")
        elif i == "塗":
            List.append("9FF3")
        elif i == "雅":
            List.append("9FF4")
        elif i == "斬":
            List.append("9FF5")
        elif i == "基":
            List.append("9FF6")
        elif i == "偃":
            List.append("9FF7")
        elif i == "厚":
            List.append("9FF8")
        elif i == "雰":
            List.append("9FF9")
        elif i == "典":
            List.append("9FFA")
        elif i == "湾":
            List.append("9FFB")
        elif i == "鎌":
            List.append("9FFC")
        elif i == "殺":
            List.append("E040")
        elif i == "尾":
            List.append("E041")
        elif i == "冠":
            List.append("E042")
        elif i == "匠":
            List.append("E043")
        elif i == "鍛":
            List.append("E044")
        elif i == "旋":
            List.append("E045")
        elif i == "誉":
            List.append("E046")
        elif i == "炎":
            List.append("E047")
        elif i == "竜":
            List.append("E048")
        elif i == "爪":
            List.append("E049")
        elif i == "隼":
            List.append("E04A")
        elif i == "紋":
            List.append("E04B")
        elif i == "創":
            List.append("E04C")
        elif i == "牙":
            List.append("E04D")
        elif i == "岩":
            List.append("E04E")
        elif i == "剛":
            List.append("E04F")
        elif i == "柩":
            List.append("E050")
        elif i == "副":
            List.append("E051")
        elif i == "葬":
            List.append("E052")
        elif i == "鋼":
            List.append("E053")
        elif i == "易":
            List.append("E054")
        elif i == "裂":
            List.append("E055")
        elif i == "妖":
            List.append("E056")
        elif i == "稲":
            List.append("E057")
        elif i == "慈":
            List.append("E058")
        elif i == "忠":
            List.append("E059")
        elif i == "円":
            List.append("E05A")
        elif i == "卓":
            List.append("E05B")
        elif i == "帝":
            List.append("E05C")
        elif i == "嵐":
            List.append("E05E")
        elif i == "乙":
            List.append("E05F")
        elif i == "杖":
            List.append("E060")
        elif i == "職":
            List.append("E061")
        elif i == "殴":
            List.append("E062")
        elif i == "権":
            List.append("E063")
        elif i == "標":
            List.append("E064")
        elif i == "笏":
            List.append("E065")
        elif i == "狂":
            List.append("E066")
        elif i == "節":
            List.append("E067")
        elif i == "孔":
            List.append("E068")
        elif i == "雀":
            List.append("E069")
        elif i == "如":
            List.append("E06A")
        elif i == "角":
            List.append("E06B")
        elif i == "青":
            List.append("E06C")
        elif i == "紡":
            List.append("E06D")
        elif i == "慟":
            List.append("E06E")
        elif i == "哭":
            List.append("E06F")
        elif i == "銀":
            List.append("E070")
        elif i == "左":
            List.append("E071")
        elif i == "東":
            List.append("E072")
        elif i == "蛮":
            List.append("E073")
        elif i == "錫":
            List.append("E074")
        elif i == "匹":
            List.append("E075")
        elif i == "蛇":
            List.append("E076")
        elif i == "祓":
            List.append("E077")
        elif i == "詠":
            List.append("E078")
        elif i == "唱":
            List.append("E079")
        elif i == "柄":
            List.append("E07A")
        elif i == "斧":
            List.append("E07B")
        elif i == "槍":
            List.append("E07C")
        elif i == "槌":
            List.append("E07D")
        elif i == "叉":
            List.append("E07E")
        elif i == "矛":
            List.append("E080")
        elif i == "鉄":
            List.append("E081")
        elif i == "陣":
            List.append("E082")
        elif i == "賜":
            List.append("E083")
        elif i == "堅":
            List.append("E084")
        elif i == "固":
            List.append("E085")
        elif i == "杭":
            List.append("E086")
        elif i == "灰":
            List.append("E087")
        elif i == "冶":
            List.append("E088")
        elif i == "科":
            List.append("E089")
        elif i == "駆":
            List.append("E08A")
        elif i == "逐":
            List.append("E08B")
        elif i == "逸":
            List.append("E08C")
        elif i == "骸":
            List.append("E08D")
        elif i == "緑":
            List.append("E08E")
        elif i == "薙":
            List.append("E08F")
        elif i == "傑":
            List.append("E090")
        elif i == "狩":
            List.append("E091")
        elif i == "弓":
            List.append("E092")
        elif i == "弾":
            List.append("E093")
        elif i == "扉":
            List.append("E094")
        elif i == "貫":
            List.append("E095")
        elif i == "鎧":
            List.append("E096")
        elif i == "七":
            List.append("E097")
        elif i == "軌":
            List.append("E098")
        elif i == "吐":
            List.append("E099")
        elif i == "尽":
            List.append("E09A")
        elif i == "浄":
            List.append("E09B")
        elif i == "環":
            List.append("E09C")
        elif i == "縫":
            List.append("E09D")
        elif i == "板":
            List.append("E09E")
        elif i == "糸":
            List.append("E09F")
        elif i == "甲":
            List.append("E0A0")
        elif i == "殊":
            List.append("E0A1")
        elif i == "継":
            List.append("E0A2")
        elif i == "塞":
            List.append("E0A3")
        elif i == "赴":
            List.append("E0A4")
        elif i == "網":
            List.append("E0A5")
        elif i == "編":
            List.append("E0A6")
        elif i == "洋":
            List.append("E0A7")
        elif i == "島":
            List.append("E0A8")
        elif i == "巫":
            List.append("E0A9")
        elif i == "兜":
            List.append("E0AA")
        elif i == "頬":
            List.append("E0AB")
        elif i == "築":
            List.append("E0AC")
        elif i == "頑":
            List.append("E0AD")
        elif i == "漢":
            List.append("E0AE")
        elif i == "帽":
            List.append("E0AF")
        elif i == "薄":
            List.append("E0B0")
        elif i == "濃":
            List.append("E0B1")
        elif i == "愉":
            List.append("E0B2")
        elif i == "輪":
            List.append("E0B3")
        elif i == "及":
            List.append("E0B4")
        elif i == "喰":
            List.append("E0B5")
        elif i == "鮫":
            List.append("E0B6")
        elif i == "致":
            List.append("E0B7")
        elif i == "鉈":
            List.append("E0B8")
        elif i == "駄":
            List.append("E0B9")
        elif i == "篭":
            List.append("E0BA")
        elif i == "授":
            List.append("E0BB")
        elif i == "袋":
            List.append("E0BC")
        elif i == "瑠":
            List.append("E0BD")
        elif i == "璃":
            List.append("E0BE")
        elif i == "佐":
            List.append("E0BF")
        elif i == "賢":
            List.append("E0C0")
        elif i == "癒":
            List.append("E0C1")
        elif i == "偏":
            List.append("E0C2")
        elif i == "疾":
            List.append("E0C3")
        elif i == "巧":
            List.append("E0C4")
        elif i == "伴":
            List.append("E0C5")
        elif i == "徐":
            List.append("E0C6")
        elif i == "縞":
            List.append("E0C7")
        elif i == "瑪":
            List.append("E0C8")
        elif i == "瑙":
            List.append("E0C9")
        elif i == "験":
            List.append("E0CA")
        elif i == "華":
            List.append("E0CB")
        elif i == "姫":
            List.append("E0CC")
        elif i == "象":
            List.append("E0CD")
        elif i == "靴":
            List.append("E0CE")
        elif i == "膝":
            List.append("E0CF")
        elif i == "蹴":
            List.append("E0D0")
        elif i == "枠":
            List.append("E0D1")
        elif i == "謎":
            List.append("E0D2")
        elif i == "隣":
            List.append("E0D3")
        elif i == "徒":
            List.append("E0D4")
        elif i == "携":
            List.append("E0D5")
        elif i == "塵":
            List.append("E0D6")
        elif i == "繰":
            List.append("E0D7")
        elif i == "翔":
            List.append("E0D8")
        elif i == "閃":
            List.append("E0D9")
        elif i == "渦":
            List.append("E0DA")
        elif i == "纏":
            List.append("E0DB")
        elif i == "垂":
            List.append("E0DC")
        elif i == "屠":
            List.append("E0DD")
        elif i == "龍":
            List.append("E0DE")
        elif i == "叩":
            List.append("E0DF")
        elif i == "片":
            List.append("E0E0")
        elif i == "跳":
            List.append("E0E1")
        elif i == "招":
            List.append("E0E2")
        elif i == "規":
            List.append("E0E3")
        elif i == "模":
            List.append("E0E4")
        elif i == "雷":
            List.append("E0E5")
        elif i == "鐘":
            List.append("E0E6")
        elif i == "震":
            List.append("E0E7")
        elif i == "撼":
            List.append("E0E8")
        elif i == "範":
            List.append("E0E9")
        elif i == "複":
            List.append("E0EA")
        elif i == "弧":
            List.append("E0EB")
        elif i == "距":
            List.append("E0EC")
        elif i == "鉱":
            List.append("E0ED")
        elif i == "棺":
            List.append("E0EE")
        elif i == "焉":
            List.append("E0EF")
        elif i == "裁":
            List.append("E0F0")
        elif i == "漆":
            List.append("E0F1")
        elif i == "淵":
            List.append("E0F2")
        elif i == "系":
            List.append("E0F3")
        elif i == "列":
            List.append("E0F4")
        elif i == "限":
            List.append("E0F5")
        elif i == "控":
            List.append("E0F6")
        elif i == "満":
            List.append("E0F7")
        elif i == "隔":
            List.append("E0F8")
        elif i == "嘘":
            List.append("E0F9")
        elif i == "漏":
            List.append("E0FA")
        elif i == "披":
            List.append("E0FB")
        elif i == "露":
            List.append("E0FC")
        elif i == "令":
            List.append("E140")
        elif i == "抵":
            List.append("E141")
        elif i == "抗":
            List.append("E142")
        elif i == "痺":
            List.append("E143")
        elif i == "僅":
            List.append("E144")
        elif i == "延":
            List.append("E145")
        elif i == "秒":
            List.append("E146")
        elif i == "縛":
            List.append("E147")
        elif i == "遭":
            List.append("E148")
        elif i == "促":
            List.append("E149")
        elif i == "械":
            List.append("E14A")
        elif i == "瀕":
            List.append("E14B")
        elif i == "微":
            List.append("E14C")
        elif i == "熊":
            List.append("E14D")
        elif i == "洞":
            List.append("E14E")
        elif i == "窟":
            List.append("E14F")
        elif i == "消":
            List.append("E150")
        elif i == "三":
            List.append("E151")
        elif i == "々":
            List.append("E152")
        elif i == "★":
            List.append("E153")
        elif i == "ｚ":
            List.append("E154")
        elif i == "…":
            List.append("E155")
        elif i == "壺":
            List.append("E156")
        elif i == "鎚":
            List.append("E157")
        elif i == "亜":
            List.append("E158")
        elif i == "翼":
            List.append("E159")
        elif i == "殻":
            List.append("E15A")
        elif i == "棲":
            List.append("E15B")
        elif i == "爬":
            List.append("E15C")
        elif i == "閲":
            List.append("E15D")
        elif i == "覧":
            List.append("E15E")
        elif i == "個":
            List.append("E15F")
        elif i == "削":
            List.append("E161")
        elif i == "辞":
            List.append("E162")
        elif i == "揺":
            List.append("E163")
        elif i == "魅":
            List.append("E164")
        elif i == "哀":
            List.append("E165")
        elif i == "検":
            List.append("E166")
        elif i == "還":
            List.append("E167")
        elif i == "艇":
            List.append("E168")
        elif i == "獲":
            List.append("E169")
        elif i == "憎":
            List.append("E16A")
        elif i == "恵":
            List.append("E16B")
        elif i == "稽":
            List.append("E16C")
        elif i == "磨":
            List.append("E16D")
        elif i == "銘":
            List.append("E16E")
        elif i == "侍":
            List.append("E16F")
        elif i == "緊":
            List.append("E170")
        elif i == "壺":
            List.append("E171")
        elif i == "鎚":
            List.append("E172")
        elif i == "亜":
            List.append("E173")
        elif i == "翼":
            List.append("E174")
        elif i == "殻":
            List.append("E175")
        elif i == "棲":
            List.append("E176")
        elif i == "爬":
            List.append("E177")
        elif i == "閲":
            List.append("E178")
        elif i == "覧":
            List.append("E179")
        elif i == "個":
            List.append("E17A")
        elif i == "削":
            List.append("E17B")
        elif i == "瞳":
            List.append("E17C")
        elif i == "墜":
            List.append("E17D")
        elif i == "燐":
            List.append("E17E")
        elif i == "砲":
            List.append("E17F")
        elif i == "双":
            List.append("E181")
        elif i == "拳":
            List.append("E182")
        elif i == "覆":
            List.append("E183")
        elif i == "推":
            List.append("E184")
        elif i == "測":
            List.append("E185")
        elif i == "貼":
            List.append("E186")
        elif i == "触":
            List.append("E187")
        elif i == "憶":
            List.append("E188")
        elif i == "讃":
            List.append("E189")
        elif i == "非":
            List.append("E18A")
        elif i == "握":
            List.append("E18B")
        elif i == "映":
            List.append("E18C")
        elif i == "写":
            List.append("E18D")
        elif i == "渉":
            List.append("E18E")
        elif i == "軸":
            List.append("E18F")
        elif i == "述":
            List.append("E190")
        elif i == "粋":
            List.append("E191")
        elif i == "妨":
            List.append("E192")
        elif i == "吉":
            List.append("E193")
        elif i == "鍋":
            List.append("E194")
        elif i == "銅":
            List.append("E195")
        elif i == "柳":
            List.append("E196")
        elif i == "丁":
            List.append("E197")
        elif i == "凶":
            List.append("E198")
        elif i == "陽":
            List.append("E199")
        elif i == "河":
            List.append("E19A")
        elif i == "脈":
            List.append("E19B")
        elif i == "超":
            List.append("E19C")
        elif i == "領":
            List.append("E19D")
        elif i == "域":
            List.append("E19E")
        elif i == "飯":
            List.append("E19F")
        elif i == "寿":
            List.append("E1A0")
        elif i == "餓":
            List.append("E1A1")
        elif i == "司":
            List.append("E1A2")
        elif i == "荷":
            List.append("E1A3")
        elif i == "担":
            List.append("E1A4")
        elif i == "臓":
            List.append("E1A5")
        elif i == "ヶ":
            List.append("E1A6")
        elif i == "告":
            List.append("E1A7")
        elif i == "析":
            List.append("E1A8")
        elif i == "透":
            List.append("E1A9")
        elif i == "筋":
            List.append("E1AA")
        elif i == "励":
            List.append("E1AB")
        elif i == "看":
            List.append("E1AC")
        elif i == "皿":
            List.append("E1AD")
        elif i == "誌":
            List.append("E1AE")
        elif i == "碑":
            List.append("E1AF")
        elif i == "焚":
            List.append("E1B0")
        elif i == "萌":
            List.append("E1B1")
        elif i == "吼":
            List.append("E1B2")
        elif i == "齢":
            List.append("E1B3")
        elif i == "陛":
            List.append("E1B4")
        elif i == "姑":
            List.append("E1B5")
        elif i == "歓":
            List.append("E1B6")
        elif i == "挨":
            List.append("E1B7")
        elif i == "拶":
            List.append("E1B8")
        elif i == "繊":
            List.append("E1B9")
        elif i == "粛":
            List.append("E1BA")
        elif i == "専":
            List.append("E1BB")
        elif i == "己":
            List.append("E1BC")
        elif i == "紹":
            List.append("E1BD")
        elif i == "粗":
            List.append("E1BE")
        elif i == "往":
            List.append("E1BF")
        elif i == "郎":
            List.append("E1C0")
        elif i == "懸":
            List.append("E1C1")
        elif i == "逢":
            List.append("E1C2")
        elif i == "瀬":
            List.append("E1C3")
        elif i == "杯":
            List.append("E1C4")
        elif i == "岸":
            List.append("E1C5")
        elif i == "泳":
            List.append("E1C6")
        elif i == "詰":
            List.append("E1C7")
        elif i == "耗":
            List.append("E1C8")
        elif i == "酬":
            List.append("E1C9")
        elif i == "噛":
            List.append("E1CA")
        elif i == "虚":
            List.append("E1CB")
        elif i == "蓮":
            List.append("E1CC")
        elif i == "踊":
            List.append("E1CD")
        elif i == "拓":
            List.append("E1CE")
        elif i == "崇":
            List.append("E1CF")
        elif i == "伸":
            List.append("E1D0")
        elif i == "芝":
            List.append("E1D1")
        elif i == "脚":
            List.append("E1D2")
        elif i == "四":
            List.append("E1D3")
        elif i == "墓":
            List.append("E1D4")
        elif i == "駒":
            List.append("E1D5")
        elif i == "卑":
            List.append("E1D6")
        elif i == "劣":
            List.append("E1D7")
        elif i == "末":
            List.append("E1D8")
        elif i == "克":
            List.append("E1D9")
        elif i == "否":
            List.append("E1DA")
        elif i == "旗":
            List.append("E1DB")
        elif i == "秩":
            List.append("E1DC")
        elif i == "序":
            List.append("E1DD")
        elif i == "絆":
            List.append("E1DE")
        elif i == "酷":
            List.append("E1DF")
        elif i == "層":
            List.append("E1E0")
        elif i == "研":
            List.append("E1E1")
        elif i == "媒":
            List.append("E1E2")
        elif i == "閣":
            List.append("E1E3")
        elif i == "巡":
            List.append("E1E4")
        elif i == "駐":
            List.append("E1E5")
        elif i == "屯":
            List.append("E1E6")
        elif i == "挑":
            List.append("E1E7")
        elif i == "慎":
            List.append("E1E8")
        elif i == "臆":
            List.append("E1E9")
        elif i == "怯":
            List.append("E1EA")
        elif i == "揮":
            List.append("E1EB")
        elif i == "謹":
            List.append("E1EC")
        elif i == "誕":
            List.append("E1ED")
        elif i == "班":
            List.append("E1EE")
        elif i == "攪":
            List.append("E1EF")
        elif i == "戒":
            List.append("E1F0")
        elif i == "老":
            List.append("E1F1")
        elif i == "排":
            List.append("E1F2")
        elif i == "伏":
            List.append("E1F3")
        elif i == "刑":
            List.append("E1F4")
        elif i == "乾":
            List.append("E1F5")
        elif i == "陥":
            List.append("E1F6")
        elif i == "乞":
            List.append("E1F7")
        elif i == "至":
            List.append("E1F8")
        elif i == "聴":
            List.append("E1F9")
        elif i == "符":
            List.append("E1FA")
        elif i == "宣":
            List.append("E1FB")
        elif i == "脳":
            List.append("E1FC")
        elif i == "凌":
            List.append("E1FD")
        elif i == "駕":
            List.append("E241")
        elif i == "歪":
            List.append("E242")
        elif i == "ｍ":
            List.append("E243")
        elif i == "ｋ":
            List.append("E244")
        elif i == "ｇ":
            List.append("E245")
        elif i == "把":
            List.append("E246")
        elif i == "漠":
            List.append("E247")
        elif i == "隆":
            List.append("E248")
        elif i == "録":
            List.append("E249")
        elif i == "徹":
            List.append("E24A")
        elif i == "氏":
            List.append("E24B")
        elif i == "撹":
            List.append("E24C")
        elif i == "阻":
            List.append("E24D")
        elif i == "渇":
            List.append("E24E")
        elif i == "讐":
            List.append("E24F")
        elif i == "恨":
            List.append("E250")
        elif i == "却":
            List.append("E251")
        elif i == "顛":
            List.append("E252")
        elif i == "岐":
            List.append("E253")
        elif i == "哲":
            List.append("E254")
        elif i == "凝":
            List.append("E255")
        elif i == "彗":
            List.append("E256")
        elif i == "膨":
            List.append("E257")
        elif i == "陰":
            List.append("E258")
        elif i == "謀":
            List.append("E259")
        elif i == "川":
            List.append("E25B")
        elif i == "沿":
            List.append("E25C")
        elif i == "泉":
            List.append("E25D")
        elif i == "犬":
            List.append("E25E")
        elif i == "璧":
            List.append("E25F")
        elif i == "傲":
            List.append("E260")
        elif i == "慢":
            List.append("E261")
        elif i == "鹿":
            List.append("E262")
        elif i == "委":
            List.append("E263")
        elif i == "憩":
            List.append("E264")
        elif i == "扇":
            List.append("E265")
        elif i == "給":
            List.append("E266")
        elif i == "冑":
            List.append("E267")
        elif i == "宮":
            List.append("E268")
        elif i == "紫":
            List.append("E269")
        elif i == "燭":
            List.append("E26A")
        elif i == "灯":
            List.append("E26B")
        elif i == "憐":
            List.append("E26C")
        elif i == "舗":
            List.append("E26D")
        elif i == "菌":
            List.append("E26E")
        elif i == "課":
            List.append("E26F")
        elif i == "庭":
            List.append("E270")
        elif i == "衆":
            List.append("E271")
        elif i == "厨":
            List.append("E272")
        elif i == "遥":
            List.append("E273")
        elif i == "仙":
            List.append("E274")
        elif i == "央":
            List.append("E275")
        elif i == "湯":
            List.append("E276")
        elif i == "呂":
            List.append("E277")
        elif i == "浸":
            List.append("E278")
        elif i == "寺":
            List.append("E279")
        elif i == "挿":
            List.append("E27B")
        elif i == "昏":
            List.append("E27C")
        elif i == "為":
            List.append("E27D")
        elif i == "刷":
            List.append("E27E")
        elif i == "暑":
            List.append("E27F")
        elif i == "季":
            List.append("E280")
        elif i == "償":
            List.append("E281")
        elif i == "奴":
            List.append("E282")
        elif i == "捜":
            List.append("E283")
        elif i == "財":
            List.append("E284")
        elif i == "奉":
            List.append("E285")
        elif i == "師":
            List.append("E286")
        elif i == "購":
            List.append("E287")
        elif i == "療":
            List.append("E288")
        elif i == "池":
            List.append("E289")
        elif i == "羅":
            List.append("E28A")
        elif i == "憂":
            List.append("E28B")
        elif i == "評":
            List.append("E28C")
        elif i == "噌":
            List.append("E28D")
        elif i == "轟":
            List.append("E28E")
        elif i == "五":
            List.append("E28F")
        elif i == "縦":
            List.append("E290")
        elif i == "輩":
            List.append("E291")
        elif i == "勅":
            List.append("E292")
        elif i == "請":
            List.append("E293")
        elif i == "棄":
            List.append("E294")
        elif i == "惧":
            List.append("E295")
        elif i == "監":
            List.append("E296")
        elif i == "滝":
            List.append("E297")
        elif i == "銭":
            List.append("E298")
        elif i == "奮":
            List.append("E299")
        elif i == "純":
            List.append("E29A")
        elif i == "塹":
            List.append("E29B")
        elif i == "壕":
            List.append("E29C")
        elif i == "郭":
            List.append("E29D")
        elif i == "貯":
            List.append("E29E")
        elif i == "蔵":
            List.append("E29F")
        elif i == "斉":
            List.append("E2A0")
        elif i == "維":
            List.append("E2A1")
        elif i == "校":
            List.append("E2A2")
        elif i == "錬":
            List.append("E2A3")
        elif i == "挺":
            List.append("E2A4")
        elif i == "猟":
            List.append("E2A5")
        elif i == "尉":
            List.append("E2A6")
        elif i == "佳":
            List.append("E2A7")
        elif i == "慌":
            List.append("E2A8")
        elif i == "遂":
            List.append("E2A9")
        elif i == "凄":
            List.append("E2AA")
        elif i == "炸":
            List.append("E2AB")
        elif i == "昌":
            List.append("E2AC")
        elif i == "耕":
            List.append("E2AD")
        elif i == "批":
            List.append("E2AE")
        elif i == "宗":
            List.append("E2AF")
        elif i == "爺":
            List.append("E2B0")
        elif i == "礎":
            List.append("E2B1")
        elif i == "糧":
            List.append("E2B2")
        elif i == "蓄":
            List.append("E2B3")
        elif i == "輸":
            List.append("E2B4")
        elif i == "艦":
            List.append("E2B5")
        elif i == "搭":
            List.append("E2B6")
        elif i == "載":
            List.append("E2B7")
        elif i == "勧":
            List.append("E2B8")
        elif i == "卒":
            List.append("E2B9")
        elif i == "噂":
            List.append("E2BA")
        elif i == "湖":
            List.append("E2BB")
        elif i == "宅":
            List.append("E2BC")
        elif i == "勤":
            List.append("E2BD")
        elif i == "猛":
            List.append("E2BE")
        elif i == "皆":
            List.append("E2BF")
        elif i == "潔":
            List.append("E2C0")
        elif i == "鏡":
            List.append("E2C1")
        elif i == "麗":
            List.append("E2C2")
        elif i == "曹":
            List.append("E2C3")
        elif i == "玄":
            List.append("E2C4")
        elif i == "寂":
            List.append("E2C5")
        elif i == "壇":
            List.append("E2C6")
        elif i == "堕":
            List.append("E2C7")
        elif i == "架":
            List.append("E2C8")
        elif i == "擬":
            List.append("E2C9")
        elif i == "銃":
            List.append("E2CA")
        elif i == "貢":
            List.append("E2CB")
        elif i == "献":
            List.append("E2CC")
        elif i == "砦":
            List.append("E2CD")
        elif i == "隅":
            List.append("E2CE")
        elif i == "詩":
            List.append("E2CF")
        elif i == "吟":
            List.append("E2D0")
        elif i == "著":
            List.append("E2D1")
        elif i == "膠":
            List.append("E2D2")
        elif i == "占":
            List.append("E2D3")
        elif i == "百":
            List.append("E2D4")
        elif i == "傘":
            List.append("E2D5")
        elif i == "敢":
            List.append("E2D6")
        elif i == "惨":
            List.append("E2D7")
        elif i == "索":
            List.append("E2D8")
        elif i == "樹":
            List.append("E2D9")
        elif i == "林":
            List.append("E2DA")
        elif i == "遮":
            List.append("E2DB")
        elif i == "涼":
            List.append("E2DC")
        elif i == "粒":
            List.append("E2DD")
        elif i == "拍":
            List.append("E2DE")
        elif i == "楼":
            List.append("E2DF")
        elif i == "鎮":
            List.append("E2E0")
        elif i == "牧":
            List.append("E2E1")
        elif i == "朴":
            List.append("E2E2")
        elif i == "盾":
            List.append("E2E3")
        elif i == "核":
            List.append("E2E4")
        elif i == "皇":
            List.append("E2E5")
        elif i == "律":
            List.append("E2E6")
        elif i == "倶":
            List.append("E2E7")
        elif i == "幽":
            List.append("E2E8")
        elif i == "某":
            List.append("E2E9")
        elif i == "淑":
            List.append("E2EA")
        elif i == "六":
            List.append("E2EB")
        elif i == "冥":
            List.append("E2EC")
        elif i == "井":
            List.append("E2ED")
        elif i == "戸":
            List.append("E2EE")
        elif i == "懐":
            List.append("E2EF")
        elif i == "充":
            List.append("E2F0")
        elif i == "軟":
            List.append("E2F1")
        elif i == "冊":
            List.append("E2F2")
        elif i == "僚":
            List.append("E2F3")
        elif i == "弁":
            List.append("E2F4")
        elif i == "詞":
            List.append("E2F5")
        elif i == "督":
            List.append("E2F6")
        elif i == "滞":
            List.append("E2F7")
        elif i == "慕":
            List.append("E2F8")
        elif i == "嘆":
            List.append("E2F9")
        elif i == "溶":
            List.append("E2FA")
        elif i == "卸":
            List.append("E2FB")
        elif i == "兼":
            List.append("E2FC")
        elif i == "晰":
            List.append("E2FD")
        elif i == "煥":
            List.append("E2FE")
        elif i == "凡":
            List.append("E2FF")
        elif i == "釣":
            List.append("E343")
        elif i == "秋":
            List.append("E344")
        elif i == "洒":
            List.append("E345")
        elif i == "羊":
            List.append("E346")
        elif i == "呑":
            List.append("E347")
        elif i == "禄":
            List.append("E348")
        elif i == "狭":
            List.append("E349")
        elif i == "童":
            List.append("E34A")
        elif i == "贅":
            List.append("E34B")
        elif i == "沢":
            List.append("E34C")
        elif i == "需":
            List.append("E34D")
        elif i == "滑":
            List.append("E34E")
        elif i == "額":
            List.append("E34F")
        elif i == "袖":
            List.append("E350")
        elif i == "販":
            List.append("E351")
        elif i == "帳":
            List.append("E352")
        elif i == "簿":
            List.append("E353")
        elif i == "掠":
            List.append("E354")
        elif i == "陶":
            List.append("E355")
        elif i == "偵":
            List.append("E356")
        elif i == "患":
            List.append("E357")
        elif i == "症":
            List.append("E358")
        elif i == "咲":
            List.append("E359")
        elif i == "煎":
            List.append("E35A")
        elif i == "俊":
            List.append("E35B")
        elif i == "版":
            List.append("E35C")
        elif i == "又":
            List.append("E35E")
        elif i == "逝":
            List.append("E35F")
        elif i == "鎖":
            List.append("E360")
        elif i == "猿":
            List.append("E361")
        elif i == "窓":
            List.append("E362")
        elif i == "慨":
            List.append("E363")
        elif i == "俗":
            List.append("E364")
        elif i == "睨":
            List.append("E365")
        elif i == "競":
            List.append("E366")
        elif i == "紳":
            List.append("E367")
        elif i == "浪":
            List.append("E368")
        elif i == "癖":
            List.append("E369")
        elif i == "掴":
            List.append("E36A")
        elif i == "惚":
            List.append("E36B")
        elif i == "執":
            List.append("E36C")
        elif i == "彷":
            List.append("E36D")
        elif i == "徨":
            List.append("E36E")
        elif i == "楚":
            List.append("E36F")
        elif i == "尋":
            List.append("E370")
        elif i == "釈":
            List.append("E371")
        elif i == "札":
            List.append("E372")
        elif i == "秀":
            List.append("E373")
        elif i == "肥":
            List.append("E374")
        elif i == "雌":
            List.append("E375")
        elif i == "飢":
            List.append("E376")
        elif i == "繕":
            List.append("E377")
        elif i == "姓":
            List.append("E378")
        elif i == "墨":
            List.append("E379")
        elif i == "慰":
            List.append("E37A")
        elif i == "飽":
            List.append("E37B")
        elif i == "概":
            List.append("E37C")
        elif i == "免":
            List.append("E37D")
        elif i == "疫":
            List.append("E37E")
        elif i == "泥":
            List.append("E37F")
        elif i == "尻":
            List.append("E381")
        elif i == "脇":
            List.append("E382")
        elif i == "蒸":
            List.append("E383")
        elif i == "湿":
            List.append("E384")
        elif i == "澄":
            List.append("E385")
        elif i == "征":
            List.append("E386")
        elif i == "締":
            List.append("E387")
        elif i == "春":
            List.append("E388")
        elif i == "曇":
            List.append("E389")
        elif i == "捉":
            List.append("E38A")
        elif i == "剖":
            List.append("E38B")
        elif i == "謙":
            List.append("E38C")
        elif i == "群":
            List.append("E38D")
        elif i == "暇":
            List.append("E38E")
        elif i == "焦":
            List.append("E38F")
        elif i == "妥":
            List.append("E390")
        elif i == "俄":
            List.append("E391")
        elif i == "逮":
            List.append("E392")
        elif i == "拘":
            List.append("E393")
        elif i == "脅":
            List.append("E394")
        elif i == "潤":
            List.append("E395")
        elif i == "譲":
            List.append("E396")
        elif i == "肺":
            List.append("E397")
        elif i == "涯":
            List.append("E398")
        elif i == "摘":
            List.append("E399")
        elif i == "芽":
            List.append("E39A")
        elif i == "九":
            List.append("E39B")
        elif i == "撤":
            List.append("E39C")
        elif i == "勘":
            List.append("E39D")
        elif i == "融":
            List.append("E39E")
        elif i == "賭":
            List.append("E39F")
        elif i == "傾":
            List.append("E3A0")
        elif i == "匿":
            List.append("E3A1")
        elif i == "誠":
            List.append("E3A2")
        elif i == "‥":
            List.append("E3A3")
        elif i == "叔":
            List.append("E3A4")
        elif i == "浜":
            List.append("E3A5")
        elif i == "席":
            List.append("E3A6")
        elif i == "彩":
            List.append("E3A7")
        elif i == "頻":
            List.append("E3A8")
        elif i == "壮":
            List.append("E3A9")
        elif i == "液":
            List.append("E3AA")
        elif i == "墟":
            List.append("E3AB")
        elif i == "谷":
            List.append("E3AC")
        elif i == "膳":
            List.append("E3AD")
        elif i == "仁":
            List.append("E3AE")
        elif i == "盆":
            List.append("E3AF")
        elif i == "栽":
            List.append("E3B0")
        elif i == "培":
            List.append("E3B1")
        elif i == "欄":
            List.append("E3B2")
        elif i == "鬼":
            List.append("E3B3")
        elif i == "縄":
            List.append("E3B4")
        elif i == "梯":
            List.append("E3B5")
        elif i == "籠":
            List.append("E3B6")
        elif i == "京":
            List.append("E3B7")
        elif i == "凛":
            List.append("E3B8")
        elif i == "刊":
            List.append("E3B9")
        elif i == "漫":
            List.append("E3BA")
        elif i == "琢":
            List.append("E3BB")
        elif i == "刊":
            List.append("E3BC")
        elif i == "漫":
            List.append("E3BD")
        elif i == "摩":
            List.append("E3BE")
        elif i == "煉":
            List.append("E3BF")
        elif i == "刹":
            List.append("E3C0")
        elif i == "伯":
            List.append("E3C1")
        elif i == "蚊":
            List.append("E3C2")
        elif i == "脆":
            List.append("E3C3")
        elif i == "餌":
            List.append("E3C4")
        elif i == "桃":
            List.append("E3C5")
        elif i == "廷":
            List.append("E3C6")
        elif i == "掲":
            List.append("E3C7")
        elif i == "疎":
            List.append("E3C8")
        elif i == "沌":
            List.append("E3C9")
        elif i == "菓":
            List.append("E3CA")
        elif i == "翌":
            List.append("E3CB")
        elif i == "愕":
            List.append("E3CC")
        elif i == "釜":
            List.append("E3CD")
        elif i == "茹":
            List.append("E3CE")
        elif i == "針":
            List.append("E3CF")
        elif i == "沼":
            List.append("E3D0")
        elif i == "紀":
            List.append("E3D1")
        elif i == "礁":
            List.append("E3D2")
        elif i == "菓":
            List.append("E3D3")
        elif i == "寧":
            List.append("E3D4")
        elif i == "聡":
            List.append("E3D5")
        elif i == "舌":
            List.append("E3D6")
        elif i == "菓":
            List.append("E3D7")
        elif i == "畳":
            List.append("E3D8")
        elif i == "懲":
            List.append("E3D9")
        elif i == "契":
            List.append("E3DA")
        elif i == "肢":
            List.append("E3DB")
        elif i == "藤":
            List.append("E3DC")
        elif i == "α":
            List.append("E3DD")
        elif i == "β":
            List.append("E3DE")
        elif i == "禍":
            List.append("E3DF")
        elif i == "壷":
            List.append("E3E0")
        elif i == "馴":
            List.append("E3E1")
        elif i == "樺":
            List.append("E3E2")
        elif i == "貰":
            List.append("E3E3")
        elif i == "馳":
            List.append("E3E4")
        elif i == "掟":
            List.append("E3E5")
        elif i == "懇":
            List.append("E3E6")
        elif i == "嬉":
            List.append("E3E7")
        elif i == "挫":
            List.append("E3E8")
        elif i == "松":
            List.append("E3E9")
        elif i == "鼓":
            List.append("E3EA")
        elif i == "較":
            List.append("E3EB")
        elif i == "亀":
            List.append("E3EC")
        elif i == "貿":
            List.append("E3ED")
        elif i == "綿":
            List.append("E3EE")
        elif i == "邸":
            List.append("E3EF")
        elif i == "雇":
            List.append("E3F0")
        elif i == "烏":
            List.append("E3F1")
        elif i == "唄":
            List.append("E3F2")
        elif i == "剃":
            List.append("E3F3")
        elif i == "稿":
            List.append("E3F4")
        elif i == "椅":
            List.append("E3F5")
        elif i == "旺":
            List.append("E3F6")
        elif i == "託":
            List.append("E3F7")
        elif i == "盟":
            List.append("E3F8")
        elif i == "虐":
            List.append("E3F9")
        elif i == "覗":
            List.append("E3FA")
        elif i == "戯":
            List.append("E3FB")
        elif i == "撮":
            List.append("E3FC")
        elif i == "ヱ":
            List.append("E3FD")
        elif i == "泡":
            List.append("E441")
        elif i == "隕":
            List.append("E442")
        elif i == "磁":
            List.append("E443")
        elif i == "洩":
            List.append("E444")
        elif i == "窃":
            List.append("E445")
        elif i == "滴":
            List.append("E446")
        elif i == "虎":
            List.append("E447")
        elif i == "怨":
            List.append("E448")
        elif i == "凱":
            List.append("E449")
        elif i == "旦":
            List.append("E44A")
        elif i == "那":
            List.append("E44B")
        elif i == "崖":
            List.append("E44C")
        elif i == "ｅ":
            List.append("E44D")
        elif i == "ｙ":
            List.append("E44E")
        elif i == "ｔ":
            List.append("E44F")
        elif i == "ｏ":
            List.append("E450")
        elif i == "ｙ":
            List.append("E451")
        elif i == "ｈ":
            List.append("E452")
        elif i == "ｅ":
            List.append("E453")
        elif i == "ａ":
            List.append("E454")
        elif i == "ｒ":
            List.append("E455")
        elif i == "ｔ":
            List.append("E456")
        elif i == "妄":
            List.append("E457")
        elif i == "鼬":
            List.append("E458")
        elif i == "也":
            List.append("E459")
        elif i == "貌":
            List.append("E45A")
        elif i == "髭":
            List.append("E45B")
        elif i == "紛":
            List.append("E45C")
        elif i == "盤":
            List.append("E45E")
        elif i == "苛":
            List.append("E45F")
        elif i == "碧":
            List.append("E460")
        elif i == "桜":
            List.append("E461")
        elif i == "丼":
            List.append("E462")
        elif i == "迅":
            List.append("E463")
        elif i == "州":
            List.append("E464")
        elif i == "燥":
            List.append("E465")
        elif i == "軒":
            List.append("E466")
        else:
            List.append(i)
    return " ".join(List)
