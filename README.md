# efd-python

Simple Python hello-world starter project.

## Build
```bash
python -m compileall .
```

This compiles the Python source into bytecode and produces `.pyc` files in `__pycache__/` directories, which is useful for checking that the code is valid before deployment.

## Run
```bash
python app.py
```

Expected output:
```text
Hello, World!
```

## Test
```bash
python -m unittest test_app
```
