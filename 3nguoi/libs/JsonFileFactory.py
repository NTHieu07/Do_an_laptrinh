import json
import os

class JsonFileFactory:
    def write_data(self, arr_data, filename):
        """
        Hàm này dùng để parse object thành jsonstring.
        Nếu phần tử trong arr_data là dictionary thì ghi trực tiếp,
        còn nếu là đối tượng thì sử dụng __dict__.
        :param arr_data: mảng đối tượng hoặc dictionary
        :param filename: nơi lưu trữ jsonstring cho object
        :return: True nếu thành công
        """
        json_string = json.dumps(
            [
                item if isinstance(item, dict) else item.__dict__
                for item in arr_data
            ],
            default=str,
            indent=4,
            ensure_ascii=False
        )
        with open(filename, 'w', encoding='utf-8') as json_file:
            json_file.write(json_string)

    def read_data(self, filename, ClassName):
        """
        Hàm đọc jsonstring và phục hồi lại mô hình lớp ClassName
        với ClassName là tên lớp được chỉ định phục hồi OOP.
        :param filename:
        :param ClassName:
        :return: danh sách đối tượng được phục hồi
        """
        if not os.path.isfile(filename):
            return []
        with open(filename, 'r', encoding='utf-8') as file:
            arr_data = json.loads(file.read(), object_hook=lambda cls: ClassName(**cls))
        return arr_data
