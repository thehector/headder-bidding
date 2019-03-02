FROM golang:latest 
RUN mkdir /auctions 
ADD . /auctions/ 
WORKDIR /auctions 
RUN go build -o main .
EXPOSE 8000
CMD ["/auctions/main"]
