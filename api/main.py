from fastapi import FastAPI
app = FastAPI(title='Pakistan Drug Index API')

@app.get('/')
def root():
    return {'status': 'running'}
