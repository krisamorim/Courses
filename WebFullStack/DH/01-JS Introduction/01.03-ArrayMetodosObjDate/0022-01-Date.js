/*
Object Date()

Methods to Date():
- getDay(): Retunrs a number that refers to the day of the week, remembering that for JS the week starts on Sunday and it is equal to 0
- getDate(): the current day
- getMonth: Retunrs a number that refers to the month, remembering that for JS month starts on January and it is equal to 0
- getFullYear(): Returns the year in full

*/

const data = new Date();
console.log(data.getDay())
console.log(data.getMonth())
console.log(data)


const data2 = new Date('2019-01-12')
console.log(data2.getMonth())
console.log(data2)

const data3 = new Date();
data3.setYear(2018);
data3.setMonth(2);
data3.setDate(1)
console.log(data3)