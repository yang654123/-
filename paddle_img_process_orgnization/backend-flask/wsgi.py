from app import create_app, db
from flask_cors import CORS

app = create_app()
CORS(app, resources=r'/*')

'''
# 初始化数据库
    from app import create_app, db 
    app = create_app() 
    app.app_context().push() 
    db.create_all()
'''

if __name__ == "__main__":
    print(app.url_map)
    app.run(host='localhost', port=3000, threaded=False)


# 算法哪块 需要自己加   所有的函数在 F:\代码\backend-flask\app\Controller\routes.py 里边   
