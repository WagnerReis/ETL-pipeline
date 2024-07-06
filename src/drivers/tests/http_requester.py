class HttpRequesterSpy:
    def __init__(self) -> None:
        self.request_from_page_counter = 0

    def request_from_page(self) -> dict[str, str | int]:
        self.request_from_page_counter += 1
        return {
            "status_code": 200,
            "html": "<h1>HelloWord</h1>"
        }
