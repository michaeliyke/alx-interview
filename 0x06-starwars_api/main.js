#!/usr/bin/node
// learning about the requests in node

const https = require('https');
const url = 'https://reqres.in/api/users';

https.get(url, (res) => {
  let data = '';

  res.on('data', (chunk) => {
    data += chunk;
  });

  res.on('end', () => {
    const users = JSON.parse(data);
    console.log(users);
  });

}
).on('error', (err) => {
  console.log('Error: ' + err.message);
}
);


