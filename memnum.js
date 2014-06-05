
String.prototype.replaceAll = function(str1, str2, ignore){
	return this.replace(new RegExp(str1.replace(/([\/\,\!\\\^\$\{\}\[\]\(\)\.\*\+\?\|\<\>\-\&])/g,"\\$&"),(ignore?"gi":"g")),(typeof(str2)=="string")?str2.replace(/\$/g,"$$$$"):str2);
}

map = function(func, arr){
    for(var i=0; i<arr.length; i++){
        arr[i] = func(arr[i])
    }
    return arr;
}

//filter
filter = function(func, arr){
    ret = [];
    for(var i=0; i<arr.length; i++){
        if (!!func(arr[i])){
            ret.push(arr[i]);
        }
    }
    return ret;
}
//         0   1           2                3                 4              5                 
//nummap = [[], [],  ["a","b","c"], ["d","e", "f"], ["g", "h", "i"], ["j", "k", "l"],
//             6               7              8                   9
//          ["m", "n", "o"], ["p","q", "r"], ["s","t","u"], ["v", "x", "y","z"]]

//          0      1           2                3                 4            5                 
numap = [["o"], ["l"],  ["a","b","c"], ["d","e", "f"], ["g", "h", "i"], ["j", "k"],
//             6               7              8                   9
          ["m", "n"], ["p","q", "r"], ["s","t","u"], ["v", "x", "y","z"]]         
          
//TODO: Make smarter
getPhrase = function(num){
   map(function(n){return numap[n][0]}, num) 
}          
          
genmn = function(){
    //get phone number
    var pnum = document.getElementById('phonenumber').value;
    var numvect = pnum.replaceAll("-", "").split("");
    if (numvect.length != 10) { //error check
        alert("Please enter a valid phone number");
        //TODO: check if all are valid digits
    }
    var num = map(parseInt, numvect.slice(3)); //number part of phone number- get last 7 digits   
    //console.log(num)
    
    var phrase = getPhrase(num);
    //console.log(phrase);
    
    var areacode = numvect.slice(0,3).join(""); //area code
    document.getElementById('output').value=areacode+"-"+phrase.join("");
            
}


clearfield = function(){
    //clears value
    document.getElementById('phonenumber').value="";
    document.getElementById('output').value="";
    //console.log("Clearing value")
}
