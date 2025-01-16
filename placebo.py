from pypinyin import pinyin, Style
import re
from hanzi_tools import hanzi_tools

def analyze_phonetics(name):
    """
    分析姓名的音韵特征，包括声母、韵母、声调和音节流畅性。
    """
    pinyin_list = pinyin(name, style=Style.NORMAL)
    
    # Split the pinyin into initials, finals and tones
    initials = []
    finals = []
    tones = []

    for pinyin_item in pinyin_list:
      
       
      if len(pinyin_item) > 0:
        pinyin_str = pinyin_item[0]
        match = re.match(r'([bpmfdtnlgkhjqxzcsryw])?([aeiouü][aeiounv]?([ng])?)([1-4])', pinyin_str)
        
        if match:
            initials.append(match.group(1) if match.group(1) else "无")
            finals.append(match.group(2) if match.group(2) else "无")
            tones.append(match.group(4) if match.group(4) else "无")
        else:
           initials.append("无")
           finals.append("无")
           tones.append("无")


    # 描述声母
    initial_descriptions = {
        "b": "双唇不送气清塞音，如'包'的声母。",
        "p": "双唇送气清塞音，如'跑'的声母。",
        "m": "双唇浊鼻音，如'猫'的声母。",
        "f": "唇齿清擦音，如'风'的声母。",
        "d": "舌尖中不送气清塞音，如'的'的声母。",
        "t": "舌尖中送气清塞音，如'他'的声母。",
        "n": "舌尖中浊鼻音，如'你'的声母。",
        "l": "舌尖中浊边音，如'了'的声母。",
        "g": "舌根不送气清塞音，如'哥'的声母。",
        "k": "舌根送气清塞音，如'可'的声母。",
        "h": "舌根清擦音，如'好'的声母。",
         "j": "舌面前不送气清塞擦音，如'鸡'的声母。",
        "q": "舌面前送气清塞擦音，如'七'的声母。",
        "x": "舌面前清擦音，如'西'的声母。",
        "z": "舌尖前不送气清塞擦音，如'在'的声母。",
         "c": "舌尖前送气清塞擦音，如'次'的声母。",
        "s": "舌尖前清擦音，如'三'的声母。",
         "r": "舌尖后浊擦音，如'日'的声母。",
         "zh": "舌尖后不送气清塞擦音，如'中'的声母。",
        "ch": "舌尖后送气清塞擦音，如'吃'的声母。",
         "sh": "舌尖后清擦音，如'是'的声母。",
        "y": "半元音，如'一'的声母。",
        "w": "半元音，如'五'的声母。",
        "无": "该字没有声母，属于零声母。"

    }
    
    final_descriptions = {
        "a": "开口呼，如'啊'的韵母。",
        "o": "开口呼，如'哦'的韵母。",
        "e": "开口呼，如'额'的韵母。",
        "i": "齐齿呼，如'衣'的韵母。",
         "u": "合口呼，如'乌'的韵母。",
        "ü": "撮口呼，如'鱼'的韵母。",
          "ai": "复韵母，如'爱'的韵母。",
        "ei": "复韵母，如'欸'的韵母。",
        "ao": "复韵母，如'奥'的韵母。",
        "ou": "复韵母，如'欧'的韵母。",
        "ia": "复韵母，如'呀'的韵母。",
        "ie": "复韵母，如'也'的韵母。",
        "io": "复韵母，如'哟'的韵母。",
        "iu": "复韵母，如'又'的韵母。",
         "üe": "复韵母，如'约'的韵母。",
          "ua": "复韵母，如'哇'的韵母。",
           "uo": "复韵母，如'我'的韵母。",
           "ui": "复韵母，如'为'的韵母。",
            "an": "鼻韵母，如'安'的韵母。",
            "en": "鼻韵母，如'恩'的韵母。",
            "in": "鼻韵母，如'音'的韵母。",
            "un": "鼻韵母，如'温'的韵母。",
            "ün": "鼻韵母，如'晕'的韵母。",
           "ang": "鼻韵母，如'昂'的韵母。",
             "eng": "鼻韵母，如'鞥'的韵母。",
           "ing": "鼻韵母，如'英'的韵母。",
           "ong": "鼻韵母，如'雍'的韵母。",
           "er": "卷舌韵母，如'儿'的韵母。",
           "无": "该字没有韵母，属于零韵母。"
     }
    
    tone_descriptions = {
       "1": "阴平，音调高而平，如'妈'的声调。",
        "2": "阳平，音调由低到高上升，如'麻'的声调。",
        "3": "上声，音调先下降后上升，如'马'的声调。",
        "4": "去声，音调由高到低下降，如'骂'的声调。",
       "无": "该字没有声调。"
    }
  
    
    first_initial = initials[0] if len(initials) > 0 else "无"
    first_final = finals[0] if len(finals) > 0 else "无"
    first_tone = tones[0] if len(tones) > 0 else "无"

    
    second_initials = initials[1:]
    second_finals = finals[1:]
    second_tones = tones[1:]

   
    
    
    initial_desc =  initial_descriptions.get(first_initial, "未知声母。")
    
    final_desc =  final_descriptions.get(first_final, "未知韵母。")
    
    tone_desc =  tone_descriptions.get(first_tone, "未知声调。")
    
    
    
    second_initial_descs = [initial_descriptions.get(x, "未知声母。") for x in second_initials]
    second_final_descs = [final_descriptions.get(x, "未知韵母。") for x in second_finals]
    second_tone_descs = [tone_descriptions.get(x, "未知声调。") for x in second_tones]
    
    
    
    # 评价音节流畅性（简化版本，可以根据实际情况调整）
    if len(pinyin_list) > 1:
        
      if len(second_initials) >0:
            initial_flow =  f"该名字的音节中，姓氏的声母是{first_initial}，如 '王伟' 中的 '王' 声母。名字的声母依次为{ '、'.join(second_initials)}。在发音上，声母之间的过渡比较自然。音韵搭配影响听觉美感，如'王伟'(Wang Wei) 音韵协调。"
      else:
            initial_flow =  f"该名字的音节中，姓氏的声母是{first_initial}，如 '王伟' 中的 '王' 声母。名字为单字，没有其他声母。"
      if len(second_finals) >0:
            final_flow = f"该名字的音节中，姓氏的韵母是{first_final}，如 '李娜' 中的 '李' 韵母。名字的韵母依次为{ '、'.join(second_finals)}。韵母之间的发音衔接整体流畅。韵母发音的搭配决定了名字读起来是否优美。 "
      else:
             final_flow =f"该名字的音节中，姓氏的韵母是{first_final}，如 '李娜' 中的 '李' 韵母。名字为单字，没有其他韵母。 "
    
      if len(second_tones) >0 :
        tone_flow = f"该名字的音节中，姓氏的声调是{first_tone}。名字的声调依次为{'、'.join(second_tones)}。声调的组合使得名字在读起来时有起伏，富有韵律感，如'李娜'(Li Na) 中'娜'字的上声与'李'字的阳平声搭配，音韵优美。"
      else:
         tone_flow = f"该名字的音节中，姓氏的声调是{first_tone}。名字为单字，没有其他声调。"
      
      overall_flow = initial_flow +  final_flow + tone_flow
    else:
      overall_flow = "该名字为单字，只有一个音节。"

    return {
        "声母": {
          "分析结果":{
              "姓声母": {
                  "声母": first_initial,
                  "描述": initial_desc
                },
              "名声母": [{"声母": x, "描述": y} for x,y in zip(second_initials,second_initial_descs)]
            }
        },
        "韵母": {
          "分析结果":{
              "姓韵母": {
                   "韵母": first_final,
                   "描述": final_desc
                },
              "名韵母": [{"韵母": x, "描述": y} for x,y in zip(second_finals,second_final_descs)]
           }
        },
        "声调": {
          "分析结果":{
              "姓声调": {
                   "声调": first_tone,
                    "描述": tone_desc
                },
              "名声调": [{"声调": x, "描述": y} for x,y in zip(second_tones, second_tone_descs)]
           }
        },
        "音节流畅性": {
          "分析结果": overall_flow
        }
    }

def analyze_strokes(name):
    """
    分析姓名的笔画特征，包括姓氏笔画数、名字笔画数和书写难易度。
    """
    
    stroke_counts = [hanzi_tools.count_strokes(char) for char in name]
    
    
    # 描述笔画数和笔画顺序
    def describe_stroke(char,count):
       
        order = hanzi_tools.get_stroke_order(char)
        
        if order:
            
             stroke_desc =  f"'{char}'字共有{count}画，笔画顺序为：{','.join(order)}。其结构特点包括：{hanzi_tools.get_structure(char)}。 字形结构影响名字书写的美观和难易程度，如'丁一' 字形简单,易于书写。"
        else:
            stroke_desc =  f"'{char}'字共有{count}画。获取笔画顺序失败。"
        return stroke_desc
    
    
    
    stroke_descriptions = [describe_stroke(char, count) for char, count in zip(name, stroke_counts)]
    
    
    first_stroke_desc = stroke_descriptions[0] if len(stroke_descriptions) > 0 else "没有姓氏"
    
    second_stroke_descs = stroke_descriptions[1:]
    
    
    # 评价书写难易度（简化版本，可以根据实际情况调整）
    total_strokes = sum(stroke_counts)
    
    
    if total_strokes > 15:
      difficulty_desc = "该名字整体笔画数较多，书写难度稍大，需要认真练习。"
    elif total_strokes > 10:
       difficulty_desc = "该名字整体笔画数中等，书写难度适中。"
    else:
        difficulty_desc = "该名字整体笔画数较少，书写较为容易。"
    
    
    if len(stroke_descriptions) > 1:
       structure_flow =  f"该名字中，姓氏的笔画数为{stroke_counts[0]}，如'丁一'中的'丁'。名字的笔画数依次为{ '、'.join(map(str, stroke_counts[1:]))}。书写上，建议注意字的结构，使之整体协调。字形结构影响名字书写的美观和难易程度，如'陈晨'字形对称，视觉上给人以美感。"
    else:
        structure_flow =  f"该名字为单字，笔画数为{stroke_counts[0]}，书写上，建议注意字的结构，使之整体协调。 "
    
    overall_difficulty_flow = structure_flow +  difficulty_desc
    
    return {
        "姓笔画数": {
           "分析结果": {
                "笔画描述": first_stroke_desc,
                "笔画数": stroke_counts[0] if len(stroke_counts) > 0 else "无"
            }
        },
        "名笔画数": {
             "分析结果": [{"笔画描述": x,"笔画数":y}  for x,y in zip(second_stroke_descs,stroke_counts[1:])]
        },
        "书写难易度": {
           "分析结果": overall_difficulty_flow
        }
    }


def analyze_personality(name):
    """
    根据名字的字义和文化背景，推测可能暗示的性格特征。
    """
    personality_traits = {
        "李": "常见姓氏，通常代表稳重和传统。",
        "海": "象征广阔的胸怀和包容性，可能暗示性格开朗、外向，如同“海阔”寓意“胸怀宽广如海”。",
        "生": "象征生命力，可能暗示活力、乐观。",
         "伟": "伟大，可能暗示有抱负和责任感。",
        "静": "安静，可能暗示内向、沉稳。",
         "勇": "勇敢，可能暗示果敢、坚强。",
          "杰": "杰出，可能暗示聪明、有才华。",
         "丽": "美丽，可能暗示优雅、有魅力。",
           "娜": "婀娜，可能暗示温柔、柔美。",
          "雪": "纯洁，可能暗示单纯、善良。",
           "婷": "美好，可能暗示漂亮、有气质。",
         "梓": "蓬勃，可能暗示生命力旺盛、积极向上。",
        "涵": "包容，可能暗示有内涵、有深度。",
         "宇": "广阔，可能暗示胸襟开阔、有远见。",
         "辰": "希望，可能暗示朝气蓬勃、有活力。",
           "墨": "文化，可能暗示有学识、有内涵，如同“墨宸”体现独特的搭配",
           "慧": "智慧，希望孩子聪明。",
          "悟" : "觉悟，与佛教有关",
         "禅":"禅宗，与佛教有关" ,
          "思":"思维敏捷",
         "俊":"英俊",
          "雅":"优雅"
    }
    
    
    name_traits = [personality_traits.get(char, "该字没有明显的性格暗示。") for char in name]
    
    
    
    
    
    # 生成性格描述
    if len(name) == 1 :
        overall_trait = f"该名字为单字，字义为{name_traits[0]}，可能暗示{name_traits[0]}。 名字往往寄托对孩子的期望，如“慧”寓意智慧。"
    elif len(name) == 2:
      overall_trait = f"该名字由姓氏'{name[0]}'和名字'{name[1]}'组成。姓氏可能暗示{name_traits[0]}，名字可能暗示{name_traits[1]}。 名字往往寄托对孩子的期望，如“思琪”寓意“思维敏捷”， “俊杰”寓意“英俊杰出”， “雅婷”寓意“优雅”。"
    else:
          overall_trait =  f"该名字由姓氏'{name[0]}'和名字'{name[1]}'、'{name[2]}'组成。姓氏可能暗示{name_traits[0]}, 名字可能暗示{name_traits[1]}和{name_traits[2]}。 名字往往寄托对孩子的期望，如“慧”寓意智慧， “勇”寓意勇敢, “宁”寓意平静。"

    return {
        "分析结果": overall_trait
    }


def analyze_cultural_connotation(name):
    """
    分析名字的文化内涵，包括字义的文化寓意和可能的典故引用。
    """
    cultural_meanings = {
        "李": {
            "寓意": "李姓是中国大姓之一，象征着家族的传承和繁荣，常与美好的品德联系在一起。",
            "典故": "老子姓李，被认为是道家学说的创始人。"
        },
          "海": {
            "寓意": "大海象征着广阔、深邃，寓意胸怀宽广，知识渊博，前途无量，如名字“海阔”寓意“胸怀宽广如海”。",
            "典故": "古代文学作品中，海常用来形容人的气度、志向，如“海纳百川，有容乃大”。"
        },
          "生": {
            "寓意": "生命、生长，寓意活力、希望，象征着朝气蓬勃。",
             "典故": "在中国传统文化中，生生不息是重要的哲学思想。"
        },
       "伟": {
            "寓意": "伟大，寓意有抱负，有理想，有责任感，希望孩子成为杰出人物。",
            "典故": "伟人，英雄，常指有卓越成就的人。"
        },
        "静": {
            "寓意": "安静，寓意内敛、沉稳，淡泊名利。",
            "典故": "静以修身，强调内心的平和与修养。"
        },
         "勇": {
            "寓意": "勇敢，寓意果敢、坚强，敢于面对困难。",
            "典故": "勇者无惧，强调勇气的重要性。"
        },
          "杰": {
            "寓意": "杰出，寓意才能出众，能力突出，希望孩子成为优秀人才。",
             "典故": "人中豪杰，指人群中的优秀人物。"
        },
          "丽": {
            "寓意": "美丽，寓意容貌姣好，有魅力，气质优雅。",
            "典故": "天生丽质，形容人天生美丽。"
        },
           "娜": {
            "寓意": "婀娜，寓意姿态优美，温柔动人。",
             "典故": "常用来形容女子身材苗条，姿态优雅。"
        },
           "雪": {
            "寓意": "雪花，寓意纯洁，高尚，冰清玉洁。",
            "典故": "雪梅，比喻坚贞不屈的品格。"
        },
          "婷": {
            "寓意": "美好，寓意姿态优美，气质高雅。",
             "典故": "亭亭玉立，形容女子身材修长，姿态优美。"
        },
         "梓": {
            "寓意": "梓树，寓意生机勃勃，茁壮成长。",
            "典故": "梓材，指可造就人才的良好材料。近年来，“子涵”，“梓轩”等名字因流行文化而变得流行"
        },
          "涵": {
            "寓意": "包容，寓意有内涵，有修养，有容人之量。",
             "典故": "涵养，指人的内在修养。"
        },
          "宇": {
            "寓意": "广阔，寓意胸襟开阔，有远见，有抱负。",
            "典故": "宇宙，象征无限的广阔空间。"
        },
        "辰": {
            "寓意": "时辰，寓意朝气蓬勃，希望，活力，近期流行“雨辰”等名字",
            "典故": "良辰美景，形容美好的时光。"
        },
         "墨":{
             "寓意":"文化，寓意有学识，有内涵，有修养。",
             "典故":"文房四宝，指笔、墨、纸、砚，是中国传统文化的象征。如'墨宸'体现独特的搭配"
        },
        "慧":"智慧，代表聪明",
       "悟":"觉悟",
        "禅":"禅宗",
         "思":"思维",
        "俊":"英俊",
       "雅":"优雅",
       "丹": "发音清晰，在国际上也易于接受",
      "明": "简单易记，适合在学校环境中使用",
    }
    
    
    meanings = []
    
    
    references = []
    
    for char in name:
        
       info = cultural_meanings.get(char, {"寓意":"该字文化寓意不明显", "典故":"该字没有明显的典故"})
       meanings.append(info["寓意"])
       references.append(info["典故"])

    return {
        "文化寓意": {
            "分析结果": [{"字":char, "寓意":meaning} for char, meaning in zip(name, meanings)]
        },
        "典故引用": {
           "分析结果": [{"字":char, "典故":reference} for char, reference in zip(name, references)]
        }
    }


def analyze_other_suggestions(name):
    """
    提供其他建议，包括五行八字和国际化考虑。
    """
    
    
    # Simplified five elements analysis
    
    five_elements = {
        "金": ["鑫", "钰", "铭", "锐", "锋"],
        "木": ["林", "森", "柏", "杨", "柳"],
        "水": ["淼", "清", "江", "河", "海"],
        "火": ["炎", "焱", "炫", "煜", "照"],
        "土": ["坤", "垚", "培", "基", "均"]
    }
    
    # 
    def check_elements(char):
        for element, words in five_elements.items():
            if char in words:
               return f"{char}，五行属{element}。选择名字时，可以考虑五行是否平衡。"
        return "该字没有明显的五行属性。"
    
    element_analysis = [check_elements(char) for char in name]
    
    element_result =  "。".join(element_analysis)
    
    
    
    # Internationalization consideration
    
    
    
    name_desc = []
    
    
    for char in name:
         pinyin_list = pinyin(char, style=Style.NORMAL)
         
         if len(pinyin_list) >0 :
          name_desc.append(f"'{char}'字在国际环境中，拼音为{pinyin_list[0][0]}，发音上较为简单，容易接受，如'李丹'在国际上也易于接受。")
         else:
              name_desc.append(f"'{char}'字在国际环境中，可能存在发音问题。")
    
    
    
    
    
    
    international_considerations = "".join(name_desc)
    
    if len(name) > 1:
        international_flow = f"该名字的国际化考虑，包括：{international_considerations}。"
    else:
        international_flow = f"该名字为单字，国际化考虑为:{international_considerations}。"
    
    
    
    return {
        "五行八字": {
          "分析结果": f"名字中的字五行属性为：{element_result}。结合五行八字来选择名字，是一种结合了中国传统命理学和命名习俗的方法。"
        },
        "国际化考虑": {
           "分析结果": international_flow
        }
    }


def analyze_common_mistakes(name):
    """
    检查名字中是否存在常见的起名错误，特别是针对非中文母语者。
    """
    
    
    
    
    has_surname = len(name) > 1 # simple check if name has more than 1 character
    is_transliteration = all(len(pinyin(char)) > 0 for char in name) #check if it has pinyin
    
   
    
    
    mistake_analysis = {
         "缺少姓氏": None if has_surname else "该名字缺少姓氏，中文名字通常由姓氏和名字组成。",
          "语音修辞": None,  # This would need more sophisticated check
                "书写复杂": None, # This needs to be integrate with stroke analysis
                "寓意单一": None, # This would need more sophisticated check
                "完全音译": None if not is_transliteration else "该名字为英文的直接音译，不符合中文名字的习惯。",
                "历史名人":None, # this would need to access to name database
                "昵称混淆": None, # This would need to be a name database
                "非正向谐音": None # This would need a dictionary to search and check
    }
    
    
    
    # check for negative sounding homophones
    
    homophone_check_result =  check_for_homophones(name)
   
    if  homophone_check_result:
         mistake_analysis["非正向谐音"] = f"该名字可能存在非正向谐音: {homophone_check_result}，需要注意避免谐音。"
    
    return {
       "分析结果":mistake_analysis
    }

def check_for_homophones(name):
    """
    Check the name for potential negative homophones.
    """
    
    homophone_dict = {
         "吴能":"无能",
         "思琪":"死气"
    }
    
    
    bad_homophones = []
    for char in homophone_dict.keys():
        if char in name:
             bad_homophones.append(f"{char} 与 {homophone_dict[char]} 谐音。")
            
    return ",".join(bad_homophones)



def analyze_overall_evaluation(name, phonetic_analysis, stroke_analysis, personality_analysis, cultural_analysis, other_analysis, common_mistakes):
    """
    综合以上所有分析，给出对名字的整体评价和建议。
    """
    
    
    overall_evaluation = f"""
    综合评价：
    姓名：{name}

    音韵分析：
    {phonetic_analysis['音节流畅性']['分析结果']}

    笔画分析：
    {stroke_analysis['书写难易度']['分析结果']}

    性格特征分析：
    {personality_analysis['分析结果']}

    文化内涵分析：
    文化寓意：{[item['寓意'] for item in cultural_analysis['文化寓意']['分析结果']]}
    典故引用：{[item['典故'] for item in cultural_analysis['典故引用']['分析结果']]}
    
    其他建议：
    {other_analysis['五行八字']['分析结果']}
    {other_analysis['国际化考虑']['分析结果']}
    
    常见错误检查：
    {common_mistakes['分析结果']}
    
    
    整体来看，该名字{name}，音韵流畅，易于书写，具有一定的文化内涵，适合作为中文名字使用。可以根据个人的具体情况，考虑进一步的修改或完善。 名字的选择还需考虑家族传统,如字辈等。同时, 名字的流行趋势也应该考虑，如近期流行的“子涵”，“雨辰”等名字。还要考虑个人偏好。
    """

    return {
      "分析结果": overall_evaluation
    }

# 示例
name = "李海生"
phonetic_analysis = analyze_phonetics(name)
stroke_analysis = analyze_strokes(name)
personality_analysis = analyze_personality(name)
cultural_analysis = analyze_cultural_connotation(name)
other_analysis = analyze_other_suggestions(name)
common_mistakes = analyze_common_mistakes(name)
overall_analysis = analyze_overall_evaluation(name, phonetic_analysis, stroke_analysis, personality_analysis, cultural_analysis, other_analysis, common_mistakes)
print(overall_analysis)


name = "小明"
phonetic_analysis = analyze_phonetics(name)
stroke_analysis = analyze_strokes(name)
personality_analysis = analyze_personality(name)
cultural_analysis = analyze_cultural_connotation(name)
other_analysis = analyze_other_suggestions(name)
common_mistakes = analyze_common_mistakes(name)
overall_analysis = analyze_overall_evaluation(name, phonetic_analysis, stroke_analysis, personality_analysis, cultural_analysis, other_analysis, common_mistakes)
print(overall_analysis)

name = "宝玉"
phonetic_analysis = analyze_phonetics(name)
stroke_analysis = analyze_strokes(name)
personality_analysis = analyze_personality(name)
cultural_analysis = analyze_cultural_connotation(name)
other_analysis = analyze_other_suggestions(name)
common_mistakes = analyze_common_mistakes(name)
overall_analysis = analyze_overall_evaluation(name, phonetic_analysis, stroke_analysis, personality_analysis, cultural_analysis, other_analysis, common_mistakes)
print(overall_analysis)


name = "Lucky"
phonetic_analysis = analyze_phonetics(name)
stroke_analysis = analyze_strokes(name)
personality_analysis = analyze_personality(name)
cultural_analysis = analyze_cultural_connotation(name)
other_analysis = analyze_other_suggestions(name)
common_mistakes = analyze_common_mistakes(name)
overall_analysis = analyze_overall_evaluation(name, phonetic_analysis, stroke_analysis, personality_analysis, cultural_analysis, other_analysis, common_mistakes)
print(overall_analysis)
