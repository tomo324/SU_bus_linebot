# SU_bus_linebot
##  概要
大学へ向かうバスの遅延を通知してくれるLineBot  
## 目的
私が通っている大学は駅からバスで通学しなければならず、過去に遅延によって講義に遅れそうになることが何度かありました。
そこで、バスの運行情報をリアルタイムで取得し、遅延情報を通知してくれる LineBot を作成することで、この問題に対処できるのではないかと考えました。

## 仕組み
国際興業バスと西武バスのバスロケーションシステムから運行情報をスクレイピングしています。  

国際興業バス(https://transfer.navitime.biz/5931bus/pc/location/BusLocationResult?startId=00021176&goalId=00021229)  

西武バス(https://transfer.navitime.biz/seibubus-dia/pc/location/BusLocationResult?startId=00111628&goalId=00111643)  

この2つのWebサイトから北浦和駅西口から埼玉大学までの所要時間を10分おきに取得し、一定の所要時間を超えたらLineに通知するようにしています。

## Lineの表示
 
![バスbot](https://user-images.githubusercontent.com/102280498/234618453-3634c157-b4c6-4459-bd91-417f308a4b3c.jpg)
