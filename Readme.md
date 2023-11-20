<!-- [GLFM](https://docs.gitlab.com/ee/user/markdown.html)   -->

# fcs4hand2310

[TODO] example_fcs とか ex_fcs0 とか

## 概要

双葉電子工業の産業用サーボのコマンド式サーボを４つ使用するハンド。

ros2_control で制御するために hardware_fcs を使用している。

各関節角度を joint_trajectory_controller で制御し、joint_state_broadcaster で現在角度を展開するための launch ファイル及び設定ファイル群が用意されている。

humble で動作確認。

## コマンドライン覚書



全軸 torque off (inactive 状態へ遷移)

```
ros2 service call /controller_manager/set_hardware_component_state controller_manager_msgs/srv/SetHardwareComponentState "{name: ex_fcs0, target_state: {id: 0, label: inactive}}"
```

全軸 torque enable (active 状態へ遷移)

```
ros2 service call /controller_manager/set_hardware_component_state controller_manager_msgs/srv/SetHardwareComponentState "{name: ex_fcs0, target_state: {id: 0, label: active}}"
```

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

