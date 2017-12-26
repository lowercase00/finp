function addRow(id)

{
    var i = 1;
  
    var valdisper,
    	valdisamt,
    	valsalprice,
    	valqty,
    	valval,
    	valvatper,
    	valamt,
    	valmrp,
    	valnet,
    	valgross,
    	valitem,
    	valcode;
    var valuom;
    var totqty,
    	totvalamt,
    	totdisamt,
    	tottaxamt,
    	totnet;
    var q,
    	va,
    	tda,
    	tta,
    	tn;
   
    valcode 		= document.getElementById("txtcode").value;
    valitem 		= document.getElementById("txtdesc").value;
    valmrp 			= document.getElementById("txtmrp").value;
    valsalprice 	= document.getElementById("txtsalp").value;
    valqty 			= document.getElementById("txtqty").value;
    valuom 			= document.getElementById("sel2").value;
    valval 			= document.getElementById("txtval").value;
    valdisper 		= document.getElementById("txtdis").value;
    valdisamt 		= document.getElementById("txtdisamt").value;
    valamt 			= document.getElementById("txttax").value;
    valnet 			= document.getElementById("txtnet").value;
    valvatper 		= document.getElementById("sel").value;
    valgross 		= document.getElementById("txtgross").value;
   
    if (valcode != "" && valcode != null) {
        var tbody = document.getElementById
        (id).getElementsByTagName("TBODY")[0];
        var row = document.createElement("TR")
        var td1 = document.createElement("TD")
        	td1.appendChild(document.createTextNode(i))
        var td2 = document.createElement("TD")
        	td2.appendChild(document.createTextNode(valcode))
        var td3 = document.createElement("TD")
        	td3.appendChild(document.createTextNode(valitem))
        var td4 = document.createElement("TD")
        	td4.appendChild(document.createTextNode(valmrp))
        var td5 = document.createElement("TD")
        	td5.appendChild(document.createTextNode(valsalprice))
        var td6 = document.createElement("TD")
        	td6.appendChild(document.createTextNode(valqty))
        var td7 = document.createElement("TD")
        	td7.appendChild(document.createTextNode(valuom))
        var td8 = document.createElement("TD")
        	td8.appendChild(document.createTextNode(valval))
        var td9 = document.createElement("TD")
        	td9.appendChild(document.createTextNode(valdisamt))
        var td10 = document.createElement("TD")
	        td10.appendChild(document.createTextNode(valamt))
        var td11 = document.createElement("TD")
        	td11.appendChild(document.createTextNode(valnet))
    
       
        row.appendChild(td1);
        row.appendChild(td2);
        row.appendChild(td3);
        row.appendChild(td4);
        row.appendChild(td5);
        row.appendChild(td6);
        row.appendChild(td7);
        row.appendChild(td8);
        row.appendChild(td9);
        row.appendChild(td10);
        row.appendChild(td11);
        var row1 = document.createElement("TR")
        var tdn = document.createElement("TD")
        	tdn.appendChild(document.createTextNode(Sum(id)))
        	tbody.appendChild(row);
        
}

}

function Sum(id){

var money = 0;
	var mytable = document.getElementById(id);
	 
	  for(var v = 0; v < mytable.rows.length; v++)
            {
             for(var c = 0 ; c < mytable.rows[v].cells.length; c++)
              {
                    switch(parseInt(mytable.rows[v].cells[c]))
                    {
                     /*If cell matches number matches one with a price you need simply add it to case statement */
                     case 2:      
	                  money += parseInt(mytable.rows[v].cells[c].firstChild.innerHTML);
                         break;
                    }
               }
	     }
	 return money;

}
 

<input type="button" id="btnok" value="OK" runat="server" class="btn"   onclick="javascript:addRow('maintable')" />

