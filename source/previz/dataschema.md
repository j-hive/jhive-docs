```{eval-rst}
.. _previz:
```

## Output data schema

### The output columns from the main catalogue
This is a table of the output columns that can come from the DJA catalogues. The availability of filters varies between fields, so in most cases an output table will not have all of the magnitude columns listed here. Visit the [Filter availability](./filters.md) page to see which filters are available for which fields. 


```{include} ./tables/dja_catalogue_fields_table.md
```

### The output columns from the dense basis catalogue
This is a table of all the output columns that can come from the dense basis catalogue for a field. All columns with a `_50` after them are the median values from the fitting. The dense basis catalogue also includes values that are 1 $\sigma$ above and below the median, which are not included in the `jhive_previz` output catalogues.

```{include} ./tables/db_catalogue_fields_table.md
```

### The output columns from the MorphFITS catalogue
Below is a table of all the output columns that can come from the MorphFITS catalogue for a field. Similar to the output for the DJA catalogue, not all filters are available for all fields, so only a subset of these columns will be present in an output catalogue for a specific field.

```{include} ./tables/mf_catalogue_fields_table.md
```
