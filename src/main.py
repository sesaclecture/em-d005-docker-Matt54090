# 문제 1.
#
# Docker 이미지를 다운로드하는 명령어를 생성하세요. => pull
#
# image_name은 다운로드할 Docker 이미지 이름입니다.
def make_docker_pull_command(image_name):
    return f"docker pull {image_name}"


# 문제 2.
#
# Docker 컨테이너를 실행하는 명령어를 생성하세요. => run
#
# image_name은 실행할 Docker 이미지 이름입니다.
def make_docker_run_command(image_name):
    return f"docker run {image_name}"


# 문제 3.
#
# Port Mapping이 포함된 Docker 실행 명령어를 생성하세요.
#
# host_port는 호스트 PC 포트 번호입니다.
# container_port는 컨테이너 내부 포트 번호입니다.
#
# Docker에서 사용하는 Port Mapping 옵션을 활용하세요.
# -p 옵션 : -p 8080:80 -> 호스트 포트:컨테이너 포트 순서대로
def make_port_mapping_command(
    image_name,
    host_port,
    container_port,
):
    return f"docker run -p {host_port}:{container_port} {image_name}"


# 문제 4.
#
# Volume Mapping이 포함된 Docker 실행 명령어를 생성하세요. -> Volume Mapping이란 폴더 공유
#
# host_dir은 호스트 PC 디렉토리입니다.
# container_dir은 컨테이너 내부 디렉토리입니다.
#
# Docker에서 사용하는 Volume Mapping 옵션을 활용하세요.
# -v 옵션 : -v /home/pi/data:/data -> 호스트의 pi data 디렉토리를 컨테이너의 /data로 연결
def make_volume_mapping_command(
    host_dir,
    container_dir,
    image_name,
):
    return f"docker run -v {host_dir}:{container_dir} {image_name}"


# 문제 5.
#
# Docker Compose Service 내용을 생성하세요.
#
# service_name은 서비스 이름입니다.
# image_name은 Docker 이미지 이름입니다.
# host_port는 호스트 포트 번호입니다.
# container_port는 컨테이너 포트 번호입니다.
#
# 반환값은 docker-compose.yml 일부 내용이라고 가정합니다.
# yaml 파일은 들여쓰기 주의
#
# image 와 ports 항목을 포함해야 합니다.
def make_compose_service(
    service_name,           # 서비스 이름
    image_name,             # 사용할 이미지
    host_port,              # 포트 목록(호스트)
    container_port,         # 포트 목록(컨테이너)
):
    return f"""{service_name}:
   image: {image_name}
   ports:
     - "{host_port}:{container_port}"
"""
