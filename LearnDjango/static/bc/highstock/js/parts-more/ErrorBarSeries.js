/* ****************************************************************************
 * Start error bar series code                                                *
 *****************************************************************************/

// 1 - set default options
defaultPlotOptions.errorbar = merge(defaultPlotOptions.boxplot, {
	color: '#000000',
	grouping: false,
	linkedTo: ':previous',
	tooltip: {
		pointFormat: defaultPlotOptions.arearange.tooltip.pointFormat
	},
	whiskerWidth: null
});

// 2 - Create the series object
seriesTypes.errorbar = extendClass(seriesTypes.boxplot, {
	type: 'errorbar',
	pointArrayMap: ['low', 'high'], // array point configs are mapped to this
	toYData: function (point) { // return a plain array for speedy calculation
		return [point.low, point.high];
	},
	pointValKey: 'high', // defines the top of the tracker
	doQuartiles: false,

	/**
	 * Get the width and X offset, either on top of the linked series column
	 * or standalone
	 */
	getColumnMetrics: function () {
		return (this.linkedParent && this.linkedParent.columnMetrics) || 
			seriesTypes.column.prototype.getColumnMetrics.call(this);
	}
});

/* ****************************************************************************
 * End error bar series code                                                  *
 *****************************************************************************/
