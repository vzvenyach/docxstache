# docxstache

Write a word document with `mustache`, run docxstache, and get a new docx.

## Usage:

```
git clone https://github.com/vzvenyach/docxstache.git
cd docxstache
virtualenv env
source env/bin/activate
pip install -r requirements.txt
python app.py example.docx example.json out.docx
```

## Status

Currently, the only thing docxstache can handle is the use of curly braces `{{this_works}}`. Would love help thinking through how to get the other features working.

## Roadmap

The vision here is to wrap it into a module, so that it's as simple as a `pip install` and let it rip.

## License

MIT