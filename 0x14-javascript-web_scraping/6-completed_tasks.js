#!/usr/bin/node
// script that computes the number of tasks completed by user id.

const reqst = require('request');

reqst(process.argv[2], function (error, respons, value) {
  if (error) {
    console.log(error);
  } else {
    const completedTask = {};
    const val = JSON.parse(value);

    for (let i = 0; i < val.length; i++) {
      const uId = val[i].userId;
      const comp = val[i].completed;

      if (comp && !completedTask[uId]) {
        completedTask[uId] = 0;
      }
      if (comp) {
        completedTask[uId]++;
      }
    }
    console.log(completedTask);
  }
});
