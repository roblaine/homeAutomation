FROM mhart/alpine-node:latest

COPY . /app
RUN cd app && npm install
CMD ["node", "/app/bin/www"]
