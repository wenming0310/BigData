# -*- coding:utf-8 -*-
from bs4 import BeautifulSoup
html_doc = """<!DOCTYPE html>
<!-- saved from url=(0022)https://www.baidu.com/ -->
<html><head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
    
    
    <meta http-equiv="X-UA-Compatible" content="IE=Edge">
	<meta content="always" name="referrer">
    <meta name="theme-color" content="#2932e1">
    <link rel="shortcut icon" href="https://www.baidu.com/favicon.ico" type="image/x-icon">
    <link rel="search" type="application/opensearchdescription+xml" href="https://www.baidu.com/content-search.xml" title="百度搜索">
    <link rel="icon" sizes="any" mask="" href="https://www.baidu.com/img/baidu_85beaf5496f291521eb75ba38eacbd87.svg">
	
	
	<link rel="dns-prefetch" href="https://s1.bdstatic.com/">
	<link rel="dns-prefetch" href="https://t1.baidu.com/">
	<link rel="dns-prefetch" href="https://t2.baidu.com/">
	<link rel="dns-prefetch" href="https://t3.baidu.com/">
	<link rel="dns-prefetch" href="https://t10.baidu.com/">
	<link rel="dns-prefetch" href="https://t11.baidu.com/">
	<link rel="dns-prefetch" href="https://t12.baidu.com/">
	<link rel="dns-prefetch" href="https://b1.bdstatic.com/">
    
    <title>百度一下，你就知道</title>
    

<style id="css_index" index="index" type="text/css">html,body{height:100%}
html{overflow-y:auto}
body{font:12px arial;text-align:;background:#fff}
body,p,form,ul,li{margin:0;padding:0;list-style:none}
body,form,#fm{position:relative}
td{text-align:left}
img{border:0}
a{color:#00c}
a:active{color:#f60}
input{border:0;padding:0}
#wrapper{position:relative;_position:;min-height:100%}
#head{padding-bottom:100px;text-align:center;*z-index:1}
#ftCon{height:50px;position:absolute;bottom:47px;text-align:left;width:100%;margin:0 auto;z-index:0;overflow:hidden}
.ftCon-Wrapper{overflow:hidden;margin:0 auto;text-align:center;*width:640px}
.qrcodeCon{text-align:center;position:absolute;bottom:140px;height:60px;width:100%}
#qrcode{display:inline-block;*float:left;*margin-top:4px}
#qrcode .qrcode-item{float:left}
#qrcode .qrcode-item-2{margin-left:33px}
#qrcode .qrcode-img{width:60px;height:60px}
#qrcode .qrcode-item-1 .qrcode-img{background:url(https://ss1.bdstatic.com/5eN1bjq8AAUYm2zgoY3K/r/www/cache/static/protocol/https/home/img/qrcode/zbios_efde696.png) 0 0 no-repeat}
#qrcode .qrcode-item-2 .qrcode-img{background:url(https://ss1.bdstatic.com/5eN1bjq8AAUYm2zgoY3K/r/www/cache/static/protocol/https/home/img/qrcode/nuomi_365eabd.png) 0 0 no-repeat}
@media only screen and (-webkit-min-device-pixel-ratio:2){#qrcode .qrcode-item-1 .qrcode-img{background-image:url(https://ss1.bdstatic.com/5eN1bjq8AAUYm2zgoY3K/r/www/cache/static/protocol/https/home/img/qrcode/zbios_x2_9d645d9.png);background-size:60px 60px}
#qrcode .qrcode-item-2 .qrcode-img{background-image:url(https://ss1.bdstatic.com/5eN1bjq8AAUYm2zgoY3K/r/www/cache/static/protocol/https/home/img/qrcode/nuomi_x2_55dc5b7.png);background-size:60px 60px}}
#qrcode .qrcode-text{color:#999;line-height:23px;margin:3px 0 0}
#qrcode .qrcode-text a{color:#999;text-decoration:none}
#qrcode .qrcode-text p{text-align:center}
#qrcode .qrcode-text b{color:#666;font-weight:700}
#qrcode .qrcode-text span{letter-spacing:1px}
#ftConw{display:inline-block;text-align:left;margin-left:33px;line-height:22px;position:relative;top:-2px;*float:right;*margin-left:0;*position:static}
#ftConw,#ftConw a{color:#999}
#ftConw{text-align:center;margin-left:0}
.bg{background-image:url(https://ss1.bdstatic.com/5eN1bjq8AAUYm2zgoY3K/r/www/cache/static/protocol/https/global/img/icons_5859e57.png);background-repeat:no-repeat;_background-image:url(https://ss1.bdstatic.com/5eN1bjq8AAUYm2zgoY3K/r/www/cache/static/protocol/https/global/img/icons_d5b04cc.gif)}
.c-icon{display:inline-block;width:14px;height:14px;vertical-align:text-bottom;font-style:normal;overflow:hidden;background:url(https://ss1.bdstatic.com/5eN1bjq8AAUYm2zgoY3K/r/www/cache/static/protocol/https/global/img/icons_5859e57.png) no-repeat 0 0;_background-image:url(https://ss1.bdstatic.com/5eN1bjq8AAUYm2zgoY3K/r/www/cache/static/protocol/https/global/img/icons_d5b04cc.gif)}
.c-icon-triangle-down-blue{background-position:-480px -168px}
.c-icon-chevron-unfold2{background-position:-504px -168px}
#m{width:720px;margin:0 auto}
#nv a,#nv b,.btn,#lk{font-size:14px}
#nv{height:19px;font-size:16px;margin:0 0 4px;text-align:left;text-indent:137px}
.s_btn{width:95px;height:32px;padding-top:2px\9;font-size:14px;background-color:#ddd;background-position:0 -48px;cursor:pointer}
.s_btn_h{background-position:-240px -48px}
.s_btn_wr{width:97px;height:34px;display:inline-block;background-position:-120px -48px;*position:relative;z-index:0;vertical-align:top}
#jgwab{margin-left:19px}
#cp .c-icon-icrlogo,.c-icon-jgwablogo{width:14px;height:17px;display:inline-block;overflow:hidden;background:url(https://ss1.bdstatic.com/5eN1bjq8AAUYm2zgoY3K/r/www/cache/static/protocol/https/global/img/icons_5859e57.png) no-repeat;_background-image:url(https://ss1.bdstatic.com/5eN1bjq8AAUYm2zgoY3K/r/www/cache/static/protocol/https/global/img/icons_d5b04cc.gif)}
#cp .c-icon-icrlogo{background-position:-600px -96px;position:relative;top:3px}
.c-icon-jgwablogo{background-position:-623px -96px;position:relative;top:3px}
#shouji{margin-right:14px}
#u{display:none}
#c-tips-container{display:none}
#wrapper{min-width:810px;height:100%;min-height:600px}
#head{position:relative;padding-bottom:0;height:100%;min-height:600px}
#head .head_wrapper{height:100%}
#m{position:relative}
#fm{padding-left:40px;top:-37px}
#lh a{margin-left:62px}
#lh #seth,#lh #setf{margin-left:0}
#lk{position:absolute;display:none;top:0;right:0;margin:33px 0}
#lk span{font:14px "宋体"}
#nv{position:absolute;display:none;top:0;right:0}
#lm{color:#666;width:100%;height:60px;margin-top:60px;line-height:15px;font-size:13px;position:absolute;top:0;left:0}
#lm a{color:#666}
#pad-version{line-height:40px}
.s_ipt_wr.bg,.s_btn_wr.bg,#su.bg{background-image:none}
.s_btn_wr{width:auto;height:auto;border-bottom:1px solid transparent;*border-bottom:0}
.s_btn{width:100px;height:36px;color:#fff;font-size:15px;letter-spacing:1px;background:#3385ff;border-bottom:1px solid #2d78f4;outline:medium;*border-bottom:0;-webkit-appearance:none;-webkit-border-radius:0}
.s_btn.btnhover{background:#317ef3;border-bottom:1px solid #2868c8;*border-bottom:0;box-shadow:1px 1px 1px #ccc}
.s_btn_h{background:#3075dc;box-shadow:inset 1px 1px 5px #2964bb;-webkit-box-shadow:inset 1px 1px 5px #2964bb;-moz-box-shadow:inset 1px 1px 5px #2964bb;-o-box-shadow:inset 1px 1px 5px #2964bb}
#result_logo{display:none}
#index_logo img{display:inline-block;width:270px;height:129px}
#s_tab{display:none}
.s_form{position:relative;top:38.2%}
.s_form_wrapper{position:relative;top:-191px}
.s_ipt_wr{height:34px}
#head .c-icon-bear-round{display:none}
#form{margin:22px auto 0;width:641px;text-align:left;z-index:100}
#form .bdsug,#fm .bdsug{top:35px}
.bdsug{display:none;position:absolute;width:538px;background:#fff;border:1px solid #ccc;_overflow:hidden;box-shadow:1px 1px 3px #ededed;-webkit-box-shadow:1px 1px 3px #ededed;-moz-box-shadow:1px 1px 3px #ededed;-o-box-shadow:1px 1px 3px #ededed}
.bdsug.bdsugbg ul{background:url(https://ss1.bdstatic.com/5eN1bjq8AAUYm2zgoY3K/r/www/cache/static/protocol/https/home/img/sugbg_1762fe7.png) 100% 100% no-repeat;background-size:100px 110px;background-image:url(https://ss1.bdstatic.com/5eN1bjq8AAUYm2zgoY3K/r/www/cache/static/protocol/https/home/img/sugbg_90fc9cf.gif)\9}
.bdsug li{width:522px;color:#000;font:14px arial;line-height:25px;padding:0 8px;position:relative;cursor:default}
.bdsug li.bdsug-s{background:#f0f0f0}
.bdsug-store span,.bdsug-store b{color:#7A77C8}
.bdsug-store-del{font-size:12px;color:#666;text-decoration:underline;position:absolute;right:8px;top:0;cursor:pointer;display:none}
.bdsug-s .bdsug-store-del{display:inline-block}
.bdsug-ala{display:inline-block;border-bottom:1px solid #e6e6e6}
.bdsug-ala h3{line-height:14px;background:url(//www.baidu.com/img/sug_bd.png) no-repeat left center;margin:8px 0 5px;font-size:12px;font-weight:400;color:#7B7B7B;padding-left:20px}
.bdsug-ala p{font-size:14px;font-weight:700;padding-left:20px}
.bdsug .bdsug-direct{width:auto;padding:0;border-bottom:1px solid #f1f1f1}
.bdsug .bdsug-direct p{color:#00c;font-weight:700;line-height:34px;padding:0 8px;cursor:pointer;white-space:nowrap;overflow:hidden}
.bdsug .bdsug-direct p img{width:16px;height:16px;margin:7px 6px 9px 0;vertical-align:middle}
.bdsug .bdsug-direct p span{margin-left:8px}
.bdsug .bdsug-direct p i{font-size:12px;line-height:100%;font-style:normal;font-weight:400;color:#fff;background-color:#2b99ff;display:inline;text-align:center;padding:1px 5px;*padding:2px 5px 0;margin-left:8px;overflow:hidden}
.bdsug .bdsug-pcDirect{color:#000;font-size:14px;line-height:30px;height:30px;background-color:#f8f8f8}
.bdsug .bdsug-pc-direct-tip{position:absolute;right:15px;top:8px;width:55px;height:15px;display:block;background:url(https://ss1.bdstatic.com/5eN1bjq8AAUYm2zgoY3K/r/www/cache/static/protocol/https/global/img/pc_direct_42d6311.png) no-repeat 0 0}
.bdsug li.bdsug-pcDirect-s{background-color:#f0f0f0}
.bdsug .bdsug-pcDirect-is{color:#000;font-size:14px;line-height:22px;background-color:#f8f8f8}
.bdsug .bdsug-pc-direct-tip-is{position:absolute;right:15px;top:3px;width:55px;height:15px;display:block;background:url(https://ss1.bdstatic.com/5eN1bjq8AAUYm2zgoY3K/r/www/cache/static/protocol/https/global/img/pc_direct_42d6311.png) no-repeat 0 0}
.bdsug li.bdsug-pcDirect-is-s{background-color:#f0f0f0}
.bdsug .bdsug-pcDirect-s .bdsug-pc-direct-tip,.bdsug .bdsug-pcDirect-is-s .bdsug-pc-direct-tip-is{background-position:0 -15px}
.bdsug .bdsug-newicon{color:#929292;opacity:.7;font-size:12px;display:inline-block;line-height:22px;letter-spacing:2px}
.bdsug .bdsug-s .bdsug-newicon{opacity:1}
.bdsug .bdsug-newicon i{letter-spacing:0;font-style:normal}
.toggle-underline{text-decoration:none}
.toggle-underline:hover{text-decoration:underline}
.tools{position:absolute;right:-75px}
#mHolder{width:62px;position:relative;z-index:296;display:none}
#mCon{height:18px;line-height:18px;position:absolute;cursor:pointer}
#mCon span{color:#00c;display:block;width:24px}
#mCon .hw{text-decoration:underline;cursor:pointer;display:inline-block}
#mCon .pinyin{display:inline-block}
#mCon .c-icon-chevron-unfold2{margin-left:5px}
#mMenu a{width:100%;height:100%;display:block;line-height:22px;text-indent:6px;text-decoration:none;filter:none\9}
#mMenu,#user ul{box-shadow:1px 1px 2px #ccc;-moz-box-shadow:1px 1px 2px #ccc;-webkit-box-shadow:1px 1px 2px #ccc;filter:progid:DXImageTransform.Microsoft.Shadow(Strength=2, Direction=135, Color=#cccccc)\9}
#mMenu{width:56px;border:1px solid #9b9b9b;list-style:none;position:absolute;right:27px;top:28px;display:none;background:#fff}
#mMenu a:hover{background:#ebebeb}
#mMenu .ln{height:1px;background:#ebebeb;overflow:hidden;font-size:1px;line-height:1px;margin-top:-1px}
#u1 a:link,#u1 a:visited{color:#666;text-decoration:none}
#u1 a:hover,#u1 a:active{text-decoration:underline}
#u1 a:active{color:#00c}
#u1{z-index:2;color:#fff;position:absolute;right:0;top:0;margin:19px 0 5px;padding:0 96px 0 0}
#u1 .reg{display:none}
#u1 a.pf,#u1 a.pf:visited{display:inline-block;float:left;color:#333;line-height:24px;font-size:13px;margin-left:20px;overflow:hidden;text-decoration:underline}
#u1 a.lb,#u1 a.lb:visited,#u1 a.username{display:inline-block;float:left;color:#333;font-size:13px;line-height:24px;margin-left:20px;text-decoration:underline}
#u1 a.bri,#u1 a.bri:visited{display:inline-block;position:absolute;right:10px;width:60px;height:23px;float:left;color:#fff;background:#38f;line-height:24px;font-size:13px;text-align:center;overflow:hidden;border-bottom:1px solid #38f;margin-left:19px;margin-right:2px}
#u1 a.bri.brihover{display:none;text-decoration:none;color:#333;background:0 0;border-bottom:1px solid transparent;margin-left:19px}
#u1 #lm a{color:#00c;text-decoration:underline}
#u1 a.mnav,#u1 a.mnav:visited{float:left;color:#333;font-weight:700;line-height:24px;margin-left:20px;font-size:13px;text-decoration:underline}
#u1 a.pf:hover,#u1 a.lb:hover,#u1 a.mnav:hover{color:#00c}
.briiconsbg{background-repeat:no-repeat;background-size:300px 18px;background-image:url(https://ss1.bdstatic.com/5eN1bjq8AAUYm2zgoY3K/r/www/cache/static/protocol/https/home/img/icons_0c37e9b.png);background-image:url(https://ss1.bdstatic.com/5eN1bjq8AAUYm2zgoY3K/r/www/cache/static/protocol/https/home/img/icons_809ae65.gif)\9}
.bdpfmenu{background-color:#fff;border:1px solid #d1d1d1;position:absolute;right:160px;width:68px;top:36px;margin-top:-1px;_margin-top:-3px;z-index:2;box-shadow:1px 1px 5px #d1d1d1;-webkit-box-shadow:1px 1px 5px #d1d1d1;-moz-box-shadow:1px 1px 5px #d1d1d1;-o-box-shadow:1px 1px 5px #d1d1d1}
.bdpfmenu a{display:block;text-align:left;margin:0!important;padding:0 9px;line-height:26px;text-decoration:none}
#wrapper .bdpfmenu a:link,#wrapper .bdpfmenu a:visited{background:#fff;color:#333}
#wrapper .bdpfmenu a:hover,#wrapper .bdpfmenu a:active{background:#38f;text-decoration:none;color:#fff}
#wrapper .bdnuarrow{width:0;height:0;font-size:0;line-height:0;display:block;position:absolute;top:-10px;left:50%;margin-left:-5px}
#wrapper .bdnuarrow em,#wrapper .bdnuarrow i{width:0;height:0;font-size:0;line-height:0;display:block;position:absolute;border:5px solid transparent;border-style:dashed dashed solid}
#wrapper .bdnuarrow em{border-bottom-color:#d8d8d8;top:-1px}
#wrapper .bdnuarrow i{border-bottom-color:#fff;top:0}
.s-isindex-wrap #wrapper .bdnuarrow{height:13px;background:url(https://ss1.bdstatic.com/5eN1bjq8AAUYm2zgoY3K/r/www/cache/static/protocol/https/home/img/icons_0c37e9b.png) no-repeat -90px -1px}
#wrapper .bdnuarrow.bdbriarrow{right:104px;display:none!important}
#wrapper .bdbri{width:85px;min-height:100px;border-left:1px solid #e7e7e7;position:absolute;background-color:#f9f9f9;overflow:hidden;z-index:2;right:0;top:0}
#prefpanel{background:#fafafa;display:none;opacity:0;position:fixed;_position:absolute;top:-359px;z-index:1000;width:100%;min-width:960px;border-bottom:1px solid #ebebeb}
#prefpanel form{_width:850px}
#wrapper .bdbriimgtitle{color:#333;text-align:center;width:66px;height:43px;line-height:43px;padding-top:9px;margin:0 auto;border-bottom:#f0f0f0 1px solid;font-size:13px;cursor:default}
#wrapper .briscrollwrapper{overflow:hidden}
#wrapper .briscrollwrapperContainer{position:relative}
#wrapper .bdbri.bdbriimg .bdmainlink a,#wrapper .bdbri.bdbriimg .bdothlink a{display:block;text-align:center;width:66px;height:76px;margin:0 auto;border-bottom:#f0f0f0 1px solid;color:#666;text-decoration:none;overflow:hidden}
#wrapper .bdbri.bdbriimg .bdmainlink a:visited,#wrapper .bdbri.bdbriimg .bdothlink a:visited{color:#666}
#wrapper .bdbri.bdbriimg .bdmainlink a:hover,#wrapper .bdbri.bdbriimg .bdothlink a:hover{color:#666;text-decoration:underline}
#wrapper .bdbri.bdbriimg .bdmainlink a:active,#wrapper .bdbri.bdbriimg .bdothlink a:active{color:#00c;text-decoration:underline}
#wrapper .bdbri.bdbriimg span{width:36px;height:36px;display:block;margin:10px auto 5px;background:url(https://ss1.bdstatic.com/5eN1bjq8AAUYm2zgoY3K/r/www/cache/static/protocol/https/home/img/logos/bdbri_icons_0a62ce1.png) no-repeat;cursor:pointer}
#wrapper .bdbri.bdbriimg .bdbrimore,#wrapper .bdbri.bdbriimg .bdbrievenmore{clear:both;text-align:center}
#wrapper .bdbri.bdbriimg .bdbrievenmore{margin-top:15px;height:30px;width:85px;overflow:hidden}
#wrapper .bdbri.bdbriimg span.bdbriimgitem_1{background-position:0 0}
#wrapper .bdbri.bdbriimg span.bdbriimgitem_2{background-position:-36px 0}
#wrapper .bdbri.bdbriimg span.bdbriimgitem_3{width:40px;background-position:-72px 0}
#wrapper .bdbri.bdbriimg span.bdbriimgitem_4{background-position:-112px 0}
#wrapper .bdbri.bdbriimg span.bdbriimgitem_5{background-position:-148px 0}
#wrapper .bdbri.bdbriimg span.bdbriimgitem_6{background-position:-184px 0}
#wrapper .bdbri.bdbriimg span.bdbriimgitem_7{background-position:-220px 0}
#wrapper .bdbri.bdbriimg .bdbrievenmore a:link,#wrapper .bdbri.bdbriimg .bdbrievenmore a:visited{color:#666;text-decoration:underline}
#wrapper .bdbri.bdbriimg .bdbrievenmore a:hover{color:#666;text-decoration:underline}
#wrapper .bdbri.bdbriimg .bdbrievenmore a:active{color:#00c}
.bdbriscroll-ctrl-scroll{position:absolute;top:10px;right:1px;width:8px;border-top:1px solid #e4e4e4;border-left:1px solid #e4e4e4;cursor:default;-webkit-user-select:none;-moz-user-select:none}
.bdbriscroll-ctrl-scroll .bdbriscroll-axis{width:8px;left:0;z-index:0;position:absolute;background:#f2f2f2}
.bdbriscroll-ctrl-scroll-touch .bdbriscroll-axis{width:7px;background:#f2f2f2}
.bdbriscroll-ctrl-scroll-hover .bdbriscroll-axis{background:#f2f2f2}
.bdbriscroll-ctrl-scroll .bdbriscroll-slider{overflow:hidden;width:7px;height:14px;position:absolute;left:0;z-index:10;display:none;background:#d9d9d9;margin-top:-1px;margin-left:-1px;border-right:1px solid #cecece;border-bottom:1px solid #cecece;cursor:default}
.bdbriscroll-ctrl-scroll-touch .bdbriscroll-slider,.bdbriscroll-ctrl-scroll-hover .bdbriscroll-slider{background:#b8b8b8;border-right:1px solid #afafaf;border-bottom:1px solid #afafaf}
.s_ipt::-webkit-input-placeholder{padding-left:3px;color:#aaa;font-size:13px}
.s_ipt::-moz-placeholder{padding-left:3px;color:#aaa;font-size:13px}
.s_ipt:-ms-input-placeholder{padding-left:3px;color:#aaa;font-size:13px}
.s_ipt::placeholder{padding-left:3px;color:#aaa;font-size:13px}
.kw-placeholder{position:absolute;top:0;left:0;color:#aaa;font-size:13px;height:35px;line-height:35px;padding-left:10px;max-width:360px;z-index:99;pointer-events:none}
.kw-placeholder.placeholders-hidden{visibility:hidden}</style>

<!--[if lte IE 8]>
<style index="index" data-compress="strip">
.s_form{top:260px}
</style>
<![endif]-->
<!--[if IE 8]>
<style index="index" data-compress="strip">
#u1 a.mnav,#u1 a.mnav:visited,#u1 a.lb,#u1 a.lb:visited,#u1 a.pf,#u1 a.pf:visited,#u1 a.bri,#u1 a.bri:visited{font-family:simsun;}
</style>
<![endif]-->
<style data-for="debug">
#debug{display:none!important;}
</style>
<style data-for="result" id="css_index_result" type="text/css">#seth{display:inline;behavior:url(#default#homepage)}
#setf{display:inline}
#sekj{margin-left:14px}
#st,#sekj{display:none}
.s_ipt_wr{border:1px solid #b6b6b6;border-color:#7b7b7b #b6b6b6 #b6b6b6 #7b7b7b;background:#fff;display:inline-block;vertical-align:top;width:539px;margin-right:0;border-right-width:0;border-color:#b8b8b8 transparent #ccc #b8b8b8;overflow:hidden}
.wrapper_s .s_ipt_wr{width:439px}
.wrapper_s .s_ipt{width:434px}
.wrapper_s .s_ipt_tip{width:434px}
.s_ipt_wr:hover,.s_ipt_wr.ipthover{border-color:#999 transparent #b3b3b3 #999}
.s_ipt_wr.iptfocus{border-color:#4791ff transparent #4791ff #4791ff}
.s_ipt_tip{color:#aaa;position:absolute;z-index:-10;font:16px/22px arial;height:32px;line-height:32px;padding-left:7px;overflow:hidden;width:526px}
.s_ipt{width:526px;height:22px;font:16px/18px arial;line-height:22px;margin:6px 0 0 7px;padding:0;background:transparent;border:0;outline:0;-webkit-appearance:none}
#kw{position:relative}
#u .username i{background-position:-408px -144px}
.bdpfmenu,.usermenu{border:1px solid #d1d1d1;position:absolute;width:105px;top:36px;z-index:302;box-shadow:1px 1px 5px #d1d1d1;-webkit-box-shadow:1px 1px 5px #d1d1d1;-moz-box-shadow:1px 1px 5px #d1d1d1;-o-box-shadow:1px 1px 5px #d1d1d1}
.bdpfmenu{font-size:12px;background-color:#fff}
.bdpfmenu a,.usermenu a{display:block;text-align:left;margin:0!important;padding:0 9px;line-height:26px;text-decoration:none}
.briiconsbg{background-repeat:no-repeat;background-size:300px 18px;background-image:url(https://ss1.bdstatic.com/5eN1bjq8AAUYm2zgoY3K/r/www/cache/static/protocol/https/home/img/icons_0c37e9b.png);background-image:url(https://ss1.bdstatic.com/5eN1bjq8AAUYm2zgoY3K/r/www/cache/static/protocol/https/home/img/icons_809ae65.gif)\9}
#u{z-index:301;position:absolute;right:0;top:0;margin:21px 9px 5px 0;padding:0}
.wrapper_s #u{margin-right:3px}
#u a{text-decoration:underline;color:#333;margin:0 7px}
.wrapper_s #u a{margin-right:0 6px}
#u div a{text-decoration:none}
#u a:hover{text-decoration:underline}
#u .back_org{color:#666;float:left;display:inline-block;height:24px;line-height:24px}
#u .bri{display:inline-block;width:24px;height:24px;float:left;line-height:24px;color:transparent;background:url(https://ss1.bdstatic.com/5eN1bjq8AAUYm2zgoY3K/r/www/cache/static/protocol/https/home/img/icons_0c37e9b.png) no-repeat 4px 3px;background-size:300px 18px;background-image:url(https://ss1.bdstatic.com/5eN1bjq8AAUYm2zgoY3K/r/www/cache/static/protocol/https/home/img/icons_809ae65.gif)\9;overflow:hidden}
#u .bri:hover,#u .bri.brihover{background-position:-18px 3px}
#mCon #imeSIcon{background-position:-408px -144px;margin-left:0}
#mCon span{color:#333}
.bdpfmenu a:link,.bdpfmenu a:visited,#u .usermenu a:link,#u .usermenu a:visited{background:#fff;color:#333}
.bdpfmenu a:hover,.bdpfmenu a:active,#u .usermenu a:hover,#u .usermenu a:active{background:#38f;text-decoration:none;color:#fff}
.bdpfmenu{width:70px}
.usermenu{width:68px;right:8px}
#wrapper .bdnuarrow{width:0;height:0;font-size:0;line-height:0;display:block;position:absolute;top:-10px;left:50%;margin-left:-5px}
#wrapper .bdnuarrow em,#wrapper .bdnuarrow i{width:0;height:0;font-size:0;line-height:0;display:block;position:absolute;border:5px solid transparent;border-style:dashed dashed solid}
#wrapper .bdnuarrow em{border-bottom-color:#d8d8d8;top:-1px}
#wrapper .bdnuarrow i{border-bottom-color:#fff;top:0}
#prefpanel{background:#fafafa;display:none;opacity:0;position:fixed;_position:absolute;top:-359px;z-index:500;width:100%;min-width:960px;border-bottom:1px solid #ebebeb}
#prefpanel form{_width:850px}
#kw_tip{cursor:default;display:none;margin-top:1px}
#bds-message-wrapper{top:43px}
.quickdelete-wrap{position:relative}
.quickdelete-wrap input{width:500px}
.wrapper_l .quickdelete-wrap input{width:500px}
.wrapper_s .quickdelete-wrap input{width:402px}
input::-ms-clear{display:none}
.quickdelete{width:32px;height:32px;background:url(https://ss1.bdstatic.com/5eN1bjq8AAUYm2zgoY3K/r/www/cache/static/protocol/https/global/img/quickdelete_33e3eb8.png) no-repeat;background-position:10px 10px;position:absolute;display:block}
.quickdelete:hover{background-position:10px -24px}
#lh a{margin-left:25px}
.bdbriwrapper-tuiguang{display:none!important}</style>
<!--[if IE 8]>
<style index="index" data-compress="strip">
.s_ipt{background-color:#FFF;}
</style>
<![endif]-->

    
<script data-compress="strip">
function h(obj){
    obj.style.behavior='url(#default#homepage)';
	var a = obj.setHomePage('//www.baidu.com/');
}
</script>

<noscript>
    &lt;meta http-equiv="refresh" content="0; url=/baidu.html?from=noscript"/&gt;
</noscript>

    <script>window._ASYNC_START=new Date().getTime();</script>
<script data-require-id="plugins/swfobject" src="https://ss1.bdstatic.com/5eN1bjq8AAUYm2zgoY3K/r/www/cache/static/protocol/https/plugins/swfobject_0178953.js" async=""></script><script data-require-id="soutu/js/tu" src="https://ss1.bdstatic.com/5eN1bjq8AAUYm2zgoY3K/r/www/cache/static/protocol/https/soutu/js/tu_329aca4.js" async=""></script><link rel="stylesheet" href="https://ss1.bdstatic.com/5eN1bjq8AAUYm2zgoY3K/r/www/cache/static/protocol/https/soutu/css/soutu.css" type="text/css" data-for="result"></head>

<body link="#0000cc"><div id="ks_search_css"><p style="display:none;">ks</p><style type="text/css">.ks_search_container{position:relative;width:100%;}.ks_search_container .ks_search_title{height:30px;background:url(http://dl.liebao.cn/pandora/res/ks_search_bg.png) no-repeat -11px -47px;color:#FFF;font-size:14px;font-family:"微软雅黑","宋体","黑体" ;font-weight:bold;line-height:30px;padding-left:38px;}.ks_search_container .ks_search_original{width:100%;border:1px solid #D01400;border-radius:0px 5px 5px 5px;;padding:5px;background-color:#FFEFEB;}.ks_search_danger_tip{position:absolute; z-index:10000;width:260px; display:none;} .ks_search_danger_tip span{float:left;display:block;width:210px;font:13px "微软雅黑","宋体","黑体";font-weight:normal;color:#B22100;margin-left:2px;} .ks_search_danger_tip span.black{color:#000;} .ks_search_danger_tip .ks_search_danger_tip_logo{width:22px;height:22px;margin-left:13px;float:left;} .ks_search_danger_tip .ks_search_danger_tip_logo_1{background:url(http://dl.liebao.cn/pandora/res/ks_search_bg.png) no-repeat -11px -90px;} .ks_search_danger_tip .ks_search_danger_tip_logo_2{background:url(http://dl.liebao.cn/pandora/res/ks_search_bg.png) no-repeat -11px -13px;} .ks_search_danger_tip .ks_search_leftbar1,.ks_search_danger_tip .ks_search_leftbar2{width:0;height:0;position:absolute;} .ks_search_danger_tip .ks_search_leftbar1{border:transparent 7px solid;top:10px;left:6px;} .ks_search_danger_tip .ks_search_leftbar2{border:transparent 6px solid;top:-6px;left:-5px;} .ks_search_danger_tip .ks_search_leftbar1_1{border-right-color:#D01400;} .ks_search_danger_tip .ks_search_leftbar2_1{border-right-color:#FFEFEB;} .ks_search_danger_tip .ks_search_leftbar1_2{border-right-color:#69c071;} .ks_search_danger_tip .ks_search_leftbar2_2{border-right-color:#EBF8E8;} .ks_search_danger_tip .ks_search_tip_content{border-radius:5px;width:250px;position:absolute;left:19px;padding:5px 5px 8px 0px;} .ks_search_danger_tip .ks_search_tip_content_1{border:1px solid #D01400;background-color:#FFEFEB;} .ks_search_danger_tip .ks_search_tip_content_2{border:1px solid #69c071;background-color:#EBF8E8;} .ks_search_danger_tip .ks_search_tip_content .ks_search_tip_warning{padding-top:5px;} .ks_search_danger_tip .ks_search_tip_content .ks_search_tip_guide{clear:both;text-align:left;padding-left:38px;color:#027A0E;font:12px "黑体" normal;margin-bottom:10px;padding-top:10px;} .ks_search_danger_tip .ks_search_tip_content .ks_search_tip_guide a{color:#027A0E;text-decoration:underline;} .ks_search_danger_tip .ks_search_additional_btn{clear:both;display:inline-block;background-color:#4cc438 ;background:-webkit-gradient(linear, 0 0, 0 100%, from(#4cc438), to(#41A830));border:1px solid #2c961a;color:#fff;text-decoration:none;border-radius:3px;width:86px;height:26px;line-height:26px;letting-spacing:2px;font-size:12px;} .ks_search_safe_logo{background:url(http://dl.liebao.cn/pandora/res/ks_search_bg.png) no-repeat -11px -13px;width:21px;height:21px;line-height:21px;overflow:hidden;display:inline-block;margin-left: 6px;}.ks_search_safe_tip{z-index:1000;position:absolute;left:30px;float:left;display:none;white-space:nowrap;}.ks_search_safe_content{background-color:#DFFFD2;border:1px solid #227107;height:26px;line-height:26px;font-size:12px;font-weight:bold;border-radius:3px;display:block;padding-left:3px;color:#2c800f;padding-left:10px;z-index:10000}.ks_search_safe_leftbar1 , .ks_search_safe_leftbar2{width:0;height:0;position:absolute;}.ks_search_safe_leftbar1{border:transparent 7px solid;border-right-color:#227107;top:8px;left:-13px;}.ks_search_safe_leftbar2{border:transparent 6px solid;border-right-color:#DFFFD2;top:-6px;left:-5px;}</style></div>
	<script>
	if (/Chrome\/37.0.2062.94/i.test(navigator.userAgent) && (/(windows 7)|(windows nt 6.1)/i.test(navigator.userAgent))) {
		var _chrome_37_fix = document.createElement("style");
		_chrome_37_fix.type="text/css";
		_chrome_37_fix.setAttribute("data-for","result");
		_chrome_37_fix.innerHTML = ".t,.f16,#kw,.s_ipt,.c-title,.c-title-size,.to_zhidao,.to_tieba,.to_zhidao_bottom{font-size:15px;} .ec-hospital-info-main h2,.ad-widget-gx_sck-ylzx-doctor-info h2,.ec-card-main h2,.ad-widget-h1 h2,.ad-widget-title h2,.ad-widget-small-head h2,.ad-widget-small-head h2 a,.ad-widget-header .ec-figcaption h2{font-size: 15px !important;}";
		document.getElementsByTagName("head")[0].appendChild(_chrome_37_fix);
	}
	</script>
    <div id="wrapper" style="display: block;">
        


        


<script>if(window.bds&&bds.util&&bds.util.setContainerWidth){bds.util.setContainerWidth();}</script><div id="head"><div class="head_wrapper"><div class="s_form"><div class="s_form_wrapper soutu-env-nomac soutu-env-index"><div id="lg"><img hidefocus="true" src="https://www.baidu.com/img/bd_logo1.png" width="270" height="129" usemap="#mp"><map name="mp"><area style="outline:none;" hidefocus="true" shape="rect" coords="0,0,270,129" href="https://www.baidu.com/s?wd=%E4%BB%8A%E6%97%A5%E6%96%B0%E9%B2%9C%E4%BA%8B&amp;tn=SE_PclogoS_8whnvm25&amp;sa=ire_dl_gh_logo&amp;rsv_dl=igh_logo_pcs" onmousedown="return ns_c({fm: &#39;tab&#39;, tab: &#39;felogo&#39;, rsv_platform: &#39;wwwhome&#39; })" target="_blank" title="点击一下，了解更多"></map></div><a href="https://www.baidu.com/" id="result_logo" onmousedown="return c({&#39;fm&#39;:&#39;tab&#39;,&#39;tab&#39;:&#39;logo&#39;})"><img src="https://www.baidu.com/img/baidu_jgylogo3.gif" alt="到百度首页" title="到百度首页"></a><form id="form" name="f" action="https://www.baidu.com/s" class="fm"><input type="hidden" name="ie" value="utf-8"><input type="hidden" name="f" value="8"><input type="hidden" name="rsv_bp" value="0"><input type="hidden" name="rsv_idx" value="1"><input type="hidden" name="ch" value=""><input type="hidden" name="tn" value="baidu"><input type="hidden" name="bar" value=""><span class="bg s_ipt_wr quickdelete-wrap iptfocus"><span class="soutu-btn"></span><input id="kw" name="wd" class="s_ipt" value="" maxlength="255" autocomplete="off"><a href="javascript:;" id="quickdelete" title="清空" class="quickdelete" style="top: 0px; right: 0px; display: none;"></a></span><span class="bg s_btn_wr"><input type="submit" id="su" value="百度一下" class="bg s_btn"></span><span class="tools"><span id="mHolder"><div id="mCon"><span>输入法</span></div><ul id="mMenu"><li><a href="javascript:;" name="ime_hw">手写</a></li><li><a href="javascript:;" name="ime_py">拼音</a></li><li class="ln"></li><li><a href="javascript:;" name="ime_cl">关闭</a></li></ul></span></span><input type="hidden" name="rn" value=""><input type="hidden" name="oq" value=""><input type="hidden" name="rsv_pq" value="a9a770450000d7b1"><input type="hidden" name="rsv_t" value="9550Yj5gRjB6nfuvyt31PzmH/Vz4F/YyBtk1JZk+J3nqigWuUvrWwvcGMYs"><input type="hidden" name="rqlang" value="cn"><input type="hidden" name="rsv_enter" value="1"><input type="hidden" name="rsv_sug3" value="1"></form><div id="m"></div></div></div><div id="u"><a class="toindex" href="https://www.baidu.com/">百度首页</a><a href="javascript:;" name="tj_settingicon" class="pf">设置<i class="c-icon c-icon-triangle-down"></i></a><a href="https://passport.baidu.com/v2/?login&amp;tpl=mn&amp;u=http%3A%2F%2Fwww.baidu.com%2F&amp;sms=5" name="tj_login" class="lb" onclick="return false;">登录</a></div><div id="u1"><a href="http://news.baidu.com/" name="tj_trnews" class="mnav">新闻</a><a href="http://www.hao123.com/" name="tj_trhao123" class="mnav">hao123</a><a href="http://map.baidu.com/" name="tj_trmap" class="mnav">地图</a><a href="http://v.baidu.com/" name="tj_trvideo" class="mnav">视频</a><a href="http://tieba.baidu.com/" name="tj_trtieba" class="mnav">贴吧</a><a href="http://xueshu.baidu.com/" name="tj_trxueshu" class="mnav">学术</a><a href="https://passport.baidu.com/v2/?login&amp;tpl=mn&amp;u=http%3A%2F%2Fwww.baidu.com%2F&amp;sms=5" name="tj_login" class="lb" onclick="return false;">登录</a><a href="http://www.baidu.com/gaoji/preferences.html" name="tj_settingicon" class="pf">设置</a><a href="http://www.baidu.com/more/" name="tj_briicon" class="bri" style="display: block;">更多产品</a></div></div></div>



<div class="s_tab" id="s_tab">
    <b>网页</b><a href="http://news.baidu.com/ns?cl=2&amp;rn=20&amp;tn=news&amp;word=" wdfield="word" onmousedown="return c({&#39;fm&#39;:&#39;tab&#39;,&#39;tab&#39;:&#39;news&#39;})">新闻</a><a href="http://tieba.baidu.com/f?kw=&amp;fr=wwwt" wdfield="kw" onmousedown="return c({&#39;fm&#39;:&#39;tab&#39;,&#39;tab&#39;:&#39;tieba&#39;})">贴吧</a><a href="http://zhidao.baidu.com/q?ct=17&amp;pn=0&amp;tn=ikaslist&amp;rn=10&amp;word=&amp;fr=wwwt" wdfield="word" onmousedown="return c({&#39;fm&#39;:&#39;tab&#39;,&#39;tab&#39;:&#39;zhidao&#39;})">知道</a><a href="http://music.baidu.com/search?fr=ps&amp;ie=utf-8&amp;key=" wdfield="key" onmousedown="return c({&#39;fm&#39;:&#39;tab&#39;,&#39;tab&#39;:&#39;music&#39;})">音乐</a><a href="http://image.baidu.com/search/index?tn=baiduimage&amp;ps=1&amp;ct=201326592&amp;lm=-1&amp;cl=2&amp;nc=1&amp;ie=utf-8&amp;word=" wdfield="word" onmousedown="return c({&#39;fm&#39;:&#39;tab&#39;,&#39;tab&#39;:&#39;pic&#39;})">图片</a><a href="http://v.baidu.com/v?ct=301989888&amp;rn=20&amp;pn=0&amp;db=0&amp;s=25&amp;ie=utf-8&amp;word=" wdfield="word" onmousedown="return c({&#39;fm&#39;:&#39;tab&#39;,&#39;tab&#39;:&#39;video&#39;})">视频</a><a href="http://map.baidu.com/m?word=&amp;fr=ps01000" wdfield="word" onmousedown="return c({&#39;fm&#39;:&#39;tab&#39;,&#39;tab&#39;:&#39;map&#39;})">地图</a><a href="http://wenku.baidu.com/search?word=&amp;lm=0&amp;od=0&amp;ie=utf-8" wdfield="word" onmousedown="return c({&#39;fm&#39;:&#39;tab&#39;,&#39;tab&#39;:&#39;wenku&#39;})">文库</a><a href="https://www.baidu.com/more/" onmousedown="return c({&#39;fm&#39;:&#39;tab&#39;,&#39;tab&#39;:&#39;more&#39;})">更多»</a>
</div>

        

<div class="qrcodeCon">
	<div id="qrcode">
		<div class="qrcode-item qrcode-item-1">
			<div class="qrcode-img"></div>
			<div class="qrcode-text">
					<p><b>百度</b></p>
			</div>
		</div>
	</div>
</div>
<div id="ftCon">

<div class="ftCon-Wrapper"><div id="ftConw"><p id="lh"><a id="setf" href="https://www.baidu.com/cache/sethelp/help.html" onmousedown="return ns_c({&#39;fm&#39;:&#39;behs&#39;,&#39;tab&#39;:&#39;favorites&#39;,&#39;pos&#39;:0})" target="_blank">把百度设为主页</a><a onmousedown="return ns_c({&#39;fm&#39;:&#39;behs&#39;,&#39;tab&#39;:&#39;tj_about&#39;})" href="http://home.baidu.com/">关于百度</a><a onmousedown="return ns_c({&#39;fm&#39;:&#39;behs&#39;,&#39;tab&#39;:&#39;tj_about_en&#39;})" href="http://ir.baidu.com/">About&nbsp;&nbsp;Baidu</a><a onmousedown="return ns_c({&#39;fm&#39;:&#39;behs&#39;,&#39;tab&#39;:&#39;tj_tuiguang&#39;})" href="http://e.baidu.com/?refer=888">百度推广</a></p><p id="cp">©2018&nbsp;Baidu&nbsp;<a href="http://www.baidu.com/duty/" onmousedown="return ns_c({&#39;fm&#39;:&#39;behs&#39;,&#39;tab&#39;:&#39;tj_duty&#39;})">使用百度前必读</a>&nbsp;<a href="http://jianyi.baidu.com/" class="cp-feedback" onmousedown="return ns_c({&#39;fm&#39;:&#39;behs&#39;,&#39;tab&#39;:&#39;tj_homefb&#39;})">意见反馈</a>&nbsp;京ICP证030173号&nbsp;<i class="c-icon-icrlogo"></i>&nbsp;<a id="jgwab" target="_blank" href="http://www.beian.gov.cn/portal/registerSystemInfo?recordcode=11000002000001">京公网安备11000002000001号</a>&nbsp;<i class="c-icon-jgwablogo"></i></p></div></div></div>
        <div id="wrapper_wrapper">
        </div>
    <div class="bdpfmenu" style="left: 814px; top: 48px; display: none;"><div class="bdnuarrow"><em></em><i></i></div><a class="setpref" href="javascript:;">搜索设置</a><a href="https://www.baidu.com/gaoji/advanced.html" target="_blank">高级搜索</a><a href="javascript:;">关闭预测</a><a href="javascript:;">搜索历史</a></div></div>
    <div class="c-tips-container" id="c-tips-container"></div>
    
    <script>
        window.__async_strategy=2;
        //window.__switch_add_mask=false;
    </script>
    
    
<script>
var bds={
    se:{},
    su:{
        urdata:[],
                urSendClick:function(){}
    },
    util:{},
    use:{},
    comm : {
        domain:"http://www.baidu.com",
        ubsurl : "https://sp0.baidu.com/5bU_dTmfKgQFm2e88IuM_a/w.gif",
        tn:"baidu",
        queryEnc:"",
        queryId:"",
        inter:"",
        templateName:"",
        sugHost : "https://sp0.baidu.com/5a1Fazu8AA54nxGko9WTAnF6hhy/su",
        query : "",
        dpquery: "",
        qid : "a9a770450000d7b1",
        cid : "0",
        sid : "1434_25810_21108_17001_20930",
        indexSid : "1434_25810_21108_17001_20930",
        stoken : "",
        serverTime : "1519569543",
        user : "",
        username : "",
        userid : "0",
        loginAction : [],
        useFavo : "",
        pinyin : "",
        favoOn : "",
        cookie : {"BAIDUID":"46323B1F94874789336F4DCE8BBE82D9:FG=1","BIDUPSID":"46323B1F94874789336F4DCE8BBE82D9","PSTM":"1519565960","pgv_pvi":"7544076288","pgv_si":"s1943414784","H_PS_645EC":"3606G0yvkUwII1jinzg8qyraWTyQ6grh3rJ9WoSCb0eh1SmKI1mCOL7ni9k","BDORZ":"B490B5EBF6F3CD402E515D22BCDA1598","BD_CK_SAM":"1","PSINO":"5","BD_HOME":"0","H_PS_PSSID":"1434_25810_21108_17001_20930","BD_UPN":"16314753"},
        userAgent : "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.98 Safari/537.36 LBBROWSER",
                curResultNum:"0",
        rightResultExist:false,
        protectNum:0,
        zxlNum:0,
        pageNum:1,
        pageSize:10,
        newindex:0,
        async:2,
        maxPreloadThread:5,
        maxPreloadTimes:10,
        preloadMouseMoveDistance:5,
        switchAddMask:false,
        isDebug:false,
        ishome : 1,
        flagTranslateResult:0,
        globalLogFlag:0
	,encTn:'9550Yj5gRjB6nfuvyt31PzmH/Vz4F/YyBtk1JZk+J3nqigWuUvrWwvcGMYs'    }
};



    


//防止从结果页打开的页面中通过opener.xxx来影响百度页面


var name,navigate,al_arr=[];
var selfOpen = window.open;eval("var open = selfOpen;");
var isIE=navigator.userAgent.indexOf("MSIE")!=-1&&!window.opera;
var E = bds.ecom= {};

bds.se.mon = {'loadedItems':[],'load':function(){},'srvt':-1};

try {
    bds.se.mon.srvt = parseInt(document.cookie.match(new RegExp("(^| )BDSVRTM=([^;]*)(;|$)"))[2]);
    document.cookie="BDSVRTM=;expires=Sat, 01 Jan 2000 00:00:00 GMT";
}catch(e){}

//兼容之前一些变量
var
bdUser        = bds.comm.user?bds.comm.user:null,
bdQuery       = bds.comm.query,
bdUseFavo     = bds.comm.useFavo,
bdFavoOn      = bds.comm.favoOn,
bdCid         = bds.comm.cid,
bdSid         = bds.comm.sid,
bdServerTime  = bds.comm.serverTime,
bdQid         = bds.comm.queryId,
bdstoken      = bds.comm.stoken,
login_success = [];



</script>
<script>
/* https域名转换工具 */
bds.util.domain = (function(){
	    																					            																							var list = {
        "graph.baidu.com": "https://sp0.baidu.com/-aYHfD0a2gU2pMbgoY3K",
		"p.qiao.baidu.com":"https://sp0.baidu.com/5PoXdTebKgQFm2e88IuM_a",
		"vse.baidu.com":"https://sp3.baidu.com/6qUDsjip0QIZ8tyhnq",
		"hdpreload.baidu.com":"https://sp3.baidu.com/7LAWfjuc_wUI8t7jm9iCKT-xh_",
		"lcr.open.baidu.com":"https://sp2.baidu.com/8LUYsjW91Qh3otqbppnN2DJv",
		"kankan.baidu.com":"https://sp3.baidu.com/7bM1dzeaKgQFm2e88IuM_a",
		"xapp.baidu.com":"https://sp2.baidu.com/yLMWfHSm2Q5IlBGlnYG",
		"dr.dh.baidu.com":"https://sp0.baidu.com/-KZ1aD0a2gU2pMbgoY3K",
		"xiaodu.baidu.com":"https://sp0.baidu.com/yLsHczq6KgQFm2e88IuM_a",
		"sensearch.baidu.com":"https://sp1.baidu.com/5b11fzupBgM18t7jm9iCKT-xh_",
		"s1.bdstatic.com":"https://ss1.bdstatic.com/5eN1bjq8AAUYm2zgoY3K",
		"olime.baidu.com":"https://sp0.baidu.com/8bg4cTva2gU2pMbgoY3K",
		"app.baidu.com":"https://sp2.baidu.com/9_QWsjip0QIZ8tyhnq",
		"i.baidu.com":"https://sp0.baidu.com/74oIbT3kAMgDnd_",
		"c.baidu.com":"https://sp0.baidu.com/9foIbT3kAMgDnd_",
		"sclick.baidu.com":"https://sp0.baidu.com/5bU_dTmfKgQFm2e88IuM_a",
		"nsclick.baidu.com":"https://sp1.baidu.com/8qUJcD3n0sgCo2Kml5_Y_D3",
		"sestat.baidu.com":"https://sp1.baidu.com/5b1ZeDe5KgQFm2e88IuM_a",
		"eclick.baidu.com":"https://sp3.baidu.com/-0U_dTmfKgQFm2e88IuM_a",
		"api.map.baidu.com":"https://sp2.baidu.com/9_Q4sjOpB1gCo2Kml5_Y_D3",
		"ecma.bdimg.com":"https://ss1.bdstatic.com/-0U0bXSm1A5BphGlnYG",
		"ecmb.bdimg.com":"https://ss0.bdstatic.com/-0U0bnSm1A5BphGlnYG",
        "t1.baidu.com":"https://ss0.baidu.com/6ON1bjeh1BF3odCf",
        "t2.baidu.com":"https://ss1.baidu.com/6OZ1bjeh1BF3odCf",
        "t3.baidu.com":"https://ss2.baidu.com/6OV1bjeh1BF3odCf",
		"t10.baidu.com":"https://ss0.baidu.com/6ONWsjip0QIZ8tyhnq",
		"t11.baidu.com":"https://ss1.baidu.com/6ONXsjip0QIZ8tyhnq",
		"t12.baidu.com":"https://ss2.baidu.com/6ONYsjip0QIZ8tyhnq",
		"i7.baidu.com":"https://ss0.baidu.com/73F1bjeh1BF3odCf",
		"i8.baidu.com":"https://ss0.baidu.com/73x1bjeh1BF3odCf",
		"i9.baidu.com":"https://ss0.baidu.com/73t1bjeh1BF3odCf",
		"b1.bdstatic.com":"https://ss0.bdstatic.com/9uN1bjq8AAUYm2zgoY3K",
		"ss.bdimg.com":"https://ss1.bdstatic.com/5aV1bjqh_Q23odCf",
		"opendata.baidu.com":"https://sp0.baidu.com/8aQDcjqpAAV3otqbppnN2DJv",
		"api.open.baidu.com":"https://sp0.baidu.com/9_Q4sjW91Qh3otqbppnN2DJv",
		"tag.baidu.com":"https://sp1.baidu.com/6LMFsjip0QIZ8tyhnq",
		"f3.baidu.com":"https://sp2.baidu.com/-uV1bjeh1BF3odCf",
		"s.share.baidu.com":"https://sp0.baidu.com/5foZdDe71MgCo2Kml5_Y_D3",	
		"bdimg.share.baidu.com":"https://ss1.baidu.com/9rA4cT8aBw9FktbgoI7O1ygwehsv",
        "1.su.bdimg.com":"https://ss0.bdstatic.com/k4oZeXSm1A5BphGlnYG",
        "2.su.bdimg.com":"https://ss1.bdstatic.com/kvoZeXSm1A5BphGlnYG",
        "3.su.bdimg.com":"https://ss2.bdstatic.com/kfoZeXSm1A5BphGlnYG",
        "4.su.bdimg.com":"https://ss3.bdstatic.com/lPoZeXSm1A5BphGlnYG",
        "5.su.bdimg.com":"https://ss0.bdstatic.com/l4oZeXSm1A5BphGlnYG",
        "6.su.bdimg.com":"https://ss1.bdstatic.com/lvoZeXSm1A5BphGlnYG",
        "7.su.bdimg.com":"https://ss2.bdstatic.com/lfoZeXSm1A5BphGlnYG",
        "8.su.bdimg.com":"https://ss3.bdstatic.com/iPoZeXSm1A5BphGlnYG"
	};


	var get = function(url) {
		if(location.protocol === "http") {
			return url;
		}
		var reg = /^(http[s]?:\/\/)?([^\/]+)(.*)/,
		matches = url.match(reg);
		/* 判断传入参数是域名还是地址，分别做处理 */
		url = list.hasOwnProperty(matches[2])&&(list[matches[2]] + matches[3]) || url;
		return url;
	},
	set = function(kdomain,vdomain) {
		list[kdomain] = vdomain;
	};
	return {
		get : get,
		set : set
	}
})();
</script>
<script>
//让用户更快看到首页
if(!location.hash.match(/[^a-zA-Z0-9]wd=/)){
    document.getElementById("wrapper").style.display='block';
    setTimeout(function(){
        try{
            var kw=document.getElementById("kw");
            kw.focus();
			kw.parentNode.className="bg s_ipt_wr iptfocus quickdelete-wrap";
        }catch(e){}
    },0);
}

</script>
<script type="text/javascript" src="https://ss1.bdstatic.com/5eN1bjq8AAUYm2zgoY3K/r/www/cache/static/protocol/https/jquery/jquery-1.10.2.min_65682a2.js"></script>




<script>
(function(){

    var result_common_css="<style data-for=\"result\" id=\"css_result\" type=\"text\/css\">body{color:#333;background:#fff;padding:6px 0 0;margin:0;position:relative;min-width:900px}body,th,td,.p1,.p2{font-family:arial}p,form,ol,ul,li,dl,dt,dd,h3{margin:0;padding:0;list-style:none}input{padding-top:0;padding-bottom:0;-moz-box-sizing:border-box;-webkit-box-sizing:border-box;box-sizing:border-box}table,img{border:0}td{font-size:9pt;line-height:18px}em{font-style:normal;color:#c00}a em{text-decoration:underline}cite{font-style:normal;color:green}.m,a.m{color:#666}a.m:visited{color:#606}.g,a.g{color:green}.c{color:#77c}.f14{font-size:14px}.f10{font-size:10.5pt}.f16{font-size:16px}.f13{font-size:13px}.bg{background-image:url(https:\/\/ss1.bdstatic.com\/5eN1bjq8AAUYm2zgoY3K\/r\/www\/cache\/static\/protocol\/https\/global\/img\/icons_5859e57.png);_background-image:url(https:\/\/ss1.bdstatic.com\/5eN1bjq8AAUYm2zgoY3K\/r\/www\/cache\/static\/protocol\/https\/global\/img\/icons_d5b04cc.gif);background-repeat:no-repeat}#u,#head,#tool,#search,#foot{font-size:12px}.logo{width:117px;height:38px;cursor:pointer}.p1{line-height:120%;margin-left:-12pt}.p2{width:100%;line-height:120%;margin-left:-12pt}#wrapper{_zoom:1}#container{word-break:break-all;word-wrap:break-word}.container_s{width:1002px}.container_l{width:1222px}#content_left{width:636px;float:left;padding-left:35px}#content_right{border-left:1px solid #e1e1e1;float:right}.container_s #content_right{width:271px}.container_l #content_right{width:434px}.content_none{padding-left:35px}#u{color:#999;white-space:nowrap;position:absolute;right:10px;top:4px;z-index:299}#u a{color:#00c;margin:0 5px}#u .reg{margin:0}#u .last{margin-right:0}#u .un{font-weight:700;margin-right:5px}#u ul{width:100%;background:#fff;border:1px solid #9b9b9b}#u li{height:25px}#u li a{width:100%;height:25px;line-height:25px;display:block;text-align:left;text-decoration:none;text-indent:6px;margin:0;filter:none\\9}#u li a:hover{background:#ebebeb}#u li.nl{border-top:1px solid #ebebeb}#user{display:inline-block}#user_center{position:relative;display:inline-block}#user_center .user_center_btn{margin-right:5px}.userMenu{width:64px;position:absolute;right:7px;_right:2px;top:15px;top:14px\\9;*top:15px;padding-top:4px;display:none;*background:#fff}#head{padding-left:35px;margin-bottom:20px;width:900px}.fm{clear:both;position:relative;z-index:297}.nv a,.nv b,.btn,#page,#more{font-size:14px}.s_nav{height:45px}.s_nav .s_logo{margin-right:20px;float:left}.s_nav .s_logo img{border:0;display:block}.s_tab{line-height:18px;padding:20px 0 0;float:left}.s_nav a{color:#00c;font-size:14px}.s_nav b{font-size:14px}.s_ipt_wr{width:536px;height:30px;display:inline-block;margin-right:5px;background-position:0 -96px;border:1px solid #b6b6b6;border-color:#7b7b7b #b6b6b6 #b6b6b6 #7b7b7b;vertical-align:top}.s_ipt{width:523px;height:22px;font:16px\/18px arial;line-height:22px;margin:5px 0 0 7px;padding:0;background:#fff;border:0;outline:0;-webkit-appearance:none}.s_btn{width:95px;height:32px;padding-top:2px\\9;font-size:14px;padding:0;background-color:#ddd;background-position:0 -48px;border:0;cursor:pointer}.s_btn_h{background-position:-240px -48px}.s_btn_wr{width:97px;height:34px;display:inline-block;background-position:-120px -48px;*position:relative;z-index:0;vertical-align:top}.sethf{padding:0;margin:0;font-size:14px}.set_h{display:none;behavior:url(#default#homepage)}.set_f{display:none}.shouji{margin-left:19px}.shouji a{text-decoration:none}#head .bdsug{top:33px}#search form{position:relative}#search form .bdsug{bottom:33px}.bdsug{display:none;position:absolute;z-index:1;width:538px;background:#fff;border:1px solid #ccc;_overflow:hidden;box-shadow:1px 1px 3px #ededed;-webkit-box-shadow:1px 1px 3px #ededed;-moz-box-shadow:1px 1px 3px #ededed;-o-box-shadow:1px 1px 3px #ededed}.bdsug.bdsugbg ul{background:url(https:\/\/ss1.bdstatic.com\/5eN1bjq8AAUYm2zgoY3K\/r\/www\/cache\/static\/protocol\/https\/home\/img\/sugbg_1762fe7.png) 100% 100% no-repeat;background-size:100px 110px;background-image:url(https:\/\/ss1.bdstatic.com\/5eN1bjq8AAUYm2zgoY3K\/r\/www\/cache\/static\/protocol\/https\/home\/img\/sugbg_90fc9cf.gif)\\9}.bdsug li{width:522px;color:#000;font:14px arial;line-height:22px;padding:0 8px;position:relative;cursor:default}.bdsug li.bdsug-s{background:#f0f0f0}.bdsug-store span,.bdsug-store b{color:#7A77C8}.bdsug-store-del{font-size:12px;color:#666;text-decoration:underline;position:absolute;right:8px;top:0;cursor:pointer;display:none}.bdsug-s .bdsug-store-del{display:inline-block}.bdsug-ala{display:inline-block;border-bottom:1px solid #e6e6e6}.bdsug-ala h3{line-height:14px;background:url(\/\/www.baidu.com\/img\/sug_bd.png) no-repeat left center;margin:8px 0 5px;font-size:12px;font-weight:400;color:#7B7B7B;padding-left:20px}.bdsug-ala p{font-size:14px;font-weight:700;padding-left:20px}.bdsug .bdsug-direct{width:auto;padding:0;border-bottom:1px solid #f1f1f1}.bdsug .bdsug-direct p{color:#00c;font-weight:700;line-height:34px;padding:0 8px;cursor:pointer;white-space:nowrap;overflow:hidden}.bdsug .bdsug-direct p img{width:16px;height:16px;margin:7px 6px 9px 0;vertical-align:middle}.bdsug .bdsug-direct p span{margin-left:8px}.bdsug .bdsug-direct p i{font-size:12px;line-height:100%;font-style:normal;font-weight:400;color:#fff;background-color:#2b99ff;display:inline;text-align:center;padding:1px 5px;*padding:2px 5px 0;margin-left:8px;overflow:hidden}.bdsug .bdsug-pcDirect{color:#000;font-size:14px;line-height:30px;height:30px;background-color:#f8f8f8}.bdsug .bdsug-pc-direct-tip{position:absolute;right:15px;top:8px;width:55px;height:15px;display:block;background:url(https:\/\/ss1.bdstatic.com\/5eN1bjq8AAUYm2zgoY3K\/r\/www\/cache\/static\/protocol\/https\/global\/img\/pc_direct_42d6311.png) no-repeat 0 0}.bdsug li.bdsug-pcDirect-s{background-color:#f0f0f0}.bdsug .bdsug-pcDirect-is{color:#000;font-size:14px;line-height:22px;background-color:#f8f8f8}.bdsug .bdsug-pc-direct-tip-is{position:absolute;right:15px;top:3px;width:55px;height:15px;display:block;background:url(https:\/\/ss1.bdstatic.com\/5eN1bjq8AAUYm2zgoY3K\/r\/www\/cache\/static\/protocol\/https\/global\/img\/pc_direct_42d6311.png) no-repeat 0 0}.bdsug li.bdsug-pcDirect-is-s{background-color:#f0f0f0}.bdsug .bdsug-pcDirect-s .bdsug-pc-direct-tip,.bdsug .bdsug-pcDirect-is-s .bdsug-pc-direct-tip-is{background-position:0 -15px}.bdsug .bdsug-newicon{color:#929292;opacity:.7;font-size:12px;display:inline-block;line-height:22px;letter-spacing:2px}.bdsug .bdsug-s .bdsug-newicon{opacity:1}.bdsug .bdsug-newicon i{letter-spacing:0;font-style:normal}.toggle-underline{text-decoration:none}.toggle-underline:hover{text-decoration:underline}#tb_mr{color:#00c;cursor:pointer;position:relative;z-index:298}#tb_mr b{font-weight:400;text-decoration:underline}#tb_mr small{font-size:11px}#page{font:14px arial;white-space:nowrap;padding-left:35px}#page a,#page strong{display:inline-block;vertical-align:text-bottom;height:66px;text-align:center;line-height:34px;text-decoration:none;overflow:hidden;margin-right:9px;background:#fff}#page a{cursor:pointer}#page a:hover{background:0 0}#page .n:hover,#page a:hover .pc{background:#f2f8ff;border:1px solid #38f}#page .n{height:34px;padding:0 18px;border:1px solid #e1e2e3}#page span{display:block}#page .pc{width:34px;height:34px;border:1px solid #e1e2e3;cursor:pointer}#page .fk{width:24px;height:24px;margin-bottom:6px;margin-left:6px;cursor:pointer}#page strong .fk,#page strong .pc{cursor:auto}#page .fk .c-icon-bear-pn{top:-3px;position:relative}#page .fkd .c-icon-bear-pn{top:3px;position:relative}#page .fk_cur .c-icon-bear-p{top:-2px;position:relative}#page strong .pc{border:0;width:36px;height:36px;line-height:36px}#page .nums{display:inline-block;vertical-align:text-bottom;height:36px;line-height:36px;margin-left:10px}#rs{width:900px;background:#fff;padding:8px 0;margin:20px 0 0 15px}#rs td{width:5%}#rs th{font-size:14px;font-weight:400;line-height:19px;white-space:nowrap;text-align:left;vertical-align:top}#rs .tt{font-weight:700;padding:0 10px 0 20px}#rs_top{font-size:14px;margin-bottom:22px}#rs_top a{margin-right:18px}#container .rs{margin:30px 0 20px;padding:5px 0 15px;font-size:14px;width:540px;padding-left:121px;position:relative;background-color:#fafafa}#container .noback{background-color:#fff}#content_left .rs{margin-left:-121px}#container .rs table{width:540px}#container .rs td{width:5px}#container .rs th{font-size:14px;font-weight:400;white-space:nowrap;text-align:left;vertical-align:top;width:175px;line-height:22px}#container .rs .tt{font-weight:700;padding:0 10px 0 20px;padding:0;line-height:30px;font-size:16px}#container .rs a{margin:0;height:24px;width:173px;display:inline-block;line-height:25px;border:1px solid #ebebeb;text-align:center;vertical-align:middle;overflow:hidden;outline:0;color:#333;background-color:#fff;text-decoration:none}#container .rs a:hover{border-color:#388bff}.c-tip-con .c-tip-menu-b ul{width:100px}.c-tip-con .c-tip-menu-b ul{text-align:center}.c-tip-con .c-tip-menu-b li a{display:block;text-decoration:none;cursor:pointer;background-color:#fff;padding:3px 0;color:#666}.c-tip-con .c-tip-menu-b li a:hover{display:block;background-color:#ebebeb}#search{width:900px;padding:35px 0 16px 35px}#search .s_help{position:relative;top:10px}#foot{height:20px;line-height:20px;color:#77c;background:#e6e6e6;text-align:center}#foot span{color:#666}.site_tip{font-size:12px;margin-bottom:20px}.site_tip_icon{width:56px;height:56px;background:url(\/\/www.baidu.com\/aladdin\/img\/tools\/tools-3.png) -288px 0 no-repeat}.to_zhidao,.to_tieba,.to_zhidao_bottom{font-size:16px;line-height:24px;margin:20px 0 0 35px}.to_tieba .c-icon-tieba{float:left}.f{line-height:115%;*line-height:120%;font-size:100%;width:33.7em;word-break:break-all;word-wrap:break-word}.h{margin-left:8px;width:100%}.r{word-break:break-all;cursor:hand;width:238px}.t{font-weight:400;font-size:medium;margin-bottom:1px}.pl{padding-left:3px;height:8px;padding-right:2px;font-size:14px}.mo,a.mo:link,a.mo:visited{color:#666;font-size:100%;line-height:10px}.htb{margin-bottom:5px}.jc a{color:#c00}a font[size=\"3\"] font,font[size=\"3\"] a font{text-decoration:underline}div.blog,div.bbs{color:#707070;padding-top:2px;font-size:13px}.result{width:33.7em;table-layout:fixed}.result-op .f{word-wrap:normal}.nums{font-size:12px;color:#999}.tools{position:absolute;top:10px;white-space:nowrap}#mHolder{width:62px;position:relative;z-index:296;top:-18px;margin-left:9px;margin-right:-12px;display:none}#mCon{height:18px;position:absolute;top:3px;top:6px\\9;cursor:pointer;line-height:18px}.wrapper_l #mCon{right:7px}#mCon span{color:#00c;display:block}#mCon .hw{text-decoration:underline;cursor:pointer;display:inline-block}#mCon .pinyin{display:inline-block}#mCon .c-icon-chevron-unfold2{margin-left:5px}#mMenu{width:56px;border:1px solid #9b9b9b;position:absolute;right:7px;top:23px;display:none;background:#fff}#mMenu a{width:100%;height:100%;color:#00c;display:block;line-height:22px;text-indent:6px;text-decoration:none;filter:none\\9}#mMenu a:hover{background:#ebebeb}#mMenu .ln{height:1px;background:#ebebeb;overflow:hidden;font-size:1px;line-height:1px;margin-top:-1px}.op_LAMP{background:url(\/\/www.baidu.com\/cache\/global\/img\/aladdinIcon-1.0.gif) no-repeat 0 2px;color:#77C;display:inline-block;font-size:13px;height:12px;*height:14px;width:16px;text-decoration:none;zoom:1}.EC_mr15{margin-left:0}.pd15{padding-left:0}.map_1{width:30em;font-size:80%;line-height:145%}.map_2{width:25em;font-size:80%;line-height:145%}.favurl{background-repeat:no-repeat;background-position:0 1px;padding-left:20px}.dan_tip{font-size:12px;margin-top:4px}.dan_tip a{color:#b95b07}#more,#u ul,#mMenu,.msg_holder{box-shadow:1px 1px 2px #ccc;-moz-box-shadow:1px 1px 2px #ccc;-webkit-box-shadow:1px 1px 2px #ccc;filter:progid:DXImageTransform.Microsoft.Shadow(Strength=2, Direction=135, Color=#cccccc)\\9}.hit_top{line-height:18px;margin:0 15px 10px 0;width:516px}.hit_top .c-icon-bear{height:18px;margin-right:4px}#rs_top_new,.hit_top_new{width:538px;font-size:13px;line-height:1.54;word-wrap:break-word;word-break:break-all;margin:0 0 14px}.zhannei-si{margin:0 0 10px 121px}.zhannei-si-none{margin:10px 0 -10px 121px}.zhannei-search{margin:10px 0 0 121px;color:#999;font-size:14px}.f a font[size=\"3\"] font,.f font[size=\"-1\"] a font{text-decoration:underline}h3 a font{text-decoration:underline}.c-title{font-weight:400;font-size:16px}.c-title-size{font-size:16px}.c-abstract{font-size:13px}.c-abstract-size{font-size:13px}.c-showurl{color:green;font-size:13px}.c-showurl-color{color:green}.c-cache-color{color:#666}.c-lightblue{color:#77c}.c-highlight-color{color:#c00}.c-clearfix:after{content:\".\";display:block;height:0;clear:both;visibility:hidden}.c-clearfix{zoom:1}.c-wrap{word-break:break-all;word-wrap:break-word}.c-icons-outer{overflow:hidden;display:inline-block;vertical-align:bottom;*vertical-align:-1px;_vertical-align:bottom}.c-icons-inner{margin-left:-4px}.c-container table.result,.c-container table.result-op{width:100%}.c-container td.f{font-size:13px;line-height:1.54;width:auto}.c-container .vd_newest_main{width:auto}.c-customicon{display:inline-block;width:16px;height:16px;vertical-align:text-bottom;font-style:normal;overflow:hidden}.c-tip-icon i{display:inline-block;cursor:pointer}.c-tip-con{position:absolute;z-index:1;top:22px;left:-35px;background:#fff;border:1px solid #dcdcdc;border:1px solid rgba(0,0,0,.2);-webkit-transition:opacity .218s;transition:opacity .218s;-webkit-box-shadow:0 2px 4px rgba(0,0,0,.2);box-shadow:0 2px 4px rgba(0,0,0,.2);padding:5px 0;display:none;font-size:12px;line-height:20px}.c-tip-arrow{width:0;height:0;font-size:0;line-height:0;display:block;position:absolute;top:-16px}.c-tip-arrow-down{top:auto;bottom:0}.c-tip-arrow em,.c-tip-arrow ins{width:0;height:0;font-size:0;line-height:0;display:block;position:absolute;border:8px solid transparent;border-style:dashed dashed solid}.c-tip-arrow em{border-bottom-color:#d8d8d8}.c-tip-arrow ins{border-bottom-color:#fff;top:2px}.c-tip-arrow-down em,.c-tip-arrow-down ins{border-style:solid dashed dashed;border-color:transparent}.c-tip-arrow-down em{border-top-color:#d8d8d8}.c-tip-arrow-down ins{border-top-color:#fff;top:-2px}.c-tip-arrow .c-tip-arrow-r{border-bottom-color:#82c9fa;top:2px}.c-tip-arrow-down .c-tip-arrow-r{border-bottom-color:transparent;top:-2px}.c-tip-arrow .c-tip-arrow-c{border-bottom-color:#fecc47;top:2px}.c-tip-arrow-down .c-tip-arrow-c{border-bottom-color:transparent;top:-2px}.c-tip-con h3{font-size:12px}.c-tip-con .c-tip-title{margin:0 10px;display:inline-block;width:239px}.c-tip-con .c-tip-info{color:#666;margin:0 10px 1px;width:239px}.c-tip-con .c-tip-cer{width:370px;color:#666;margin:0 10px 1px}.c-tip-con .c-tip-title{width:auto;_width:354px}.c-tip-con .c-tip-item-i{padding:3px 0 3px 20px;line-height:14px}.c-tip-con .c-tip-item-i .c-tip-item-icon{margin-left:-20px}.c-tip-con .c-tip-menu ul{width:74px}.c-tip-con .c-tip-menu ul{text-align:center}.c-tip-con .c-tip-menu li a{display:block;text-decoration:none;cursor:pointer;background-color:#fff;padding:3px 0;color:#0000d0}.c-tip-con .c-tip-menu li a:hover{display:block;background-color:#ebebeb}.c-tip-con .c-tip-notice{width:239px;padding:0 10px}.c-tip-con .c-tip-notice .c-tip-notice-succ{color:#4cbd37}.c-tip-con .c-tip-notice .c-tip-notice-fail{color:#f13F40}.c-tip-con .c-tip-notice .c-tip-item-succ{color:#444}.c-tip-con .c-tip-notice .c-tip-item-fail{color:#aaa}.c-tip-con .c-tip-notice .c-tip-item-fail a{color:#aaa}.c-tip-close{right:10px;position:absolute;cursor:pointer}.ecard{height:86px;overflow:hidden}.c-tools{display:inline}.c-tools-share{width:239px;padding:0 10px}.c-fanyi{display:none;width:20px;height:20px;border:solid 1px #d1d1d1;cursor:pointer;position:absolute;margin-left:516px;text-align:center;color:#333;line-height:22px;opacity:.9;background-color:#fff}.c-fanyi:hover{background-color:#39f;color:#fff;border-color:#39f;opacity:1}.c-fanyi-title,.c-fanyi-abstract{display:none}.icp_info{color:#666;margin-top:2px;font-size:13px}.icon-gw,.icon-unsafe-icon{background:#2c99ff;vertical-align:text-bottom;*vertical-align:baseline;height:16px;padding-top:0;padding-bottom:0;padding-left:6px;padding-right:6px;line-height:16px;_padding-top:2px;_height:14px;_line-height:14px;font-size:12px;font-family:simsun;margin-left:10px;overflow:hidden;display:inline-block;-moz-border-radius:1px;-webkit-border-radius:1px;border-radius:1px;color:#fff}a.icon-gw{color:#fff;background:#2196ff;text-decoration:none;cursor:pointer}a.icon-gw:hover{background:#1e87ef}a.icon-gw:active{height:15px;_height:13px;line-height:15px;_line-height:13px;padding-left:5px;background:#1c80d9;border-left:1px solid #145997;border-top:1px solid #145997}.icon-unsafe-icon{background:#e54d4b}#con-at{margin-bottom:9px;padding-left:121px;border-bottom:1px #ebebeb solid}#con-at .result-op{font-size:13px;line-height:1.52em}.wrapper_l #con-at .result-op{width:1058px}.wrapper_s #con-at .result-op{width:869px}#con-ar{margin-bottom:40px}#con-ar .result-op{margin-bottom:28px;font-size:13px;line-height:1.52em}.result_hidden{position:absolute;top:-10000px;left:-10000px}#content_left .result-op,#content_left .result{margin-bottom:14px;border-collapse:collapse}#content_left .c-border .result-op,#content_left .c-border .result{margin-bottom:25px}#content_left .c-border .result-op:last-child,#content_left .c-border .result:last-child{margin-bottom:12px}#content_left .result .f,#content_left .result-op .f{padding:0}.subLink_factory{border-collapse:collapse}.subLink_factory td{padding:0}.subLink_factory td.middle,.subLink_factory td.last{color:#666}.subLink_factory td a{text-decoration:underline}.subLink_factory td.rightTd{text-align:right}.subLink_factory_right{width:100%}.subLink_factory_left td{padding-right:26px}.subLink_factory_left td.last{padding:0}.subLink_factory_left td.first{padding-right:75px}.subLink_factory_right td{width:90px}.subLink_factory_right td.first{width:auto}.general_image_pic a{background:#fff no-repeat center center;text-decoration:none;display:block;overflow:hidden;text-align:left}.res_top_banner{height:36px;text-align:left;border-bottom:1px solid #e3e3e3;background:#f7f7f7;font-size:13px;padding-left:8px;color:#333;position:relative;z-index:302}.res_top_banner span{_zoom:1}.res_top_banner .res_top_banner_icon{background-position:0 -216px;width:18px;height:18px;margin:9px 10px 0 0}.res_top_banner .res_top_banner_icon_baiduapp{background:url(https:\/\/ss1.bdstatic.com\/5eN1bjq8AAUYm2zgoY3K\/r\/www\/cache\/static\/protocol\/https\/global\/img\/baiduappLogo_de45621.png) no-repeat 0 0;width:24px;height:24px;margin:3px 10px 0 0;position:relative;top:3px}.res_top_banner .res_top_banner_icon_windows{background:url(https:\/\/ss1.bdstatic.com\/5eN1bjq8AAUYm2zgoY3K\/r\/www\/cache\/static\/protocol\/https\/global\/img\/winlogo_e925689.png) no-repeat 0 0;width:18px;height:18px;margin:9px 10px 0 0}.res_top_banner .res_top_banner_download{display:inline-block;width:65px;line-height:21px;_padding-top:1px;margin:0 0 0 10px;color:#333;background:#fbfbfb;border:1px solid #b4b6b8;text-align:center;text-decoration:none}.res_top_banner .res_top_banner_download:hover{border:1px solid #38f}.res_top_banner .res_top_banner_download:active{background:#f0f0f0;border:1px solid #b4b6b8}.res_top_banner .res_top_banner_close{background-position:-672px -144px;cursor:pointer;position:absolute;right:10px;top:10px}.res_top_banner_for_win{height:34px;text-align:left;border-bottom:1px solid #f0f0f0;background:#fdfdfd;font-size:13px;padding-left:12px;color:#333;position:relative;z-index:302}.res_top_banner_for_win span{_zoom:1;color:#666}.res_top_banner_for_win .res_top_banner_download{display:inline-block;width:auto;line-height:21px;_padding-top:1px;margin:0 0 0 16px;color:#333;text-align:left;text-decoration:underline}.res_top_banner_for_win .res_top_banner_icon_windows{background:url(https:\/\/ss1.bdstatic.com\/5eN1bjq8AAUYm2zgoY3K\/r\/www\/cache\/static\/protocol\/https\/global\/img\/winlogo_e925689.png) no-repeat 0 0;width:18px;height:18px;margin:8px 8px 0 0}.res_top_banner_for_win .res_top_banner_close{background-position:-672px -144px;cursor:pointer;position:absolute;right:10px;top:10px}.res-gap-right16{margin-right:16px}.res-border-top{border-top:1px solid #f3f3f3}.res-border-bottom{border-bottom:1px solid #f3f3f3}.res-queryext-pos{position:relative;top:1px;_top:0}.c-trust-ecard{height:86px;_height:97px;overflow:hidden}@-moz-document url-prefix(){.result,.f{width:538px}}body{min-width:1000px}#ftCon{display:none}#qrcode{display:none}#pad-version{display:none}#index_guide{display:none}#index_logo{display:none}#u1{display:none}.s_ipt_wr{height:32px}body{padding:0}.s_form:after,.s_tab:after{content:\".\";display:block;height:0;clear:both;visibility:hidden}.s_form{zoom:1;height:55px;padding:0 0 0 10px}#result_logo{float:left;margin:7px 0 0}#result_logo img{width:101px}#head{padding:0;margin:0;width:100%;position:absolute;z-index:301;min-width:1000px;background:#fff;border-bottom:1px solid #ebebeb;position:fixed;_position:absolute;-webkit-transform:translateZ(0)}#head .head_wrapper{_width:1000px}#head.s_down{box-shadow:0 0 5px #888}.fm{clear:none;float:left;margin:11px 0 0 10px}#s_tab{background:#f8f8f8;line-height:36px;height:38px;padding:55px 0 0 121px;float:none;zoom:1}#s_tab a,#s_tab b{width:54px;display:inline-block;text-decoration:none;text-align:center;color:#666;font-size:14px}#s_tab b{border-bottom:2px solid #38f;font-weight:700;color:#323232}#s_tab a:hover{color:#323232}#content_left{width:540px;padding-left:121px;padding-top:5px}#content_right{margin-top:45px}#content_bottom{width:540px;padding-left:121px}#page{padding:0 0 0 121px;margin:30px 0 40px}.to_tieba,.to_zhidao_bottom{margin:10px 0 0 121px;padding-top:5px}.nums{margin:0 0 0 121px;height:42px;line-height:42px}#rs{padding:0;margin:6px 0 0 121px;width:600px}#rs th{width:175px;line-height:22px}#rs .tt{padding:0;line-height:30px}#rs td{width:5px}#rs table{width:540px}#help{background:#f5f6f5;zoom:1;padding:0 0 0 50px;float:right}#help a{color:#777;padding:0 15px;text-decoration:none}#help a:hover{color:#333}#foot{background:#f5f6f5;border-top:1px solid #ebebeb;text-align:left;height:42px;line-height:42px;margin-top:40px;*margin-top:0}#foot .foot_c{float:left;padding:0 0 0 121px}.content_none{padding:45px 0 25px 121px}.nors p{font-size:18px;font-family:microsoft yahei;color:#000}.nors p em{color:#c00}.nors .tip_head{color:#666;font-size:13px;line-height:28px}.nors li{color:#333;line-height:28px;font-size:13px;font-family:'\u5b8b\u4f53';padding-left:30px;list-style-position:inside;list-style-type:disc}#mCon{top:5px}.s_ipt_wr.bg,.s_btn_wr.bg,#su.bg{background-image:none}.s_ipt_wr.bg{background:0 0}.s_btn_wr{width:auto;height:auto;border-bottom:1px solid transparent;*border-bottom:0}.s_btn{width:100px;height:34px;color:#fff;letter-spacing:1px;background:#3385ff;border-bottom:1px solid #2d78f4;outline:medium;*border-bottom:0;-webkit-appearance:none;-webkit-border-radius:0}.s_btn.btnhover{background:#317ef3;border-bottom:1px solid #2868c8;*border-bottom:0;box-shadow:1px 1px 1px #ccc}.s_btn_h{background:#3075dc;box-shadow:inset 1px 1px 3px #2964bb;-webkit-box-shadow:inset 1px 1px 3px #2964bb;-moz-box-shadow:inset 1px 1px 3px #2964bb;-o-box-shadow:inset 1px 1px 3px #2964bb}#wrapper_wrapper .container_l .EC_ppim_top,#wrapper_wrapper .container_xl .EC_ppim_top{width:640px}#wrapper_wrapper .container_s .EC_ppim_top{width:570px}#head .c-icon-bear-round{display:none}.container_l #content_right{width:384px}.container_l{width:1212px}.container_xl #content_right{width:384px}.container_xl{width:1257px}.index_tab_top{display:none}.index_tab_bottom{display:none}#lg{display:none}#m{display:none}#ftCon{display:none}#ent_sug{position:absolute;margin:141px 0 0 130px;font-size:13px;color:#666}.foot_fixed_bottom{position:fixed;bottom:0;width:100%;_position:absolute;_bottom:auto}#head .headBlock{margin:-5px 0 6px 121px}#content_left .leftBlock{margin-bottom:14px;padding-bottom:5px;border-bottom:1px solid #f3f3f3}.hint_toprq_tips{position:relative;width:537px;height:19px;line-height:19px;overflow:hidden;display:none}.hint_toprq_tips span{color:#666}.hint_toprq_icon{margin:0 4px 0 0}.hint_toprq_tips_items{width:444px;_width:440px;max-height:38px;position:absolute;left:95px;top:1px}.hint_toprq_tips_items div{display:inline-block;float:left;height:19px;margin-right:18px;white-space:nowrap;word-break:keep-all}.translateContent{max-width:350px}.translateContent .translateTool{height:16px;margin:-3px 2px}.translateContent .action-translate,.translateContent .action-search{display:inline-block;width:20px;height:16px;background:url(https:\/\/ss1.bdstatic.com\/5eN1bjq8AAUYm2zgoY3K\/r\/www\/cache\/static\/protocol\/https\/global\/img\/translate_tool_icon_57087b6.gif) no-repeat}.translateContent .action-translate{background-position:0 0;border-right:1px solid #dcdcdc}.translateContent .action-translate:hover{background-position:0 -20px}.translateContent .action-search{background-position:-20px 0}.translateContent .action-search:hover{background-position:-20px -20px}.nums{width:538px}.search_tool{_padding-top:15px}.head_nums_cont_outer{height:40px;overflow:hidden;position:relative}.head_nums_cont_inner{position:relative}.search_tool_conter .c-gap-left{margin-left:23px}.search_tool_conter .c-icon-triangle-down{opacity:.6}.search_tool_conter .c-icon-triangle-down:hover{opacity:1}.search_tool,.search_tool_close{float:right}.search_tool,.search_tool_conter span{cursor:pointer;color:#666}.search_tool:hover,.search_tool_conter span:hover{color:#333}.search_tool_conter{font-size:12px;color:#666;margin:0 0 0 121px;height:42px;width:538px;line-height:42px;*height:auto;*line-height:normal;*padding:14px 0}.search_tool_conter span strong{color:#666}.c-tip-con .c-tip-langfilter ul{width:80px;text-align:left;color:#666}.c-tip-con .c-tip-langfilter li a{text-indent:15px;color:#666}.c-tip-con .c-tip-langfilter li span{text-indent:15px;padding:3px 0;color:#999;display:block}.c-tip-con .c-tip-timerfilter ul{width:115px;text-align:left;color:#666}.c-tip-con .c-tip-timerfilter-ft ul{width:180px}.c-tip-con .c-tip-timerfilter-si ul{width:206px;padding:7px 10px 10px}.c-tip-con .c-tip-timerfilter li a{text-indent:15px;color:#666}.c-tip-con .c-tip-timerfilter li span{text-indent:15px;padding:3px 0;color:#999;display:block}.c-tip-con .c-tip-timerfilter-ft li a,.c-tip-con .c-tip-timerfilter-ft li span{text-indent:20px}.c-tip-custom{padding:0 15px 10px;position:relative;zoom:1}.c-tip-custom hr{border:0;height:0;border-top:1px solid #ebebeb}.c-tip-custom p{color:#b6b6b6;height:25px;line-height:25px;margin:2px 0}.c-tip-custom .c-tip-custom-et{margin-bottom:7px}.c-tip-custom-input,.c-tip-si-input{display:inline-block;font-size:11px;color:#333;margin-left:4px;padding:0 2px;width:74%;height:16px;line-height:16px\\9;border:1px solid #ebebeb;outline:0;box-sizing:content-box;-webkit-box-sizing:content-box;-moz-box-sizing:content-box;overflow:hidden;position:relative}.c-tip-custom-input-init{color:#d4d4d4}.c-tip-custom-input-focus,.c-tip-si-input-focus{border:1px solid #3385ff}.c-tip-timerfilter-si .c-tip-si-input{width:138px;height:22px;line-height:22px;vertical-align:0;*vertical-align:-6px;_vertical-align:-5px;padding:0 5px;margin-left:0}.c-tip-con .c-tip-timerfilter li .c-tip-custom-submit,.c-tip-con .c-tip-timerfilter li .c-tip-timerfilter-si-submit{display:inline;padding:4px 10px;margin:0;color:#333;border:1px solid #d8d8d8;font-family:inherit;font-weight:400;text-align:center;vertical-align:0;background-color:#f9f9f9;outline:0}.c-tip-con .c-tip-timerfilter li .c-tip-custom-submit:hover,.c-tip-con .c-tip-timerfilter li .c-tip-timerfilter-si-submit:hover{display:inline;border-color:#388bff}.c-tip-timerfilter-si-error,.c-tip-timerfilter-custom-error{display:none;color:#3385FF;padding-left:4px}.c-tip-timerfilter-custom-error{padding:0;margin:-5px -13px 7px 0}#c-tip-custom-calenderCont{position:absolute;background:#fff;white-space:nowrap;padding:5px 10px;color:#000;border:1px solid #e4e4e4;-webkit-box-shadow:0 2px 4px rgba(0,0,0,.2);box-shadow:0 2px 4px rgba(0,0,0,.2)}#c-tip-custom-calenderCont p{text-align:center;padding:2px 0 4px;*padding:4px 0}#c-tip-custom-calenderCont p i{color:#8e9977;cursor:pointer;text-decoration:underline;font-size:13px}#c-tip-custom-calenderCont .op_cal{background:#fff}.op_cal table{background:#eeefea;margin:0;border-collapse:separate}.op_btn_pre_month,.op_btn_next_month{cursor:pointer;display:block;margin-top:6px}.op_btn_pre_month{float:left;background-position:0 -46px}.op_btn_next_month{float:right;background-position:-18px -46px}.op_cal .op_mon_pre1{padding:0}.op_mon th{text-align:center;font-size:12px;background:#FFF;font-weight:700;border:1px solid #FFF;padding:0}.op_mon td{text-align:center;cursor:pointer}.op_mon h5{margin:0;padding:0 4px;text-align:center;font-size:14px;background:#FFF;height:28px;line-height:28px;border-bottom:1px solid #f5f5f5;margin-bottom:5px}.op_mon strong{font-weight:700}.op_mon td{padding:0 5px;border:1px solid #fff;font-size:12px;background:#fff;height:100%}.op_mon td.op_mon_pre_month{color:#a4a4a4}.op_mon td.op_mon_cur_month{color:#00c}.op_mon td.op_mon_next_month{color:#a4a4a4}.op_mon td.op_mon_day_hover{color:#000;border:1px solid #278df2}.op_mon td.op_mon_day_selected{color:#FFF;border:1px solid #278df2;background:#278df2}.op_mon td.op_mon_day_disabled{cursor:not-allowed;color:#ddd}.zhannei-si-none,.zhannei-si,.hit_quet,.zhannei-search{display:none}#c-tip-custom-calenderCont .op_mon td.op_mon_cur_month{color:#000}#c-tip-custom-calenderCont .op_mon td.op_mon_day_selected{color:#fff}.c-icon-toen{width:24px;height:24px;line-height:24px;background-color:#1cb7fd;color:#fff;font-size:14px;font-weight:700;font-style:normal;display:block;display:inline-block;float:left;text-align:center}.hint_common_restop{width:538px;color:#999;font-size:12px;text-align:left;margin:5px 0 10px 121px}#con-at~#wrapper_wrapper .hint_common_restop{padding-top:7px}.sitelink{overflow:auto;zoom:1}.sitelink_summary{float:left;width:47%;padding-right:30px}.sitelink_summary a{font-size:1.1em;position:relative}.sitelink_summary_last{padding-right:0}.sitelink_en{overflow:auto;zoom:1}.sitelink_en_summary{float:left;width:47%;padding-right:30px}.sitelink_en_summary a{font-size:1.1em;position:relative}.sitelink_en_summary_last{padding-right:0}.sitelink_en_summary_title,.sitelink_en_summary .m{height:22px;overflow:hidden}.without-summary-sitelink-en-container{overflow:hidden;height:22px}.without-summary-sitelink-en{float:left}.without-summary-sitelink-en-delimiter{margin-right:5px;margin-left:5px}.c-frame{margin-bottom:18px}.c-offset{padding-left:10px}.c-gray{color:#666}.c-gap-top-small{margin-top:5px}.c-gap-top{margin-top:10px}.c-gap-bottom-small{margin-bottom:5px}.c-gap-bottom{margin-bottom:10px}.c-gap-left{margin-left:12px}.c-gap-left-small{margin-left:6px}.c-gap-right{margin-right:12px}.c-gap-right-small{margin-right:6px}.c-gap-right-large{margin-right:16px}.c-gap-left-large{margin-left:16px}.c-gap-icon-right-small{margin-right:5px}.c-gap-icon-right{margin-right:10px}.c-gap-icon-left-small{margin-left:5px}.c-gap-icon-left{margin-left:10px}.c-container{width:538px;font-size:13px;line-height:1.54;word-wrap:break-word;word-break:break-word}.c-container .c-container{width:auto}.c-container table{border-collapse:collapse;border-spacing:0}.c-container td{font-size:13px;line-height:1.54}.c-default{font-size:13px;line-height:1.54;word-wrap:break-word;word-break:break-all}.c-container .t,.c-default .t{line-height:1.54}.c-default .t{margin-bottom:0}.cr-content{width:259px;font-size:13px;line-height:1.54;color:#333;word-wrap:break-word;word-break:normal}.cr-content table{border-collapse:collapse;border-spacing:0}.cr-content td{font-size:13px;line-height:1.54;vertical-align:top}.cr-offset{padding-left:17px}.cr-title{font-size:14px;line-height:1.29;font-weight:700}.cr-title-sub{float:right;font-size:13px;font-weight:400}.c-row{*zoom:1}.c-row:after{display:block;height:0;content:\"\";clear:both;visibility:hidden}.c-span2{width:29px}.c-span3{width:52px}.c-span4{width:75px}.c-span5{width:98px}.c-span6{width:121px}.c-span7{width:144px}.c-span8{width:167px}.c-span9{width:190px}.c-span10{width:213px}.c-span11{width:236px}.c-span12{width:259px}.c-span13{width:282px}.c-span14{width:305px}.c-span15{width:328px}.c-span16{width:351px}.c-span17{width:374px}.c-span18{width:397px}.c-span19{width:420px}.c-span20{width:443px}.c-span21{width:466px}.c-span22{width:489px}.c-span23{width:512px}.c-span24{width:535px}.c-span2,.c-span3,.c-span4,.c-span5,.c-span6,.c-span7,.c-span8,.c-span9,.c-span10,.c-span11,.c-span12,.c-span13,.c-span14,.c-span15,.c-span16,.c-span17,.c-span18,.c-span19,.c-span20,.c-span21,.c-span22,.c-span23,.c-span24{float:left;_display:inline;margin-right:17px;list-style:none}.c-span-last{margin-right:0}.c-span-last-s{margin-right:0}.container_l .cr-content{width:351px}.container_l .cr-content .c-span-last-s{margin-right:17px}.container_l .cr-content-narrow{width:259px}.container_l .cr-content-narrow .c-span-last-s{margin-right:0}.c-border{width:518px;padding:9px;border:1px solid #e3e3e3;border-bottom-color:#e0e0e0;border-right-color:#ececec;box-shadow:1px 2px 1px rgba(0,0,0,.072);-webkit-box-shadow:1px 2px 1px rgba(0,0,0,.072);-moz-box-shadow:1px 2px 1px rgba(0,0,0,.072);-o-box-shadow:1px 2px 1px rgba(0,0,0,.072)}.c-border .c-gap-left{margin-left:10px}.c-border .c-gap-left-small{margin-left:5px}.c-border .c-gap-right{margin-right:10px}.c-border .c-gap-right-small{margin-right:5px}.c-border .c-border{width:auto;padding:0;border:0;box-shadow:none;-webkit-box-shadow:none;-moz-box-shadow:none;-o-box-shadow:none}.c-border .c-span2{width:34px}.c-border .c-span3{width:56px}.c-border .c-span4{width:78px}.c-border .c-span5{width:100px}.c-border .c-span6{width:122px}.c-border .c-span7{width:144px}.c-border .c-span8{width:166px}.c-border .c-span9{width:188px}.c-border .c-span10{width:210px}.c-border .c-span11{width:232px}.c-border .c-span12{width:254px}.c-border .c-span13{width:276px}.c-border .c-span14{width:298px}.c-border .c-span15{width:320px}.c-border .c-span16{width:342px}.c-border .c-span17{width:364px}.c-border .c-span18{width:386px}.c-border .c-span19{width:408px}.c-border .c-span20{width:430px}.c-border .c-span21{width:452px}.c-border .c-span22{width:474px}.c-border .c-span23{width:496px}.c-border .c-span24{width:518px}.c-border .c-span2,.c-border .c-span3,.c-border .c-span4,.c-border .c-span5,.c-border .c-span6,.c-border .c-span7,.c-border .c-span8,.c-border .c-span9,.c-border .c-span10,.c-border .c-span11,.c-border .c-span12,.c-border .c-span13,.c-border .c-span14,.c-border .c-span15,.c-border .c-span16,.c-border .c-span17,.c-border .c-span18,.c-border .c-span19,.c-border .c-span20,.c-border .c-span21,.c-border .c-span22,.c-border .c-span23,.c-border .c-span24{margin-right:10px}.c-border .c-span-last{margin-right:0}.c-loading{display:block;width:50px;height:50px;background:url(\/\/www.baidu.com\/aladdin\/img\/tools\/loading.gif) no-repeat 0 0}.c-vline{display:inline-block;margin:0 3px;border-left:1px solid #ddd;width:0;height:12px;_vertical-align:middle;_overflow:hidden}.c-icon{background:url(https:\/\/ss1.bdstatic.com\/5eN1bjq8AAUYm2zgoY3K\/r\/www\/cache\/static\/protocol\/https\/global\/img\/icons_5859e57.png) no-repeat 0 0;_background-image:url(https:\/\/ss1.bdstatic.com\/5eN1bjq8AAUYm2zgoY3K\/r\/www\/cache\/static\/protocol\/https\/global\/img\/icons_d5b04cc.gif)}.c-icon{display:inline-block;width:14px;height:14px;vertical-align:text-bottom;font-style:normal;overflow:hidden}.c-icon-unfold,.c-icon-fold,.c-icon-chevron-unfold,.c-icon-chevron-fold{width:12px;height:12px}.c-icon-star,.c-icon-star-gray{width:60px}.c-icon-qa-empty,.c-icon-safeguard,.c-icon-register-empty,.c-icon-zan,.c-icon-music,.c-icon-music-gray,.c-icon-location,.c-icon-warning,.c-icon-doc,.c-icon-xls,.c-icon-ppt,.c-icon-pdf,.c-icon-txt,.c-icon-play-black,.c-icon-gift,.c-icon-baidu-share,.c-icon-bear,.c-icon-bear-border,.c-icon-location-blue,.c-icon-hotAirBall,.c-icon-moon,.c-icon-streetMap,.c-icon-mv,.c-icon-zhidao-s,.c-icon-shopping{width:16px;height:16px}.c-icon-bear-circle,.c-icon-warning-circle,.c-icon-warning-triangle,.c-icon-warning-circle-gray{width:18px;height:18px}.c-icon-tieba,.c-icon-zhidao,.c-icon-bear-p,.c-icon-bear-pn{width:24px;height:24px}.c-icon-ball-blue,.c-icon-ball-red{width:38px;height:38px}.c-icon-unfold:hover,.c-icon-fold:hover,.c-icon-chevron-unfold:hover,.c-icon-chevron-fold:hover,.c-icon-download:hover,.c-icon-lyric:hover,.c-icon-v:hover,.c-icon-hui:hover,.c-icon-bao:hover,.c-icon-person:hover,.c-icon-high-v:hover,.c-icon-phone:hover,.c-icon-nuo:hover,.c-icon-fan:hover,.c-icon-med:hover,.c-icon-air:hover,.c-icon-share2:hover,.c-icon-v1:hover,.c-icon-v2:hover,.c-icon-write:hover,.c-icon-R:hover{border-color:#388bff}.c-icon-unfold:active,.c-icon-fold:active,.c-icon-chevron-unfold:active,.c-icon-chevron-fold:active,.c-icon-download:active,.c-icon-lyric:active,.c-icon-v:active,.c-icon-hui:active,.c-icon-bao:active,.c-icon-person:active,.c-icon-high-v:active,.c-icon-phone:active,.c-icon-nuo:active,.c-icon-fan:active,.c-icon-med:active,.c-icon-air:active,.c-icon-share2:active,.c-icon-v1:active,.c-icon-v2:active,.c-icon-write:active,.c-icon-R:active{border-color:#a2a6ab;background-color:#f0f0f0;box-shadow:inset 1px 1px 1px #c7c7c7;-webkit-box-shadow:inset 1px 1px 1px #c7c7c7;-moz-box-shadow:inset 1px 1px 1px #c7c7c7;-o-box-shadow:inset 1px 1px 1px #c7c7c7}.c-icon-v3:hover{border-color:#ffb300}.c-icon-v3:active{border-color:#a2a6ab;background-color:#f0f0f0;box-shadow:inset 1px 1px 1px #c7c7c7;-webkit-box-shadow:inset 1px 1px 1px #c7c7c7;-moz-box-shadow:inset 1px 1px 1px #c7c7c7;-o-box-shadow:inset 1px 1px 1px #c7c7c7}.c-icon-unfold,.c-icon-fold,.c-icon-chevron-unfold,.c-icon-chevron-fold,.c-icon-download,.c-icon-lyric{border:1px solid #d8d8d8;cursor:pointer}.c-icon-v,.c-icon-hui,.c-icon-bao,.c-icon-person,.c-icon-high-v,.c-icon-phone,.c-icon-nuo,.c-icon-fan,.c-icon-med,.c-icon-air,.c-icon-share2,.c-icon-v1,.c-icon-v2,.c-icon-v3,.c-icon-write,.c-icon-R{border:1px solid #d8d8d8;cursor:pointer;border-color:transparent;_border-color:tomato;_filter:chroma(color=#ff6347)}.c-icon-v1,.c-icon-v2,.c-icon-v3,.c-icon-v1-noborder,.c-icon-v2-noborder,.c-icon-v3-noborder,.c-icon-v1-noborder-disable,.c-icon-v2-noborder-disable,.c-icon-v3-noborder-disable{width:19px}.c-icon-download,.c-icon-lyric{width:16px;height:16px}.c-icon-play-circle,.c-icon-stop-circle{width:18px;height:18px}.c-icon-play-circle-middle,.c-icon-stop-circle-middle{width:24px;height:24px}.c-icon-play-black-large,.c-icon-stop-black-large{width:36px;height:36px}.c-icon-play-black-larger,.c-icon-stop-black-larger{width:52px;height:52px}.c-icon-flag{background-position:0 -144px}.c-icon-bus{background-position:-24px -144px}.c-icon-calendar{background-position:-48px -144px}.c-icon-street{background-position:-72px -144px}.c-icon-map{background-position:-96px -144px}.c-icon-bag{background-position:-120px -144px}.c-icon-money{background-position:-144px -144px}.c-icon-game{background-position:-168px -144px}.c-icon-user{background-position:-192px -144px}.c-icon-globe{background-position:-216px -144px}.c-icon-lock{background-position:-240px -144px}.c-icon-plane{background-position:-264px -144px}.c-icon-list{background-position:-288px -144px}.c-icon-star-gray{background-position:-312px -144px}.c-icon-circle-gray{background-position:-384px -144px}.c-icon-triangle-down{background-position:-408px -144px}.c-icon-triangle-up{background-position:-432px -144px}.c-icon-triangle-up-empty{background-position:-456px -144px}.c-icon-sort-gray{background-position:-480px -144px}.c-icon-sort-up{background-position:-504px -144px}.c-icon-sort-down{background-position:-528px -144px}.c-icon-down-gray{background-position:-552px -144px}.c-icon-up-gray{background-position:-576px -144px}.c-icon-download-noborder{background-position:-600px -144px}.c-icon-lyric-noborder{background-position:-624px -144px}.c-icon-download-white{background-position:-648px -144px}.c-icon-close{background-position:-672px -144px}.c-icon-fail{background-position:-696px -144px}.c-icon-success{background-position:-720px -144px}.c-icon-triangle-down-g{background-position:-744px -144px}.c-icon-refresh{background-position:-768px -144px}.c-icon-chevron-left-gray{background-position:-816px -144px}.c-icon-chevron-right-gray{background-position:-840px -144px}.c-icon-setting{background-position:-864px -144px}.c-icon-close2{background-position:-888px -144px}.c-icon-chevron-top-gray-s{background-position:-912px -144px}.c-icon-fullscreen{background-position:0 -168px}.c-icon-safe{background-position:-24px -168px}.c-icon-exchange{background-position:-48px -168px}.c-icon-chevron-bottom{background-position:-72px -168px}.c-icon-chevron-top{background-position:-96px -168px}.c-icon-unfold{background-position:-120px -168px}.c-icon-fold{background-position:-144px -168px}.c-icon-chevron-unfold{background-position:-168px -168px}.c-icon-qa{background-position:-192px -168px}.c-icon-register{background-position:-216px -168px}.c-icon-star{background-position:-240px -168px}.c-icon-star-gray{position:relative}.c-icon-star-gray .c-icon-star{position:absolute;top:0;left:0}.c-icon-play-blue{background-position:-312px -168px}.c-icon-pic{width:16px;background-position:-336px -168px}.c-icon-chevron-fold{background-position:-360px -168px}.c-icon-video{width:18px;background-position:-384px -168px}.c-icon-circle-blue{background-position:-408px -168px}.c-icon-circle-yellow{background-position:-432px -168px}.c-icon-play-white{background-position:-456px -168px}.c-icon-triangle-down-blue{background-position:-480px -168px}.c-icon-chevron-unfold2{background-position:-504px -168px}.c-icon-right{background-position:-528px -168px}.c-icon-right-empty{background-position:-552px -168px}.c-icon-new-corner{width:15px;background-position:-576px -168px}.c-icon-horn{background-position:-600px -168px}.c-icon-right-large{width:18px;background-position:-624px -168px}.c-icon-wrong-large{background-position:-648px -168px}.c-icon-circle-blue-s{background-position:-672px -168px}.c-icon-play-gray{background-position:-696px -168px}.c-icon-up{background-position:-720px -168px}.c-icon-down{background-position:-744px -168px}.c-icon-stable{background-position:-768px -168px}.c-icon-calendar-blue{background-position:-792px -168px}.c-icon-triangle-down-blue2{background-position:-816px -168px}.c-icon-triangle-up-blue2{background-position:-840px -168px}.c-icon-down-blue{background-position:-864px -168px}.c-icon-up-blue{background-position:-888px -168px}.c-icon-ting{background-position:-912px -168px}.c-icon-piao{background-position:-936px -168px}.c-icon-wrong-empty{background-position:-960px -168px}.c-icon-warning-circle-s{background-position:-984px -168px}.c-icon-chevron-left{background-position:-1008px -168px}.c-icon-chevron-right{background-position:-1032px -168px}.c-icon-circle-gray-s{background-position:-1056px -168px}.c-icon-v,.c-icon-v-noborder{background-position:0 -192px}.c-icon-hui{background-position:-24px -192px}.c-icon-bao{background-position:-48px -192px}.c-icon-phone{background-position:-72px -192px}.c-icon-qa-empty{background-position:-96px -192px}.c-icon-safeguard{background-position:-120px -192px}.c-icon-register-empty{background-position:-144px -192px}.c-icon-zan{background-position:-168px -192px}.c-icon-music{background-position:-192px -192px}.c-icon-music-gray{background-position:-216px -192px}.c-icon-location{background-position:-240px -192px}.c-icon-warning{background-position:-264px -192px}.c-icon-doc{background-position:-288px -192px}.c-icon-xls{background-position:-312px -192px}.c-icon-ppt{background-position:-336px -192px}.c-icon-pdf{background-position:-360px -192px}.c-icon-txt{background-position:-384px -192px}.c-icon-play-black{background-position:-408px -192px}.c-icon-play-black:hover{background-position:-432px -192px}.c-icon-gift{background-position:-456px -192px}.c-icon-baidu-share{background-position:-480px -192px}.c-icon-bear{background-position:-504px -192px}.c-icon-R{background-position:-528px -192px}.c-icon-bear-border{background-position:-576px -192px}.c-icon-person,.c-icon-person-noborder{background-position:-600px -192px}.c-icon-location-blue{background-position:-624px -192px}.c-icon-hotAirBall{background-position:-648px -192px}.c-icon-moon{background-position:-672px -192px}.c-icon-streetMap{background-position:-696px -192px}.c-icon-high-v,.c-icon-high-v-noborder{background-position:-720px -192px}.c-icon-nuo{background-position:-744px -192px}.c-icon-mv{background-position:-768px -192px}.c-icon-fan{background-position:-792px -192px}.c-icon-med{background-position:-816px -192px}.c-icon-air{background-position:-840px -192px}.c-icon-share2{background-position:-864px -192px}.c-icon-v1,.c-icon-v1-noborder{background-position:-888px -192px}.c-icon-v2,.c-icon-v2-noborder{background-position:-912px -192px}.c-icon-v3,.c-icon-v3-noborder{background-position:-936px -192px}.c-icon-v1-noborder-disable{background-position:-960px -192px}.c-icon-v2-noborder-disable{background-position:-984px -192px}.c-icon-v3-noborder-disable{background-position:-1008px -192px}.c-icon-write{background-position:-1032px -192px}.c-icon-zhidao-s{background-position:-1056px -192px}.c-icon-shopping{background-position:-1080px -192px}.c-icon-bear-circle{background-position:0 -216px}.c-icon-warning-circle{background-position:-24px -216px}.c-icon-warning-triangle{width:24px;background-position:-48px -216px}.c-icon-warning-circle-gray{background-position:-72px -216px}.c-icon-ball-red{background-position:0 -240px}.c-icon-ball-blue{background-position:-48px -240px}.c-icon-tieba{background-position:0 -288px}.c-icon-zhidao{background-position:-48px -288px}.c-icon-bear-p{background-position:-96px -288px}.c-icon-bear-pn{background-position:-144px -288px}.c-icon-download{background-position:0 -336px}.c-icon-lyric{background-position:-24px -336px}.c-icon-play-circle{background-position:-48px -336px}.c-icon-play-circle:hover{background-position:-72px -336px}.c-icon-stop-circle{background-position:-96px -336px}.c-icon-stop-circle:hover{background-position:-120px -336px}.c-icon-play-circle-middle{background-position:0 -360px}.c-icon-play-circle-middle:hover{background-position:-48px -360px}.c-icon-stop-circle-middle{background-position:-96px -360px}.c-icon-stop-circle-middle:hover{background-position:-144px -360px}.c-icon-play-black-large{background-position:0 -408px}.c-icon-play-black-large:hover{background-position:-48px -408px}.c-icon-stop-black-large{background-position:-96px -408px}.c-icon-stop-black-large:hover{background-position:-144px -408px}.c-icon-play-black-larger{background-position:0 -456px}.c-icon-play-black-larger:hover{background-position:-72px -456px}.c-icon-stop-black-larger{background-position:-144px -456px}.c-icon-stop-black-larger:hover{background-position:-216px -456px}.c-recommend{font-size:0;padding:5px 0;border:1px solid #f3f3f3;border-left:0;border-right:0}.c-recommend .c-icon{margin-bottom:-4px}.c-recommend .c-gray,.c-recommend a{font-size:13px}.c-recommend-notopline{padding-top:0;border-top:0}.c-recommend-vline{display:inline-block;margin:0 10px -2px;border-left:1px solid #d8d8d8;width:0;height:12px;_vertical-align:middle;_overflow:hidden}.c-text{display:inline-block;padding:2px;text-align:center;vertical-align:text-bottom;font-size:12px;line-height:100%;font-style:normal;font-weight:400;color:#fff;overflow:hidden}a.c-text{text-decoration:none}.c-text-new{background-color:#f13f40}.c-text-info{padding-left:0;padding-right:0;font-weight:700;color:#2b99ff;*vertical-align:baseline;_position:relative;_top:2px}.c-text-info b{_position:relative;_top:-1px}.c-text-info span{padding:0 2px;font-weight:400}.c-text-important{background-color:#1cb7fd}.c-text-public{background-color:#2b99ff}.c-text-warning{background-color:#ff830f}.c-text-prompt{background-color:#f5c537}.c-text-danger{background-color:#f13f40}.c-text-safe{background-color:#52c277}.c-text-empty{padding-top:1px;padding-bottom:1px;border:1px solid #d8d8d8;cursor:pointer;color:#23b9fd;background-color:#fff}.c-text-empty:hover{border-color:#388bff}.c-text-empty:active{border-color:#a2a6ab;background-color:#f0f0f0;box-shadow:inset 1px 1px 1px #c7c7c7;-webkit-box-shadow:inset 1px 1px 1px #c7c7c7;-moz-box-shadow:inset 1px 1px 1px #c7c7c7;-o-box-shadow:inset 1px 1px 1px #c7c7c7}.c-text-mult{padding-left:5px;padding-right:5px}.c-text-gray{background-color:#666}.c-btn,.c-btn:visited{color:#333!important}.c-btn{display:inline-block;padding:0 14px;margin:0;height:24px;line-height:25px;font-size:13px;filter:chroma(color=#000000);*zoom:1;border:1px solid #d8d8d8;cursor:pointer;font-family:inherit;font-weight:400;text-align:center;vertical-align:middle;background-color:#f9f9f9;overflow:hidden;outline:0}.c-btn:hover{border-color:#388bff}.c-btn:active{border-color:#a2a6ab;background-color:#f0f0f0;box-shadow:inset 1px 1px 1px #c7c7c7;-webkit-box-shadow:inset 1px 1px 1px #c7c7c7;-moz-box-shadow:inset 1px 1px 1px #c7c7c7;-o-box-shadow:inset 1px 1px 1px #c7c7c7}a.c-btn{text-decoration:none}button.c-btn{height:26px;_line-height:18px;*overflow:visible}button.c-btn::-moz-focus-inner{padding:0;border:0}.c-btn .c-icon{margin-top:5px}.c-btn-disable{color:#999!important}.c-btn-disable:visited{color:#999!important}.c-btn-disable:hover{border:1px solid #d8d8d8;cursor:default}.c-btn-disable:active{border-color:#d8d8d8;background-color:#f9f9f9;box-shadow:none;-webkit-box-shadow:none;-moz-box-shadow:none;-o-box-shadow:none}.c-btn-mini{padding-left:5px;padding-right:5px;height:18px;line-height:18px;font-size:12px}button.c-btn-mini{height:20px;_height:18px;_line-height:14px}.c-btn-mini .c-icon{margin-top:2px}.c-btn-large{height:28px;line-height:28px;font-size:14px;font-family:\"\u5fae\u8f6f\u96c5\u9ed1\",\"\u9ed1\u4f53\"}button.c-btn-large{height:30px;_line-height:24px}.c-btn-large .c-icon{margin-top:7px;_margin-top:6px}.c-btn-primary,.c-btn-primary:visited{color:#fff!important}.c-btn-primary{background-color:#388bff;border-color:#3c8dff #408ffe #3680e6}.c-btn-primary:hover{border-color:#2678ec #2575e7 #1c6fe2 #2677e7;background-color:#388bff;background-image:url(data:image\/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAACCAMAAACuX0YVAAAABlBMVEVnpv85i\/9PO5r4AAAAD0lEQVR42gEEAPv\/AAAAAQAFAAIros7PAAAAAElFTkSuQmCC);*background-image:none;background-repeat:repeat-x;box-shadow:1px 1px 1px rgba(0,0,0,.4);-webkit-box-shadow:1px 1px 1px rgba(0,0,0,.4);-moz-box-shadow:1px 1px 1px rgba(0,0,0,.4);-o-box-shadow:1px 1px 1px rgba(0,0,0,.4)}.c-btn-primary:active{border-color:#178ee3 #1784d0 #177bbf #1780ca;background-color:#388bff;background-image:none;box-shadow:inset 1px 1px 1px rgba(0,0,0,.15);-webkit-box-shadow:inset 1px 1px 1px rgba(0,0,0,.15);-moz-box-shadow:inset 1px 1px 1px rgba(0,0,0,.15);-o-box-shadow:inset 1px 1px 1px rgba(0,0,0,.15)}.c-btn .c-icon{float:left}.c-dropdown2{position:relative;display:inline-block;width:100%;height:26px;line-height:26px;font-size:13px;vertical-align:middle;outline:0;_font-family:SimSun;background-color:#fff;word-wrap:normal;word-break:normal}.c-dropdown2 .c-dropdown2-btn-group{position:relative;height:24px;border:1px solid #999;border-bottom-color:#d8d8d8;border-right-color:#d8d8d8;-moz-user-select:none;-webkit-user-select:none;user-select:none}.c-dropdown2:hover .c-dropdown2-btn-group,.c-dropdown2-hover .c-dropdown2-btn-group{box-shadow:inset 1px 1px 0 0 #d8d8d8;-webkit-box-shadow:inset 1px 1px 0 0 #d8d8d8;-moz-box-shadow:inset 1px 1px 0 0 #d8d8d8;-o-box-shadow:inset 1px 1px 0 0 #d8d8d8}.c-dropdown2:hover .c-dropdown2-btn-icon,.c-dropdown2-hover .c-dropdown2-btn-icon{box-shadow:inset 0 1px 0 0 #d8d8d8;-webkit-box-shadow:inset 0 1px 0 0 #d8d8d8;-moz-box-shadow:inset 0 1px 0 0 #d8d8d8;-o-box-shadow:inset 0 1px 0 0 #d8d8d8}.c-dropdown2:hover .c-dropdown2-btn-icon-border,.c-dropdown2-hover .c-dropdown2-btn-icon-border{background-color:#f2f2f2}.c-dropdown2 .c-dropdown2-btn{height:24px;padding-left:10px;padding-right:10px;cursor:default;overflow:hidden;white-space:nowrap}.c-dropdown2 .c-dropdown2-btn-icon{position:absolute;top:0;right:0;width:23px;height:24px;line-height:24px;background-color:#fff;padding:0 1px 0 10px}.c-dropdown2 .c-dropdown2-btn-icon-border{height:24px;width:23px;border-left:1px solid #d9d9d9;text-align:center;zoom:1}.c-dropdown2 .c-icon-triangle-down{*margin-top:5px;_margin-left:2px}.c-dropdown2 .c-dropdown2-menu{position:absolute;left:0;top:100%;_margin-top:0;width:100%;overflow:hidden;border:1px solid #bbb;background:#fff;visibility:hidden}.c-dropdown2 .c-dropdown2-menu-inner{overflow:hidden}.c-dropdown2 .c-dropdown2-option{background-color:#fff;cursor:pointer}.c-dropdown2 .c-dropdown2-selected{background-color:#f5f5f5}.c-dropdown2-common ul,.c-dropdown2-common li{margin:0;padding:0;list-style:none}.c-dropdown2-common .c-dropdown2-option{height:26px;line-height:26px;font-size:12px;color:#333;white-space:nowrap;cursor:pointer;padding-left:10px}.c-dropdown2-common .c-dropdown2-selected{background-color:#f5f5f5}.c-dropdown2-common .c-dropdown2-menu-group .c-dropdown2-group{padding-left:10px;font-weight:700;cursor:default}.c-dropdown2-common .c-dropdown2-menu-group .c-dropdown2-option{padding-left:20px}.c-img{display:block;min-height:1px;border:0 0}.c-img3{width:52px}.c-img4{width:75px}.c-img6{width:121px}.c-img7{width:144px}.c-img12{width:259px}.c-img15{width:328px}.c-img18{width:397px}.c-border .c-img3{width:56px}.c-border .c-img4{width:78px}.c-border .c-img7{width:144px}.c-border .c-img12{width:254px}.c-border .c-img15{width:320px}.c-border .c-img18{width:386px}.c-index{display:inline-block;padding:1px 0;color:#fff;width:14px;line-height:100%;font-size:12px;text-align:center;background-color:#8eb9f5}.c-index-hot,.c-index-hot1{background-color:#f54545}.c-index-hot2{background-color:#ff8547}.c-index-hot3{background-color:#ffac38}.c-input{display:inline-block;padding:0 4px;height:24px;line-height:24px\\9;font-size:13px;border:1px solid #999;border-bottom-color:#d8d8d8;border-right-color:#d8d8d8;outline:0;box-sizing:content-box;-webkit-box-sizing:content-box;-moz-box-sizing:content-box;vertical-align:top;overflow:hidden}.c-input:hover{box-shadow:inset 1px 1px 1px 0 #d8d8d8;-webkit-box-shadow:inset 1px 1px 1px 0 #d8d8d8;-moz-box-shadow:inset 1px 1px 1px 0 #d8d8d8;-o-box-shadow:inset 1px 1px 1px 0 #d8d8d8}.c-input .c-icon{float:right;margin-top:6px}.c-input .c-icon-left{float:left;margin-right:4px}.c-input input{float:left;height:22px;*padding-top:4px;margin-top:2px;font-size:13px;border:0;outline:0}.c-input{width:180px}.c-input input{width:162px}.c-input-xmini{width:65px}.c-input-xmini input{width:47px}.c-input-mini{width:88px}.c-input-mini input{width:70px}.c-input-small{width:157px}.c-input-small input{width:139px}.c-input-large{width:203px}.c-input-large input{width:185px}.c-input-xlarge{width:341px}.c-input-xlarge input{width:323px}.c-input12{width:249px}.c-input12 input{width:231px}.c-input20{width:433px}.c-input20 input{width:415px}.c-border .c-input{width:178px}.c-border .c-input input{width:160px}.c-border .c-input-xmini{width:68px}.c-border .c-input-xmini input{width:50px}.c-border .c-input-mini{width:90px}.c-border .c-input-mini input{width:72px}.c-border .c-input-small{width:156px}.c-border .c-input-small input{width:138px}.c-border .c-input-large{width:200px}.c-border .c-input-large input{width:182px}.c-border .c-input-xlarge{width:332px}.c-border .c-input-xlarge input{width:314px}.c-border .c-input12{width:244px}.c-border .c-input12 input{width:226px}.c-border .c-input20{width:420px}.c-border .c-input20 input{width:402px}.c-numberset{*zoom:1}.c-numberset:after{display:block;height:0;content:\"\";clear:both;visibility:hidden}.c-numberset li{float:left;margin-right:17px;list-style:none}.c-numberset .c-numberset-last{margin-right:0}.c-numberset a{display:block;width:50px;text-decoration:none;text-align:center;border:1px solid #d8d8d8;cursor:pointer}.c-numberset a:hover{border-color:#388bff}.c-border .c-numberset li{margin-right:10px}.c-border .c-numberset .c-numberset-last{margin-right:0}.c-border .c-numberset a{width:54px}.c-table{width:100%;border-collapse:collapse;border-spacing:0}.c-table th,.c-table td{padding-left:10px;line-height:1.54;font-size:13px;border-bottom:1px solid #f3f3f3;text-align:left}.cr-content .c-table th:first-child,.cr-content .c-table td:first-child{padding-left:0}.c-table th{padding-top:4px;padding-bottom:4px;font-weight:400;color:#666;border-color:#f0f0f0;white-space:nowrap;background-color:#fafafa}.c-table td{padding-top:6.5px;padding-bottom:6.5px}.c-table-hasimg td{padding-top:10px;padding-bottom:10px}.c-table a,.c-table em{text-decoration:none}.c-table a:hover,.c-table a:hover em{text-decoration:underline}.c-table a.c-icon:hover{text-decoration:none}.c-table .c-btn:hover,.c-table .c-btn:hover em{text-decoration:none}.c-table-nohihead th{background-color:transparent}.c-table-noborder td{border-bottom:0}.c-tabs-nav-movetop{margin:-10px -9px 0 -10px;position:relative}.c-tabs-nav{border-bottom:1px solid #d9d9d9;background-color:#fafafa;line-height:1.54;font-size:0;*zoom:1;_overflow-x:hidden;_position:relative}.c-tabs-nav:after{display:block;height:0;content:\"\";clear:both;visibility:hidden}.c-tabs-nav .c-tabs-nav-btn{float:right;_position:absolute;_top:0;_right:0;_z-index:1;background:#fafafa}.c-tabs-nav .c-tabs-nav-btn .c-tabs-nav-btn-prev,.c-tabs-nav .c-tabs-nav-btn .c-tabs-nav-btn-next{float:left;padding:6px 2px;cursor:pointer}.c-tabs-nav .c-tabs-nav-btn .c-tabs-nav-btn-disable{cursor:default}.c-tabs-nav .c-tabs-nav-view{_position:relative;overflow:hidden;*zoom:1;margin-bottom:-1px}.c-tabs-nav .c-tabs-nav-view .c-tabs-nav-li{margin-bottom:0}.c-tabs-nav .c-tabs-nav-more{float:left;white-space:nowrap}.c-tabs-nav li,.c-tabs-nav a{color:#666;font-size:13px;*zoom:1}.c-tabs-nav li{display:inline-block;margin-bottom:-1px;*display:inline;padding:3px 15px;vertical-align:bottom;border-style:solid;border-width:2px 1px 0;border-color:transparent;_border-color:tomato;_filter:chroma(color=#ff6347);list-style:none;cursor:pointer;white-space:nowrap;overflow:hidden}.c-tabs-nav a{text-decoration:none}.c-tabs-nav .c-tabs-nav-sep{height:16px;width:0;padding:0;margin-bottom:4px;border-style:solid;border-width:0 1px;border-color:transparent #fff transparent #dedede}.c-tabs-nav .c-tabs-nav-selected{_position:relative;border-color:#2c99ff #e4e4e4 #fff #dedede;background-color:#fff;color:#000;cursor:default}.c-tabs-nav-one .c-tabs-nav-selected{border-color:transparent;_border-color:tomato;_filter:chroma(color=#ff6347);background-color:transparent;color:#666}.c-tabs .c-tabs .c-tabs-nav{padding:10px 0 5px;border:0 0;background-color:#fff}.c-tabs .c-tabs .c-tabs-nav li,.c-tabs .c-tabs .c-tabs-nav a{color:#00c}.c-tabs .c-tabs .c-tabs-nav li{padding:0 5px;position:static;margin:0 10px;border:0 0;cursor:pointer;white-space:nowrap}.c-tabs .c-tabs .c-tabs-nav .c-tabs-nav-sep{height:11px;width:0;padding:0;margin:0 0 4px;border:0 0;border-left:1px solid #d8d8d8}.c-tabs .c-tabs .c-tabs-nav .c-tabs-nav-selected{background-color:#2c99ff;color:#fff;cursor:default}.c-tag{padding-top:3px;margin-bottom:3px;height:1.7em;font-size:13px;line-height:1.4em;transition:height .3s ease-in;-webkit-transition:height .3s ease-in;-moz-transition:height .3s ease-in;-ms-transition:height .3s ease-in;-o-transition:height .3s ease-in;*zoom:1;overflow:hidden}.c-tag:after{display:block;height:0;content:\"\";clear:both;visibility:hidden}.c-tag-cont{overflow:hidden;*zoom:1}.c-tag-type,.c-tag-li,.c-tag-more,.c-tag-cont span{margin:2px 0}.c-tag-type,.c-tag-li,.c-tag-cont span{float:left}.c-tag-type,.c-tag-more{color:#666}.c-tag-li,.c-tag-cont span{padding:0 4px;display:inline-block;margin-right:12px;white-space:nowrap;cursor:pointer;color:#00c}.c-tag .c-tag-selected{background:#388bff;color:#fff}.c-tag-more{float:right;background:#fff;cursor:pointer;*height:18px}.c-tool{display:inline-block;width:56px;height:56px;background:url(\/\/www.baidu.com\/aladdin\/img\/tools\/tools-5.png) no-repeat}.c-tool-region{background-position:0 0}.c-tool-calendar{background-position:-72px 0}.c-tool-city{background-position:-144px 0}.c-tool-phone-pos{background-position:-216px 0}.c-tool-other{background-position:-288px 0}.c-tool-midnight{background-position:-360px 0}.c-tool-kefu{width:121px;background-position:-432px 0}.c-tool-phone{background-position:-576px 0}.c-tool-car{background-position:-648px 0}.c-tool-station{background-position:0 -72px}.c-tool-cheat{background-position:-72px -72px}.c-tool-counter{background-position:-144px -72px}.c-tool-time{background-position:-216px -72px}.c-tool-zip{background-position:-288px -72px}.c-tool-warning{background-position:-360px -72px}.c-tool-ip{background-position:0 -144px}.c-tool-unit{background-position:-72px -144px}.c-tool-rate{background-position:-144px -144px}.c-tool-conversion{background-position:-288px -144px}.c-tool-ads{background-position:-360px -144px}.soutu-input{padding-left:55px!important}.soutu-input-image{position:absolute;left:1px;top:1px;height:28px;width:49px;z-index:1;padding:0;background:#e6e6e6;border:1px solid #e6e6e6}.soutu-input-thumb{height:28px;width:28px;min-width:1px}.soutu-input-close{position:absolute;right:0;top:0;cursor:pointer;display:block;width:22px;height:28px}.soutu-input-close::after{content:\" \";position:absolute;right:3px;top:50%;cursor:pointer;margin-top:-7px;display:block;width:14px;height:14px;background:url(https:\/\/ss1.bdstatic.com\/5eN1bjq8AAUYm2zgoY3K\/r\/www\/cache\/static\/protocol\/https\/soutu\/img\/soutu_icons_new_8abaf8a.png) no-repeat -163px 0}.soutu-input-image:hover .soutu-input-close::after{background-position:-215px 2px}.fb-hint{margin-top:5px;transition-duration:.9s;opacity:0;display:none;color:red}.fb-img{display:none}.fb-hint-tip{height:44px;line-height:24px;background-color:#38f;color:#fff;box-sizing:border-box;width:269px;font-size:16px;padding:10px;padding-left:14px;position:absolute;top:-65px;right:-15px;border-radius:3px;z-index:299}.fb-hint-tip::before{content:\"\";width:0;height:0;display:block;position:absolute;border-left:8px solid transparent;border-right:8px solid transparent;border-top:8px solid #38f;bottom:-8px;right:25px}.fb-mask,.fb-mask-light{position:absolute;top:0;left:0;bottom:0;right:0;z-index:296;background-color:#000;filter:alpha(opacity=60);background-color:rgba(0,0,0,.6)}.fb-mask-light{background-color:#fff;filter:alpha(opacity=0);background-color:rgba(255,255,255,0)}.fb-success .fb-success-text{text-align:center;color:#333;font-size:13px;margin-bottom:14px}.fb-success-text.fb-success-text-title{color:#3b6;font-size:16px;margin-bottom:16px}.fb-success-text-title i{width:16px;height:16px;margin-right:5px}.fb-list-container{box-sizing:border-box;padding:4px 8px;position:absolute;top:0;left:0;bottom:0;right:0;z-index:298;display:block;width:100%;cursor:pointer;margin-top:-5px;margin-left:-5px}.fb-list-container-hover{background-color:#fff;border:2px #38f solid}.fb-list-container-first{box-sizing:border-box;padding-left:10px;padding-top:5px;position:absolute;top:0;left:0;bottom:0;right:0;z-index:297;display:block;width:100%;cursor:pointer;margin-top:-5px;margin-left:-5px;border:3px #f5f5f5 dashed;border-radius:3px}.fb-des-content{font-size:13px!important;color:#000}.fb-des-content::-webkit-input-placeholder{font-size:13px!important;color:#9a9a9a}.fb-des-content:-moz-placeholder{font-size:13px!important;color:#9a9a9a}.fb-des-content::-moz-placeholder{font-size:13px!important;color:#9a9a9a}.fb-des-content:-ms-input-placeholder{font-size:13px!important;color:#9a9a9a}.fb-btn,.fb-btn:visited{color:#333!important}.fb-select{position:relative;background-color:#fff;border:1px solid #ccc}.fb-select i{position:absolute;right:2px;top:7px}.fb-type{width:350px;box-sizing:border-box;height:28px;font-size:13px;line-height:28px;border:0;word-break:normal;word-wrap:normal;position:relative;appearance:none;-moz-appearance:none;-webkit-appearance:none;display:inline-block;vertical-align:middle;line-height:normal;color:#333;background-color:transparent;border-radius:0;overflow:hidden;outline:0;padding-left:5px}.fb-type::-ms-expand{display:none}.fb-btn{display:inline-block;padding:0 14px;margin:0;height:24px;line-height:25px;font-size:13px;filter:chroma(color=#000000);*zoom:1;border:1px solid #d8d8d8;cursor:pointer;font-family:inherit;font-weight:400;text-align:center;vertical-align:middle;background-color:#f9f9f9;overflow:hidden;outline:0}.fb-btn:hover{border-color:#388bff}.fb-btn:active{border-color:#a2a6ab;background-color:#f0f0f0;box-shadow:inset 1px 1px 1px #c7c7c7;-webkit-box-shadow:inset 1px 1px 1px #c7c7c7;-moz-box-shadow:inset 1px 1px 1px #c7c7c7;-o-box-shadow:inset 1px 1px 1px #c7c7c7}a.fb-btn{text-decoration:none}button.fb-btn{height:26px;_line-height:18px;*overflow:visible}button.fb-btn::-moz-focus-inner{padding:0;border:0}.fb-btn .c-icon{margin-top:5px}.fb-btn-primary,.fb-btn-primary:visited{color:#fff!important}.fb-btn-primary{background-color:#388bff;_width:82px;border-color:#3c8dff #408ffe #3680e6}.fb-btn-primary:hover{border-color:#2678ec #2575e7 #1c6fe2 #2677e7;background-color:#388bff;background-image:url(data:image\/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAACCAMAAACuX0YVAAAABlBMVEVnpv85i\/9PO5r4AAAAD0lEQVR42gEEAPv\/AAAAAQAFAAIros7PAAAAAElFTkSuQmCC);background-repeat:repeat-x;box-shadow:1px 1px 1px rgba(0,0,0,.4);-webkit-box-shadow:1px 1px 1px rgba(0,0,0,.4);-moz-box-shadow:1px 1px 1px rgba(0,0,0,.4);-o-box-shadow:1px 1px 1px rgba(0,0,0,.4)}.fb-btn-primary:active{border-color:#178ee3 #1784d0 #177bbf #1780ca;background-color:#388bff;background-image:none;box-shadow:inset 1px 1px 1px rgba(0,0,0,.15);-webkit-box-shadow:inset 1px 1px 1px rgba(0,0,0,.15);-moz-box-shadow:inset 1px 1px 1px rgba(0,0,0,.15);-o-box-shadow:inset 1px 1px 1px rgba(0,0,0,.15)}.fb-feedback-right-dialog{position:fixed;z-index:299;bottom:0;right:0}.fb-feedback-list-dialog,.fb-feedback-list-dialog-left{position:absolute;z-index:299}.fb-feedback-list-dialog:before{content:\"\";width:0;height:0;display:block;position:absolute;top:15px;left:-6px;border-top:8px solid transparent;border-bottom:8px solid transparent;border-right:8px solid #fff}.fb-feedback-list-dialog-left:before{content:\"\";width:0;height:0;display:block;position:absolute;top:15px;right:-6px;border-top:8px solid transparent;border-bottom:8px solid transparent;border-left:8px solid #fff}.fb-header{padding-left:20px;padding-right:20px;margin-top:14px;text-align:left;-moz-user-select:none}.fb-header .fb-close{opacity:.2;filter:alpha(opacity=20)}.fb-close{text-decoration:none;margin-top:2px;float:right;font-size:20px;font-weight:700;line-height:18px;color:#666;text-shadow:0 1px 0 #fff}.fb-header a.fb-close:hover{text-decoration:none}.fb-header-tips{font-size:16px;margin:0;color:#333;text-rendering:optimizelegibility}.fb-body{margin-bottom:0;padding:20px;padding-top:10px;overflow:hidden;text-align:left}.fb-modal,.fb-success{background-color:#fff;cursor:default;top:100%;left:100%;width:390px;overflow:hidden;border:1px solid #999;*border:1px solid #ddd;font-size:13px;line-height:1.54}.fb-textarea textarea{width:350px;height:64px;padding:4px;margin:10px 0;vertical-align:top;resize:none;overflow:auto;box-sizing:border-box;display:inline-block;border:1px solid #ccc;-webkit-border-radius:0;-moz-border-radius:0;border-radius:0;-webkit-box-shadow:inset 0 1px 1px rgba(0,0,0,.075);-moz-box-shadow:inset 0 1px 1px rgba(0,0,0,.075);box-shadow:inset 0 1px 1px rgba(0,0,0,.075);-webkit-transition:border linear .2s,box-shadow linear .2s;-moz-transition:border linear .2s,box-shadow linear .2s;-ms-transition:border linear .2s,box-shadow linear .2s;-o-transition:border linear .2s,box-shadow linear .2s;transition:border linear .2s,box-shadow linear .2s}.fb-guide{padding-top:10px;color:#9a9a9a;margin-left:-20px;padding-left:20px;border-right-width:0;margin-right:-20px;padding-right:25px;margin-bottom:-20px;padding-bottom:15px}.fb-footer{padding-top:10px;text-align:left}.fb-block{overflow:hidden;position:relative}.fb-block .fb-email{height:28px;line-height:26px;width:350px;border:1px solid #ccc;padding:4px;padding-top:0;box-sizing:border-box;padding-bottom:0;display:inline-block;font-family:'Helvetica Neue',Helvetica,Arial,sans-serif;vertical-align:middle!important;-webkit-border-radius:0;-moz-border-radius:0;border-radius:0;-webkit-box-shadow:inset 0 1px 1px rgba(0,0,0,.075);-moz-box-shadow:inset 0 1px 1px rgba(0,0,0,.075);box-shadow:inset 0 1px 1px rgba(0,0,0,.075);-webkit-transition:border linear .2s,box-shadow linear .2s;-moz-transition:border linear .2s,box-shadow linear .2s;-ms-transition:border linear .2s,box-shadow linear .2s;-o-transition:border linear .2s,box-shadow linear .2s;transition:border linear .2s,box-shadow linear .2s}.fb-email{font-size:13px!important;color:#000}.fb-email::-webkit-input-placeholder{font-size:13px!important;color:#9a9a9a}.fb-email:-moz-placeholder{font-size:13px!important;color:#9a9a9a}.fb-email::-moz-placeholder{font-size:13px!important;color:#9a9a9a}.fb-email:-ms-input-placeholder{font-size:13px!important;color:#9a9a9a}.fb-cut-block{height:15px;padding-bottom:10px}.fb-canvas-block{height:172px;border:1px solid #ccc;margin-bottom:10px;position:relative;overflow:hidden;width:100%;background-position:center;box-sizing:border-box}.fb-canvas-block img{width:350px;position:absolute}.fb-canvas-block img[src=\"\"]{opacity:0}.fb-cut-input{width:14px;height:14px;margin:0;margin-right:10px;display:inline-block;border:1px solid #ccc}.fb-cut-btn{width:60px!important}#fb_tips_span{vertical-align:middle}#fb_popwindow{display:block;left:457px;top:69.5px;position:absolute;width:450px;z-index:999999;background:none repeat scroll 0 0 #fff;border:1px solid #999;border-radius:3px;box-shadow:0 0 9px #999;padding:0}#feedback_dialog_content{text-align:center}#fb_right_post_save:hover{background-image:url(data:image\/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAACCAMAAACuX0YVAAAABlBMVEVnpv85i\/9PO5r4AAAAD0lEQVR42gEEAPv\/AAAAAQAFAAIros7PAAAAAElFTkSuQmCC);background-repeat:repeat-x;box-shadow:1px 1px 1px rgba(0,0,0,.4);-webkit-box-shadow:1px 1px 1px rgba(0,0,0,.4);-moz-box-shadow:1px 1px 1px rgba(0,0,0,.4);-o-box-shadow:1px 1px 1px rgba(0,0,0,.4)}.fb-select-icon{position:absolute;bottom:6px;right:5px;width:16px;height:16px;box-sizing:content-box;background-position:center center;background-repeat:no-repeat;background-size:7px 4px;-webkit-background-size:7px 4px;background-image:url(data:image\/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAcAAAAECAYAAABCxiV9AAAABGdBTUEAALGPC\/xhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAAABmJLR0QAAAAAAAD5Q7t\/AAAACXBIWXMAAAsSAAALEgHS3X78AAAAKElEQVQI12Ps7Or6z4ADMDIwMDBgU1BeVsbICOMgKygvK2PEMAbdBAAhxA08t5Q3VgAAAABJRU5ErkJggg==)}.fb-select-shorter{position:relative;min-height:28px}.fb-type-container{line-height:28px;position:absolute;top:28px;width:100%;background-color:#fff;border:1px solid #ccc;z-index:300;margin-left:-1px;display:none}.fb-type-item,.fb-type-selected{height:28px;line-height:30px;padding-left:4px}.fb-type-item:hover{background:#f5F5F5}<\/style>";
    result_common_css=$(result_common_css);
    result_common_css.attr("data-for","result");

    var index_css= $('head [index]');
    var wrapper=$("#wrapper");
    window.index_on=function(){
        index_css.insertAfter("meta:eq(0)");
        result_common_css.remove();
        wrapper.show();
        if(bds.su&&bds.su.U&&bds.su.U.homeInit){
            bds.su.U.homeInit();
        }
        //$("#wrapper_wrapper").remove();
    };
    window.index_off=function(){
        //不能操作dom，只能改css，否则会丢失输入法状态
        result_common_css.insertAfter("meta:eq(0)");
        wrapper.show();
        index_css.remove();

        //$("<div id='wrapper_wrapper'></div>").appendTo("#wrapper");
    };
})();

//首页UA diff 监控
$(window).on("load",function() {

	var rand = Math.random();

	if(rand < 0.01) {
		try {
		var baseUrl = "//www.baidu.com/nocache/fesplg/s.gif?log_type=hm&type=uamonitor&",
			queryString = "";

		queryString += "&c_ua=" + encodeURIComponent(navigator.userAgent);
		queryString += "&s_ua=" + encodeURIComponent(bds.comm.userAgent);

		var url=baseUrl+queryString,
			img = new Image(),
			img_rand="_LOG_"+new Date().getTime();
		img.onload=function(){
			delete window[img_rand];
		};
		window[img_rand]=img;
		img.src=url;
		} catch(e) {};
	}
});

</script>

<script type="text/javascript">var Cookie={set:function(e,t,o,i,s,n){document.cookie=e+"="+(n?t:escape(t))+(s?"; expires="+s.toGMTString():"")+(i?"; path="+i:"; path=/")+(o?"; domain="+o:"")},get:function(e,t){var o=document.cookie.match(new RegExp("(^| )"+e+"=([^;]*)(;|$)"));return null!=o?unescape(o[2]):t},clear:function(e,t,o){this.get(e)&&(document.cookie=e+"="+(t?"; path="+t:"; path=/")+(o?"; domain="+o:"")+";expires=Fri, 02-Jan-1970 00:00:00 GMT")}};!function(){function save(e){var t=[];for(tmpName in options)options.hasOwnProperty(tmpName)&&"duRobotState"!==tmpName&&t.push('"'+tmpName+'":"'+options[tmpName]+'"');
var o="{"+t.join(",")+"}";bds.comm.personalData?$.ajax({url:"//www.baidu.com/ups/submit/addtips/?product=ps&tips="+encodeURIComponent(o)+"&_r="+(new Date).getTime(),success:function(){writeCookie(),"function"==typeof e&&e()}}):(writeCookie(),"function"==typeof e&&setTimeout(e,0))}function set(e,t){options[e]=t}function get(e){return options[e]}function writeCookie(){if(options.hasOwnProperty("sugSet")){var e="0"==options.sugSet?"0":"3";clearCookie("sug"),Cookie.set("sug",e,document.domain,"/",expire30y)
}if(options.hasOwnProperty("sugStoreSet")){var e=0==options.sugStoreSet?"0":"1";clearCookie("sugstore"),Cookie.set("sugstore",e,document.domain,"/",expire30y)}if(options.hasOwnProperty("isSwitch")){var t={0:"2",1:"0",2:"1"},e=t[options.isSwitch];clearCookie("ORIGIN"),Cookie.set("ORIGIN",e,document.domain,"/",expire30y)}if(options.hasOwnProperty("imeSwitch")){var e=options.imeSwitch;clearCookie("bdime"),Cookie.set("bdime",e,document.domain,"/",expire30y)}}function writeBAIDUID(){var e,t,o,i=Cookie.get("BAIDUID");
/FG=(\d+)/.test(i)&&(t=RegExp.$1),/SL=(\d+)/.test(i)&&(o=RegExp.$1),/NR=(\d+)/.test(i)&&(e=RegExp.$1),options.hasOwnProperty("resultNum")&&(e=options.resultNum),options.hasOwnProperty("resultLang")&&(o=options.resultLang),Cookie.set("BAIDUID",i.replace(/:.*$/,"")+("undefined"!=typeof o?":SL="+o:"")+("undefined"!=typeof e?":NR="+e:"")+("undefined"!=typeof t?":FG="+t:""),".baidu.com","/",expire30y,!0)}function clearCookie(e){Cookie.clear(e,"/"),Cookie.clear(e,"/",document.domain),Cookie.clear(e,"/","."+document.domain),Cookie.clear(e,"/",".baidu.com")
}function reset(e){options=defaultOptions,save(e)}var defaultOptions={sugSet:1,sugStoreSet:1,isSwitch:1,isJumpHttps:1,imeSwitch:0,resultNum:10,skinOpen:1,resultLang:0,duRobotState:"000"},options={},tmpName,expire30y=new Date;expire30y.setTime(expire30y.getTime()+94608e7);try{if(bds&&bds.comm&&bds.comm.personalData){if("string"==typeof bds.comm.personalData&&(bds.comm.personalData=eval("("+bds.comm.personalData+")")),!bds.comm.personalData)return;for(tmpName in bds.comm.personalData)defaultOptions.hasOwnProperty(tmpName)&&bds.comm.personalData.hasOwnProperty(tmpName)&&"SUCCESS"==bds.comm.personalData[tmpName].ErrMsg&&(options[tmpName]=bds.comm.personalData[tmpName].value)
}try{parseInt(options.resultNum)||delete options.resultNum,parseInt(options.resultLang)||"0"==options.resultLang||delete options.resultLang}catch(e){}writeCookie(),"sugSet"in options||(options.sugSet=3!=Cookie.get("sug",3)?0:1),"sugStoreSet"in options||(options.sugStoreSet=Cookie.get("sugstore",0));var BAIDUID=Cookie.get("BAIDUID");"resultNum"in options||(options.resultNum=/NR=(\d+)/.test(BAIDUID)&&RegExp.$1?parseInt(RegExp.$1):10),"resultLang"in options||(options.resultLang=/SL=(\d+)/.test(BAIDUID)&&RegExp.$1?parseInt(RegExp.$1):0),"isSwitch"in options||(options.isSwitch=2==Cookie.get("ORIGIN",0)?0:1==Cookie.get("ORIGIN",0)?2:1),"imeSwitch"in options||(options.imeSwitch=Cookie.get("bdime",0))
}catch(e){}window.UPS={writeBAIDUID:writeBAIDUID,reset:reset,get:get,set:set,save:save}}(),function(){var e="https://ss1.bdstatic.com/5eN1bjq8AAUYm2zgoY3K/r/www/cache/static/protocol/https/plugins/every_cookie_4644b13.js";("Mac68K"==navigator.platform||"MacPPC"==navigator.platform||"Macintosh"==navigator.platform||"MacIntel"==navigator.platform)&&(e="https://ss1.bdstatic.com/5eN1bjq8AAUYm2zgoY3K/r/www/cache/static/protocol/https/plugins/every_cookie_mac_82990d4.js"),setTimeout(function(){$.ajax({url:e,cache:!0,dataType:"script"})},0);var t=navigator&&navigator.userAgent?navigator.userAgent:"",o=document&&document.cookie?document.cookie:"",i=!!(t.match(/(msie [2-8])/i)||t.match(/windows.*safari/i)&&!t.match(/chrome/i)||t.match(/(linux.*firefox)/i)||t.match(/Chrome\/29/i)||t.match(/mac os x.*firefox/i)||o.match(/\bISSW=1/)||0==UPS.get("isSwitch"));
bds&&bds.comm&&(bds.comm.supportis=!i,bds.comm.isui=!0),window.__restart_confirm_timeout=!0,window.__confirm_timeout=8e3,window.__disable_is_guide=!0,window.__disable_swap_to_empty=!0,window.__switch_add_mask=!0;var s="https://ss1.bdstatic.com/5eN1bjq8AAUYm2zgoY3K/r/www/cache/static/protocol/https/global/js/all_async_search_b8644da.js",n="/script";document.write("<script src='"+s+"'><"+n+">"),bds.comm.newindex&&$(window).on("index_off",function(){$('<div class="c-tips-container" id="c-tips-container"></div>').insertAfter("#wrapper"),window.__sample_dynamic_tab&&$("#s_tab").remove()
}),bds.comm&&bds.comm.ishome&&Cookie.get("H_PS_PSSID")&&(bds.comm.indexSid=Cookie.get("H_PS_PSSID"))}();</script><script src="https://ss1.bdstatic.com/5eN1bjq8AAUYm2zgoY3K/r/www/cache/static/protocol/https/global/js/all_async_search_b8644da.js"></script>



<script>
if(bds.comm.supportis){
    window.__restart_confirm_timeout=true;
    window.__confirm_timeout=8000;
    window.__disable_is_guide=true;
    window.__disable_swap_to_empty=true;
}
initPreload({
    'isui':true,
    'index_form':"#form",
    'index_kw':"#kw",
    'result_form':"#form",
    'result_kw':"#kw"
});
</script>

<script>
if(navigator.cookieEnabled){
	document.cookie="NOJS=;expires=Sat, 01 Jan 2000 00:00:00 GMT";
}
</script>










</body></html>"""
soup = BeautifulSoup(html_doc, 'html.parser')
#print(soup.prettify())
#print(soup.title)
#print(soup.title.name)
print(soup.title.string)
#print(soup.find_all('a')[0])
print(soup.find(id='kw'))