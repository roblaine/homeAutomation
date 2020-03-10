FROM mhart/alpine-node AS base

FROM base AS builder
WORKDIR /install
COPY package.json .
RUN npm install --prefix=/install

FROM base
COPY --from=builder /install/node_modules/ /usr/lib/node_modules/
ENV NODE_PATH '/usr/lib/node_modules:/src/node_modules'

WORKDIR /src
ADD src/ .
ADD bin/ ./bin/
ADD .env.sample .
EXPOSE 3000
ENTRYPOINT sh
# ENTRYPOINT ["node", "/src/bin/www"]
