def timeConvert(sec):
    h = sec // 3600
    s = sec % 3600
    m = s // 60 
    s = s % 60 
    print(f"{sec}초는 {h}시간 {m}분 {s}초입니다.")


timeConvert(12345)