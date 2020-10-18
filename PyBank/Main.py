{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "import os\n",
    "import csv\n",
    "        "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Files to load and output (Remember to change these)\n",
    "file_to_load = os.path.join(\"Resources\", \"budget_data.csv\")\n",
    "file_to_output = os.path.join(\"analysis\", \"budget_analysis.txt\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Financial Analysis\n",
      "----------------------------\n",
      "Total Months: 86\n",
      "Total: $38382578\n",
      "Average  Change: $-2315.12\n",
      "Greatest Increase in Profits: Feb-2012 ($1926159)\n",
      "Greatest Decrease in Profits: Sep-2013 ($-2196167)\n",
      "\n"
     ]
    }
   ],
   "source": [
    "total_months = 0\n",
    "month_of_change = []\n",
    "net_change_list = []\n",
    "greatest_increase = [\"\", 0]\n",
    "greatest_decrease = [\"\", 9999999999999999999]\n",
    "total_net = 0\n",
    "\n",
    "# Read the csv\n",
    "with open(file_to_load) as financial_data:\n",
    "    reader = csv.reader(financial_data)\n",
    "\n",
    "    # Read the header row\n",
    "    header = next(reader)\n",
    "\n",
    "    # Extract first row\n",
    "    first_row = next(reader)\n",
    "    total_months += 1\n",
    "    total_net += int(first_row[1])\n",
    "    prev_net = int(first_row[1])\n",
    "\n",
    "    for row in reader:\n",
    "\n",
    "        # Track the total\n",
    "        total_months += 1\n",
    "        total_net += int(row[1])\n",
    "\n",
    "        # Track the net change\n",
    "        net_change = int(row[1]) - prev_net\n",
    "        prev_net = int(row[1])\n",
    "        net_change_list += [net_change]\n",
    "        month_of_change += [row[0]]\n",
    "\n",
    "        # Calculate the greatest increase\n",
    "        if net_change > greatest_increase[1]:\n",
    "            greatest_increase[0] = row[0]\n",
    "            greatest_increase[1] = net_change\n",
    "\n",
    "        # Calculate the greatest decrease\n",
    "        if net_change < greatest_decrease[1]:\n",
    "            greatest_decrease[0] = row[0]\n",
    "            greatest_decrease[1] = net_change\n",
    "            \n",
    "# Calculate the Average Net Change\n",
    "net_monthly_avg = sum(net_change_list) / len(net_change_list)\n",
    "\n",
    "# Generate Output Summary\n",
    "output = (\n",
    "    f\"Financial Analysis\\n\"\n",
    "    f\"----------------------------\\n\"\n",
    "    f\"Total Months: {total_months}\\n\"\n",
    "    f\"Total: ${total_net}\\n\"\n",
    "    f\"Average  Change: ${net_monthly_avg:.2f}\\n\"\n",
    "    f\"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\\n\"\n",
    "    f\"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\\n\")\n",
    "\n",
    "# Print\n",
    "print(output)\n",
    "\n",
    "# Export\n",
    "with open(file_to_output, \"w\") as txt_file:\n",
    "    txt_file.write(output)\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
