FROM mhart/alpine-node AS base

FROM base AS builder
WORKDIR /install
COPY package.json .
RUN npm install --prefix=/install

FROM base
COPY --from=builder /install/node_modules/ /usr/lib/node_modules/
WORKDIR /app
COPY src/ .
COPY bin/ .
EXPOSE 3000
ENTRYPOINT ["node", "www"]
