FROM lecafard/nsjail-ctf

WORKDIR /home/ctf
COPY nsjail.sh /home/ctf/
COPY src/ /home/ctf/chal
EXPOSE 1337/tcp
CMD ["/home/ctf/nsjail.sh"]
