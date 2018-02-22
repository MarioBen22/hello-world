#Mario Benavides
#Program Status - Completed
# This program asks users how many cookies they want and displays the amount of ingredients needed.

# number of cookies desired
cookies=input('Enter number of cookies: ')

#calculations
x=(int(cookies))
sugar=(x/48)*1.5
butter=(x/48)*1
flour=(x/48)*2.75

#answer
print('You need '+ '{:.2f}'.format(sugar)+' cups of sugar, '
      + '{:.2f}'.format(butter)+' cups of butter,' ' and '
      + '{:.2f}'.format(flour)+' cups of flour.')
