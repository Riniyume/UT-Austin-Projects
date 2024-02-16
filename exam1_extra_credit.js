printjson("****************************************************************");
printjson("1) Inserting a document with insertOne():");
var documentInsertOne = {
  _id: ObjectId("1433a948e4b01cf7256990bd"),
  st: 'x+59810-014300',
  position: { type: 'Point', coordinates: [ -23.1, 79.8 ] },
  elevation: 9999,
  callLetters: 'TFWB',
  qualityControlProcess: 'V020'
};
printjson(db.data.insertOne(documentInsertOne));

printjson("****************************************************************");
printjson("2) Insert multiple documents with insertMany(1st set):");
var documentsInsertMany = [
  {
    _id: ObjectId(),
    st: 'x+59800-029701',
    position: { type: 'Point', coordinates: [ -13.4, 50.5 ] },
    elevation: 9938,
    callLetters: 'TFWC',
    qualityControlProcess: 'V021'
  },
  {
    _id: ObjectId(),
    st: 'x+59800-029707',
    position: { type: 'Point', coordinates: [ -31.7, 69.0 ] },
    elevation: 9967,
    callLetters: 'TFWD',
    qualityControlProcess: 'V022'
  }
];
printjson(db.data.insertMany(documentsInsertMany));

printjson("****************************************************************");
printjson("3) Insert multiple documents with insertMany(2nd set):");
var documentsInsertMany2 = [
  {
    _id: ObjectId(),
    st: 'x+69800-014304',
    position: { type: 'Point', coordinates: [ 49.2, 68.3 ] },
    elevation: 10101,
    callLetters: 'TFWC',
    qualityControlProcess: 'V024'
  },
  {
    _id: ObjectId(),
    st: 'x+59800-029705',
    position: { type: 'Point', coordinates: [ -19.8, 46.3 ] },
    elevation: 10092,
    callLetters: 'TFWG',
    qualityControlProcess: 'V015'
  },
  {
    _id: ObjectId(),
    st: 'x+59800-014305',
    position: { type: 'Point', coordinates: [ -79.8, 16.3 ] },
    elevation: 9999,
    callLetters: 'TFWC',
    qualityControlProcess: 'V015'
  }
];
printjson(db.data.insertMany(documentsInsertMany2));

printjson("****************************************************************");
printjson("4) Document update with updateOne():");
var filterUpdateOne = { st: 'x+59810-014300' };
var updateOne = {
  $set: {
    airTemperature: { value: 5.0, quality: '1' },
    elevation: 9976
  }
};
printjson(db.data.updateOne(filterUpdateOne, updateOne));

printjson("****************************************************************");
printjson("5) Document update with updateOne() and $push:");
var filterUpdatePush = { st: 'x+59800-029700' };
var updatePush = {
  $push: {
    pastWeatherObservationManual: {
      atmosphericCondition: { value: '1', quality: '2' },
      period: { value: 4, quality: '2' }
    }
  }
};
printjson(db.data.updateOne(filterUpdatePush, updatePush));

printjson("****************************************************************");
printjson("6) Document update with updateMany(1st set):");
var filterUpdateMany = { elevation: { $lt: 9999 } };
var updateMany = {
  $inc: { elevation: 100 }
};
printjson(db.data.updateMany(filterUpdateMany, updateMany));

printjson("****************************************************************");
printjson("7) Document update with updateMany(2nd set):");
var filterUpdateMany2 = { "elevation": { $gt: 9999 } };
var updateMany2 = {
  $inc: { "elevation": -50 }
};
printjson(db.data.updateMany(filterUpdateMany2, updateMany2));

printjson("****************************************************************");
printjson("8) Document delete with deleteOne():");
var filterDeleteOne = { st: 'x+59800-029702' };
printjson(db.data.deleteOne(filterDeleteOne));

printjson("****************************************************************");
printjson("9) Document delete with deleteMany(1st set):");
var filterDeleteMany = { elevation: { $gt: 9999 } };
printjson(db.data.deleteMany(filterDeleteMany));

printjson("****************************************************************");
printjson("10) Document delete with deleteMany(2nd set):");
var filterDeleteMany2 = { "callLetters": "TFWB" };
printjson(db.data.deleteMany(filterDeleteMany2));