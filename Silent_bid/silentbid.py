import os
print("=======WELCOME TO SILENT BIDDER========")

def highest_bidder(bid_info):
    highest=0
    winner=""
    for find in bid_info:
        bidder_price=bid_info[find]
        if bidder_price > highest:
            highest=bidder_price
            winner=find                 
    print(f"highest bidder is '{winner}' with bidding price of '{highest}' ")        


bid_info={
}
end_bidding=False

while not end_bidding:
    name=input("Enter your name : ")
    bid_price=int(input("Enter your bid price : "))
    bid_info[name]=bid_price

    choice=input("Are there any more bidders ? Type yes or no : ").lower()

    if choice == 'no':
        highest_bidder(bid_info)
        end_bidding=True
    elif choice == 'yes':
        os.system('cls')    
