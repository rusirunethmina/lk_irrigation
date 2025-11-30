class Markdown:
    @staticmethod
    def table(d_list: list[dict]) -> list[str]:
        keys = d_list[0].keys()
        lines = []

        is_numerical = {}
        for key in keys:
            is_numerical[key] = all(
                isinstance(d[key], (int, float))
                or (
                    isinstance(d[key], str)
                    and d[key]
                    .replace(".", "", 1)
                    .replace("-", "", 1)
                    .isdigit()
                )
                for d in d_list
            )

        header = "| " + " | ".join(keys) + " |"
        lines.append(header)

        separator = (
            "| "
            + " | ".join(
                "---:" if is_numerical[key] else "---" for key in keys
            )
            + " |"
        )
        lines.append(separator)

        for d in d_list:
            row = "| " + " | ".join(str(d[key]) for key in keys) + " |"
            lines.append(row)

        lines.append("")
        return lines
