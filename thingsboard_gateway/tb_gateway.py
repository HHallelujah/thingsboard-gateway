#     Copyright 2024. ThingsBoard
#
#     Licensed under the Apache License, Version 2.0 (the "License");
#     you may not use this file except in compliance with the License.
#     You may obtain a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#     Unless required by applicable law or agreed to in writing, software
#     distributed under the License is distributed on an "AS IS" BASIS,
#     WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#     See the License for the specific language governing permissions and
#     limitations under the License.
import sys
from os import curdir, listdir, mkdir, path

from thingsboard_gateway.gateway.tb_gateway_service import TBGatewayService
from thingsboard_gateway.gateway.hot_reloader import HotReloader


def main():
    if "logs" not in listdir(curdir):
        mkdir("logs")

    try:
        # 尝试从命令行参数中获取一个布尔值 hot_reload，并在没有提供参数时设置默认值为 False。
        # sys.argv 是一个列表，包含命令行参数。sys.argv[0] 是脚本名称，sys.argv[1] 是第一个命令行参数。
        hot_reload = bool(sys.argv[1])
    except IndexError:
        hot_reload = False

    # 根据 hot_reload 的值来决定是使用 HotReloader 还是直接启动 TBGatewayService
    if hot_reload:
        HotReloader(TBGatewayService)
    else:
        # 将路径中的斜杠替换为当前操作系统的路径分隔符，以确保在不同操作系统上的兼容性。
        TBGatewayService(path.dirname(path.abspath(__file__)) + '/config/tb_gateway.json'.replace('/', path.sep))


def daemon():
    TBGatewayService("/etc/thingsboard-gateway/config/tb_gateway.json".replace('/', path.sep))


if __name__ == '__main__':
    main()
