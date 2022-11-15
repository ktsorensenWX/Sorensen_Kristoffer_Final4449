/*
 Highstock JS v8.1.2 (2020-06-16)

 Indicator series type for Highstock

 (c) 2010-2019 Pawe Fus

 License: www.highcharts.com/license
*/
(function(a){"object"===typeof module&&module.exports?(a["default"]=a,module.exports=a):"function"===typeof define&&define.amd?define("highcharts/indicators/bollinger-bands",["highcharts","highcharts/modules/stock"],function(d){a(d);a.Highcharts=d;return a}):a("undefined"!==typeof Highcharts?Highcharts:void 0)})(function(a){function d(a,b,d,n){a.hasOwnProperty(b)||(a[b]=n.apply(null,d))}a=a?a._modules:{};d(a,"mixins/multipe-lines.js",[a["parts/Globals.js"],a["parts/Utilities.js"]],function(a,b){var d=
b.defined,n=b.error,p=b.merge,q=a.seriesTypes.sma;return{pointArrayMap:["top","bottom"],pointValKey:"top",linesApiNames:["bottomLine"],getTranslatedLinesNames:function(e){var a=[];(this.pointArrayMap||[]).forEach(function(c){c!==e&&a.push("plot"+c.charAt(0).toUpperCase()+c.slice(1))});return a},toYData:function(e){var a=[];(this.pointArrayMap||[]).forEach(function(c){a.push(e[c])});return a},translate:function(){var e=this,a=e.pointArrayMap,c=[],b;c=e.getTranslatedLinesNames();q.prototype.translate.apply(e,
arguments);e.points.forEach(function(d){a.forEach(function(a,r){b=d[a];null!==b&&(d[c[r]]=e.yAxis.toPixels(b,!0))})})},drawGraph:function(){var a=this,b=a.linesApiNames,c=a.points,w=c.length,r=a.options,z=a.graph,t={options:{gapSize:r.gapSize}},k=[],f;a.getTranslatedLinesNames(a.pointValKey).forEach(function(a,b){for(k[b]=[];w--;)f=c[w],k[b].push({x:f.x,plotX:f.plotX,plotY:f[a],isNull:!d(f[a])});w=c.length});b.forEach(function(b,c){k[c]?(a.points=k[c],r[b]?a.options=p(r[b].styles,t):n('Error: "There is no '+
b+' in DOCS options declared. Check if linesApiNames are consistent with your DOCS line names." at mixin/multiple-line.js:34'),a.graph=a["graph"+b],q.prototype.drawGraph.call(a),a["graph"+b]=a.graph):n('Error: "'+b+" doesn't have equivalent in pointArrayMap. To many elements in linesApiNames relative to pointArrayMap.\"")});a.points=c;a.options=r;a.graph=z;q.prototype.drawGraph.call(a)}}});d(a,"indicators/bollinger-bands.src.js",[a["parts/Globals.js"],a["parts/Utilities.js"],a["mixins/multipe-lines.js"]],
function(a,b,d){var n=b.isArray,p=b.merge;b=b.seriesType;var q=a.seriesTypes.sma;b("bb","sma",{params:{period:20,standardDeviation:2,index:3},bottomLine:{styles:{lineWidth:1,lineColor:void 0}},topLine:{styles:{lineWidth:1,lineColor:void 0}},tooltip:{pointFormat:'<span style="color:{point.color}">\u25cf</span><b> {series.name}</b><br/>Top: {point.top}<br/>Middle: {point.middle}<br/>Bottom: {point.bottom}<br/>'},marker:{enabled:!1},dataGrouping:{approximation:"averages"}},p(d,{pointArrayMap:["top",
"middle","bottom"],pointValKey:"middle",nameComponents:["period","standardDeviation"],linesApiNames:["topLine","bottomLine"],init:function(){q.prototype.init.apply(this,arguments);this.options=p({topLine:{styles:{lineColor:this.color}},bottomLine:{styles:{lineColor:this.color}}},this.options)},getValues:function(a,b){var c=b.period,d=b.standardDeviation,e=a.xData,p=(a=a.yData)?a.length:0,t=[],k=[],f=[],l;if(!(e.length<c)){var A=n(a[0]);for(l=c;l<=p;l++){var u=e.slice(l-c,l);var m=a.slice(l-c,l);var g=
q.prototype.getValues.call(this,{xData:u,yData:m},b);u=g.xData[0];g=g.yData[0];for(var x=0,y=m.length,v=0;v<y;v++){var h=(A?m[v][b.index]:m[v])-g;x+=h*h}h=Math.sqrt(x/(y-1));m=g+d*h;h=g-d*h;t.push([u,m,g,h]);k.push(u);f.push([m,g,h])}return{values:t,xData:k,yData:f}}}}));""});d(a,"masters/indicators/bollinger-bands.src.js",[],function(){})});
//# sourceMappingURL=bollinger-bands.js.map