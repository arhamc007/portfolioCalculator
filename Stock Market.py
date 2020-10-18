total=100000
AAPL=400
AMZ=200
OMW=150
ashare=100
bshare=100
#round 1
x= input (" did user buy AAPL stocks in round 1?  yes or no " )
if x == "yes" :
    bought= int(input("Please enter the number of shares bought "))
    ashare=ashare + bought
    total = total - (bought*AAPL)
    print ("Your total after purchasing is ", total, " with ", ashare, " shares of AAPL")

y= input (" did user sell AAPL stocks in round 1?  yes or no " )
if y == "yes" :
    sold= int(input("Please enter the number of shares sold "))
    ashare=ashare - sold
    total = total + (sold*AAPL)
    print ("Your total after purchasing is ", total, " with ", ashare, " shares of AAPL")
x= input (" did user buy AMZ stocks in round 1?  yes or no " )
if x == "yes" :
    bought= int(input("Please enter the number of shares bought "))
    bshare=bshare+bought
    total = total - (bought*AMZ)
    print ("Your total after purchasing is ", total, " with ", bshare, " shares of AMZ")
y= input (" did user sell AMZ stocks in round 1?  yes or no " )
if y == "yes" :
    sold= int(input("Please enter the number of shares sold "))
    bshare=bshare-sold
    total = total + (sold*AMZ)
    print ("Your total after purchasing is ", total, " with ", bshare, " shares of AMZ")
#round 2
    
AAPL=500
AMZ= 1700
x= input (" did user buy AAPL stocks in round 2?  yes or no " )
if x == "yes" :
    bought= int(input("Please enter the number of shares bought "))
    ashare=ashare+bought
    total = total - (bought*AAPL)
    print ("Your total after purchasing is ", total, " with ", ashare, " shares of AAPL")
    
y= input ("did user sell AAPL stocks in round 2?  yes or no " )
if y == "yes" :
    sold= int(input("Please enter the number of shares sold "))
    ashare=ashare - sold
    total = total + (sold*AAPL)
    print ("Your total after purchasing is ", total, " with ", ashare, " shares of AAPL")

#Round 3
AAPL = 700
AMZ=1200
x= input (" did user buy AAPL stocks in round 3?  yes or no " )
if x == "yes" :
    bought= int(input("Please enter the number of shares bought "))
    ashare=ashare+bought
    total = total - (bought*AAPL)
    print ("Your total after purchasing is ", total, " with ", ashare, " shares of AAPL")
    
y= input ("did user sell AAPL stocks in round 3?  yes or no " )
if y == "yes" :
    sold= int(input("Please enter the number of shares sold "))
    ashare=ashare - sold
    total = total + (sold*AAPL)
    print ("Your total after purchasing is ", total, " with ", ashare, " shares of AAPL")
#END
print ("Your total cash is ", total, " with ", ashare, " shares of AAPL and ", bshare, "shares of AMZ")

total= total + (ashare*AAPL) + (bshare*AMZ)
print ("total portfolio value is ", total)








