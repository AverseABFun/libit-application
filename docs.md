## GET /
Takes one parameter, `id`, and returns either a JSON object in the format:
```json
{
    "error": true,
    "errCode": 1,
    "errMsg": "Note not found"
}
```
or a JSON object in the format:
```json
{
    "error": false,
    "result": "(note content)"
}
```

## PUT /
Takes one parameter, `note`, and returns a JSON object in the format:
```json
{
    "error": false,
    "result": "(uuid v4/note id)"
}
```

## POST /
Takes two parameters, `id` and `note`, and returns a JSON object in the format:
```json
{
    "error": false,
    "result": ""
}
```

## DELETE /
Takes one parameter, `id`, and returns a JSON object in the format:
```json
{
    "error": true,
    "errCode": 1,
    "errMsg": "Note not found"
}
```
or a JSON object in the format:
```json
{
    "error": false,
    "result": "(previous content of the note before it was deleted)"
}
```