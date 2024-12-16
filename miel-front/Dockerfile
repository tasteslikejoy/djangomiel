FROM node:22.12.0

WORKDIR /app

COPY package*.json /app/

RUN npm install

COPY . /app

EXPOSE 3000

WORKDIR /app/miel-front

CMD ["npm", "run", "dev"]