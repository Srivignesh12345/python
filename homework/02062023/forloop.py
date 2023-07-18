max_tickets=100
ticket_price=100
sold_tickets=0
while sold_tickets < max_tickets:
    print("there are",max_tickets-sold_tickets,"are available")
    num_tickets=int(input("how many tickets you need,tell me:  "))
if num_tickets> max_tickets - sold_tickets:
    print("Sorry i dont have enough tickets....")
else:
    total_price=num_tickets*ticket_price
    print("you have bought",num_tickets,"the tickets costs $",total_price)
    sold_tickets+=num_tickets
print("the tickets are over,thankyou for your business")        