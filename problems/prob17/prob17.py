nums = {
  1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five',
  6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten',
  11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen',
  15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen',
  19: 'nineteen', 20: 'twenty', 30: 'thirty', 40: 'forty', 50: 'fifty',
  60: 'sixty', 70: 'seventy', 80: 'eighty', 90: 'ninety'
}

for pre in [20,30,40,50,60,70,80,90]:
  for i in range(1, 10):
    nums[pre+i] = nums[pre] + nums[i]

for pre in range(1, 10):
  nums[100*pre] = nums[pre] + 'hundred'
  for i in range(1, 100):
    nums[100*pre+i] = nums[100*pre] + 'and' + nums[i]

nums[1000] = 'onethousand'

print sum(map(len, nums.values()))
