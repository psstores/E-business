phantom.outputEncoding="gbk";
var fs=require('fs');
var x = require('casper').selectXPath;
var data = fs.read('cookies.txt');
phantom.cookies = JSON.parse(data); 
var casper=require('casper').create({
	   pageSettings: {
	   	  javascriptEnabled: true,
          loadImages: false,
          loadPlugins: true,
          userAgent: 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:39.0) Gecko/20100101 Firefox/39.0',
          
      },
      viewportSize: {width: 1920,height: 7226}
});
//命令行传入参数
var url_taobao=casper.cli.get('URL')
var start=url_taobao.search(/beginPage=/i)+10
var end=url_taobao.search(/&offset/i)	
var page=url_taobao.slice(start,end)

// function assertElement(){
// 	if(this.exists(div[class='test'])){
// 		this.echo('found it')
// 	}else{
// 		this.echo('not found')
// 	}
// }
// casper.echo(page)
// casper.exit()
// var page=4
// var url_taobao='http://s.1688.com/selloffer/offer_search.htm?keywords=%D7%D4%C5%C4%C9%F1%C6%F7&sug=1_0&n=y&spm=a260k.635.1998096057.d1#beginPage=5&offset=9&filterP4pIds=1201122244,521279035344,44905301557,44632737573,523778196750,524414222456,45304569184,523080670148'
casper.start(url_taobao,function(){
})
casper.wait(6000,function(){
	this.scrollToBottom()
	fs.write('1688.html',this.getHTML(),'w')
	this.capture(page+'.png')
})
casper.then(function(){
	//通过function里面的page传递参数
	links=this.evaluate(function(page){
	var links=document.querySelector("ul[id='sm-offer-list']").querySelectorAll("li[id^='offer']");
	return Array.prototype.map.call(links,function(e){
		$page=page
		try{
			$title=e.querySelector("div[class='sm-offer-title sw-dpl-offer-title'] a").innerHTML.replace(/<[^>].*?>/g,"").trim().replace(/"/g,'\\"')
		}catch(err){
			try{
				$title=$title=e.querySelector("div[class='s-widget-offershopwindowtitle sm-offer-title sw-dpl-offer-title'] a").innerHTML.replace(/<[^>].*?>/g,"").trim().replace(/"/g,'\\"')
			}catch(err){
				$title='请你检查属性值是否出错'
			}
		}

		try{
			$price=e.querySelector("div[class='sm-offer-price sw-dpl-offer-price'] span[class='sm-offer-priceNum sw-dpl-offer-priceNum']").innerHTML.replace(/<[^>].*?>/g,"").replace(/\s/g,'')
		}catch(err){
			try{
				$price=e.querySelector("span[class='sm-offer-priceNum sw-dpl-offer-priceNum']").getAttribute('title')
			}catch(err){
				$price='请你检查属性值是否出错'
			}
		}

		try{
			$deal=e.querySelector("div[class='sm-offer-price sw-dpl-offer-price'] span[class='sm-offer-trade sw-dpl-offer-trade ']").getAttribute('title')
		}catch(err){
			try{
				$deal=e.querySelector("span[class='sm-offer-trade sw-dpl-offer-trade ']").getAttribute('title')
			}catch(err){
				$deal='成立为0件'
			}
		}

		try{
			$store_name=e.querySelector("div[class='sm-offer-company sw-dpl-offer-company'] a").getAttribute('title')
		}catch(err){
			try{
				$store_name=e.querySelector("div[class='s-widget-offershopwindowcompanyinfo sm-offer-company sw-dpl-offer-company'] a").getAttribute('title')
			}catch(err){
				$store_name='请你检查属性值是否出错'
			}
		}


		try{
			$store_url=e.querySelector("div[class='sm-offer-company sw-dpl-offer-company'] a").getAttribute('href')
		}catch(err){
			try{
				$store_url=e.querySelector("div[class='s-widget-offershopwindowcompanyinfo sm-offer-company sw-dpl-offer-company'] a").getAttribute('href')
			}catch(err){
				$store_url='请你检查属性值是否出错'
			}
		}

		try{
			$item_url=e.querySelector("div[class='sm-offer-title sw-dpl-offer-title'] a").getAttribute('href')
		}catch(err){
			try{
				$item_url=e.querySelector("div[class='s-widget-offershopwindowtitle sm-offer-title sw-dpl-offer-title'] a").getAttribute('href')
			}catch(err){
				$item_url='请你检查属性值是否出错'
			}
		}

		try{
			$year=e.querySelector("div[class='sm-offer-company sw-dpl-offer-company'] span[class=''sm-offer-companyTag sw-dpl-offer-companyTag] a").innerHTML.replace(/<[^>].*?>/g,"").replace(/\s/g,'')
		}catch(err){
			try{
				$year=e.querySelector("span[class='sm-offer-companyTag sw-dpl-offer-companyTag'] a").innerHTML.replace(/<[^>].*?>/g,"").replace(/\s/g,'')
			}catch(err){
				$year=0
			}
		}
		$li_num=links.length

		//此处处理字符串输出为Json格式，方便python处理。
		$f="{\"page\":\""+$page+"\","+
		   "\"title\":\""+$title+"\","+
		   "\"price\":\""+$price+"\","+
		   "\"deal\":\""+$deal+"\","+
		   "\"store_name\":\""+$store_name+"\","+
		   "\"item_url\":\""+$item_url+"\","+
		   "\"store_url\":\""+$store_url+"\","+
		   "\"li_num\":\""+$li_num+"\","+
		   "\"year\":\""+$year+"\""+"}";

		return $f
				})
		// return links.length
			},page)

	data="["+links+"]"
	require('utils').dump(data)
	// fs.write('aliexpress.txt',data,'w')
})
casper.run(function(){
	this.exit()
})
