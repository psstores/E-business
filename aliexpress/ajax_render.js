//var fs=require('fs');
phantom.outputEncoding="GBK";
var fs=require('fs');
var x = require('casper').selectXPath;
 var data = fs.read('cookies.txt');

phantom.cookies = JSON.parse(data); 

var casper=require('casper').create({
	   pageSettings: {
	   	  javascriptEnabled: true,
          loadImages: false,
          loadPlugins: true,
          userAgent: 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:39.0) Gecko/20100101 Firefox/39.0'
      },
     viewportSize: {width: 1920,height: 7226},
	//logLevel:'debug',
	//verbose:true
});
var page=casper.cli.get('page') 
var url='http://www.aliexpress.com/af/smart%252Bwatch/'+page+'.html?isAffiliate=y&initiative_id=SB_20151220044354&site=glo&shipCountry=US&SearchText=smart+watch&CatId=200010206'
//var url='http://www.aliexpress.com/wholesale?site=glo&g=y&SearchText=&'+page+'=11&initiative_id=SB_20151209062919&shipCountry=US&needQuery=n'               
// var url='http://s.1688.com/selloffer/offer_search.htm?keywords=%C6%BD%BA%E2%B3%B5&sug=2_0&n=y&spm=a260k.635.1998096057.d1#beginPage='+page+'&offset='
// var url='http://s.1688.com/selloffer/offer_search.htm?keywords=%D7%D4%C5%C4%B8%CB&n=y&spm=a260k.635.1998096057.d1#beginPage=2&offset='
//http://s.1688.com/selloffer/offer_search.htm?keywords=%D7%D4%C5%C4%B8%CB&n=y&spm=a260k.635.1998096057.d1#beginPage=3&offset=

casper.start(url,function(){
	
	this.scrollToBottom();
	//this.echo(data);
	//this.capture('test1.png')
})
casper.wait(5000,function(){
//return this.getHTML(),
this.capture('aliexpress.png')
this.echo(this.getHTML())
//fs.write('temp.html',this.getHTML(),'w')
})

// casper.then(function(){
// 	fs.write('temp.html',this.getHTML(),'w')
// })

// casper.start(url,function(){

// // 	this.evaluate(function() {
// // 		this.
  
// // });

// 		fs.write('temp.html',this.getHTML(),'w');
// 		this.capture('test.png')

// 	//this.echo (__utils__.getElementByXPath('.//img')),
// 	// this.echo ('this is a test'),
// 	//this.assertExists(x('//*[@href="//shoppingcart.aliexpress.com"]'), 'the element exists')
//    // if (this.visible('#hplogo')) {
//    //      this.echo("I can see the logo");
//    //  } else {
//    //      this.echo("I can't see the logo");
//    //  }



// })





casper.run(function(){

	//this.echo('So the whole suite ended');
	//__utils__.echo('php');
	this.exit();
})
//http://g01.a.alicdn.com/kf/HTB1kFXxIpXXXXbFXVXXq6xXFXXX2/222419831/HTB1kFXxIpXXXXbFXVXXq6xXFXXX2.jpg?size=128946&height=968&width=790&hash=6b7675c3c37ccb16c5bae8e62ce94824

//USAGE: E:\toolkit\n1k0-casperjs-e3a77d0\bin>python casperjs site.js --url=http://spys.ru/free-proxy-list/IE/ --outputfile='temp.html' 
   
 // var fs = require('fs'); 
 // var casper = require('casper').create({ 
 //  pageSettings: { 
 //  loadImages: false,     
 //  loadPlugins: false,    
 //  userAgent: 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.137 Safari/537.36 LBBROWSER'
 // }, 
 // logLevel: "debug",//日志等级 
 // verbose: true  // 记录日志到控制台 
 //  }); 
 // var url = casper.cli.raw.get('url'); 
 // var outputfile = casper.cli.raw.get('outputfile'); 
 // //请求页面 
 // casper.start(url, function () { 
 // fs.write(outputfile, this.getHTML(), 'w'); 
 // }); 
   
 // casper.run(); 