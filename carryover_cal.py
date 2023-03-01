import re

from hoshino import Service

sv_help='''
计算返还时间下的时间轴。
[转秒 <返还时间> <时间轴>] 返还时间后必须换行
可接受的时间格式：以65秒为例，“065”，“65s”，“105”，“1:05”，“01：05”等均可。
例：输入       返回
“转秒 35       “35秒的时间轴：
119 公主凯露    0:24 公主凯露
1:13 似似花     0:18 似似花
01：05	露娜    0:10 露娜
0058 春花       0:03 春花“
54 水电”
'''.strip()
sv = Service('转秒', bundle='pcr查询', help_=sv_help)

def check_time(time):
    time = int(time)
    if time < 90:
        return time
    elif 99 < time < 130:
        return time - 40
    else:
        return -1

def add_zero(num):
    if num < 10:
        return '0' + str(num)
    return str(num)

@sv.on_prefix(('转秒', '补偿计算', '补时计算'))
async def carryover_cal(bot, ev):
    lines = ev.message.extract_plain_text().split('\n') 
    match = re.match(r'\d+[:：]?\d*', lines[0].strip())
    if match is not None:
        time = check_time(match.group().replace(':', '').replace('：',''))
        if time < 20:
            time == -1
        if time != -1:
            diff = 90 - time
            if time > 59:
                ftime = f'1分{add_zero(time % 60)}秒'
            else:
                ftime = f'{time}秒'
            newlines = [f'{ftime}的时间轴：']
            for line in lines[1:]:
                match = re.match(r'^\s*(\d+[:：]?\d*)', line)
                if match is not None:
                    tl = check_time(match.group(1).replace(':', '').replace('：',''))
                    if tl != -1:
                        if tl >= diff:
                            tl -= diff
                            newtime = str(tl // 60) + ':' + add_zero(tl % 60)
                            newlines.append(line.replace(match.group(1), newtime))
                        else:
                            newlines.append('其余操作未在区间内，已忽略。')
                            break
                    else:
                        newlines.append(line)
                else:
                    newlines.append(line)
            await bot.send(ev, '\n'.join(newlines), at_sender=True)
        else:
            await bot.send(ev, '返还时间不合法或为满补时，请核对后重试。', at_sender=True)
    else:
        await bot.send(ev, '未能获取返还时间，请核对后重试。', at_sender=True)
