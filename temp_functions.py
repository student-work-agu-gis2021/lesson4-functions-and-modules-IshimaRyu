"""今まで作ってきた関数を一つのファイルに入れた"""
def celsius_to_fahr(temp_fahrenheit):
  """華氏をtemp_fahrenheitに代入すると摂氏に変化して、その値を返す"""
  converted_temp=9/5 * temp_fahrenheit +32
  return converted_temp
  
def temp_classifier(temp_celsius):
  """クラス分けしたい摂氏をtemp_celsiusに代入すると、その温度を4つのクラスのどこかに分ける"""
  if temp_celsius<-2:
    return 0
  elif temp_celsius>=-2 and temp_celsius<2:
    return 1
  elif temp_celsius>=2 and temp_celsius<15:
    return 2
  elif temp_celsius>=15:
    return 3