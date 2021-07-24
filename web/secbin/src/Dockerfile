FROM node:14

COPY . /var/www/app
WORKDIR /var/www/app
EXPOSE 2010
ENV PORT 90
RUN echo "NEWBIE{1m491n3_54y1N9_1T5_uH4x0r4bL3}" >> /etc/passwd

RUN npm install
RUN mkdir uploads/

CMD [ "node", "index.js" ]

