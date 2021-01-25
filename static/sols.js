var tfConfig = {
        base_path: 'tablefilter/',
        alternate_rows: true,
        btn_reset: true,
        rows_counter: true,
        loader: true,
        status_bar: true,
        mark_active_columns: {
            highlight_column: true
        },
        highlight_keywords: true,
        no_results_message: true,
        col_0: 'checklist',
        col_1: 'select',
        col_2: 'multiple',
        col_types: [
            'string', 'string', 'number',
            'number', 'number', 'number',
            'number', 'number', 'number'
        ],
        col_widths: [
            '180px', '120px', '120px',
            '100px', '100px', '100px',
            '100px', '100px', '100px'
        ],
        extensions: [{
            name: 'sort'
        }],

        /** Material Design Lite integration */

        // aligns filter at cell bottom when Material Design Lite is enabled
        filters_cell_tag: 'th',

        // allows Material Design Lite table styling
        themes: [{
            name: 'transparent'
        }]
    };

    var tf = new TableFilter(document.querySelector('#demo'), tfConfig);
    tf.init();