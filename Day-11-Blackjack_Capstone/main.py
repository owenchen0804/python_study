
cards = [11,2,3,4,5,6,7,8,9,20,10,10,10]

import random
from art import logo

def deal_card():
    """"Returns a random card from the deck"""
    return random.choice(cards)

def calculate_score(cards):
    """Take a list of cards and return the score calculated from the cards"""

    #1 特殊情况，正好2张牌且为21点
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    #2 特殊情况
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

#   注意！只在is_game_over为True了之后才退出游戏的
#   所以要完全跳出play_game()之后才会进入到调用compare()的阶段！
def compare(user_score, computer_score):
    if user_score > 21 and computer_score > 21:
        return "You went over. You lose! 😤"
    if user_score == computer_score:
        return "Draw 🙃"
    if computer_score == 0:
        return "You lose, opponenet has Blackjack 😱"
    if user_score == 0:
        return "Win with a Blackjack 😎"
    if user_score > 21:
        return "You went over. You lose 😭"
    if computer_score > 21:
        return "Opponent went over. You win 😁"
    if user_score > computer_score:
        return "You win 😃"
    return "You lose 😤"

def play_game():
    # 作为一个每次run的时候执行的function，不需要代入参数
    # 只要is_game_over不为True就会继续执行
    print(logo)

    user_cards = []
    computer_cards = []
    is_game_over = False

    # 每次先给user & computer各发两张牌
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    # 如果is_game_over为False就继续这个循环
    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"    Your cards: {user_cards}, current score: {user_score}")
        #   根据规则只会展示computer手牌的第一张
        print(f"    Computer's first card: {computer_cards[0]}")

        # 如果出现了BJ或者爆炸了就直接game over:
        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            #   如果走到这里说明没有提前结束，那么要问user是否继续加牌
            user_should_deal = input("Type 'y' to get another card, or type 'n' to pass: ")
            if user_should_deal == 'y':
                user_cards.append(deal_card())
            else:
                is_game_over = True
    
    #   走到这里说明user的操作已经全部结束了，也就是is_game_over一定已经为True
    #   接下来再是根据庄家的规则，小于 7点必须继续加牌，否则可以停止发牌
    while computer_socre != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        #   注意每次发完牌要再计算一下电脑手牌的总数
        computer_score = calculate_score(computer_cards)

    #   跳出上面的while后，进入到结算环节，这时候才会进入compare()的调用阶段！

    #   公布所有的牌型
    print(f"    Your final hand: {user_cards}, final score: {user_score}")
    print(f"    Computer's final hand: {computer_cards}, final score: {computer_score}")

    print(compare(user_score, computer_score=))

    #   最后的最后，问玩家还要不要继续
    while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == 'y':
        play_game().