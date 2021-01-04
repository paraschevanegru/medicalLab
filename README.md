## Medical Laboratory GUI

### Installation

The GUI requires:
- Python 3.7+
- Tkinter
- cx_Oracle
- docker

#### Run Oracle Standard Edition 12c Release 2

```
# Create a new local directory for storing data
mkdir -p oracle/data

# Pull docker image https://github.com/MaksymBilenko/docker-oracle-12c.git
docker pull quay.io/maksymbilenko/oracle-12c

# Run docker image. It might take a few minutes to start it. You can follow using docker ps and docker logs -f container_id
# Where container_id can be obtained from docker ps
docker run -d -p 8080:8080 -p 1521:1521 -v $PWD/oracle/data:/u01/app/oracle -e DBCA_TOTAL_MEMORY=2048 quay.io/maksymbilenko/oracle-12c

# View that container has started
docker ps
```
#### Run medicalgui
```
git clone https://github.com/paraschevanegru/medicalLab.git
pip install -r requirements.txt
pip install ./medicalLab

medicalgui  # launches graphical tool
```
