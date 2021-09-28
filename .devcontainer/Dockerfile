# linprog.fsu.edu runs on CentoOS 7
FROM centos:7

# dev tools
# git2 is not included in yum's default repository set
RUN yum -y install https://packages.endpoint.com/rhel/7/os/x86_64/endpoint-repo-1.9-1.x86_64.rpm
RUN yum -y install git 

# runtime dependencies
# ideally all of these should also be present on linprog
# make sure to ssh in and check before installing anything in the container
RUN yum -y install python3

