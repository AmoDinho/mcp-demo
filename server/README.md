# MCP Calculator

A server application exposing a calculator tool through the Model Context Protocol (MCP).

## Description

This project implements a calculator service that can be accessed through the Model Context Protocol. It's built using TypeScript and Express.js to provide a robust and type-safe implementation.

## Prerequisites

- Node.js (v14 or later recommended)
- npm (v6 or later recommended)

## Installation

Clone the repository and install the dependencies:

```
git clone https://github.com/yourusername/mcp-calculator.git
cd mcp-calculator
npm install
```

## Available Commands

Build the project:

```
yarn run build
```

This compiles the TypeScript code to JavaScript in the dist directory.

Start the server:

```
yarn run start
```

Runs the compiled server from the dist directory.

Development mode:

```
yarn run dev
```

Runs the server in development mode with automatic reloading.

## How to test the server

From an MCP server repository
To inspect an MCP server implementation, there's no need to clone this repo. Instead, use npx. For example, if your server is built at src/server.ts:

```
npx @modelcontextprotocol/inspector node src/server.ts
```

License

MIT
