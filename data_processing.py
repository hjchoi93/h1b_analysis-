import pandas as pd

lca_df_2024_Q4 = pd.read_csv("lca.csv", low_memory=False)

def app_wages_df(df: pd.DataFrame):
    wages_df = (lca_df_2024_Q4
           .groupby(["JOB_TITLE", "EMPLOYER_NAME", "WILLFUL_VIOLATOR", "H_1B_DEPENDENT", "VISA_CLASS", "CASE_STATUS"])
           [["WAGE_RATE_OF_PAY_FROM", "PREVAILING_WAGE"]]
           .median()
           .sort_values(by=["WAGE_RATE_OF_PAY_FROM"], ascending=False)
           .reset_index()
           )
    
    app_numbers_df = (lca_df_2024_Q4
        .groupby(["JOB_TITLE", "EMPLOYER_NAME", "WILLFUL_VIOLATOR", "H_1B_DEPENDENT", "VISA_CLASS", "CASE_STATUS"])
        ["CASE_NUMBER"]
        .count()
        .sort_values(ascending=False).head(50)
        .reset_index()
        .rename(columns={"CASE_NUMBER": "APP_NUMBERS"}))

    final_df = app_numbers_df.merge(wages_df, how="left", on=["JOB_TITLE", "EMPLOYER_NAME", "WILLFUL_VIOLATOR", "H_1B_DEPENDENT", "VISA_CLASS", "CASE_STATUS"])

    return final_df

