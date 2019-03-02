# Bidding Service
## This is bidding service written using flask. 
  ### Valid Bid Object 
    `{
        "bidPrice": 9,
        "currency": "USD",
        "id": "9d30a941-22bf-4709-8f9b-a90538b25eeb",
        "placementID": "121"
    }`


# Auction Service
## This is auction service written in go.
It has one endpoint which make concurrent requests to `bidding services`. The bids accepted in time are sorted by price in descending order and then returned.

# To run both the services
### Using docker-compose
run `docker-compose up`.

