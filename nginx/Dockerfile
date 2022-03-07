FROM nginx:latest

RUN apt-get update && apt-get -y install vim

#COPY ./nginx.conf /etc/nginx/
#COPY ./sites-available/sampleproject.conf /etc/nginx/sites-available/

#RUN mkdir -p /etc/nginx/sites-enabled/\
#    && ln -s /etc/nginx/sites-available/sampleproject.conf /etc/nginx/sites-enabled/

#EXPOSE 80
#CMD ["nginx", "-g", "daemon off;"]

#FROM nginx:latest
#
#RUN apt-get update && apt-get -y install vim
#
#RUN mkdir -p /etc/nginx/sites-enabled/ \
#    mkdir -p /etc/nginx/sites-available/
#
#COPY default.conf /etc/nginx/sites-available/
#
#RUN ln -s /etc/nginx/sites-available/default.conf /etc/nginx/sites-enabled/

#CMD ['nginx', '-g', 'daemon off;']

#EXPOSE 80
#COPY ./nginx.conf /etc/nginx/sites-available/
#COPY ./nginx-app.conf /etc/nginx/nginx.conf
#RUN mkdir -p /etc/nginx/sites-enabled/\
#    && ln -s /etc/nginx/sites-available/nginx-app.conf /etc/nginx/sites-enabled/