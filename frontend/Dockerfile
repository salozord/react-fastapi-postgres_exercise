FROM node:18-alpine

ADD package.json /package.json

ENV NODE_PATH="/node_modules"
ENV PATH="/node_modules/.bin:$PATH"
RUN npm install

WORKDIR /front
ADD . /front

EXPOSE 8000

CMD ["npm", "start"]