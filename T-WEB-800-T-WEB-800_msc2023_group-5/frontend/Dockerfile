FROM node:17-alpine3.14

LABEL description="This is docker for frontend Epic Road Trip"

WORKDIR /app

COPY ["package.json", "package-lock.json", "./"]

RUN npm install

COPY . .

CMD ["npm", "start"]