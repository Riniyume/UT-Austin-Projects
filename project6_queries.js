printjson("****************************************************************");
printjson("0) Number of documents in the data collection from sample_weatherdata");
printjson(db.data.countDocuments())

printjson("****************************************************************");
printjson("1) Find documents with Air Temperature between 3.0 and 4.0, Visibility Distance = 10000, 'position.type' is 'Point', sorted by timestamp in ascending order");
printjson(db.data.find({ $and: [ { "airTemperature.value": { $gt: 3.0, $lt: 4.0 } }, { "visibility.distance.value": 10000 }, { "position.type": "Point" } ]}, { ts: 1, "airTemperature.value": 1, "visibility.distance.value": 1, "position.type": 1, _id: 0 }).sort({ ts: 1 }).limit(5));

printjson("****************************************************************");
printjson("2) Find documents where 'position.type' is 'Point' or 'skyCondition.ceilingHeight.value' is less than 1000, sorted by timestamp in ascending order");
printjson(db.data.find({ $or: [ { "position.type": "Point" }, { "skyCondition.ceilingHeight.value": { $lt: 1000 } } ]}, { ts: 1, "position.type": 1, "skyCondition.ceilingHeight.value": 1, _id: 0 }).sort({ ts: 1 }).limit(5));

printjson("****************************************************************");
printjson("3) Find documents where 'position.type' is 'Point', 'pastWeatherObservationManual' array contains an object with 'atmosphericCondition.value' equal to '0', Pressure is above 1019.0, and Air Temperature is between 3.0 and 4.0, sorted by timestamp in ascending order");
printjson(db.data.find({ "position.type": "Point", "pastWeatherObservationManual.atmosphericCondition.value": "0", "pressure.value": { $gt: 1019.0 }, "airTemperature.value": { $gt: 3.0, $lt: 4.0 } }, { ts: 1, "position.type": 1, "pastWeatherObservationManual.atmosphericCondition.value": 1, "pressure.value": 1, "airTemperature.value": 1, _id: 0 }).sort({ ts: 1 }).limit(5));
          
printjson("****************************************************************");
printjson("4) Find documents where Air Temperature is above 3.0°C or Condition is 'Rain', sorted by timestamp in ascending order");
printjson(db.data.find({ $or: [ { "airTemperature.value": { $gt: 3.0 } }, { Condition: "Rain" } ]}, { ts: 1, "airTemperature.value": 1, Condition: 1, _id: 0 }).sort({ ts: 1 }).limit(5));
          
printjson("****************************************************************");
printjson("5) Find documents where 'position.type' is 'Point' and 'position.coordinates' contains specific coordinates");
printjson(db.data.find({ "position.type": "Point", "position.coordinates": [ -29.7, 59.8 ] }, { ts: 1, "position.type": 1, "position.coordinates": 1, _id: 0 }));

printjson("****************************************************************");
printjson("6) Find documents where 'skyCondition.ceilingHeight.value' is less than 1000 and 'skyCondition.cavok' is 'N', sorted by timestamp in ascending order");
printjson(db.data.find({ "skyCondition.ceilingHeight.value": { $lt: 1000 }, "skyCondition.cavok": "N" }, { ts: 1, "skyCondition.ceilingHeight.value": 1, "skyCondition.cavok": 1, _id: 0 }).sort({ ts: 1 }).limit(5));

printjson("****************************************************************");
printjson("7) Find documents where 'pastWeatherObservationManual' array contains an object with 'atmosphericCondition.value' equal to '0', limit to 5 results");
printjson(db.data.find({ "pastWeatherObservationManual": { $elemMatch: { "atmosphericCondition.value": "0" } } }, { ts: 1, "pastWeatherObservationManual.atmosphericCondition.value": 1, _id: 0}).limit(5));

printjson("****************************************************************");
printjson("8) Find documents where 'presentWeatherObservationManual' array contains an object with 'condition' equal to '02' or '03', limit to 5 results");
printjson(db.data.find({ "presentWeatherObservationManual": { $elemMatch: { $or: [{ condition: "02" }, { condition: "03" }] } }}, { ts: 1, "presentWeatherObservationManual.condition": 1, _id: 0}).limit(5));

printjson("****************************************************************");
printjson("9) Find documents where 'pastWeatherObservationManual' array contains an object with 'atmosphericCondition.value' equal to '0' and 'period.value' is 3, limit to 5 results");
printjson(db.data.find({ "pastWeatherObservationManual": { $elemMatch: { "atmosphericCondition.value": "0", "period.value": 3 } }}, { ts: 1, "pastWeatherObservationManual.atmosphericCondition.value": 1, "pastWeatherObservationManual.period.value": 1, _id: 0 }).limit(5));


printjson("****************************************************************");
printjson("10) Find documents where Air Temperature is above 4.0 or visibility.distance.value is 5000 and 'position.type' is 'Point', sorted by timestamp in ascending order");
printjson(db.data.find({ $or: [ { "airTemperature.value": { $gt: 4.0 } }, { "visibility.distance.value": 5000, "position.type": "Point" } ]}, { ts: 1, "airTemperature.value": 1, "visibility.distance.value": 1, "position.type": 1, _id: 0 }).sort({ ts: 1 }).limit(5));