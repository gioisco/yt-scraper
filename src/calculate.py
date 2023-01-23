import pandas as pd
import matplotlib.pyplot as plt

while True:
    n = input("Enter the number of videos to use for mean calculation: ")
    if n == "":
        print("No input received. Exiting...")
        exit()
    elif n.isdigit():
        n = int(n)
        break
    else:
        print("Invalid input. Please insert a number.")
print("")

df = pd.read_csv( 'videos_data.csv',
    parse_dates=['date_time'],
    dtype={
        'video_id': 'string',
        'view_count': 'int32',
        'title': 'string'
        })

# Validate df
grouped = df.groupby(df["date_time"].dt.date)
for date, group in grouped:
    if len(group) < n:
        print(f"Error: Value {n} is not acceptable as minimum number of videos required per date.")
        print(f"For the date {date}, there are only {len(group)} videos available.")
        exit()

print()
print("- Selection dataframe -")
selection_df = df.groupby(df["date_time"].dt.date).tail(n)
print(selection_df)

print()
print("- Calculating mean -")
mean_df = selection_df.groupby(df["date_time"].dt.date)["view_count"].mean().round(0).reset_index(name='mean')
print(mean_df)

print()
print("- Calculating median -")
median_df = selection_df.groupby(df["date_time"].dt.date)["view_count"].median().round(0).reset_index(name='median')
print(median_df)

print()
print("- Result -")
result = mean_df.merge(median_df, on='date_time')
result.set_index('date_time', inplace=True)
print(result)

# Draw plot
result.plot( y=['mean', 'median'], kind='line', style = '-', marker='o', color=['r','g'])
plt.legend(["mean","median"])
fig1 = plt.gcf()

# Save file and show plot
filename = 'mean_median_views.png'
fig1.savefig(filename, bbox_inches='tight', dpi=150)
print("Saved " + filename)
plt.show()

