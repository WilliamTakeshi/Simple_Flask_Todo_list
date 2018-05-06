# Simple Flask API

## Overview

A simple flask REST API using Flask-RESTFul and SQLite


## FrontEnd

The front-end is made with bootstrap and jQuery. It's made using modals and ajax calls.

## Design API

The v0 API is formed by only 1 table.

* Tasks

## Endpoints

We have now 2 endpoints

* /v0/task/
* /v0/task/taskid

All items have some of the following properties, with required properties in bold:

Field | Description
------|------------
**id** | The item's unique id. int
**title** | The title of the task. str
**description** | The description of the task. str
**done** | A boolean field explaning if the task is done or not. bool

The Task API have this properties

HTTP Method | Action | Examples
------|------------ | -------
GET | Obtain information about all tasks | /v0/task
POST | Post information about a task | /v0/task

GET | Obtain information about an task | /v0/task/**taskid**
PUT | Update information about an task | /v0/task/**taskid**
DELETE | Delete information about an task (need JWT Auth) | /v0/task/**taskid**


For example: GET {{url}}/v0/appointment/2

```javascript
{
    "id": 2,
    "date_begin": "Comprar leite",
    "date_end": "Ir no supermercado comprar leite",
    "done": false
}
```
