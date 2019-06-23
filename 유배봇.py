import discord
import asyncio
import random
import os

client = discord.Client()


@client.event
async def on_ready():
    print("login")
    print(client.user.name)
    print(client.user.id)
    print("----------------")
    await client.change_presence(game=discord.Game(name='유배봇 !도움말', type=1))


@client.event
async def on_message(message):
    #if message.content.startswith('!명령어'):
        #await client.send_message(message.channel, " 저는 날씨 팀나누기 긴급소식 게임추천 서비스 유배봇 닉네임 경고도움말 사다리타기 주사위 메뉴추천 (!를 앞에 쓰셔야 합니다!) 이라는 명령어가 있어요")
    if message.content.startswith('!초무'):
        await client.send_message(message.channel, "```피방에서의 최대시간 13시간 유저```")
    if message.content.startswith('!솔드'):
        await client.send_message(message.channel, "```스타2 맞구라 유저```")
    if message.content.startswith('!환이'):
        await client.send_message(message.channel,"```환이형```")
    if message.content.startswith('!돼지'):
        await client.send_message(message.channel, "```초무님의 그림자입니다.```")
    if message.content.startswith('!퓨아'):
        await client.send_message(message.channel, "```알려주셔서 감사합니다!```")
    if message.content.startswith('!정인'):
        await client.send_message(message.channel, "```일본 갔다가 돌아왔다는 사람입니다.(정비공)```")
    if message.content.startswith('!아싸킹'):
        await client.send_message(message.channel, "```동정마법사까지 몇년 안남았다...```")
    if message.content.startswith('!마루'):
        await client.send_message(message.channel, "```Streamer Member```")
    if message.content.startswith('!??'):
        await client.send_message(message.channel, "```?? ??? ????? ??? ??? ????! ???? ?? ???? ???!!```")
    if message.content.startswith('!머기업'):
        await client.send_message(message.channel, "```카트 고인물```")
    if message.content.startswith('!이기중'):
         await client.send_message(message.channel, "```오락실 가는 사람```")
    if message.content.startswith('!콩나물'):
        await client.send_message(message.channel, "```디코방1위 맴버입니다.```")
    if message.content.startswith('!카제로시스트'):
        await client.send_message(message.channel, "```2019-01-14일에 들어온 희귀한 사람```")
    if message.content.startswith('!류'):
        await client.send_message(message.channel, "```FPS의 신이자 전설을 가지고 있는 살아있는 신화 ```")
    if message.content.startswith('!윈치아'):
        await client.send_message(message.channel, "```ꥪힷퟤ```")
    if message.content.startswith('!prosty'):
        await client.send_message(message.channel, "```노틸주위를 떠다니는 신비한 유성.```")
    if message.content.startswith('!맹달'):
        await client.send_message(message.channel, "```보름달```")
    if message.content.startswith('!유배봇'):
        await client.send_message(message.channel, "```쿨타임을 집어넣어 볼까 생각중입니다. (언제나 업데이트를 가지는 유배봇! 열심히할게요!```")
    if message.content.startswith('!경고도움말'):
        await client.send_message(message.channel, "```아직 미완성 구역입니다.대단히죄송합니다.ㅠ.ㅠ```")
    if message.content.startswith('!닉네임'):
        await client.send_message(message.channel, "```닉네임 앞에 !를 붙이고 사용할수 있습니다. 현재 음식 분쇄기 맹달 그 카제로시스트 윈치아 류 콩나물 이기중 머기업 ?? 마루 아싸킹 정인 퓨아 돼지 환이 솔드 초무 님을 사용할수 있습니다.```")
    if message.content.startswith('!사다리타기'):
        await client.send_message(message.channel, "```아직 미완성 구역입니다.대단히죄송합니다.ㅠ.ㅠ```")
    if message.content.startswith('!주사위'):
        await client.send_message(message.channel, "```아직 미완성 구역입니다.대단히죄송합니다.ㅠ.ㅠ```")
    if message.content.startswith('!컨텐츠'):
        await client.send_message(message.channel, "```현재 지원하지않은 서비스 입니다.```")
    if message.content.startswith('!메뉴추천'):
        await client.send_message(message.channel, "``` 현재 라면뭐먹지 음료수뭐먹지 과자뭐먹지 라는 메뉴가 있습니다.```")
    if message.content.startswith('!서비스'):
        await client.send_message(message.channel, "```현재 가능한 서비스는 팀나누기 날씨 게임추천 메뉴추천 닉네임 유배봇입니다.```")
    if message.content.startswith('!긴급소식'):
        await client.send_message(message.channel, "```이제 시험임```")
    if message.content.startswith('!게임추천'):
        await client.send_message(message.channel, "```현재 모든게임 스팀게임 블리자드게임 카카오게임 를 서비스 하고 있습니다. ```")
    if message.content.startswith('!오늘오전날씨'):
        await client.send_message(message.channel, "```아직 업데이트가 되지 않았습니다.```")
    if message.content.startswith('!오늘오후날씨'):
        await client.send_message(message.channel, "```아직 업데이트가 되지 않았습니다.```")
    if message.content.startswith('!내일오전날씨'):
        await client.send_message(message.channel, "```아직 업데이트가 되지 않았습니다.```")
    if message.content.startswith('!내일오후날씨'):
        await client.send_message(message.channel, "```아직 업데이트가 되지 않았습니다.```")
    if message.content.startswith('!날씨'):
        await client.send_message(message.channel, "```현재 오늘오전날씨 오늘오후날씨 내일오전날씨 내일오후날씨 기능이 있습니다```")
    if message.content.startswith('!팀나누기'):
        await client.send_message(message.channel, "```팀을 나누는 방법은 a b c d/1 1 2 2 입니다```")
    if message.content.startswith('!분쇄기'):
        await client.send_message(message.channel, "```System Coding Error ```")
    if message.content.startswith('!미니언'):
        await client.send_message(message.channel, "```Streamer Member```")
    if message.content.startswith('!무배봇'):
        await client.send_message(message.channel, "```동생입니다.```")
    if message.content.startswith('!도움말'):
        await client.send_message(message.channel, "```1.작동하는 기능을 알아보시려면 서비스 기능을```")
    ("```2.서비스 기능을 모든 명령어를 알아보시려면 명령어 기능을```")
    ("```3.음식에 대해서 알아보고 싶으시면 메뉴추천기능을```")
    ("```4.팀나누는 기능을 알아보시려면 팀나누기 기능을```")
    ("```5.사람들의 닉네임 기능을 알아보시려면 닉네임 기능을```")
    ("```6.날씨 기능을 알아보시려면 날씨 기능을```")
    ("```7.사다리타기 기능을 알아보시려면 사다리타기 기능을```")
    ("```8.게임추천을 받으시려면 게임추천기능을```")
    ("```9.컨텐츠에 대해서 알아보시려면 컨텐츠 기능을```")
    ("```10.주사위게임을 하시려면 주사위 기능을```")
    ("```11.나중에 추후 업데이트 될겁니다.```")

    if message.content.startswith('!라면뭐먹지'):
        food = "삼양 너구리 진라면 짜파게티 순한진짬뽕 매운진짬뽕 신라면 참깨라면 스낵면 불닭볶음면 비빔면"
        foodchoice = food.split(" ")
        foodnumber = random.randint(1, len(foodchoice))
        foodesult = foodchoice[foodnumber-1]
        await client.send_message(message.channel, foodesult)
    if message.content.startswith('!음료수뭐먹지'):
        food = "밀키스 코코팜 포카리스웨트 토레타 콜라 사이다 환타"
        foodchoice = food.split(" ")
        foodnumber = random.randint(1, len(foodchoice))
        foodesult = foodchoice[foodnumber - 1]
        await client.send_message(message.channel, foodesult)
    if message.content.startswith('!과자뭐먹지'):
        food = "양파링 포스틱 포카칩 오징어칩 "
        foodchoice = food.split(" ")
        foodnumber = random.randint(1, len(foodchoice))
        foodesult = foodchoice[foodnumber - 1]
        await client.send_message(message.channel, foodesult)

    if message.content.startswith('!스팀게임'):
        food = "카스글옵 배틀그라운드 문명 돈스타브 레식 아이작 스타듀밸리"
        foodchoice = food.split(" ")
        foodnumber = random.randint(1, len(foodchoice))
        foodesult = foodchoice[foodnumber - 1]
        await client.send_message(message.channel, foodesult)
    if message.content.startswith('!블리자드게임'):
        food = "김도형과스타2맞구라 스타2 오버워치 히오스 블랙옵스"
        foodchoice = food.split(" ")
        foodnumber = random.randint(1, len(foodchoice))
        foodesult = foodchoice[foodnumber - 1]
        await client.send_message(message.channel, foodesult)
    if message.content.startswith('!카카오게임'):
        food = "배틀그라운드"
        foodchoice = food.split(" ")
        foodnumber = random.randint(1, len(foodchoice))
        foodesult = foodchoice[foodnumber - 1]
        await client.send_message(message.channel, foodesult)
    if message.content.startswith('!모든게임'):
        food = "배틀그라운드 김도형과스타2맞구라 스타2 오버워치 히오스 블랙옵스 카스글옵 배틀그라운드 문명 돈스타브 레식 아이작 스타듀밸리"
        foodchoice = food.split(" ")
        foodnumber = random.randint(1, len(foodchoice))
        foodesult = foodchoice[foodnumber - 1]
        await client.send_message(message.channel, foodesult)

    if message.content.startswith('!팀나누기'):
        team = message.content[6:]
        peopleteam = team.split("/")
        people = peopleteam[0]
        team = peopleteam[1]
        person = people.split(" ")
        teamname = team.split(" ")
        random.shuffle(teamname)
        for i in range(0, len(person)):
         await client.send_message(message.channel, person[i] + "---->" + teamname[i])

    #여기는 다른 사람들이 용도로 쓰는 곳 입니다.

    if message.content.startswith('#라면뭐먹지'):
       food = "삼양 너구리 진라면 짜파게티 순한진짬뽕 매운진짬뽕 신라면 참깨라면 스낵면 불닭볶음면"
       foodchoice = food.split(" ")
       foodnumber = random.randint(1, len(foodchoice))
       foodesult = foodchoice[foodnumber-1]
       await client.send_message(message.channel, foodesult)
    if message.content.startswith('#음료수뭐먹지'):
        food = "밀키스 코코팜 포카리스웨트 토레타 콜라 사이다 환타"
        foodchoice = food.split(" ")
        foodnumber = random.randint(1, len(foodchoice))
        foodesult = foodchoice[foodnumber - 1]
        await client.send_message(message.channel, foodesult)
    if message.content.startswith('#과자뭐먹지'):
        food = "양파링 포스틱 포카칩 오징어칩 "
        foodchoice = food.split(" ")
        foodnumber = random.randint(1, len(foodchoice))
        foodesult = foodchoice[foodnumber - 1]
        await client.send_message(message.channel, foodesult)

    if message.content.startswith('#스팀게임'):
        food = "카스글옵 배틀그라운드 문명 돈스타브 레식 아이작 스타듀밸리"
        foodchoice = food.split(" ")
        foodnumber = random.randint(1, len(foodchoice))
        foodesult = foodchoice[foodnumber - 1]
        await client.send_message(message.channel, foodesult)
    if message.content.startswith('#블리자드게임'):
        food = "스타2 오버워치 히오스 블랙옵스"
        foodchoice = food.split(" ")
        foodnumber = random.randint(1, len(foodchoice))
        foodesult = foodchoice[foodnumber - 1]
        await client.send_message(message.channel, foodesult)
    if message.content.startswith('#카카오게임'):
        food = "배틀그라운드"
        foodchoice = food.split(" ")
        foodnumber = random.randint(1, len(foodchoice))
        foodesult = foodchoice[foodnumber - 1]
        await client.send_message(message.channel, foodesult)
    if message.content.startswith('#모든게임'):
        food = "배틀그라운드 스타2 오버워치 히오스 블랙옵스 카스글옵 배틀그라운드 문명 돈스타브 레식 아이작 스타듀밸리 OSU"
        foodchoice = food.split(" ")
        foodnumber = random.randint(1, len(foodchoice))
        foodesult = foodchoice[foodnumber - 1]
        await client.send_message(message.channel, foodesult)

    if message.content.startswith('#팀나누기'):
        team = message.content[6:]
        peopleteam = team.split("/")
        people = peopleteam[0]
        team = peopleteam[1]
        person = people.split(" ")
        teamname = team.split(" ")
        random.shuffle(teamname)
        for i in range(0, len(person)):
         await client.send_message(message.channel, person[i] + "---->" + teamname[i])

    if message.content.startswith('#게임추천'):
        await client.send_message(message.channel, "현재 모든게임 스팀게임 블리자드게임 카카오게임 를 서비스 하고 있습니다. ")
    if message.content.startswith('#전국날씨'):
        await client.send_message(message.channel, "https://search.naver.com/search.naver?where=nexearch&query=%EC%A0%84%EA%B5%AD%EB%82%A0%EC%94%A8&ie=utf8&sm=tab_she&qdt=0")
    if message.content.startswith('#날씨'):
        await client.send_message(message.channel, "현재 전국날씨 기능이 있습니다")
    if message.content.startswith('#팀나누기'):
        await client.send_message(message.channel, "팀을 나누는 방법은 a b c d/1 1 2 2 입니다")
    if message.content.startswith('#메뉴추천'):
        await client.send_message(message.channel, "현재 라면뭐먹지 음료수뭐먹지 과자뭐먹지 라는 메뉴가 있습니다.")
    if message.content.startswith('#서비스'):
        await client.send_message(message.channel, "현재 가능한 서비스는 팀나누기 날씨 게임추천 메뉴추천 유배봇입니다.")
    if message.content.startswith('#사다리타기'):
        await client.send_message(message.channel, "아직 미완성 구역입니다.대단히죄송합니다.ㅠ.ㅠ")
    if message.content.startswith('#주사위'):
        await client.send_message(message.channel, "아직 미완성 구역입니다.대단히죄송합니다.ㅠ.ㅠ")
    if message.content.startswith('#컨텐츠'):
        await client.send_message(message.channel, "현재 지원하지않은 서비스 입니다.")
    if message.content.startswith('#명령어'):
        await client.send_message(message.channel," 저는 날씨 팀나누기 긴급소식 게임추천 서비스 유배봇 경고도움말 사다리타기 주사위 메뉴추천 (#를 앞에 쓰셔야 합니다!) 이라는 명령어가 있어요")
    if message.content.startswith('#유배봇'):
        await client.send_message(message.channel, "쿨타임을 집어넣어 볼까 생각중입니다.")
    if message.content.startswith('#경고도움말'):
        await client.send_message(message.channel, "아직 미완성 구역입니다.대단히죄송합니다.ㅠ.ㅠ")

access_token = os.environ["Bot_TOKEN"]
client.run(access_token')
