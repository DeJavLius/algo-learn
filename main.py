import sys
import subprocess
import time
from pathlib import Path
import re

def test_case_executer(code):
    indexed_def = dict()
    for idx, val in enumerate(code):
        if val.startswith("def"):
            indexed_def[val.replace("def ", "").replace("():", "")] = idx

    values = list(indexed_def.values())
    values.append(len(code))
    imp = min(values)
    imp_code = "\n".join(code[0:imp]) + "\n"
    case_list = [code[slice(values[i], values[i + 1])] for i in range(0, len(values) - 1)]
    test = []

    for case in case_list:
        test_code = imp_code + "\n".join(case)

        process = subprocess.Popen(
            [sys.executable, '-c', test_code],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )

        stdout, stderr = process.communicate()

        if process.returncode == 0:
            test.append(stdout)
            # print(stdout)
        else:
            print("❌실행 실패")
            if stdout:
                print(f"출력 내용: \n{stdout}\n")
            print(f"실패 코드: {process.returncode}")
            if stderr:
                print(f"에러 내용: \n\t{stderr}")

    return test

def time_checker(test_case, code):
    process = subprocess.Popen(
        [sys.executable, '-c', code],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )

    serialized_test_case = "".join(test_case)

    start_time = time.perf_counter()

    stdout, stderr = process.communicate(input=serialized_test_case)

    end_time = time.perf_counter()

    print("====== 실행 결과 ======")
    if process.returncode == 0:
        print("✅ 실행 완료")
        print(f"출력: \n {stdout}")
    else:
        print("❌실행 실패")
        if stdout:
            print(f"출력 내용: \n{stdout}\n")
        print(f"실패 코드: {process.returncode}")
        if stderr:
            print(f"에러 내용: \n\t{stderr}")

    print(f"progress time: {end_time - start_time:.5f}초")

if __name__ == '__main__':
    problem_name = "000_2750"
    pattern = re.compile(".*" + problem_name + ".*")
    target_dir = Path("./book")
    files = [{"name": file.name, "path": file.parent.name, "full_path": file} for file in target_dir.rglob("*.py")]

    problem = {
        "code": Path(
            next((
                file["full_path"] for file in files
                if pattern.search(str(file["name"])) and file.get("path") != "test_case"
            ), "")
        ).read_text(encoding="utf-8"),
        "test_case": Path(
            next((
                file["full_path"] for file in files
                if pattern.search(str(file["name"])) and file.get("path") == "test_case"
            ), "")
        ).read_text(encoding="utf-8").splitlines()
    }

    test_case_list = problem.pop("test_case")
    test_case = test_case_executer(test_case_list)
    code = problem.pop("code")

    for test in test_case:
        time_checker(test, code)