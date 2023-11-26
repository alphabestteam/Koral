FROM tomcat

EXPOSE 8080

RUN mv webapps webapps2
RUN mv webapps.dist/ webapps

CMD ["catalina.sh", "run"]
