<table>
    <tr>
        <th>功能</th>
        <th>命令</th>
    </tr>
    <tr>
        <td>查看pod</td>
        <td>kubectl --kubeconfig=[kubeconfig] get pod -n [namespace]</td>
    </tr>
    <tr>
        <td>查看pod所在物理机</td>
        <td>kubectl --kubeconfig=[kubeconfig] get pod -n [namespace] -o wide</td>
    </tr>
    <tr>
        <td>查看pod下的container</td>
        <td>kubectl --kubeconfig=[kubeconfig] -n namespace describe pod [pod-name]</td>
    </tr>
    <tr>
        <td>查看日志</td>
        <td>kubectl --kubeconfig=[kubeconfig] -n namespace logs [pod-name] [container-name]</td>
    </tr>
    <tr>
        <td>进入pod</td>
        <td>kubectl --kubeconfig=[kubeconfig] exec -it [pod-name] -n [namespace] /bin/bash</td>
    </tr>
    <tr>
        <td>查看jobs</td>
        <td>kubectl --kubeconfig=[kubeconfig] get jobs -n [namespace]</td>
    </tr>
    <tr>
        <td>查看定时任务</td>
        <td>kubectl --kubeconfig=[kubeconfig]  -n [namespace] get cronjob -o wide<br>
        kubectl --kubeconfig=[kubeconfig]  -n [namespace] describe cronjob [cronjob-name]]
        </td>
    </tr>

查看定时任务

kubectl --kubeconfig=cloud-sandbox00-readonly  -n acg-iot-core get cronjob -o wide

kubectl --kubeconfig=cloud-sandbox00-readonly  -n acg-iot-core describe cronjob iot-cloud-suite-charge-job
删除 pod
helm --kubeconfig=kubeconfig list -n namespace
helm --kubeconfig=kubeconfig uninstall chartname  -n namespace
kubectl --kubeconfig=kubeconfig delete pod podname -n namespace
helm --kubeconfig=old-sandbox-config list -n acg-iot-test
helm --kubeconfig=old-sandbox-config uninstall acdp-service  -n acg-iot-test
kubectl --kubeconfig=config delete pod acdp-service-0 -n acg-iot-test

kubectl --kubeconfig=kem-admin.config -n acg-iot-core get katalyst-ss

kubectl --kubeconfig=kem-admin.config -n acg-iot-core edit katalyst-ss

helm ls | grep mqtt

helm del --purge mqtt-broker

helm install . --name mqtt-broker

reference
K8S 天工平台部署-独立部署版本-标准 K8S#%E7%8B%AC%E7%AB%8B%E9%83%A8%E7%BD%B2%E7%89%88%E6%9C%AC-%E6%A0%87%E5%87%86K8S-7.3%E9%AA%8C%E8%AF%81%E7%89%A9%E6%8E%A5%E5%85%A5
k8s 基本命令
