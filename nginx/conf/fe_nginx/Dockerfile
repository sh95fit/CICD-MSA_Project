# nginx/Dockerfile
FROM nginx:1.23.2-alpine

# Nginx 설정 파일 복사
COPY nginx.conf /etc/nginx/nginx.conf

# 빌드된 React 파일 복사
# COPY --from=build /app/dist/ /usr/share/nginx/html
VOLUME /usr/share/nginx/html

# Nginx 시작 명령
CMD ["nginx", "-g", "daemon off;"]