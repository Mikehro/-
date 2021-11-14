var that;
class AsideNav{
	constructor(className){
		this.main = document.querySelector(className);
		
		this.lis= this.main.querySelectorAll(".nav-list .item");
		
		this.parentNavs = this.main.querySelectorAll(".nav-list .item .parentNav");
		
		this.init();
	}
	init(){
		for(var i=0;i<this.lis.length;i++){
			this.parentNavs[i].onclick = this.toggleNav;
		}
	}
	
	clearClass(){
		for(var i=0;i<this.lis.length;i++){
			this.lis[i].className = "item";
		}
	}
	
	toggleNav(){
		var li =this.parentNode;
		if(li.classList.contains("active")){
			li.classList.remove("active");
		}else{
			//that.clearClass();
		    li.classList.add("active");
		}
		
	}
}
var asideNav=new AsideNav(".aside-nav");