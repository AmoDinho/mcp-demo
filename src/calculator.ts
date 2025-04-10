import { ToolDefinition } from '@modelcontextprotocol/sdk';

// Define the calculator tool
export const calculatorTool: ToolDefinition = {
  name: 'calculator',
  description: 'Perform basic arithmetic operations',
  parameters: {
    type: 'object',
    properties: {
      operation: {
        type: 'string',
        enum: ['add', 'subtract', 'multiply', 'divide'],
        description: 'The operation to perform',
      },
      a: {
        type: 'number',
        description: 'First operand',
      },
      b: {
        type: 'number',
        description: 'Second operand',
      },
    },
    required: ['operation', 'a', 'b'],
  },
  handler: async (params) => {
    const { operation, a, b } = params;

    switch (operation) {
      case 'add':
        return { result: a + b };
      case 'subtract':
        return { result: a - b };
      case 'multiply':
        return { result: a * b };
      case 'divide':
        if (b === 0) {
          throw new Error('Division by zero is not allowed');
        }
        return { result: a / b };
      default:
        throw new Error(`Unknown operation: ${operation}`);
    }
  },
};
