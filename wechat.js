phantom.outputEncoding="gb2312"
var fs=require('fs')
var casper=require("casper").create({
  verbose:true
});
var data = fs.read("cookies.txt")
phantom.cookies = JSON.parse(data)
var url="http://weixin.sogou.com/gzh?openid=oIWsFtyfVeeK61kmJmfksHmtdfw0&ext=Uc8g8yaxQpF9wzNNDd71426MmuON278tLmPjdKofRHx_4qgkcyEfKliwCT-M6iB_"
function a(){
  
      var d=document.getElementById('wxmore').getAttributeNode('style').value
      return d
}
function b(){
  casper.wait(5000,function(){
   c=casper.evaluate(a);
  casper.echo(c)
  casper.capture('test.png')
  // fs.write('index.html',casper.getHTML(),'w')
            if(c=="visibility: visible;"){
              this.click('div#wxmore a')
              this.echo('正在翻页>>>>>>')
              b()
            }else{
              casper.capture('all.png')
              this.exit()
            }
      })
  
}
casper.start(url,function(){
  console.log("test is starting")
})
casper.then(b)
casper.run(function(){
  this.exit()
})