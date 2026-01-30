# -------- build stage --------
FROM node:20-alpine AS build-stage

ARG API_URL=http://localhost:8000
ENV VITE_API_URL=$API_URL

WORKDIR /app

COPY package.json package-lock.json ./
run npm ci

COPY . .
RUN npm run build
# outputs to /app/dist (Vite default)

# -------- runtime stage --------
from nginx:alpine

COPY --from=build-stage /app/dist /usr/share/nginx/html
COPY nginx.conf /etc/nginx/conf.d/default.conf

EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]