# clovers

Flexible configuration management, for non developers !

1. support json schema editor;
2. support json editor;
3. support get configurations with api;
4. support backends: builtin DB, Aliyun ACM
5. TODO: support other backends, like spring-cloud-config, ctrip apollo, etc.

## Demo

Be nice to use this

url: http://clovers.bastionhost.org/admin/

username: demo

password: demo

## Samples

### create an object type with schema editor

![object-json-schema](./media/object-json-schema.jpg)

### create a specific object with the object type

![object-json](./media/object-json.jpg)

### create an array type with schema editor

![array-json-schema](./media/array-json-schema.jpg)

### create a specific array with the array type

![array-json](./media/array-json.jpg)

## Installation

To set up a development environment quickly, install Python 2.x first. It
comes with virtualenv built-in. so create a virtual environment with:

`virtualenv env`

`source env/bin/activate`

Install dependencies:

`pip install -r requirements.txt`

Run server:

`python manage.py runserver --settings=clovers.settings.dev`
