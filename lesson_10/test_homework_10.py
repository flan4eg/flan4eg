import os
from .homework_10 import log_event

log_file = "login_system.log"


def read_last_line():       # позволяет читать последнюю строку из многострочного лога
    with open(log_file, "r") as f:
        content = f.read()
        return content.split("\n")[-2]  # смотрю во второй с конца строке потому, что, оказывается, винда создаёт ещё одну служебную строку в конце


class TestHomework10():

    def test_log_event_success(self):
        username = "username"
        status = "success"
        log_event(username, status)
        last_line = read_last_line()
        assert username in last_line
        assert status in last_line
        assert "INFO" in last_line   # необязательная строка, для красоты
        os.remove(log_file)          # решила удалять лог после каждого теста, хотя можно и не делать этого

    def test_log_event_warning(self):
        username = "username"
        status = "expired"
        log_event(username, status)
        last_line = read_last_line()
        assert username in last_line
        assert status in last_line
        assert "WARN" in last_line
        os.remove(log_file)

    def test_log_event_error(self):
        username = "username"
        status = "asdasd"
        log_event(username, status)
        last_line = read_last_line()
        assert username in last_line
        assert status in last_line
        assert "ERROR" in last_line
        os.remove(log_file)



