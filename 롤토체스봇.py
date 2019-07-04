import discord


client = discord.Client()


@client.event
async def on_ready():
    print("login")
    print(client.user.name)
    print(client.user.id)
    print("----------------")
    await client.change_presence(game=discord.Game(name='퓨아가 만든 롤토체스 !도움말', type=1))


@client.event
async def on_message(message):
    #if message.content.startswith('!도움말'):
     #   await client.send_message(message.channel, "```아이템이름+아이템이름(@@+##)// !종족 능력```")
    if message.content.startswith('뒤집개+BF'):
        await client.send_message(message.channel, "```요우무```")
    if message.content.startswith('뒤집개+곡궁'):
        await client.send_message(message.channel, "```검사```")
    if message.content.startswith('뒤집개+조끼'):
        await client.send_message(message.channel, "```기사```")
    if message.content.startswith('뒤집개+지팡이'):
        await client.send_message(message.channel, "```마법사```")
    if message.content.startswith('뒤집개+여눈'):
        await client.send_message(message.channel, "```악마```")
    if message.content.startswith('뒤집개+체력'):
        await client.send_message(message.channel, "```빙하```")
    if message.content.startswith('뒤집개+망토'):
        await client.send_message(message.channel, "```루난의 허리케인(적 두명 추가공격 50% 대미지)```")
    if message.content.startswith('체력+BF'):
        await client.send_message(message.channel, "```지크의 전령(주변 아군 공속+10%)```")
    if message.content.startswith('체력+곡궁'):
        await client.send_message(message.channel, "```거드라(광역피해 최대HP 10%)```")
    if message.content.startswith('체력+조끼'):
        await client.send_message(message.channel, "```적 화상피해(치유불가)```")
    if message.content.startswith('체력+망토'):
        await client.send_message(message.channel, "```서풍(적 5초간 추방)```")
    if message.content.startswith('체력+지팡이'):
        await client.send_message(message.channel, "```모렐(화상피해 치유불가)```")
    if message.content.startswith('체력+여눈'):
        await client.send_message(message.channel, "```구원(사망시 근처아군 HP+1000)```")
    if message.content.startswith('여눈+BF'):
        await client.send_message(message.channel, "```쇼진의창(스킬 시전 후 공격시 마나 +15%)```")
    if message.content.startswith('여눈+곡궁'):
        await client.send_message(message.channel, "```스태틱(3타마다 광역피해)```")
    if message.content.startswith('여눈+조끼'):
        await client.send_message(message.channel, "```얼어붙은 건틀릿(적 공속 20% 감소)```")
    if message.content.startswith('여눈+망토'):
        await client.send_message(message.channel, "```침묵(공격시 침묵)```")
    if message.content.startswith('여눈+지팡이'):
        await client.send_message(message.channel, "```루덴의 메아리(마법공격시 광역피해)```")
    if message.content.startswith('여눈+여눈'):
        await client.send_message(message.channel, "```대천사의 지팡이(마법 시전시 마나 +20)```")
    if message.content.startswith('지팡이+BF'):
        await client.send_message(message.channel, "```총검(가한 피해의 25% 체력회복)```")
    if message.content.startswith('지팡이+곡궁'):
        await client.send_message(message.channel, "```구인수(공격속도 +3% (중첩))```")
    if message.content.startswith('지팡이+조끼'):
        await client.send_message(message.channel, "```솔라리 팬던트(주변 아군 방어막 획득)```")
    if message.content.startswith('지팡이+망토'):
        await client.send_message(message.channel, "```이온 충격기(적 스킬 사용시 피해)```")
    if message.content.startswith('망토+BF'):
        await client.send_message(message.channel, "```피바라기(가한 피해의 35% 체력회복)```")
    if message.content.startswith('망토+조끼'):
        await client.send_message(message.channel, "```파쇄검(공격시 무장 해제)```")
    if message.content.startswith('망토+곡궁'):
        await client.send_message(message.channel, "```저주 받은 칼날(공격시 적 강등)```")
    if message.content.startswith('조끼+BF'):
        await client.send_message(message.channel, "```수호천사(부활(HP 500))```")
    if message.content.startswith('조끼+곡궁'):
        await client.send_message(message.channel, "```유령무희(치명타 회피)```")
    if message.content.startswith('곡궁+BF'):
        await client.send_message(message.channel, "```신성의 검(치명타 확률 초당 +5%)```")


    if message.content.startswith('BF+뒤집개'):
        await client.send_message(message.channel, "```요우무```")
    if message.content.startswith('곡궁+뒤집개'):
       await client.send_message(message.channel, "```검사```")
    if message.content.startswith('조끼+뒤집개'):
        await client.send_message(message.channel, "```기사```")
    if message.content.startswith('지팡이+뒤집개'):
        await client.send_message(message.channel, "```마법사```")
    if message.content.startswith('여눈+뒤집개'):
        await client.send_message(message.channel, "```악마```")
    if message.content.startswith('체력+뒤집개'):
        await client.send_message(message.channel, "```빙하```")
    if message.content.startswith('뒤집개+뒤집개'):
        await client.send_message(message.channel, "```슬롯+1칸```")
    if message.content.startswith('망토+뒤집개'):
        await client.send_message(message.channel, "```루난의 허리케인(적 두명 추가공격 50% 대미지)```")
    if message.content.startswith('BF+체력'):
        await client.send_message(message.channel, "```지크의 전령(주변 아군 공속+10%)```")
    if message.content.startswith('곡궁+체력'):
        await client.send_message(message.channel, "```거드라(광역피해 최대HP 10%)```")
    if message.content.startswith('조끼+체력'):
        await client.send_message(message.channel, "```적 화상피해(치유불가)```")
    if message.content.startswith('망토+체력'):
        await client.send_message(message.channel, "```서풍(적 5초간 추방)```")
    if message.content.startswith('지팡이+체력'):
        await client.send_message(message.channel, "```모렐(화상피해 치유불가)```")
    if message.content.startswith('여눈+체력'):
        await client.send_message(message.channel, "```구원(사망시 근처아군 HP+1000)```")
    if message.content.startswith('체력+체력'):
        await client.send_message(message.channel, "```워모그(매초 체력 3% 회복)```")
    if message.content.startswith('BF+여눈'):
        await client.send_message(message.channel, "```쇼진의창(스킬 시전 후 공격시 마나 +15%)```")
    if message.content.startswith('곡궁+여눈'):
        await client.send_message(message.channel, "```스태틱(3타마다 광역피해)```")
    if message.content.startswith('조끼+여눈'):
        await client.send_message(message.channel, "```얼어붙은 건틀릿(적 공속 20% 감소)```")
    if message.content.startswith('망토+여눈'):
        await client.send_message(message.channel, "```침묵(공격시 침묵)```")
    if message.content.startswith('지팡이+여눈'):
        await client.send_message(message.channel, "```루덴의 메아리(마법공격시 광역피해)```")

    if message.content.startswith('BF+지팡이'):
        await client.send_message(message.channel, "```총검(가한 피해의 25% 체력회복)```")
    if message.content.startswith('곡궁+지팡이'):
        await client.send_message(message.channel, "```구인수(공격속도 +3% (중첩))```")
    if message.content.startswith('조끼+지팡이'):
        await client.send_message(message.channel, "```솔라리 팬던트(주변 아군 방어막 획득)```")
    if message.content.startswith('망토+지팡이'):
        await client.send_message(message.channel, "```이온 충격기(적 스킬 사용시 피해)```")
    if message.content.startswith('지팡이+지팡이'):
        await client.send_message(message.channel, "```라바돈(주문력+50)```")
    if message.content.startswith('BF+망토'):
        await client.send_message(message.channel, "```피바라기(가한 피해의 35% 체력회복)```")
    if message.content.startswith('조끼+망토'):
        await client.send_message(message.channel, "```파쇄검(공격시 무장 해제)```")
    if message.content.startswith('망토+망토'):
        await client.send_message(message.channel, "```용의 발톱(마법저항 83%)```")
    if message.content.startswith('곡궁+망토'):
        await client.send_message(message.channel, "```저주 받은 칼날(공격시 적 강등)```")
    if message.content.startswith('BF+조끼'):
        await client.send_message(message.channel, "```수호천사(부활(HP 500))```")
    if message.content.startswith('곡궁+조끼'):
        await client.send_message(message.channel, "```유령무희(치명타 회피)```")
    if message.content.startswith('조끼+조끼'):
        await client.send_message(message.channel, "```가시갑옷(받은 피해 35% 반사)```")
    if message.content.startswith('BF+곡궁'):
        await client.send_message(message.channel, "```신성의 검(치명타 확률 초당 +5%)```")
    if message.content.startswith('곡궁+곡궁'):
        await client.send_message(message.channel, "```고속연사포(공격범위 2배 적 회피불가)```")
    if message.content.startswith('BF+BF'):
        await client.send_message(message.channel, "```무한의대검(치명타 피해 +100%)```")

#이쪽은 시너지표 입니다.
    if message.content.startswith('!명령어'):
        await client.send_message(message.channel, "```종족 시너지표 확인과 아이템 조합 확인할수 있습니다.```")
    if message.content.startswith('!악마'):
        await client.send_message(message.channel, "```바루스 엘리스 모르가나 아트록스 이블린 브랜드 스웨인```")
    if message.content.startswith('!빙하'):
        await client.send_message(message.channel, "```리산드라 브라움 볼리베어 애쉬 세주아니 애니비아```")
    if message.content.startswith('!제국'):
        await client.send_message(message.channel, "```다리우스 카타리나 드레이븐 스웨인```")
    if message.content.startswith('!귀족'):
        await client.send_message(message.channel, "```가렌 베인 피오라 루시안 레오나 케일```")
    if message.content.startswith('!해적'):
        await client.send_message(message.channel, "```그레이브즈 파이크 갱플랭크 미스 포춘```")
    if message.content.startswith('!야생'):
        await client.send_message(message.channel, "```니달리 워윅 아리 렝가 나르```")
    if message.content.startswith('!로봇'):
        await client.send_message(message.channel, "```블리츠크랭크```")
    if message.content.startswith('!용'):
        await client.send_message(message.channel, "```쉬바나 아우리솔```")
    if message.content.startswith('!추방자'):
        await client.send_message(message.channel, "```야스오```")
    if message.content.startswith('!닌자'):
        await client.send_message(message.channel, "```쉔 제드 케넨 아칼리```")
    if message.content.startswith('!유령'):
        await client.send_message(message.channel, "```모데카이저 킨드레드 카서스```")
    if message.content.startswith('!공허'):
        await client.send_message(message.channel, "```카사딘 카직스 렉사이 초가스```")
    if message.content.startswith('!유령'):
        await client.send_message(message.channel, "```트리스타나 룰루 베이가 뽀삐 케넨 나르```")

    if message.content.startswith('!제국 능력'):
        await client.send_message(message.channel, "```랜덤 한 명의 사령관은 두 배의 대미지를 가함 ```")
    if message.content.startswith('!제국 능력'):
        await client.send_message(message.channel, "```(2) 랜덤 한 명의 사령관  (4) 모든 사령관 ```")
    if message.content.startswith('!귀족 능력'):
        await client.send_message(message.channel, "```랜덤 아군 한 명의 방어력 +100 및 공격시 35 체력 회복```")
    if message.content.startswith('!귀족 능력'):
        await client.send_message(message.channel, "```(3) 랜덤 아군 한 명    (6) 모든 아군```")
    if message.content.startswith('!기사 능력'):
        await client.send_message(message.channel, "```기사는 20 대미지 무시```")
    if message.content.startswith('!기사 능력'):
        await client.send_message(message.channel, "```(2) 20의 피해량 방어 (4) 40의 피해량 방어 (6) 60의 피해량 방어```")
    if message.content.startswith('!야생 능력'):
        await client.send_message(message.channel, "```야생 종족이 공격시 분노가 쌓이며(최대 5회) 분노 스택당 7%의 공격 속도 증가```")
    if message.content.startswith('!야생 능력'):
        await client.send_message(message.channel, "```(2) 야생 종족에만 적용  (4) 모든 아군에게 적용```")
    if message.content.startswith('!닌자 능력'):
        await client.send_message(message.channel, "```닌자는 정확히 한 명 또는 네명일떄만 효과를 받음```")
    if message.content.startswith('!닌자 능력'):
        await client.send_message(message.channel, "```(1) 닌자 공격력 +40%  (4) 모든 닌자 공격력 +60% ```")
    if message.content.startswith('!유령 능력'):
        await client.send_message(message.channel, "```(2) 전투 시작시 랜덤 적 한 명에게 체력이 100으로 설정되는 저주를 시전```")
    if message.content.startswith('!공허 능력'):
        await client.send_message(message.channel, "```(3) 아군의 기본 공격은 적의 방어를 50% 무시```")
    if message.content.startswith('!빙하 능력'):
        await client.send_message(message.channel, "```공격시 일정 확률로 적을 2초간 스턴```")
    if message.content.startswith('!빙하 능력'):
        await client.send_message(message.channel, "```(2) 25% 확률로 스턴 (4) 35% 확률로 스턴 (6) 45% 확률로 스턴```")
    if message.content.startswith('!로봇 능력'):
        await client.send_message(message.channel, "```(1) 로봇은 최대 마나로 전투 시작```")
    if message.content.startswith('!용 능력'):
        await client.send_message(message.channel, "```(2) 용 종족은 마법 피해 면역```")
    if message.content.startswith('!악마 능력'):
        await client.send_message(message.channel, "```악마가 공격시 일정 확률로 상대의 마나를 전소시키고, 전소된 만큼 트루 대미지를 입힘```")
    if message.content.startswith('!악마 능력'):
        await client.send_message(message.channel, "```(2) 30% 확률로 마나 전소 (4) 50% 확률로 마나 전소 (6) 70% 확률로 마나 전스 ```")
    if message.content.startswith('!해적 능력'):
        await client.send_message(message.channel, "```(3) 다른 플레이어와의 전투 이후 0~4 골드를 추가로 획득```")
    if message.content.startswith('!야생 능력'):
        await client.send_message(message.channel, "```공격시 분노가 쌓이며(최대 5회) 분노 스택당 7%의 공격 속도 증가```")
    if message.content.startswith('!야생 능력'):
        await client.send_message(message.channel, "```(2) 야생 종록에만 적용 (4) 모든 아군에게 적용```")
    if message.content.startswith('!요들 능력'):
        await client.send_message(message.channel, "```아군 요들족은 일정 확률로 공격 회피 ```")
    if message.content.startswith('!요들 능력'):
        await client.send_message(message.channel, "```(3) 20% 확률로 회피 (6) 50% 확률로 회피```")




client.run('NTk1OTMwNzY0MDMwMjQ2OTQx.XRyQPQ.huXEHEYWl5IAyiPLcjiRtYlVwjw')


access_token = os.environ["Bot_TOKEN"]
client.run(access_token')
