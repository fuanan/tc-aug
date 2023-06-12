import subprocess


cmd_list = ['/root/miniconda3/envs/tc_aug/bin/pynguin',
            '--project-path', 'fuzz_temp/',
            '--output-path', 'pynguin_output',
            '--original-type-weight', '10',
            '--type-tracing-weight', '1',
            '-v', '--maximum-search-time', '6',
            '--module-name', 'program_under_test']


result = subprocess.run(cmd_list, env={'PYNGUIN_DANGER_AWARE':'1'})