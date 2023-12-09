<!-- [GLFM](https://docs.gitlab.com/ee/user/markdown.html)   -->

# fcs4hand2310

[TODO] example_fcs とか ex_fcs0 とか

## 概要

双葉電子工業の産業用サーボのコマンド式サーボを４つ使用するハンドです。

ros2_control で制御するために hardware_fcs を使用しています。

各関節角度を joint_trajectory_controller で制御し、joint_state_broadcaster で現在角度を展開するための launch ファイル及び設定ファイル群が用意されています。

humble で動作確認しました。

## 部品一覧

### TTL タイプ

 | 部品名           | メーカー名   | 型番                                                                                                                                                                                                                                                | 数量   | 備考                                                           |
 |------------------|--------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------|----------------------------------------------------------------|
 | サーボモジュール | 双葉電子工業 | [00400021-3 ROBOT SERVO RS304MDFF FUTABA](https://www.futaba.co.jp/product/industrial_servo/command_type_servos/rs304md) もしくは [00400020-3 ROBOT SERVO RS303MRFF](https://www.futaba.co.jp/product/industrial_servo/command_type_servos/rs303mr) | 4      |                                                                |
 | ハブ             | 双葉電子工業 | [BA2082 TB-RV71EH-7.4V/3W](https://www.futaba.co.jp/product/industrial_servo/command_type_servos/option_parts/relaybox_hub)                                                                                                                         | 1      |                                                                |
 | USB アダプタ     | 双葉電子工業 | [00400070-1 CONVERTER RSC-U485 JPN](https://www.futaba.co.jp/product/industrial_servo/command_type_servos/rsc)                                                                                                                                      | 1      | TB-RV71EH-7.4V/3W とセットで使用します（代用不可）             |
 | 電源ケーブル     | 双葉電子工業 | [BC0079 TB-RV71EH POWER CABLE](https://www.futaba.co.jp/product/industrial_servo/command_type_servos/option_parts/relaybox_hub)                                                                                                                     | 1      | つながれば代用可                                               |
 | EHコネクタ       | JST          | [EHR-4](https://www.jst-mfg.com/product/pdf/jpn/EH.pdf?65742110096e4)                                                                                                                                                                               | 4      |                                                                |
 | EH用コンタクト   | JST          | [(適宜)](https://www.jst-mfg.com/product/pdf/jpn/EH.pdf?65742110096e4)                                                                                                                                                                              | 12     | サーボモジュールは一般的な３ピンで、ハブの４ピンに交換するため |
 | モータ電源       | (適宜)       | (適宜)                                                                                                                                                                                                                                              | 1      | サーボモジュールは 4.8〜7.2[V] が定格、電流容量は不明          |
 | タッピングネジ   | (適宜)       | (調査中)                                                                                                                                                                                                                                            | 34     |                                                                |
 | 両面テープ       | (適宜)       | (薄手のもの)                                                                                                                                                                                                                                        | (適宜) | サーボモジュールとリンク部材との固定は両面テープ               |
 | リンク部材       | (適宜)       | (step ディレクトリ内を参照)                                                                                                                                                                                                                         | 各1    |                                                               |

工作箇所
 - リンク部材にサーボモジュールを両面テープで貼り付け
 - リンク部材をサーボホーンにネジ止め
 - 基部のサーボモジュール押さえをネジ止め
 - 各サーボモジュールのコネクタを EHR-4 に付け替え
 - 各種電源配線（電源、RS-485)
 
注意事項
 - USB アダプタからハブまでは RS-485 なので、ターミネート抵抗を両端に入れると安心できるかもしれません。


### RS-485 タイプ
 - サーボモジュールを [00400038-1 ROBOT SERVO RS302CDF3 FUTABA ](https://www.futaba.co.jp/product/industrial_servo/command_type_servos/rs302cd) もしくは [00400065-3 RS305CR](https://www.futaba.co.jp/product/industrial_servo/command_type_servos/rs305cr) に変更
 - 軸付きボトムケース [BS3397 RS30x BOTTOM CASE-SHAFT](https://www.futaba.co.jp/product/industrial_servo/command_type_servos/option_parts/servo_caseset) を４つ追加調達
 - フリーホーン（５個セット）[BS0168 RS2xx/RS3xx FREE HORN SET](https://www.futaba.co.jp/product/industrial_servo/command_type_servos/option_parts/servo_horn)を１セット追加調達
 - ハブを[TODO] ２つに変更




## コマンドライン覚書

全軸 torque off (inactive 状態へ遷移)

```
ros2 service call /controller_manager/set_hardware_component_state controller_manager_msgs/srv/SetHardwareComponentState "{name: ex_fcs0, target_state: {id: 0, label: inactive}}"
```

全軸 torque enable (active 状態へ遷移)

```
ros2 service call /controller_manager/set_hardware_component_state controller_manager_msgs/srv/SetHardwareComponentState "{name: ex_fcs0, target_state: {id: 0, label: active}}"
```

目標角度へ動作（ここでは [0, 0, 0, 0]）

```
ros2 action send_goal /joint_trajectory_controller_example_fcs/follow_joint_trajectory control_msgs/action/FollowJointTrajectory -f { trajectory: { joint_names: [ hndj0, hndj1, hndj2, hndj3 ], points : [ { positions: [0, 0, 0, 0], time_from_start: { sec: 0.5 }} ]}}
```

##


 | ファイル名                               | 概要                                                                                |
 |------------------------------------------|-------------------------------------------------------------------------------------|
 | launch/fcs4hand2310.launch.py             | launch スクリプト。ros2_control の設定もコーディ具されている                        |
 | urdf/fcs2310.urdf                        | 軸配置と外形を記述                                                                  |
 | urdf/fcs4hand2310.xacro                   | URDF 本体。 fcs2310.urdf を読み込んで、ros2_control タグ、hardware_fcs タグを追加。 |
 | config/ros2_controllers_fcs4hand2310.yaml | joint_trajectory_controller と joint_state_broadcaster の設定                       |


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

