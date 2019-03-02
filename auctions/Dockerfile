FROM golang:latest
RUN go get github.com/gorilla/mux
RUN mkdir /auctions
ADD . /auctions/
WORKDIR /auctions
=======
FROM golang:latest 
RUN mkdir /auctions 
ADD . /auctions/ 
WORKDIR /auctions 
>>>>>>> e763c2a4fef0d0a870f30e47f74ba1d2a2cc38b9
RUN go build -o main .
EXPOSE 8000
CMD ["/auctions/main"]
