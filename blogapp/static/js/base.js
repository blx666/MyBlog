/**
 * Created by bilixin on 16-12-12.
 */



var students_checkbox=null

var STDashborder={
    stfilter: {

        init: function(){
            var arrcookie = new Array(), select  = $("#categotryform input[name=name][checked=True]")

            $("#categotryform").on('click', function(){


            })




        },


        finter:function(){

            $('#btn_submit').on('click',function(){

                if(po_filter_ship_ajax){
                    po_filter_ship_ajax.abort()
                }

                data = $("categotryform").serialize()

                po_filter_ship_ajax = $.ajax({
                    url:$("categotryform").data('url'),
                    data:data,
                    timeout:2000,
                    sunccess:function(data){
                        $(".filer_result").html(data)

                    },
                    complete:function(){

                    },

                })
               alert('123')
            });




        },





        temp1: function(){

        },
        temp2: function(){

        },
    }
}

