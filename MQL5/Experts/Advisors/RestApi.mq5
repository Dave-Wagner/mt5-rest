#property version   "1.00"

#include <RestApi.mqh>

input string   host = "http://localhost";
input int      port = 6542;
input int      commandWaitTimeout = 10;
input string   callbackUrl = "http://localhost/callback";
input string   callbackFormat = "json";

CRestApi api;

int OnInit() {

   api.Init(host, port, commandWaitTimeout);
   api.SetCallback( callbackUrl, callbackFormat );

   EventSetMillisecondTimer(1);
   
   return(INIT_SUCCEEDED);
}

void OnDeinit(const int reason) {

   EventKillTimer();
   
   //api.Deinit();
}

void OnTimer() {
   api.Processing();
}

void OnTradeTransaction(const MqlTradeTransaction& trans,
                        const MqlTradeRequest& request,
                        const MqlTradeResult& result) {
                        
   api.OnTradeTransaction( trans, request, result );
}