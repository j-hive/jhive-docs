```{eval-rst}
.. _jhive-previz:
```

## Data Standards

### Output data format
The output data table is written out as a `.csv` file. The file name will be a combination of the `field_name` + `output_file_suffix` + `.csv`, and will be saved in the `output_path` (all variables given in `base_config.yaml`). It will have all of the columns given in the `columns_to_use` list in the `base_config.yaml` file that were found in the input data files. If a desired column does not exist in the data, then a warning will be printed out as the code runs, and the final table and metadata will not contain that column. Below is a small example of a few columns from a possible data output file. 

| id | ra | dec | abmag_435w |
| ------ | -- | --- | ---------- | 
| 1 | 3.656696 |-30.467320 | 4.861 |
| 2 | 3.656710 | -29.58395 |  |
| 3 | 3.657396 |-31.427320 | 1.934 |




### Output metadata format
The output metadata file is written out as a `.json` file. It has top-level metadata keys, including the JWST field name given in the `base_config.yaml`. It then has a `columns` key that contains all the metadata for each column. Every column should have all of the possible column metadata fields. If a column metadata field is not relevant for that column, it will have value `null`. The fields for each column are given in the table below:

| field name | description |
| ---------- | ----------- |
| display | The name displayed along the axis and in the selector of the J-HIVE Visualization tool | 
| data_type | The type of data stored in this column | 
| filt_max_val | The maximum value to allow in this column, above which will be NaN | 
| filt_min_val | The minimum value to allow in this column, below which will be NaN |
| filt_name | The name of the filter used for this data, if applicable |
| input_column_name | The name of the column in the input catalogue file | 
| input_units | The units of the column in the input catalogue file |
| is_magnitude | True if the output value is a magnitude | 
| output_num_decimals | The decimal precision to keep for this value in the output table | 
| output_units | The units of the column in the output table | 
| wl_micron | The wavelength of the filter in microns |
| zero_point | The zero point to use for converting flux to magnitude | 
| min_val | The minimum value of the data in the output column | 
| max_val | The maximum value of the data in the output column |


An example output metadata file corresponding to the example data table above is shown below.

```json
{
    "field_name": "ceers-full-grizli-v7.2",
    "columns": {
        "id": {
            "display": "DJA Source ID",
            "data_type": "int",
            "filt_max_val": null,
            "filt_min_val": null,
            "filt_name": null,
            "input_column_name": "id",
            "input_units": null,
            "is_magnitude": "false,",
            "output_num_decimals": null,
            "output_units": null,
            "wl_micron": null,
            "zero_point": null,
            "min_val": 1,
            "max_val": 76637
        },
        "ra": {
            "display": "Right Ascension",
            "data_type": "float",
            "filt_max_val": null,
            "filt_min_val": null,
            "filt_name": null,
            "input_units": "Degrees",
            "input_column_name": "ra",
            "is_magnitude": false,
            "output_num_decimals": 6,
            "output_units": "Degrees",
            "wl_micron": null,
            "zero_point": null,
            "min_val": 214.69150058467784,
            "max_val": 215.2138016303901
        },
        "dec": {
            "display": "Declination",
            "data_type": "float",
            "filt_max_val": null,
            "filt_min_val": null,
            "filt_name": null,
            "input_units": "Degrees",
            "input_column_name": "dec",
            "is_magnitude": false,
            "output_num_decimals": 6,
            "output_units": "Degrees",
            "wl_micron": null,
            "zero_point": null,
            "min_val": 52.68691669885586,
            "max_val": 53.02117022008072
        },
        "abmag_f435w": {
            "display": "Magnitude (F435W)",
            "data_type": "float",
            "filt_max_val": null,
            "filt_min_val": 0.0,
            "filt_name": "F435W",
            "input_column_name": "f435w_corr_1",
            "input_units": "microJansky",
            "is_magnitude": true,
            "output_num_decimals": 3,
            "output_units": "magnitude",
            "wl_micron": 0.43,
            "zero_point": 28.9,
            "min_val": 20.754279739992864,
            "max_val": 45.769283839665945
        },
    },
    "num_objects": 3
}
```