import uvicorn

from app.backend_pre_start import main as pre_start_main
from app.initial_data import main as init_db_main
from app.main import app


if __name__ == "__main__":
    # pre_start_main() # 先校验数据库是否设置正常
    # 然后 执行 alembic upgrade head 创建数据库 参考: https://www.jianshu.com/p/394e6453a6b0
    # init_db_main()  # 然后初始化数据库
    # 运行后端
    uvicorn.run(app, host='0.0.0.0', port=80)
