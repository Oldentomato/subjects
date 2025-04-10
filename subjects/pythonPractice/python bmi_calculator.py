
def bmiCalc(w,h):
    print(f"""
체중(kg): {w}
키(cm): {h}
BMI: {round(w / (h/100)**2, 1)}
""")
    

bmiCalc(70,175)
