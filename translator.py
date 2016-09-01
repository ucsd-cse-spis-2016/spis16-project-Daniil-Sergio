from translate import Translator


langDict = {'English': "en",
            'Spanish': "es",
            'Russian': "ru",
            'Chinese': "zh",
            'Korean': "ko",
            'French': "fr",
            'Gujarati': "gu",
            'Indonesian': "in",
            'Irish': "ga",
            'Japanese': "ja",
            'Punjabi': "pa",
            'Tagalog': "tl",
            'Urdu': "ur",
            'Vietnamese': "vi"}
wordDict = {'English': "English",
            'Spanish': "español",
            'Russian': "русский",
            'Chinese': "中文",
            'Korean': "한국어",
            'French': "français",
            'Gujarati': "ગુજરાતી",
            'Indonesian': "bahasa Indonesia",
            'Irish': "Gaeilge",
            'Japanese': "日本語",
            'Punjabi': "ਪੰਜਾਬੀ ਦੇ",
            'Tagalog': "tagalog",
            'Urdu': "اردو",
            'Vietnamese': "Tiếng Việt"}
            
def transStr(language):
    for l in langDict:
        if language == l:
            translator = Translator(to_lang=langDict[language])
            transword = wordDict[l]
            translation = translator.translate("You and your partner can both speak")
            print translation + ' ' + transword
