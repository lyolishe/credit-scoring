def clear_missing_values(data, columns, empty_rows_on):
    if bool(columns):
        data = data.drop(columns=columns)

    if bool(empty_rows_on):
        data = data.dropna(subset=empty_rows_on)

    return data  # Important: return the modified DataFrame


def paste_min_value_to_columns(data, columns):
    for column in columns:
        data[column] = data[column].fillna(data[column].min())

    return data  # Important: return the modified DataFrame