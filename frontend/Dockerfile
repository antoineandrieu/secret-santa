FROM node:18-alpine

RUN npm install -g pnpm

WORKDIR /app

COPY package*.json pnpm-lock.yaml ./

RUN pnpm install

COPY . .

# RUN pnpm run build

CMD ["npx", "vue-cli-service", "serve"]

EXPOSE 8080
