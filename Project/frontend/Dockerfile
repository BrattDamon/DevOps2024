# Use Node.js 16 with Alpine
FROM node:16-alpine

# Set the working directory inside the container
WORKDIR /app

# Copy package.json and package-lock.json first
COPY package.json package-lock.json /app/

# Install npm dependencies
RUN npm install

# Copy the rest of the code
COPY . /app/

# Build the React app
RUN npm run build

# Expose port 80 for web access
EXPOSE 3000

# Start the React app
CMD ["npm", "run", "start"]
