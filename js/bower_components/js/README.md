# $js - Asynchronous Module Definition framework

 From lightweight javascript dependencies manager to asynchronous module definition framework.  
 $js is greatly lighter than the famous AMD framework [requirejs](http://requirejs.org) or, of course, the wonderful [jQuery](http://jquery.com) framework. By using it as the only script required by your page to load you can improve significantly the performance of your page loading and make your javascript realy non obstrusive.
 Because the javascript work start after page loaded, if you use jquery, no more need of "*$(document).ready()*" function, the document will always be ready when your code will work on it.  
 If you allready loaded a script via *$js*, and you need it again in other part of your code, it will not reload it unecessary.

Simple Usage
------------

 Put this code at the top bottom of your page just before the ending body tag.

```html
<script src="js/js.pack.js" type="text/javascript"></script>
<script type="text/javascript">
    $js.dev = true;
    $js('script');
</script>
```

Dependencies manager
--------------------

### Config

Here is the default config.   

```javascript
$js.async = true;
$js.path = 'js/';
$js.pathSuffix = '.js';
$js.pathDetection = true;
$js.dev = false;
```

With *pathDetection* enabled if the *path* is allready present at start of script url, it will not be repeated, same at end for the *pathSuffix*.   
If a script url start with trailing slash "*/*", no path or pathSuffix will be added to it, allowing you to use pseudo absolute path in your domain. In the same way if a script url contain the "*://*" sign of absolute url, it will not be changed.   
If dev set to true, a time GET parameter will be added to script calling, like in jquery, to avoid the cache mechanism.   
If you put *async* to true, all scripts called from main flow will be loaded in order. It's not recommanded to do that.


### Simple call

```javascript
$js('js/script.js');
$js('js/script');
$js('script.js');
$js('script');
```

### Async Callbacks

In async mode it will not wait for dependency1 loaded to start loading dependency2. In this case, dependency2 does not depend on dependency1. The order of arguments doesn't matter.

```javascript
$js(['dependency1','dependency2'],function(){
	//when dependency1 and dependency2 are loaded
});
$js({
	dependency1:function(){
		//when dependency1 loaded
	},
	dependency2:function(){
		//when dependency2 loaded (after dependency loaded)
	},
},function(){
	//when dependency1 and dependency2 are loaded
});
```

### Sync Callbacks

The boolean *true* enable *sync* mode. In sync mode it will wait for dependency1 loaded to start loading dependency2. In this case, dependency2 does depend on dependency1. The order of arguments doesn't matter.

```javascript
$js(true,['dependency1','dependency2'],function(){
	//when dependency1 and dependency2 are loaded
});
$js(true,{
	'dependency1':function(){
		//when dependency1 loaded
	},
	'dependency2':function(){
		//when dependency2 loaded (after dependency loaded)
	},
},function(){
		//when dependency1 and dependency2 are loaded
});
```

### Alias

Alias are recursively resolved and can be a reference to several scripts.

```javascript
$js.alias('j','jquery');
$js.alias('jui',['j','jquery-ui/core','jquery-ui/widget']);
```

### Dependencies Map

A call to *dependencies* method will add the given map to allready defined. This map will be used on script calls to resolve dependencies and load them when needed but will not load the keys of map and all the map.

```javascript
$js.dependencies({
	'jquery-ui/mouse':['jui'],
	'jquery-ui/sortable':['jui','jquery-ui/mouse'],
	'jquery-ui/resizable':['jui','jquery-ui/mouse'],
	'jquery.sortElements':['j'],
});

$js([
	'jquery.sortElements',
	'jquery-ui/sortable',
	'jquery-ui/resizable',
],function(){
	//...
});
```

### Chainable

```javascript
$js('dependency1')('dependency2')(function(){
	//when dependency1 and dependency2 are loaded
});

//is equivalent of
$js(true,['dependency1','dependency2'],function(){
	//when dependency1 and dependency2 are loaded
});

//and equivalent of
$js('dependency1',function(){
	$js('dependency2',function(){
		//when dependency1 and dependency2 are loaded
	});
});

//but the difference it that you can assign the resolved function to variable
var whenReady = $js('dependency1');
whenReady = whenReady('dependency2');
whenReady(function(){
	//when dependency1 and dependency2 are loaded
});
```

CSS helper
----------

### Config

Here is the default config. See [config of js](http://redcatphp.com/js-amd#js-config) upper for details.

```javascript
$css.path = 'css/';
$css.pathSuffix = '.css';
$css.pathDetection = true;
$css.dev = false;
```

### Simple call

It will check if the link is allready present in the document and if it's the case, it will not load it. You cannot use callback on it because this feature it's not supported by browsers.

```javascript
$css('css/style.css');
$css('css/style');
$css('style.css');
$css('style');
```

Asynchronous Module Definition
------------------------------

A module can be a function or an object and can be defined in several ways. Order of arguments doesn't matter.

### Simple module definition and usage

```javascript
// definition
$js.module('random',function(){
	return Math.random();
});

// usage
var number = $js.module('random')();
```

### Module definition and usage with automatic name

```javascript
// file script.js
$js('random',function(){	
	//usage
	var number = $js.module('random')();
});

// file random.js
// here the name will be automaticaly set to 'random'
$js.module(function(){
	return Math.random();
});
```

### Complete module definition with dependencies

```javascript
// file script.js
$js('moduleA',function(){
	// will output 'test of moduleA'
	console.log( $js.module('moduleA').val );
	
	$js.module('moduleA').test();
});

// file moduleA.js
// with dependencies in sync mode
$js.module(true,['moduleB','otherDependency'],{
	val:'test of moduleA',
	test:function(){
		// will output 'result of test moduleB'
		console.log( $js.module('moduleB')() );
	}
});

// file moduleB.js
$js.module(function(){
	return 'result of moduleB';
});
```