#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Author: PythonDeveloper29042
@AuthorEmail: pythondeveloper29042@outlook.com
@ProjectName: ChineseIdiomLearner
@RepositoryName: ChineseIdiomLearner
@GitHubRepository: https://github.com/PythonDeveloper29042/ChineseIdiomLearner.git
@Version: 1.0
@CommitDate: October 29, 2024
"""

from jionlp import chinese_idiom_loader
import random
import pyttsx3
from xpinyin import Pinyin

# 初始化文本转语音引擎
tts_engine = pyttsx3.init()
tts_engine.setProperty("rate", 150)  # 设置语速

# 加载成语词典
idioms_dic = chinese_idiom_loader()
idioms = list(idioms_dic.keys())


def idiom_to_pinyin(idiom: str) -> str:
    """
    将给定的成语转换为拼音表示。

    Args:
        idiom (str): 要转换的成语。

    Returns:
        str: 成语的拼音表示。
    """
    return Pinyin().get_pinyin(idiom, "-", True)


def query_idiom():
    """
    成语查询功能，用户输入成语，程序返回拼音、解释及发音。
    """
    print("🔍 欢迎使用成语查询功能！让我们开始探索吧！")
    while True:
        idiom = input("请输入你要查询的成语或输入 0 结束 🛑: ")
        if idiom == "0":
            print("🛑 查询结束，欢迎再来！")
            break
        meaning = idioms_dic.get(idiom)
        if meaning:
            print(f"🎉 成语: {idiom}")
            print(f"🔠 拼音: {idiom_to_pinyin(idiom)}")
            print(f"📖 解释: {meaning['explanation']}")
            print("🔊 正在发音, 请仔细聆听!")
            tts_engine.say(idiom)
            tts_engine.runAndWait()
            print("发音完成!")
        else:
            print("😅 你要查询的不是一个成语! 再试一次吧!")


def guessing_game(max_attempts: int = 3):
    """
    猜成语游戏，程序随机选择一个成语并隐藏其中一个字，用户需要猜出被隐藏的字。

    Args:
        max_attempts (int): 用户可以尝试猜的最大次数。默认值为3。
    """
    score = 0
    print("🎮 欢迎来到猜成语游戏！准备好大显身手了吗？")
    while True:
        idiom = random.choice(idioms)
        meaning = idioms_dic[idiom]["explanation"]
        attempts = 0

        while attempts < max_attempts:
            hidden_index = random.randint(0, len(idiom) - 1)
            hidden_idiom = idiom[:hidden_index] + "X" + idiom[hidden_index + 1 :]
            correct_char = idiom[hidden_index]
            guess = input(f"🔎 {hidden_idiom} - {meaning} 💡 X是什么? ")

            if guess == correct_char:
                print(f'🎉 恭喜你回答正确! 成语是 "{idiom}"! 👏👏')
                score += 4 if attempts == 0 else 2
                print(f"✨ 你获得了{score}分! 继续加油!")
                break
            else:
                attempts += 1
                if attempts >= max_attempts:
                    print(f'😬 正确的成语是 "{idiom}"，没有成功，但不要气馁！💪')
                    score -= 1
                else:
                    print(f"❌ 答错了! 你还有 {max_attempts - attempts} 次机会! 😅")

        print(f"📊 你现在的分数是 {score} 分.")
        continue_game = input("🎲 再玩一局吗?\n[1] 继续 🎉\n[0] 退出 🛑\n")
        if continue_game == "0":
            print("🛑 游戏结束，感谢你的参与!")
            break


def main():
    """
    主函数，提供选择功能菜单，用户可以选择查询成语或玩猜成语游戏。
    """
    choice = input("请问你要实现什么功能呢? 🤔\n[1] 查询成语 📚\n[2] 猜成语游戏 🎮\n")
    try:
        choice = int(choice)
    except ValueError:
        print("⚠️ 请输入有效的选项 (1 或 2)。")
        return

    if choice == 1:
        query_idiom()
    elif choice == 2:
        guessing_game()
    else:
        print("⚠️ 无效选项，请输入 1 或 2。")


if __name__ == "__main__":
    main()
