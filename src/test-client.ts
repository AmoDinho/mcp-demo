import fetch from 'node-fetch';

async function testCalculator() {
  try {
    // Get the manifest
    const manifestResponse = await fetch('http://localhost:3000/mcp');
    const manifest = await manifestResponse.json();
    console.log('Server Manifest:', JSON.stringify(manifest, null, 2));

    // Test addition
    const addResponse = await fetch('http://localhost:3000/mcp', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        tool: 'calculator',
        params: {
          operation: 'add',
          a: 5,
          b: 3,
        },
      }),
    });

    const addResult = await addResponse.json();
    console.log('Addition Result:', addResult);

    // Test division
    const divideResponse = await fetch('http://localhost:3000/mcp', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        tool: 'calculator',
        params: {
          operation: 'divide',
          a: 10,
          b: 2,
        },
      }),
    });

    const divideResult = await divideResponse.json();
    console.log('Division Result:', divideResult);

    // Test error case (division by zero)
    const errorResponse = await fetch('http://localhost:3000/mcp', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        tool: 'calculator',
        params: {
          operation: 'divide',
          a: 10,
          b: 0,
        },
      }),
    });

    const errorResult = await errorResponse.json();
    console.log('Error Case:', errorResult);
  } catch (error) {
    console.error('Error testing calculator:', error);
  }
}

// Only run if directly executed
if (require.main === module) {
  testCalculator();
}
