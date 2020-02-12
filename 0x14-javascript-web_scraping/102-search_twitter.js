#!/usr/bin/node
const base64 = require('base-64');
const request = require('request');
const headers = { Authorization: 'Basic ' + base64.encode(process.argv[2] + ':' + process.argv[3]), 'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8' };
const data = { grant_type: 'client_credentials' };
request.post({ url: 'https://api.twitter.com/oauth2/token', headers: headers, qs: data }, function (err, res, body) {
  if (err) console.log(err);
  else {
    const bearerToken = JSON.parse(body).access_token;
    const headers2 = { Authorization: 'Bearer ' + bearerToken };
    const data2 = { q: process.argv[4] };
    request.get({ url: 'https://api.twitter.com/1.1/search/tweets.json', headers: headers2, qs: data2 }, function (err2, res2, body2) {
      if (err2) console.log(err2);
      else {
        for (const stat of JSON.parse(body2).statuses) console.log(`[${stat.id}] ${stat.text} by ${stat.user.name}`);
      }
    });
  }
});
