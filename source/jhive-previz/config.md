```{eval-rst}
.. _jhive-previz:
```

## Configuration Files

There are two main styles of configuration file. The `config.yaml` file is the main one that needs to be changed for running the code on different fields, or with different combinations of catalog files or output columns. The `fields.yaml` files correspond to a specific type of catalog file, and should be able to be used for multiple fields. These files should not need to be changed regularly. 

### config.yaml

The following variables found in the main config file are required to run the `jhive_previz` pipeline. 
| variable | description |
| ---------- | ----------- |
| paths | The dictionary of paths corresponding to the dictionary of file names. (Must contain `cat_path` as a key) |  
| field_name | The name of the JWST field |
| file_names | The dictionary of file names that can be used for the output catalog. Keys correspond to the `paths` dictionary keys. Must contain the key `cat_filename`, which is the main catalogue to be used. | 
| output_file_suffix | The suffix to be added to all output files written | 
| output_path | The path from the current working directory to the directory where output files will be written |
| columns_to_use | The dictionary of columns to be put into the output file. Each key is one of the `file_names` keys, and has a list of the desired columns. The `id` column is required for each file that is used. | 


Below is an example of the main `config.yaml` file. Additional keys may be added under the `paths`, `file_names` and `columns_to_use` variables. The keys must match across these dictionaries (i.e. `cat_path` matches `cat_filename`). Extra keys may be added to `paths` or `file_names` that are not in `columns_to_use`, but all keys that are in `columns_to_use` must exist in the `paths` and `file_names` dictionaries.  

```yaml
paths: # list of full paths to the corresponding files below
  cat_path: "./data/" 
  db_path: "./data/" 
  mf_path: "./data/" 

field_name: "ceers-full-grizli-v7.2" 
file_names: # list of file names that can be used for the output catalog
  cat_filename: "ceers-full-grizli-v7.2-fix_phot_apcorr.fits"
  db_filename: "ceers-full_v7.2_DB_catalog_small.cat"
  mf_filename: "file.csv"

output_file_suffix: "_jhive_viz_v1" 
output_path: "./output/" 

columns_to_use: # list of the column keys to be put in the output file
  cat_filename:
    - "id"
    - "ra"
    - "dec"
    - "abmag_f435w"
  db_filename:
    - "id"
    - "zfit_50"
```

### fields.yaml

There should be a separate `fields.yaml` file for each catalog file that is included in the `config.yaml` file. These files are primarily 
a list of columns in the catalog file that can be used in the output table, and the relevant metadata for those columns. 

The metadata fields that should be included for all columns are given in the table below. If any of these fields are not relevant for a certain column,
i.e. `zero_point` is not relevant for an `id` column, then the field should still be included and given the value `null`. 

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


An example short file structure is as follows:
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
        }
    }
}
```

