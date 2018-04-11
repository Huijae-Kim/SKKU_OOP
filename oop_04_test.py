# make moving average function

def moving_average1(input, w_size=3):
  output=[]
  for i in range(0,(len(input)-w_size+1)):
    average = float(sum(input[i:(i+w_size)]))/float(w_size)
    output += [average]
  return output
