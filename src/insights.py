from src.jobs import read


def get_unique_job_types(path):
    jobs_data = read(path)
    jobs_types = []
    for job in jobs_data:
        jobs_types.append(job["job_type"])
    types = []
    for type in jobs_types:
        if type not in types:
            types.append(type)
    return types


def filter_by_job_type(jobs, job_type):
    return [job for job in jobs if job["job_type"] == job_type]


def get_unique_industries(path):
    jobs_data = read(path)
    jobs_industries = []
    for job in jobs_data:
        if job["industry"] != "":
            jobs_industries.append(job["industry"])
    industries = []
    for type in jobs_industries:
        if type not in industries:
            industries.append(type)
    return industries


def filter_by_industry(jobs, industry):
    return [job for job in jobs if job["industry"] == industry]


def get_max_salary(path):
    jobs_data = read(path)
    jobs_salaries = []
    for job in jobs_data:
        if job["max_salary"] != "" and job["max_salary"]:
            try:
                jobs_salaries.append(int(job["max_salary"]))
            except ValueError:
                pass
    return max(jobs_salaries)


def get_min_salary(path):
    jobs_data = read(path)
    jobs_salaries = []
    for job in jobs_data:
        if job["min_salary"] != "" and job["min_salary"]:
            try:
                jobs_salaries.append(int(job["min_salary"]))
            except ValueError:
                pass
    return min(jobs_salaries)


def matches_salary_range(job, salary):
    try:
        if int(job["min_salary"]) <= salary <= int(job["max_salary"]):
            return True
        elif int(job["min_salary"]) > int(job["max_salary"]):
            raise ValueError
            # levanta uma exception
        else:
            return False
    except (ValueError, TypeError, KeyError):
        raise ValueError


def filter_by_salary_range(jobs, salary):
    """Filters a list of jobs by salary range

    Parameters
    ----------
    jobs : list
        The jobs to be filtered
    salary : int
        The salary to be used as filter

    Returns
    -------
    list
        Jobs whose salary range contains `salary`
    """
    return []
