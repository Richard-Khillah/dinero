```python
{
    id = db.Column(db.Integer, primary_key=True)
    #resturant_id = ()
    name = db.Column(db.String(50))
    cost = db.Column(db.Float)
    description = db.Column(db.String(100)) #can be a db.Text() field
    category = db.Column(db.String(25))
}
```
