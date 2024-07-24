import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from utils import ArgumentParser, LOG
from translator import PDFTranslator, TranslationConfig

if __name__ == "__main__":
    # 解析命令行
    argument_parser = ArgumentParser()
    args = argument_parser.parse_arguments()

    # 初始化配置单例
    config = TranslationConfig()
    config.initialize(args)    

    api_key = config.__getattr__('api_key')
    base_url = config.__getattr__('base_url')
    # 实例化 PDFTranslator 类，并调用 translate_pdf() 方法
    translator = PDFTranslator(config.model_name, base_url=base_url, api_key=api_key)
    translator.translate_pdf(config.input_file, config.output_file_format, pages=None)
