# Multi-stage Dockerfile for DRISHTI-NER
FROM node:20-alpine AS build

WORKDIR /app

# Copy package descriptors
COPY package*.json ./

# Install dependencies
RUN npm install

# Copy source code and assets
COPY . .

# Build application
RUN npm run build

# Production Stage with static file serving
FROM node:20-alpine AS runner

WORKDIR /app

RUN npm install -g serve

COPY --from=build /app/dist ./dist
COPY --from=build /app/public ./public

EXPOSE 3000

ENV PORT=3000

CMD ["serve", "-s", "dist", "-l", "3000"]
