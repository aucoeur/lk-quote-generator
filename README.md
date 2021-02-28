# 'Degen-erated' Quotes from Letterkenny
Simple implementation of NLP with Markov chains written in Python using scripts from S1-S6 Letterkenny as the corpus data. Dockerized and deployed with CapRover :]

## Build
`docker build -t tweetgen_lk-docker .`

## Run
`docker run -p 5000:5000 --rm --name tweetgen_lk-docker tweetgen_lk-docker`

## Health Check
 Sending `GET` request to `/health` should return `{ "Status" : "200 OK" }`
