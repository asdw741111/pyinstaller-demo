# pyinstaller打包示例

版本说明
- 基于`pyinstaller`版本`6.5.0`
- 依赖`python`版本`3.8`~`3.12`

注意事项
- 需要在对应平台执行打包, 例如打包`exe`需要在windows打包
- 使用`-i`指定图标，在windows平台需要用`ico`，mac平台用`icns`，如果安装了`Pillow`会用Pillow尽量转换成正确的格式

### 打包说明
pyinstaller支持两种打包方式
- 直接用命令 例如`pyinstaller -F main.py`
- 通过.spec文件(配置文件)打包 例如`pyinstaller main.spec`

用命令打包完成后也会自动生成.spec文件，下次可以直接用该文件打包

常用打包选项
- `-F/--onefile` 打包成一个可执行文件
- `-D/--onedir` 打包成一个目录里边包含一个可执行文件，默认为该打包方式。经测试该方式总文件大小比单文件的要大很多。
- `--hidden-import aa,bb,cc` 需要额外打包的模块, 只有非显示import的才需要
- `--exclude-module aa,bb,cc` 需要移除的模块或者包
- `-n execute_file_name`  执行打包的可执行文件名，默认和主文件名相同

## 示例说明
每个目录都是一个独立的演示示例，需要进入对应的目录下执行打包命令
### base
单文件并且只引入了`os`模块
```sh
pyinstaller -F main.py
```

### ui
使用`tkinter`作为UI库做客户端开发，单文件。该示例是窗口里边点击`选择目录`按钮选择一个目录，然后点击`执行`按钮遍历该目录下的xls和xlsx文件并显示到文本框。
```sh
pyinstaller -F main.py -n tkinter演示
```

### multi-file
包含多个文件，适合工程化打包的场景。包含绝对导入、相对导入。注意：主模块所在文件夹不会被视作package，因此除了主模块外，与主模块处在同个文件夹的模块（也就是同级的模块）也必须使用绝对导入。
```sh
pyinstaller -F main.py
```

