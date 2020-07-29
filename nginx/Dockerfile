FROM nginx

RUN rm /etc/nginx/conf.d/default.conf
COPY conf.d/default.conf /etc/nginx/conf.d/default.conf
RUN mkdir -p /var/www/web
COPY var/www/web/assets /var/www/web/assets
COPY ssl/cert.crt /etc/nginx/ssl/cert.crt
COPY ssl/cert.key /etc/nginx/ssl/cert.key
