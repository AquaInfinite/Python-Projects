from pygal import *

def main():
  with open('PYTHON PROJECTS/practice/python class/pygal/bacteria bar/bacteria.csv', 'r') as f:
    data = f.readlines()

  #data is holding a list of strings

  coupon_count = {}
  
  for line in data:
    clean_data = line.strip().split(',')
    print(clean_data)
    coupon = clean_data[0]

    if coupon in coupon_count:
      coupon_count[coupon] += 1
    else:
      coupon_count[coupon] = 1
  
  coupon_chart = Bar(width = 1600, height = 1000, title = 'Bacteria Coupons')
  
  for coupon, count in coupon_count.items():
      coupon_chart.add(coupon, count)

  coupon_chart.render_in_browser()

main()