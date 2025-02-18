FROM maven:3.8.4-openjdk-17-slim

COPY entrypoint.sh /usr/local/bin/entrypoint.sh
RUN apt-get update
RUN apt-get install dos2unix
RUN dos2unix /usr/local/bin/entrypoint.sh && chmod +x /usr/local/bin/entrypoint.sh

#Start application
WORKDIR /usr/src/app-server
ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]
CMD ["bash"]
