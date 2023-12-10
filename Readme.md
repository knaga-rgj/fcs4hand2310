<!-- [GLFM](https://docs.gitlab.com/ee/user/markdown.html)   -->

# fcs4hand2310

## 概要

[双葉電子工業の産業用サーボのコマンド式サーボ](https://www.futaba.co.jp/product/industrial_servo/command_type_servos)を４つ使用するハンドです。

リンク部材は 3D プリンタで作ることを想定しています。（step フォルダ内のデータを活用ください）

ros2_control で制御するために [hardware_fcs](https://github.com/knaga-rgj/hardware_fcs) を使用しています。

各関節角度を joint_trajectory_controller で制御し、joint_state_broadcaster で現在角度を展開するための launch ファイル及び設定ファイル群が用意されています。

humble で動作確認しました。

## 部品一覧

### TTL タイプ

 | 部品名                 | メーカー名   | 型番                                                                                                                                                                                                                                                | 数量   | 備考                                                                                                 |
 |------------------------|--------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------|------------------------------------------------------------------------------------------------------|
 | サーボモジュール       | 双葉電子工業 | [00400021-3 ROBOT SERVO RS304MDFF FUTABA](https://www.futaba.co.jp/product/industrial_servo/command_type_servos/rs304md) もしくは [00400020-3 ROBOT SERVO RS303MRFF](https://www.futaba.co.jp/product/industrial_servo/command_type_servos/rs303mr) | 4      |                                                                                                      |
 | ハブ                   | 双葉電子工業 | [BA2082 TB-RV71EH-7.4V/3W](https://www.futaba.co.jp/product/industrial_servo/command_type_servos/option_parts/relaybox_hub)                                                                                                                         | 1      |                                                                                                      |
 | USB アダプタ           | 双葉電子工業 | [00400070-1 CONVERTER RSC-U485 JPN](https://www.futaba.co.jp/product/industrial_servo/command_type_servos/rsc)                                                                                                                                      | 1      | TB-RV71EH-7.4V/3W とセットで使用します（代用不可）                                                   |
 | 電源ケーブル(ハブ側)   | 双葉電子工業 | [BC0079 TB-RV71EH POWER CABLE](https://www.futaba.co.jp/product/industrial_servo/command_type_servos/option_parts/relaybox_hub)                                                                                                                     | 1      | つながれば代用可                                                                                     |
 | EH ４ピンコネクタ      | JST          | [EHR-4](https://www.jst-mfg.com/product/pdf/jpn/EH.pdf)                                                                                                                                                                                             | 4      | ターミネート抵抗を刺すなら１つ追加。                                                                 |
 | EH用コンタクト         | JST          | [(適宜)](https://www.jst-mfg.com/product/pdf/jpn/EH.pdf)                                                                                                                                                                                            | 12     | サーボモジュールは一般的な３ピンで、ハブの４ピンに交換するため。ターミネート抵抗を挿すなら２個追加。 |
 | モータ電源             | (適宜)       | (適宜)                                                                                                                                                                                                                                              | 1      | サーボモジュールは 4.8〜7.2[V] が定格、電流容量は不明                                                |
 | 電源ケーブル（電源側） | (自作)       | (自作)                                                                                                                                                                                                                                              | 1      |                                                                                                      |
 | タッピングネジ         | (適宜)       | (調査中)                                                                                                                                                                                                                                            | 34     |                                                                                                      |
 | 両面テープ             | (適宜)       | (薄手のもの)                                                                                                                                                                                                                                        | (適宜) | サーボモジュールとリンク部材との固定は両面テープ                                                     |
 | リンク部材             | (適宜)       | (step ディレクトリ内のを 3D プリント)                                                                                                                                                                                                               | 各1    |                                                                                                      |

工作概略
 - リンク部材にサーボモジュールを両面テープで貼り付け
 - リンク部材をサーボホーンにネジ止め
 - 基部のサーボモジュール押さえをネジ止め
 - 各サーボモジュールのコネクタを EHR-4 に付け替え
 - 電源ケーブル作成（ハブ側、電源側）
 - 配線結線、動作確認、ID 焼き込み
 
注意事項
 - USB アダプタからハブまでは RS-485 なので、ターミネート抵抗を両端に入れると安心できるかもしれません。


### RS-485 タイプ

TTL タイプと比べて RS-485 通信の安心感が増す一方で作業量が増えます。特に DF11 4ピンの配線を間違えると悲惨で危険なことになるかもしれません。

 - サーボモジュールを[外形形状が同じで RS-485 タイプのもの (RS302CD や RS305CR)](https://www.futaba.co.jp/product/industrial_servo/command_type_servos) に変更
 - 軸付きボトムケース [BS3397 RS30x BOTTOM CASE-SHAFT](https://www.futaba.co.jp/product/industrial_servo/command_type_servos/option_parts/servo_caseset) を４つ追加調達
 - フリーホーン（５個セット）[BS0168 RS2xx/RS3xx FREE HORN SET](https://www.futaba.co.jp/product/industrial_servo/command_type_servos/option_parts/servo_horn)を１セット追加調達
 - ハブを [BA2085 TB DF31DF-100](https://www.futaba.co.jp/product/industrial_servo/command_type_servos/option_parts/relaybox_hub)  ２つに変更（１つでは不足するので注意）
 - 電源ケーブル（ハブ側）は削除
 - 電源ケーブルを自作（２芯、電源供給側から DF11-4 へ、VCC, GND）
 - 通信用変換ケーブルを自作（３芯、EHR-4 から DF11-4 への変換、D+, D-, GND）

 | 部品名              | メーカー名   | 型番                                                                                                                                                                                                                                   | 数量   | 備考                                                                       |
 |---------------------|--------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------|----------------------------------------------------------------------------|
 | サーボモジュール    | 双葉電子工業 | [00400038-1 ROBOT SERVO RS302CDF3 FUTABA ](https://www.futaba.co.jp/product/industrial_servo/command_type_servos/rs302cd) もしくは [00400065-3 RS305CR](https://www.futaba.co.jp/product/industrial_servo/command_type_servos/rs305cr) | 4      |                                                                            |
 | 軸付きボトムケース  | 双葉電子工業 | [BS3397 RS30x BOTTOM CASE-SHAFT](https://www.futaba.co.jp/product/industrial_servo/command_type_servos/option_parts/servo_caseset)                                                                                                     | 4      |                                                                            |
 | フリーホーン        | 双葉電子工業 | [BS0168 RS2xx/RS3xx FREE HORN SET](https://www.futaba.co.jp/product/industrial_servo/command_type_servos/option_parts/servo_horn)                                                                                                      | 1      | ５個１セット                                                               |
 | ハブ                | 双葉電子工業 | [BA2085 TB DF31DF-100](https://www.futaba.co.jp/product/industrial_servo/command_type_servos/option_parts/relaybox_hub)                                                                                                                | 1      |                                                                            |
 | USB アダプタ        | 双葉電子工業 | [00400070-1 CONVERTER RSC-U485 JPN](https://www.futaba.co.jp/product/industrial_servo/command_type_servos/rsc)                                                                                                                         | 1      | TB-RV71EH-7.4V/3W とセットで使用します（代用不可）                         |
 | EH ４ピンコネクタ   | JST          | [EHR-4](https://www.jst-mfg.com/product/pdf/jpn/EH.pdf?65742110096e4)                                                                                                                                                                  | 1      | 通信用変換ケーブル用、RCS-U485 付属品を流用するのでも可                    |
 | EH用コンタクト      | JST          | [(適宜)](https://www.jst-mfg.com/product/pdf/jpn/EH.pdf?65742110096e4)                                                                                                                                                                 | 3      | 同上                                                                       |
 | DF11 ４ピンコネクタ | ヒロセ電機   | [DF11-4DS-2C](https://www.hirose.com/ja/product/document?clcode=&productname=&series=DF11&documenttype=Catalog&lang=ja&documentid=jd_DF11_CAT)                                                                                         | 2      | 通信用変換ケーブル用と電源ケーブル用。ターミネート抵抗を挿すなら１個追加。 |
 | DF11用コンタク      | ヒロセ電機   | [(適宜)](https://www.hirose.com/ja/product/document?clcode=&productname=&series=DF11&documenttype=Catalog&lang=ja&documentid=jd_DF11_CAT)                                                                                              | 5      | 同上                                                                       |
 | 通信用変換ケーブル  | 自作         | (適宜)                                                                                                                                                                                                                                 | 1      | ３芯 D+, D-, GND                                                           |
 | モータ電源          | (適宜)       | (適宜)                                                                                                                                                                                                                                 | 1      | サーボモジュールは 4.8〜7.2[V] が定格、電流容量は不明                      |
 | 電源ケーブル        | 自作         | (適宜)                                                                                                                                                                                                                                 |        |                                                                            |
 | タッピングネジ      | (適宜)       | (調査中)                                                                                                                                                                                                                               | 34     |                                                                            |
 | 両面テープ          | (適宜)       | (薄手のもの)                                                                                                                                                                                                                           | (適宜) | サーボモジュールとリンク部材との固定は両面テープ                           |
 | リンク部材          | (適宜)       | (step ディレクトリ内のを 3D プリント)                                                                                                                                                                                                  | 各1    |                                                                            |


工作概略
 - 各サーボモジュールのボトムケースを軸付きに交換
   - 配線に目印をつける
   - DF11 ４ピンのハウジングを外す
   - サーボモジュールのボトムケースを交換する
   - DF11 ４ピンのハウジングをとりつける（信号線を挿す場所を間違えないように）
 - リンク部材にサーボモジュールを両面テープで貼り付け
 - リンク部材をサーボホーンにネジ止め
 - 基部のサーボモジュール押さえをネジ止め
 - 各サーボモジュールのコネクタを EHR-4 に付け替え
 - 電源ケーブル、通信用変換ケーブル作成
 - 配線結線、動作確認、ID 焼き込み



注意事項
 - ターミネート抵抗を両端に入れると安心できるかもしれません。
 - ボトムケースを交換する際、DF11 ４ピンコネクタを一旦バラす必要があります。配線の色も同色なため混同しないように細心の注意が必要です。


## 単体動作確認ツール python3 + dicot

[dicot](https://pypi.org/project/dicot/) が便利です。`pip3 install dicot` でインストールできます。
 
[dicot の README.md](https://github.com/lanius/dicot/blob/master/README.md) に目を通した後は、[ソース](https://github.com/lanius/dicot/blob/master/dicot/motors.py) を読むとアクセスしたいプロパティの名称がわかると思います。

シリアルデバイスは dialout group での読み書きが可能なので、Ubuntu の自分自身のユーザアカウントを dialaout グループに追加しておいてください。例えば alice というユーザ名であれば、`sudo adduser alice dialout` を実行し、再起動してください。

RSC-U485 は FTDI のドライバ (ftdi_sio) で動きますが FTDI のドライバには RSC-U485 が登録されていません。手動でその場で動くようにするには以下のコマンドを実行してください。
 
```
$ sudo su
# modrobe ftdi_sio
# echo 1115 0008 > /sys/bus/usb-serial/drivers/ftdi_sio/new_id
```

次回以降の起動時に自動で認識するようにするには、/etc/udev/rules.d 以下に適当な名前のファイルを作成して、以下の記述を書いておいてください。

```
ATTR{idVendor}=="1115", ATTR{idProduct}=="0008", GROUP="dialout", MODE="0660", RUN+="/bin/sh -c '/sbin/modprobe ftdi_sio; /bin/sh -c \"echo 1115 0008\" > /sys/bus/usb-serial/drivers/ftdi_sio/new_id'"
```




## ros2_control で動かすときのコマンドライン覚書

全軸 torque off (inactive 状態へ遷移)

```
ros2 service call /controller_manager/set_hardware_component_state controller_manager_msgs/srv/SetHardwareComponentState "{name: fcs0, target_state: {id: 0, label: inactive}}"
```

全軸 torque enable (active 状態へ遷移)

```
ros2 service call /controller_manager/set_hardware_component_state controller_manager_msgs/srv/SetHardwareComponentState "{name: fcs0, target_state: {id: 0, label: active}}"
```

目標角度へ動作（ここでは [0, 0, 0, 0], 単位はラジアン）

```
ros2 action send_goal /joint_trajectory_controller_fcs4hand2310/follow_joint_trajectory control_msgs/action/FollowJointTrajectory -f "{ trajectory: { joint_names: [ hndj0, hndj1, hndj2, hndj3 ], points : [ { positions: [0, 0, 0, 0], time_from_start: { sec: 0.5 }} ]}}"
```

## このリポジトリについて


 | ファイル名                                | 概要                                                                                       |
 |-------------------------------------------|--------------------------------------------------------------------------------------------|
 | launch/fcs4hand2310.launch.py             | launch スクリプト。ros2_control の設定もコーディングされています                           |
 | urdf/fcs2310.urdf                         | 軸配置と外形を記述。プレビューで使用。                                                     |
 | urdf/fcs4hand2310ctrl.xacro               | トップレベル URDF。fcs2310.urdf を読み込んで、ros2_control タグ、hardware_fcs タグを追加。 |
 | config/ros2_controllers_fcs4hand2310.yaml | joint_trajectory_controller と joint_state_broadcaster の設定                              |


スクリプトファイル群
 | ファイル名       | 概要                                                                                                                                                 |
 |------------------|------------------------------------------------------------------------------------------------------------------------------------------------------|
 | torque_free.sh   | ex_fcs0 (HardwareFCS) を inactive 状態にする。on_deactive() 処理中に全サーボにサーボオフ (Torque Enable = False) が送られる。                        |
 | torque_enable.sh | ex_fcs0 (HardwareFCS) を active 状態にする。on_activate() 処理中に指令値を現在値で上書きし、全サーボにサーボオン (Torque Eanble = True) が送られる。 |
 | set_angles.py    | joint_trajectory_controller_fcs4hand2310 (JointTrajectoryController) に動作指令を送る。python から `ros2 action send_goal ...` を実行している(手抜き) |



```
├── CMakeLists.txt
├── Readme.md
├── config
│   └── ros2_controllers_fcs4hand2310.yaml
├── launch
│   └── fcs4hand2310.launch.py
├── package.xml
├── scripts
│   ├── set_angles.py
│   ├── torque_enable.sh
│   └── torque_free.sh
└── urdf
    ├── RS30x_BottomShaft.dae
    ├── fcs4hand2310.xacro
    └── fcs2310.urdf
```

